# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:42:59 2012

@author: zhaiyt
"""

import os
import sys
import string
import sys
import shutil
from shellcolor import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

global convertlist
convertlist=[]
global wafer_ID
wafer_ID =[]
global mean
mean='on'
global sigma
sigma=0
global loop
loop=0
global log_f
global bad_f
global speclist
speclist=[]
global mode_list
mode_list=[]


def findFile():
    
    global convertlist
    convertlist=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for mem in files:
            if mem.split('.')[-1]=='dat':
                mem=os.path.join(root,mem)
                convertlist.append(mem)
    num=len(convertlist)
    if num==0:
        print
        raw_input('No file find ,please put data file to current dirctory')
        sys.exit()
    else:
        print
        printWait("%s files need to convert:" % num)
        print
        print 
        for hitfile in convertlist:
            printWait(hitfile)
            print
            
def convertFile():
    global log_f
    global bad_f
    global convertlist
    global wafer_ID
    row_index=[]
    infi_list=[]
    group_list=[]
    wafer_ID=[]
    infi_len_list_old=[]
    flag_str=[]
    con=[]
    for i in range(0,len(convertlist)):
        printWait('Convert %s...'%convertlist[i])
        f=open(convertlist[i], 'r')
        content=f.readlines()
        f.close()
        
        wafer_index=[]
        for j in range(0,len(content)):
            content[j]=content[j].strip('\n')
            temp_list=content[j].split(',')
            temp_list[0]=temp_list[0].upper()
            if temp_list[0].startswith('SYS_WAFERID'):
                wafer_index.append(j)
        for j in range(0,(len(wafer_index)-1)):
            content_slice=content[wafer_index[j]:wafer_index[j+1]]
            con.append(content_slice)         
        con.append(content[wafer_index[-1]:])
    
    for i in range(0,len(con)):
        row_index.append([])
        infi_list.append([])
        flag_str.append([])
        content=con[i]
        for j in range(0,len(content)):
            content[j]=content[j].strip('\n')
            temp_list=content[j].split(',')
            temp_list[0]=temp_list[0].upper()
            if temp_list[0].startswith('VBS_STEP'):
                row_index[-1].append(j)
                infi= getinfi(content[j])
                flag_str[-1].append(content[j])
                infi_list[-1].append(infi)
            elif temp_list[0].startswith('SYS_WAFERID'):
                wafer_ID.append('#'+temp_list[-1])
        row_index[-1].append(len(content))
        
    infi_len_list=[]
    for i in range(0,len(infi_list)):
        infi_len_list.append(len(infi_list[i]))
    infi_len_list_old[:]=infi_len_list
    infi_len_list.sort()
    max_len_index=infi_len_list_old.index(infi_len_list[-1])
    for i in range(0,len(infi_list[max_len_index])):
        temp_group=con[max_len_index][row_index[max_len_index][i]:row_index[max_len_index][i+1]]
        for j in range(0,len(infi_list)):
            if j==max_len_index:
                continue
            else:
                for k in range(0,len(infi_list[j])):
                    if flag_str[max_len_index][i]==flag_str[j][k]:
                        temp_group=temp_group+con[j][row_index[j][k]:row_index[j][k+1]]
        group_list.append(temp_group)
    
    makedir()
    log='_'.join(wafer_ID)+'_rhlvt_npmos'
    log_path='%s.log'%log
    bad_path='%s.list'%log
    log_f=open(log_path,'w')
    bad_f=open(bad_path,'w')
    for i in range(0,len(group_list)):
        convertGroup( group_list[i],infi_list[max_len_index][i],i )
    log_path=os.path.join(os.getcwd(),log_path)
    bad_path=os.path.join(os.getcwd(),bad_path)
    printWait('Please check log file: %s for all log messages\n'%log_path)
    printWait('Please check cleaned file: %s for \n'%bad_path)
    log_f.close() 
    bad_f.close()
        
def convertGroup(group,infi_list,group_no):
    global wafer_ID
    global log_f
    global mode_list
    type_list=['none','NMOS','PMOS']
    print
    print('Group No: %d    Polar Type: %s    Mode Type: %s   W=%f   L=%f'%(group_no,
                                                                             type_list[infi_list[0]],
                                                                            mode_list[infi_list[1]-1],
                                                                            infi_list[2],
                                                                           infi_list[3])),
    print
    log_f.writelines('\nGroup No: %d    Polar Type: %s    Mode Type: %s   W=%f   L=%f\n'%(group_no,
                                                                             type_list[infi_list[0]],
                                                                            mode_list[infi_list[1]-1],
                                                                            infi_list[2],  
                                                                        infi_list[3]))
    try:
        part_index=[]
        part_flag=[]
        part_list=[]
        vbs_flag=0
        for i in range(0,len(group)):
            temp_list=group[i].split(',')
            temp_list[0]=temp_list[0].upper()
            bias_flag=temp_list[0].split('_')
            bias_list=['VBS','IDLIN','IDSAT','VTLIN','VTSAT']
            if bias_flag[0] in bias_list:
                part_index.append(i)
                flag_list=temp_list[0].split('_')
                if flag_list[0]<>'VBS' and ( flag_list[0].startswith('V') or flag_list[0].startswith('I')):
                    flag_str='_'.join(flag_list[:2])
                    part_flag.append(flag_str)
                elif flag_list[0]=='VBS':
                    part_flag.append('VBS')
                    vbs_flag=vbs_flag+1
        part_index.append(len(group))
        for i in range(0,len(part_index)-1):
            part = group[part_index[i]:part_index[i+1]]
            part_list.append(part)
        for j in range(0,(vbs_flag-1)):
            for i in range(0,9):
                part_list[i]=part_list[i]+part_list[i+9+9*j]
        part_list=part_list[0:9]
        part_flag=part_flag[0:9]
        vbs_list,idlin_L,idlin_R,idsat_L,idsat_R,vtlin_L,vtlin_R,vtsat_L,vtsat_R=convertPart(part_list,part_flag)
        
    
        for i in range(0,loop):
            idlin_d=[]
            idsat_d=[]
            vtlin_d=[]
            vtsat_d=[]
            badindex_L=[]
            badindex_R=[]
            alllist=[idlin_L[i],idlin_R[i],idsat_L[i],idsat_R[i],vtlin_L[i],vtlin_R[i],vtsat_L[i],vtsat_R[i]]
            badlist=[[],[],[],[],[],[],[],[]]
            goodlist=[[],[],[],[],[],[],[],[]]
            
            badindex_L=[]
            badindex_R=[]
            for index,key_list in enumerate(alllist):
                if index%2==0:
                    badindex_L.extend(eatError(key_list))
                if index%2==1:
                    badindex_R.extend(eatError(key_list))
            badindex=badindex_L+badindex_R
            for index,key_list in enumerate(alllist):
                if index%2==1:
                    temp_list_L=[]
                    temp_list_R=[]
                    temp_list_L_b=[]
                    temp_list_R_b=[]
                    for j in range(0,len(key_list)):
                        flag=0
                        for k in badindex:
                            if j==k:
                                flag=1
                            else:
                                pass
                        if flag==0:
                            temp_list_R.append(alllist[index][j])
                            temp_list_L.append(alllist[index-1][j])
                        elif flag==1:
                            temp_list_R_b.append(alllist[index][j])
                            temp_list_L_b.append(alllist[index-1][j])                       
                    alllist[index][:]=temp_list_R
                    alllist[index-1][:]=temp_list_L
                    badlist[index][:]=temp_list_R_b
                    badlist[index-1][:]=temp_list_L_b
                    
            
            idlin=idlin_L[i]+idlin_R[i]
            idlin_stdev=calstdev(idlin)
            idlin_mean=calmean(idlin)
            idsat=idsat_L[i]+idsat_R[i]
            idsat_stdev=calstdev(idsat)
            idsat_mean=calmean(idsat)
            vtlin=vtlin_L[i]+vtlin_R[i]
            vtlin_stdev=calstdev(vtlin)
            vtlin_mean=calmean(vtlin)
            vtsat=vtsat_L[i]+vtsat_R[i]
            vtsat_stdev=calstdev(vtsat)
            vtsat_mean=calmean(vtsat)
            
            badindex=[]
            
            if len(idlin_L[i])==len(idlin_R[i]):
                for j in range(0,len(idlin_L[i])):
                    if sigma<>0:
                        if  abs(idlin_L[i][j]-idlin_mean) < sigma*abs(idlin_stdev) and abs(idlin_R[i][j]-idlin_mean) < sigma*abs(idlin_stdev):
                            pass
                        else:
                            badindex.append(j)
            else:
                continue
            if len(idsat_L[i])==len(idsat_R[i]):
                for j in range(0,len(idsat_L[i])):
                    if sigma<>0:
                        if abs(idsat_L[i][j]-idsat_mean)< sigma*abs(idsat_stdev) and abs(idsat_R[i][j]-idsat_mean) <sigma*abs(idsat_stdev):
                            pass
                        else:
                            badindex.append(j)
            else:
                continue
            if len(vtlin_L[i])==len(vtlin_R[i]):
                for j in range(0,len(vtlin_L[i])):
                    if sigma <> 0:
                        if abs(vtlin_L[i][j]-vtlin_mean) < sigma*abs(vtlin_stdev) and abs(vtlin_R[i][j]-vtlin_mean) < sigma*abs(vtlin_stdev):
                            pass
                        else:
                            badindex.append(j)
            else:
                continue
            if len(vtsat_L[i])==len(vtsat_R[i]):
                for j in range(0,len(vtsat_L[i])):
                    if sigma<>0:
                        if abs(vtsat_L[i][j]-vtsat_mean)<sigma*abs(vtsat_stdev) and abs(vtsat_R[i][j]-vtsat_mean) <sigma*abs(vtsat_stdev):
                            pass
                        else:
                            badindex.append(j)
            else:
                continue
            
            if len(idlin_L[i])==len(idlin_R[i]):
                if sigma<>0:
                    for j in range(0,len(idlin_L[i])):
                        flag=0
                        for k in badindex:
                            if k==j:
                                flag=1
                            else:
                                pass
                        if flag==0:                        
                            idlin_d.append(string.atof(idlin_L[i][j])-string.atof(idlin_R[i][j]))
                            goodlist[0].append(idlin_L[i][j])
                            goodlist[1].append(idlin_R[i][j])
                        else:
                            badlist[0].append(idlin_L[i][j])
                            badlist[1].append(idlin_R[i][j])
                else:
                    for j in range(0,len(idlin_L[i])):
                        idlin_d.append(string.atof(idlin_L[i][j])-string.atof(idlin_R[i][j]))
                    goodlist[0][:]=idlin_L[i]
                    goodlist[1][:]=idlin_R[i]
                    
                idlin_d_stdev=calstdev(idlin_d)
                good_list=goodlist[0]+goodlist[1]
                idlin_stdev=calstdev(good_list)                               
            else:
                continue
            if len(idsat_L[i])==len(idsat_R[i]):
                if sigma<>0:
                    for j in range(0,len(idsat_L[i])):
                        flag=0
                        for k in badindex:
                            if k==j:
                                flag=1
                            else:
                                pass
                        if flag==0:                        
                            idsat_d.append(string.atof(idsat_L[i][j])-string.atof(idsat_R[i][j]))
                            goodlist[2].append(idsat_L[i][j])
                            goodlist[3].append(idsat_R[i][j])
                        else:
                            badlist[2].append(idsat_L[i][j])
                            badlist[3].append(idsat_R[i][j])
                else:
                    for j in range(0,len(idsat_L[i])):
                        idsat_d.append(string.atof(idsat_L[i][j])-string.atof(idsat_R[i][j]))
                    goodlist[2][:]=idsat_L[i]
                    goodlist[3][:]=idsat_R[i]
                    
                idsat_d_stdev=calstdev(idsat_d)
                good_list=goodlist[2]+goodlist[3]
                idsat_stdev=calstdev(good_list)                               
            else:
                continue
            if len(vtlin_L[i])==len(vtlin_R[i]):
                if sigma<>0:
                    for j in range(0,len(vtlin_L[i])):
                        flag=0
                        for k in badindex:
                            if k==j:
                                flag=1
                            else:
                                pass
                        if flag==0:                        
                            vtlin_d.append(string.atof(vtlin_L[i][j])-string.atof(vtlin_R[i][j]))
                            goodlist[4].append(vtlin_L[i][j])
                            goodlist[5].append(vtlin_R[i][j])
                        else:
                            badlist[4].append(vtlin_L[i][j])
                            badlist[5].append(vtlin_R[i][j])
                else:
                    for j in range(0,len(vtlin_L[i])):
                        vtlin_d.append(string.atof(vtlin_L[i][j])-string.atof(vtlin_R[i][j]))
                    goodlist[4][:]=vtlin_L[i]
                    goodlist[5][:]=vtlin_R[i]
                    
                vtlin_d_stdev=calstdev(vtlin_d)
                good_list=goodlist[4]+goodlist[5]
                vtlin_stdev=calstdev(good_list)                               
            else:
                continue
            if len(vtsat_L[i])==len(vtsat_R[i]):
                if sigma<>0:
                    for j in range(0,len(vtsat_L[i])):
                        flag=0
                        for k in badindex:
                            if k==j:
                                flag=1
                            else:
                                pass
                        if flag==0:                        
                            vtsat_d.append(string.atof(vtsat_L[i][j])-string.atof(vtsat_R[i][j]))
                            goodlist[6].append(vtsat_L[i][j])
                            goodlist[7].append(vtsat_R[i][j])
                        else:
                            badlist[6].append(vtsat_L[i][j])
                            badlist[7].append(vtsat_R[i][j])
                else:
                    for j in range(0,len(vtsat_L[i])):
                        vtsat_d.append(string.atof(vtsat_L[i][j])-string.atof(vtsat_R[i][j]))
                    goodlist[6][:]=vtsat_L[i]
                    goodlist[7][:]=vtsat_R[i]
                    
                vtsat_d_stdev=calstdev(vtsat_d)
                good_list=goodlist[6]+goodlist[7]
                vtsat_stdev=calstdev(good_list)                               
            else:
                continue
            
                        
            
            
            if True:#mean == 'on' :
                if (idlin_stdev**2 - (idlin_d_stdev**2)/2)<0:
                    log_f.writelines('Idlin --> Bias No %d  Warning: the local variation is larger than the total variation!\n'%(i+1))
                    printResult('Idlin --> Bias No %d  Warning: the local variation is larger than the total variation!'%(i+1))
                    print
                    idlin_final_g =0
                else:
                    idlin_final_g = (((idlin_stdev**2 - (idlin_d_stdev**2)/2))**0.5)*1e-6
                if (idsat_stdev**2 - (idsat_d_stdev**2)/2)<0:
                    log_f.writelines('Idsat --> Bias No %d  Warning: the local variation is larger than the total variation!\n'%(i+1))
                    printResult('Idsat --> Bias No %d  Warning: the local variation is larger than the total variation!'%(i+1))
                    print
                    idsat_final_g =0
                else:
                    idsat_final_g = (((idsat_stdev**2 - (idsat_d_stdev**2)/2))**0.5)*1e-3
                idlin_final_l = idlin_d_stdev/abs(idlin_mean)
                idsat_final_l = idsat_d_stdev/abs(idsat_mean)
    
            else:
                pass
            
            if (vtlin_stdev**2 - (vtlin_d_stdev**2)/2)<0:
                log_f.writelines('vtlin --> Bias No %d  Warning: the local variation is larger than the total variation!\n'%(i+1))
                printResult('vtlin --> Bias No %d  Warning: the local variation is larger than the total variation!'%(i+1))
                print
                vtlin_final_g =0
            else:
                vtlin_final_g = abs(((vtlin_stdev**2 - (vtlin_d_stdev**2)/2)**0.5))
                
            if (vtsat_stdev**2 - (vtsat_d_stdev**2)/2)<0:
                log_f.writelines('vtsat --> Bias No %d  Warning: the local variation is larger than the total variation!\n'%(i+1))
                printResult('vtsat --> Bias No %d  Warning: the local variation is larger than the total variation!'%(i+1))
                print
                vtsat_final_g =0
            else:
                vtsat_final_g = abs(((vtsat_stdev**2 - (vtsat_d_stdev**2)/2)**0.5))
            
            vtsat_final_l = vtsat_d_stdev
            vtlin_final_l = vtlin_d_stdev
            
            writeFile(wafer_ID,infi_list,vbs_list[i],idlin_final_g,idlin_final_l,idsat_final_g,idsat_final_l,
                      vtsat_final_g,vtsat_final_l,vtlin_final_g,vtlin_final_l,badlist,goodlist)
            
            if False:#mean == 'OFF':
                idlin_final_l= idlin_final_l *abs(idlin_mean)* 1e-6
                idsat_final_l= idsat_final_l *abs(idsat_mean)* 1e-3
                writekickMean(wafer_ID,infi_list,vbs_list[i],idlin_final_l, idsat_final_l)
    except:
        log_f.writelines('Bias no %d:    Failed\n'%(group_no+1))
        printError('Bias no %d:    Failed'%(group_no+1))
        print
def convertPart(part_list, part_flag):
    global mean
    global sigma
    global loop
    
    idlin_L=[]
    idlin_R=[]
    idsat_L=[]
    idsat_R=[]
    vtlin_L=[]
    vtlin_R=[]
    vtsat_L=[]
    vtsat_R=[]
    for i, part_str in enumerate(part_flag):
        if part_str == 'VBS':
            vbs_list = vbsconvert(part_list[i][2])
            loop=len(vbs_list)
        elif part_str.startswith('IDLIN_1'):
            idlin_L = partconvert(part_list[i])
        elif part_str.startswith('IDLIN_2'):
            idlin_R = partconvert(part_list[i])
        elif part_str.startswith('IDSAT_1'):
            idsat_L = partconvert(part_list[i])
        elif part_str.startswith('IDSAT_2'):
            idsat_R = partconvert(part_list[i])
        elif part_str.startswith('VTLIN_1'):
            vtlin_L = partconvert(part_list[i])
        elif part_str.startswith('VTLIN_2'):
            vtlin_R = partconvert(part_list[i])
        elif part_str.startswith('VTSAT_1'):
            vtsat_L = partconvert(part_list[i])
        elif part_str.startswith('VTSAT_2'):
            vtsat_R = partconvert(part_list[i])
    return [vbs_list,idlin_L,idlin_R,idsat_L,idsat_R,vtlin_L,vtlin_R,vtsat_L,vtsat_R]
    

        
            
def getinfi( vbsstring ):
    global mode_list
    infi=[]
    temp_list=vbsstring.split(',')
    infi_list=temp_list[0].split('_')
    for i in range(0,len(infi_list)):
        infi_list[i]=infi_list[i].upper()
    
    infi_list[-3]=infi_list[-3].upper()
    if infi_list[-3] .startswith('NMOS'):
        infi.append(1)
    elif infi_list[-3].startswith('PMOS'):
        infi.append(-1)
    
    mode_temp = list(infi_list[-3])
    mode_temp.reverse()
    index=0
    for i in range(0,len(mode_temp)):
        if mode_temp[i].isdigit():
            index=i
            break
        else:
            pass
    mode=mode_temp[0:index]
    mode.reverse()
    mode=''.join(mode)
    if mode == 'VT':
        mode='LVT'
    if mode in mode_list:
        pass
    else:
        mode_list.append(mode)
    for i in range( 0,len(mode_list)):
        if mode_list[i]==mode:
            infi.append(i+1)
            
#    if infi_list[i].endswith('RVT'):
#        infi.append(1) 
#    elif infi_list[i].endswith('HVT'):
#        infi.append(2)
#    elif infi_list[i].endswith('LVT'):
#        infi.append(3)
#    elif infi_list[i].endswith('VT'):
#        infi.append(3)
#    elif infi_list[i].endswith('T'):
#        infi.append(3)
            
    L_str=infi_list[-1].replace('D','.')
    W_str=infi_list[-2].replace('D','.')
    infi.append(string.atof(L_str))
    infi.append(string.atof(W_str))
    
    return infi

def vbsconvert(vbs_str):
    vbslist=[]
    temp_list = vbs_str.split(',')
    for i in range(1,len(temp_list)):
        try:
            vbslist.append(string.atof(temp_list[i]))
        except:
            pass
    return vbslist
    
def partconvert(part):
    global loop
    re_list=[]
    for i in range(0,loop):
        re_list.append([])
    for i in range(1,len(part)):
        temp_list=part[i].split(',')
        if temp_list[0]<>'':
            for j in range(1,loop+1):
                try:
                    re_list[j-1].append(string.atof(temp_list[j]))
                except:
                    pass
    return re_list
 
def eatError(orilist):
    badindex=[]
    pos=[]
    neg=[]
    polar=[]
    ori_list=[]

    ori_list[:]=orilist
    orilist.sort()
    n=len(orilist)
    for i in range((n//2-2),(n//2+3)):
        if orilist[i]>=0:
            pos.append(orilist[i])
        else:
            neg.append(orilist[i])
    if len(pos)>len(neg):
        polar.extend(pos)
    else:
        polar.extend(neg)
    stander=calmean(polar[(len(polar)//2-3):(len(polar)//2+3)])
    
    for i in range(0,len(ori_list)):
        if ori_list[i]/stander>0 and (abs(ori_list[i])/abs(stander)>0.4 and abs(ori_list[i])/abs(stander)<2.5):
            pass
        else:
            badindex.append(i)
    orilist[:]=ori_list
    return badindex
            
def calstdev(valuelist):
    value_list=[]
    if len(valuelist)==0:
        return 0
    if type(valuelist[0])==str:
        for i in range(0,len(valuelist)):
            value_list.append(string.atof(valuelist[i])) 
    else:
        value_list.extend(valuelist)
    totle1= 0 
    totle2=0 
    for i in range(0,len(value_list)):
        totle1 = totle1+ value_list[i]**2
        totle2 = totle2+ value_list[i]
    n=len(value_list)
    stdev=((totle1*n - totle2**2)/(n*(n-1)))**0.5
    return stdev

def calmean(valuelist):
    value_list=[]
    for i in range(0,len(valuelist)):
        value_list.append(string.atof(valuelist[i])) 
    total=0
    for i in range(0,len(valuelist)):
        total=total+value_list[i]
    mean=total/(len(valuelist))
    return mean
    
    
def getSigma(input):
    global mean
    global sigma
    temp_list=input.split()
    for i in range(0,len(temp_list)):
        temp_list[i]=temp_list[i].upper()
        if temp_list[i].startswith('MEAN'):
            mean=temp_list[i].split('=')[-1]
        elif temp_list[i].startswith('SIGMA'):
            sigma=temp_list[i].split('=')[-1]
            sigma=string.atoi(sigma)
def writekickMean(wafer_ID,infi_list,vbs,idlin_final_l, idsat_final_l):
    global mode_list
    name_list=[]
    if len(wafer_ID)<>0:
        name_list.append('_'.join(wafer_ID))
    if infi_list[0]==1:
        name_list.append('NMOS')
    else:
        name_list.append('PMOS')
    name_list.append(mode_list[infi_list[1]-1])
#    if infi_list[1]== 1:
#        name_list.append('RVT')
#    elif infi_list[1]== 2:
#        name_list.append('HVT')
#    elif infi_list[1]== 3:
#        name_list.append('LVT')
    l=repr(infi_list[-2])
    w=repr(infi_list[-1])
    name_list.append(repr(vbs))
    name_str='_'.join(name_list)
    name_str_l=name_str+'_strip_mean'
    file_path=createFile(name_str_l)
    if os.path.exists(file_path):
        f=open(file_path,'a')
        f.writelines('%-10s%-10s'%(w,l)+'%-25e%-25e'%(idlin_final_l,idsat_final_l)+'\n')
        f.close()
    else:
        f=open(file_path,'w')
        f.writelines('%-10s%-10s'%('w','l')+'%-25s%-25s'%('idlin_final_l','idsat_final_l')+'\n')
        f.writelines('%-10s%-10s'%(w,l)+'%-25e%-25e'%(idlin_final_l,idsat_final_l)+'\n')
        f.close()
def writeFile(wafer_ID,infi_list,vbs,idlin_final_g,idlin_final_l,idsat_final_g,idsat_final_l,vtsat_final_g,vtsat_final_l,vtlin_final_g,vtlin_final_l,badlist,goodlist):
    global bad_f
    global mode_list
    name_list=[]
    if len(wafer_ID)<>0:
        name_list.append('_'.join(wafer_ID))
    if infi_list[0]==1:
        name_list.append('NMOS')
        d_type='NMOS'
    else:
        name_list.append('PMOS')
        d_type='PMOS'
    name_list.append(mode_list[infi_list[1]-1])
#    if infi_list[1]== 1:
#        name_list.append('RVT')
#    elif infi_list[1]== 2:
#        name_list.append('HVT')
#    elif infi_list[1]== 3:
#        name_list.append('LVT')
    l=repr(infi_list[-2])
    w=repr(infi_list[-1])
    name_list.append(repr(vbs))
    name_str='_'.join(name_list)
    name_str_g=name_str+'_global'+'.gspec'
    name_str_l=name_str+'_local'+'.lspec'
    name_str_raw=name_str+'_raw'+'.gwat'
    name_str_delta=name_str+'_delta'+'.lwat'
    
    delta=[[],[],[],[]]
    raw=[[],[],[],[]]

######################creat good and delete file
    bad_f.writelines("Type=%s     Mode=%s       vbs=%f         l=%s       w=%s\n"%(d_type,name_list[-2],vbs,l,w))
    flag_str=["%-25s%-25s\n"%('idlin_L','idlin_R'),\
               "%-25s%-25s\n"%('idsat_L','idsat_R'),\
               "%-25s%-25s\n"%('vtlin_L','vtlin_R'),\
               "%-25s%-25s\n"%('vtsat_L','vtsat_R'),]
    for i in range(0,len(goodlist)):
        if i%2==0:
            raw_l_list=[]
            raw_r_list=[]
            bad_f.writelines(flag_str[i//2])
            for j in range(0,len(goodlist[i])):
                bad_f.writelines('%-25s%-25s\n'%(goodlist[i][j],goodlist[i+1][j]))
                
                if i//2==0:
                    delta_value=(goodlist[i][j]-goodlist[i+1][j])*1e-6
                    raw_l=goodlist[i][j]*1e-6
                    raw_r=goodlist[i+1][j]*1e-6
                elif i//2==1:
                    delta_value=(goodlist[i][j]-goodlist[i+1][j])*1e-3
                    raw_l=goodlist[i][j]*1e-3
                    raw_r=goodlist[i+1][j]*1e-3
                else:
                    delta_value=goodlist[i][j]-goodlist[i+1][j]
                    raw_l=goodlist[i][j]
                    raw_r=goodlist[i+1][j]                  
                delta[i//2].append('%e'%delta_value)
                
                raw_l_list.append('%e'%raw_l)
                raw_r_list.append('%e'%raw_r)
            temp_list=raw_l_list+raw_r_list
            raw[i//2].extend(temp_list)
                
            bad_f.writelines('\n')
            bad_f.writelines('Delete data\n')
            for j in range(0,len(badlist[i])):
                bad_f.writelines('%-25s%-25s\n'%(badlist[i][j],badlist[i+1][j]))
            bad_f.writelines('\n')
            bad_f.writelines('\n')
    
#####################creat global spec
    file_path=createFile(name_str_g)
    if os.path.exists(file_path):
        f=open(file_path,'a')
        writelist=['.START_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l),\
                   'idlin                    idsat                    vtlin                    vtsat',\
                   '%-25e%-25e%-25e%-25e'%(idlin_final_g,idsat_final_g,vtlin_final_g,vtsat_final_g),\
                   '.END_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l)]
        f.writelines('\n'.join(writelist)+'\n')
        f.close()
    else:
        f=open(file_path,'w')
        writelist=['#',\
                   '# GLOBAL section -- global variables',\
                   '#',\
                   '.START_GLOBAL',\
                   '#Name	#Value',\
                   'INSTANCE_COL	3',\
                    'VDD	5	NMOS',\
                    'VDTHX	0.1	NMOS',\
                    'CC_VAL	1.00E-07	NMOS',\
                    'VDD	-5	PMOS',\
                    'VDTHX	-0.1	PMOS',\
                    'CC_VAL	-1.00E-07	PMOS',\
                    '.END_GLOBAL',\
                    '',\
                    '.START_OUTPUT',\
                    '#Output_Name	#Key_Output_Name	# ERROR expression	# the criteria of on-target	#Bias',\
                    'vtsat	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdd	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'vtlin	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdthx	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'idsat	Idsat	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdd	Vbs=0',\
                    'idlin	Idlin	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdthx	Vbs=0',\
                    '.END_OUTPUT',\
                    '',\
                    '# Output Spec values (Sigma) for %s device'%d_type,
                    '.START_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l),\
                    'idlin                    idsat                    vtlin                    vtsat',\
                    '%-25e%-25e%-25e%-25e'%(idlin_final_g,idsat_final_g,vtlin_final_g,vtsat_final_g),\
                    '.END_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l)]
        f.writelines('\n'.join(writelist)+'\n')
        f.close()
        
###############creat local spec
    file_path=createFile(name_str_l)
    if os.path.exists(file_path):
        f=open(file_path,'a')
        writelist=['.START_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l),\
                   'idlin                    idsat                    vtlin                    vtsat',\
                   '%-25e%-25e%-25e%-25e'%(idlin_final_l,idsat_final_l,vtlin_final_l,vtsat_final_l),\
                   '.END_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l)]
        f.writelines('\n'.join(writelist)+'\n')
        f.close()
    else:
        f=open(file_path,'w')
        writelist=['#',\
                   '# GLOBAL section -- global variables',\
                   '#',\
                   '.START_GLOBAL',\
                   '#Name	#Value',\
                   'INSTANCE_COL	3',\
                    'VDD	5	NMOS',\
                    'VDTHX	0.1	NMOS',\
                    'CC_VAL	1.00E-07	NMOS',\
                    'VDD	-5	PMOS',\
                    'VDTHX	-0.1	PMOS',\
                    'CC_VAL	-1.00E-07	PMOS',\
                    '.END_GLOBAL',\
                    '',\
                    '.START_OUTPUT',\
                    '#Output_Name	#Key_Output_Name	# ERROR expression	# the criteria of on-target	#Bias',\
                    'vtsat	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdd	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'vtlin	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdthx	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'idsat	Idsat	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdd	Vbs=0',\
                    'idlin	Idlin	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdthx	Vbs=0',\
                    '.END_OUTPUT',\
                    '',\
                    '# Output Spec values (Local Variation) for %s device'%d_type,
                    '.START_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l),\
                    'idlin                    idsat                    vtlin                    vtsat',\
                    '%-25e%-25e%-25e%-25e'%(idlin_final_l,idsat_final_l,vtlin_final_l,vtsat_final_l),\
                    '.END_DATA|%s|W=%s|L=%s|T=25'%(d_type,w,l)]
        f.writelines('\n'.join(writelist)+'\n')
        f.close()
        
#########################creat raw data wat file
    file_path=createFile(name_str_raw)
    raw_con=[]
    if os.path.exists(file_path):
        f=open(file_path,'a')
        title='.START_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)+'idlin                    idsat                    vtlin                    vtsat\n'
        tail='.END_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)
        raw_ori=[]
        for i in range(0,len(raw)):
            raw_ori.append(len(raw[i]))
        raw_ori.sort()
        
        for i in range(0,len(raw)):
            for j in range(0,(raw_ori[-1]-len(raw[i]))):
                raw[i].append('')
                
        
        f.writelines(title)
        for i in range(0,raw_ori[-1]):
            raw_con.append('%-25s%-25s%-25s%-25s'%(raw[0][i],raw[1][i],raw[2][i],raw[3][i]))
        f.writelines('\n'.join(raw_con)+'\n')
        f.writelines(tail)
        f.close()
    else:
        f=open(file_path,'w')
        title='.START_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)+'idlin                    idsat                    vtlin                    vtsat\n'
        tail='.END_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)
        writelist=['#',\
                   '# GLOBAL section -- global variables',\
                   '#',\
                   '.START_GLOBAL',\
                   '#Name	#Value',\
                   'INSTANCE_COL	3',\
                    'VDD	5	NMOS',\
                    'VDTHX	0.1	NMOS',\
                    'CC_VAL	1.00E-07	NMOS',\
                    'VDD	-5	PMOS',\
                    'VDTHX	-0.1	PMOS',\
                    'CC_VAL	-1.00E-07	PMOS',\
                    '.END_GLOBAL',\
                    '',\
                    '.START_OUTPUT',\
                    '#Output_Name	#Key_Output_Name	# ERROR expression	# the criteria of on-target	#Bias',\
                    'vtsat	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdd	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'vtlin	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdthx	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'idsat	Idsat	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdd	Vbs=0',\
                    'idlin	Idlin	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdthx	Vbs=0',\
                    '.END_OUTPUT',\
                    '',\
                    '# Output Spec values (Local Variation) for %s device'%d_type]
        f.writelines('\n'.join(writelist)+'\n')
        raw_ori=[]
        for i in range(0,len(raw)):
            raw_ori.append(len(raw[i]))
        raw_ori.sort()
        
        for i in range(0,len(raw)):
            for j in range(0,(raw_ori[-1]-len(raw[i]))):
                raw[i].append('')
                
        
        f.writelines(title)
        for i in range(0,raw_ori[-1]):
            raw_con.append('%-25s%-25s%-25s%-25s'%(raw[0][i],raw[1][i],raw[2][i],raw[3][i]))
        f.writelines('\n'.join(raw_con)+'\n')
        f.writelines(tail)
        f.close()
        f.close()



#########################creat delta data wat file
    file_path=createFile(name_str_delta)
    delta_con=[]
    if os.path.exists(file_path):
        f=open(file_path,'a')
        title='.START_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)+'idlin                    idsat                    vtlin                    vtsat\n'
        tail='.END_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)
        
        delta_ori=[]
        for i in range(0,len(delta)):
            delta_ori.append(len(delta[i]))
        delta_ori.sort()
        
        for i in range(0,len(delta)):
            for j in range(0,(delta_ori[-1]-len(delta[i]))):
                delta[i].append('')
                
        
        f.writelines(title)
        for i in range(0,delta_ori[-1]):
            delta_con.append('%-25s%-25s%-25s%-25s'%(delta[0][i],delta[1][i],delta[2][i],delta[3][i]))
        f.writelines('\n'.join(delta_con)+'\n')
        f.writelines(tail)
        f.close()
    else:
        f=open(file_path,'w')
        writelist=['#',\
                   '# GLOBAL section -- global variables',\
                   '#',\
                   '.START_GLOBAL',\
                   '#Name	#Value',\
                   'INSTANCE_COL	3',\
                    'VDD	5	NMOS',\
                    'VDTHX	0.1	NMOS',\
                    'CC_VAL	1.00E-07	NMOS',\
                    'VDD	-5	PMOS',\
                    'VDTHX	-0.1	PMOS',\
                    'CC_VAL	-1.00E-07	PMOS',\
                    '.END_GLOBAL',\
                    '',\
                    '.START_OUTPUT',\
                    '#Output_Name	#Key_Output_Name	# ERROR expression	# the criteria of on-target	#Bias',\
                    'vtsat	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdd	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'vtlin	Vth_CC	Error=(Model-Target)*1000	Error<10	Vds=Vdthx	Vbs=0	CC=CC_VAL	L_Offset=0	W_Offset=0	Current=Id',\
                    'idsat	Idsat	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdd	Vbs=0',\
                    'idlin	Idlin	Error=(Model/Target-1)*100	Error<10	Vgs=Vdd	Vds=Vdthx	Vbs=0',\
                    '.END_OUTPUT',\
                    '',\
                    '# Output Spec values (Local Variation) for %s device'%d_type]
        f.writelines('\n'.join(writelist)+'\n')
        title='.START_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)+'idlin                    idsat                    vtlin                    vtsat\n'
        tail='.END_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)
        
        delta_ori=[]
        for i in range(0,len(delta)):
            delta_ori.append(len(delta[i]))
        delta_ori.sort()
        
        for i in range(0,len(delta)):
            for j in range(0,(delta_ori[-1]-len(delta[i]))):
                delta[i].append('')
                
        
        f.writelines(title)
        for i in range(0,delta_ori[-1]):
            delta_con.append('%-25s%-25s%-25s%-25s'%(delta[0][i],delta[1][i],delta[2][i],delta[3][i]))
        f.writelines('\n'.join(delta_con)+'\n')
        f.writelines(tail)
        f.close()

def createFile(filename):
    cwdpath=os.getcwd()
    templist=filename.split('_')
    for i in range(0,len(templist)):
        if templist[i].endswith('MOS'):
            polar=templist[i]
        elif templist[i].endswith('T'):
            mode=templist[i]
            
    temp_path=os.path.join(mode,polar)
    path=os.path.join(temp_path,filename)
    path=os.path.join(cwdpath,path)
    return path
    
def makedir():
    global wafer_ID
    global mode_list
    dataname='_'.join(wafer_ID)+'_rhlvt_npmos'
    root = os.path.join('Converted data',dataname)
    for mode in mode_list:
        for polar in ['NMOS','PMOS']:
            path= os.path.join(root,mode)
            path=os.path.join(path,polar)
            if not os.path.exists(path):
                os.makedirs(path)
    os.chdir(root)

def findspecfile():
    
    global speclist
    speclist=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for mem in files:
            if mem.split('.')[-1].find('spec')<>-1:
                if mem.find('global')<>-1:
                    continue
                mem=os.path.join(root,mem)
                speclist.append(mem) 
                
def plot(filename,show_flag=0):
    f=open(filename)
    content=f.readlines()
    f.close()
    x=[]
    idlin=[]
    idsat=[]
    vtlin=[]
    vtsat=[]
    for i in range(0,len(content)):
        if content[i].startswith('.START_DATA'):
            temp_list=content[i].split('|')
            w_str=temp_list[-3].split('=')[-1]
            l_str=temp_list[-2].split('=')[-1]
            w=string.atof(w_str)
            l=string.atof(l_str)
            x.append(1/((w*l)**0.5))
        elif content[i].startswith('idlin') and content[i].endswith('vtsat\n'):
            temp_list=content[i+1].split()
            idlin.append(string.atof(temp_list[0]))
            idsat.append(string.atof(temp_list[1]))
            vtlin.append(string.atof(temp_list[2]))
            vtsat.append(string.atof(temp_list[3]))
    x=np.array(x)
    idlin=np.array(idlin)
    idsat=np.array(idsat)
    vtlin=np.array(vtlin)
    vtsat=np.array(vtsat)
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if show_flag<>'vt':
        ax.plot(x, idlin,'s',color='b',label="idlin")
        ax.plot(x, idsat,'o',color='r',label="idsat")
    if show_flag<>'id':
        ax.plot(x, vtlin, 'x',color='g',label="vtlin")
        ax.plot(x, vtsat, 'h',color='k',label="vtsat")
    ax.legend(bbox_to_anchor = (1, 0.28))
    ax.set_title(os.path.basename(filename))
    if show_flag<>0:
        plt.show()
        plt.close()
    else:
        png_path='.'.join(filename.split('.')[:-1]) + '.png'
        plt.savefig(png_path)
        plt.close()
        printWait('plot %s...\n'%filename)
       
if __name__ == '__main__':
    
    printWait('''*****************************************************************************
1.If you will delete the data out of n sigma just input sigma=n
2.If you want to check a specific .spec file's figure, input the file's name
  like '8_NMOS_HVT_-0.6_local.lspec', '8_NMOS_HVT_-0.6_local.lspec -id' for 
  idlin and idsat figure only and '8_NMOS_HVT_-0.6_local.lspec -vt' for
  vtsat and vtline figure only.
3.Input 'q' to exit
*****************************************************************************\n''')
    c_input=raw_input()
    while(c_input<>'q' and c_input<>'Q'):
        getSigma(c_input)
        if c_input.find('spec')<>-1:
            findspecfile()
            flag=0
            show_flag=1
            temp_list=c_input.split(' ')
            for i in range(0,len(temp_list)):
                if temp_list[i].find('spec')<>-1:
                    spec_name=temp_list[i].rstrip('\"\'')
                    spec_name=spec_name.lstrip('\"\'')
                elif temp_list[i].upper()=='-ID':
                    show_flag='id'
                elif temp_list[i].upper()=='-VT':
                    show_flag='vt'
                    
            for i in range(0,len(speclist)):
                if speclist[i].endswith(spec_name):
                    flag=1
                    plot(speclist[i],show_flag)
            if flag==0:
                printError('No such spec file!')
        else:
            if os.path.exists('Converted data'):
                shutil.rmtree('Converted data')
            findFile()
            #for i, data in enumerate( convertlist ):
            current=os.getcwd()
            convertFile()
            os.chdir(os.pardir)
            os.chdir(os.pardir)
            print
            printResult('Plot spec figure... \n')
            findspecfile()
            for i in range (0,len(speclist)):
                show_flag=0
                plot(speclist[i],show_flag)
        print 
        printWait('''*****************************************************************************
1.If you will delete the data out of n sigma just input sigma=n
2.If you want to check a specific .spec file's figure, input the file's name
  like '8_NMOS_HVT_-0.6_local.lspec', '8_NMOS_HVT_-0.6_local.lspec -id' for 
  idlin and idsat figure only and '8_NMOS_HVT_-0.6_local.lspec -vt' for
  vtsat and vtline figure only.
3.Input 'q' to exit
*****************************************************************************\n''')
        c_input=raw_input()
