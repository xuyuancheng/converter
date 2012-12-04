# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:32:42 2012

@author: zhaiyt
"""

#from __future__ import division
import os
import sys
from shellcolor import *
from math import exp
import copy



global convertlist
convertlist=[]
global tdt_def
tdt_def=''
global Scref
Scref=3

def findFile():
    global tdt_def
    global convertlist
    convertlist=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for mem in files:
            if mem.split('.')[-1]=='dat':
                mem=os.path.join(root,mem)
                convertlist.append(mem)
            elif mem == 'WPE_tdt_def':
                tdt_def=os.path.join(root,mem)
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
            
def parser():
    global tdt_def
    output_list=[]
    if tdt_def=='':
        printError("Can't find the tdt defination file")
        sys.exit()
    try:
        f=open(tdt_def,'r')
    except:
        printError("Can't open the tdt defination file")
        sys.exit()
    printProcess("Read the tdt defination file")
    content=f.readlines()
    start=0
    end=0
    for i in range(0,len(content)):
        if content[i].startswith('.START_OUTPUT'):
            start=i+1
        elif content[i].startswith('.END_OUTPUT'):
            end=i
    if start==0 or end==0:
        printError("Can't find the output difination part in tdt difination file")
        sys.exit()
    output=content[start:end]
    for i in range(0,len(output)):
        if not output[i].startswith('#'):
            temp_list=output[i].split()
            temp_list[0]=temp_list[0].upper()
            output_list.append(temp_list[0])
    if output_list==[]:
        printError("No output defination part found in tdt difination file")
        sys.exit()
    return output_list
        
def convert(convert_file):
    file_name=os.path.basename(convert_file)
    file_name=file_name.split('.')[0]
    try:
        in_file=open(convert_file,'r')
    except:
        printError("ERROR: Can't open file %s"%convert_file)
        sys.exit()
    content=in_file.readlines()
    out_name=''
    body_list=[]
    n_group_index=[]
    p_group_index=[]
    
    #parser the tdt defination file and get the keylist
    tdt_key_list=parser()
    
    #get group key and key_list
    group_key=''
    for i in range(0,len(content)):
        temp_list=content[i].split(',')
        if len(temp_list)<3:
            pass
        else:
            temp_list=temp_list[0].split('_')
            if len(temp_list)>3:
                group_key=temp_list[0]
                break
            else:
                pass      
    if group_key=='':
        printError("Can't get the data session")
        sys.exit()
        
    for i in range(0,len(content)):
        content[i]=content[i].strip('\n')
        if content[i].startswith('SYS_WAFERID'):
            out_name=getFilename(content[i])
            die_list=getDie(content[:i])
            for j in range(0,len(die_list)):
                die_str='#Die '+die_list[j]
                body_list.append([die_str])
        elif content[i].startswith(group_key):
            temp_list=content[i].split('_')
            if temp_list[2].startswith('N'):
                n_group_index.append(i)
            elif temp_list[2].startswith('P'):
                p_group_index.append(i)
    if n_group_index<>[]:
        if len(n_group_index)==1:
            first_group=content[n_group_index[0]:len(content)]
        else:
            first_group=content[n_group_index[0]:n_group_index[1]]
    elif p_group_index<>[]:
        if len(n_group_index)==1:
            first_group=content[p_group_index[0]:len(content)]
        else:
            first_group=content[p_group_index[0]:p_group_index[1]]
    group_key_list=[]
    unit_list=[]
    for i in range(0,len(first_group)):
        temp_list=first_group[i].split(',')
        unit_list.append(temp_list[3])
        temp_list=temp_list[0].split('_')
        temp_list[0]=temp_list[0].upper()
        group_key_list.append(temp_list[0])
        
    #key_list match?
    for i in range(0,len(tdt_key_list)):
        if not tdt_key_list[i] in group_key_list:
            printError("Can't find define output %s in data file %s"%(tdt_key_list[i],file_name))
            sys.exit()
        else:
            pass
    
    # get data head list
    key_list_output=[]
    unit_list_output=[]    
    for i in range(0,len(group_key_list)):
        if group_key_list[i] in tdt_key_list:
            key_list_output.append(group_key_list[i])
            unit_list_output.append(unit_list[i])
        
        
    #get group list
    n_group_list=[]
    p_group_list=[]
    
    out_num=len(group_key_list)
    
    body_list_n=copy.deepcopy(body_list)
    body_list_p=copy.deepcopy(body_list)
    for i in range(0,len(n_group_index)):
        if i+out_num>len(content):
            pass
        else:
            n_group_list.append(content[n_group_index[i]:(n_group_index[i]+out_num)])
    for group in n_group_list:
        instance=get_s(group[0])
        for i in range(0,len(instance)):
            instance[i]=str(instance[i])
        instance_list=[]
        instance_list.extend(instance)
        key_list=[]
        for i in range(0,len(group)):
            if judge(group[i],tdt_key_list):
                key_list=get_value(group[i],key_list,instance_list,len(body_list))
        for i in range(0,len(key_list)):
            key_list[i]='    '.join(key_list[i])
            body_list_n[i].append(key_list[i])
            
    for i in range(0,len(p_group_index)):
        if i+out_num>len(content):
            pass
        else:
            p_group_list.append(content[p_group_index[i]:(p_group_index[i]+out_num)])
    for group in p_group_list:
        instance=get_s(group[0])
        for i in range(0,len(instance)):
            instance[i]=str(instance[i])
        instance_list=[]
        instance_list.extend(instance)
        key_list=[]
        for i in range(0,len(group)):
            if judge(group[i],tdt_key_list):
                key_list=get_value(group[i],key_list,instance_list,len(body_list))
        for i in range(0,len(key_list)):
            key_list[i]='    '.join(key_list[i])
            body_list_p[i].append(key_list[i])
            
    dir_path=createFile()
    
    head,tail=read_Head_tail()
    
    data_head=get_datahead(key_list_output,unit_list_output)
    
    if n_group_index<>[]:    
        if out_name=='':
            out_name_n=file_name+'_N.tdt'
        else:
            out_name_n=out_name+'_N.tdt'
        out_name_n=os.path.join(dir_path,out_name_n)
        out=open(out_name_n,'w')
        polar='NMOS'
        head=getHead(polar,head)
        out.writelines(head)
        out.writelines('\n')
        out.writelines(data_head)
        out.writelines('\n')
        for body in body_list_n:
            for i in range(0,len(body)):
                temp_list=body[i].split()
                for j in range(0,len(temp_list)):
                    if j <6:
                        temp_list[j]='%-10s'%temp_list[j]
                    else:
                        temp_list[j]='%-20s'%temp_list[j]
                body[i]=' '.join(temp_list)
        for body in body_list_n:
            out.writelines('\n'.join(body))
            out.writelines('\n')
        out.writelines(tail)
        out.close()
    if p_group_index<>[]:    
        if out_name=='':
            out_name_p=file_name+'_P.tdt'
        else:
            out_name_p=out_name+'_P.tdt'
        out_name_p=os.path.join(dir_path,out_name_p)
        out=open(out_name_p,'w')
        polar='PMOS'
        head=getHead(polar,head)
        out.writelines(head)
        out.writelines('\n')
        out.writelines(data_head)
        out.writelines('\n')
        for body in body_list_p:
            for i in range(0,len(body)):
                temp_list=body[i].split()
                for j in range(0,len(temp_list)):
                    if j <6:
                        temp_list[j]='%-10s'%temp_list[j]
                    else:
                        temp_list[j]='%-20s'%temp_list[j]
                body[i]=''.join(temp_list)
        for body in body_list_p:
            out.writelines('\n'.join(body))
            out.writelines('\n')
        out.writelines(tail)
        out.close()
        
def judge(line,tdt_key_list):
    temp_list=line.split(',')
    temp_list=temp_list[0].split('_')
    key=temp_list[0]
    key=key.upper()
    if key in tdt_key_list:
        return True
    else:
        return False
        
def getHead(polar,head):
    for i in range(0,len(head)):
        if head[i].startswith('DEVICE_TYPE'):
            temp_list=head[i].split()
            temp_list[1]=polar
            head[i]=' '.join(temp_list)+'\n'
    return head
 
def get_datahead(group_key_list,unit_list):
    output_list=['W','L','SC_X1','SC_X2','SC_Y1','SC_Y2','SCA','SCB','SCC']
    for i in range(0,len(group_key_list)):
        output_list.append(group_key_list[i])
    output_line='    '.join(output_list)+'\n'
    out_unit_list=['um','um','um','um','um','um','um','um','um']
    for i in range(0,len(unit_list)):
        out_unit_list.append(unit_list[i])
    unit_line='    '.join(out_unit_list)
    data_head=output_line+unit_line
    return data_head
          
def read_Head_tail():
    global tdt_def
    try:
        f=open(tdt_def,'r')
    except:
        printError("Can't open tdt difination file")
        sys.exit()
    content=f.readlines()
    
    
    head_end=0
    end_start=0    
    for i in range(0,len(content)):
        if content[i].startswith('.START_DATA'):
            head_end=i+1
        elif content[i].startswith('.END_DATA'):
            end_start=i
        if head_end<>0 and end_start<>0:
            break
    if head_end==0 or end_start==0:
        printError("Parser the wat difination file for head and ending failed")
        sys.exit()
    head=content[:head_end]
    tail=content[end_start:]
    return [head,tail]


def get_value(key_line,key_list,instance_list,die_num):
    temp_list=key_line.split(',')
    if key_list==[]:
        for i in range(0,die_num):
            key_list.append([])
            key_list[-1].extend(instance_list)
        for i in range(0,len(key_list)):
            key_list[i].append(temp_list[-(die_num-i)])
    else:
        for i in range(0,len(key_list)):
            key_list[i].append(temp_list[-(die_num-i)])
    return key_list
    

def get_s(idlin_line):
    temp_str=idlin_line.split(',')[0]
    temp_list=temp_str.split('_')
    L=temp_list[-1].replace('d','.')
    W=temp_list[-2].replace('d','.')
    w=float(W)
    l=float(L)
    s_str=temp_list[-3]
    s_list=get_slist(s_str,w,l)
    re_list=[w,l]+s_list
    return re_list
    
def getDie(die_block):
    die_list=[]
    for i in range(0,len(die_block)):
        temp_list=die_block[i].split(',')
        if die_block[i].startswith('=') or len(temp_list)!=3:
            pass
        else:
            die_list.append(','.join(temp_list))
    return die_list
    
def get_slist(s_str,w,l):
    global Scref
    s_str=s_str.replace('X1','_')
    s_str=s_str.replace('X2','_') 
    s_str=s_str.replace('Y2','_')
    s_str=s_str.replace('Y1','_')
    temp_list=s_str.split('_')
    for i in range(0,len(temp_list)):
        if temp_list[i]<>'':
            temp_list[i]=temp_list[i].upper()
            temp_list[i]=temp_list[i].replace('D','.')
            temp_list[i]=float(temp_list[i])
    X1=temp_list[1]
    Y1=temp_list[3]
    X2=temp_list[2]
    Y2=temp_list[4]
    SC1=SC2=X1
    SC3=SC4=X2
    SC5=SC6=Y1
    SC7=Y2
    Wid1=0
    Wid2=w
    Wid3=0
    Wid4=w
    Len5=0
    Len6=l
    Len7=l
    Wdrawn=w
    Ldrawn=l
    SCA=Scref**2/(Wdrawn*Ldrawn)*(Wid1*(1/SC1-1/(SC1+Ldrawn))+Wid2*(1/SC2-1/(SC2+Ldrawn))+Wid3*(1/SC3-1/(SC3+Ldrawn))+Wid4*(1/SC4-1/(SC4+Ldrawn))+Len5*(1/SC5-1/(SC5+Wdrawn))+Len6*(1/SC6-1/(SC6+Wdrawn))+Len7*(1/SC7-1/(SC7+Wdrawn)))
    SCB=1/(Wdrawn*Ldrawn)*(Wid1*((SC1/10+Scref/100)*exp(-10*SC1/Scref)-((SC1+Ldrawn)/10+Scref/100)*exp(-10*(SC1+Ldrawn)/Scref))+Wid2*((SC2/10+Scref/100)*exp(-10*SC2/Scref)-((SC2+Ldrawn)/10+Scref/100)*exp(-10*(SC2+Ldrawn)/Scref))+Wid3*((SC3/10+Scref/100)*exp(-10*SC3/Scref)-((SC3+Ldrawn)/10+Scref/100)*exp(-10*(SC3+Ldrawn)/Scref))+Wid4*((SC4/10+Scref/100)*exp(-10*SC4/Scref)-((SC4+Ldrawn)/10+Scref/100)*exp(-10*(SC4+Ldrawn)/Scref))+Len5*((SC5/10+Scref/100)*exp(-10*SC5/Scref)-((SC5+Wdrawn)/10+Scref/100)*exp(-10*(SC5+Wdrawn)/Scref))+Len6*((SC6/10+Scref/100)*exp(-10*SC6/Scref)-((SC6+Wdrawn)/10+Scref/100)*exp(-10*(SC6+Wdrawn)/Scref))+Len7*((SC7/10+Scref/100)*exp(-10*SC7/Scref)-((SC7+Wdrawn)/10+Scref/100)*exp(-10*(SC7+Wdrawn)/Scref)))
    SCC=1/(Wdrawn*Ldrawn)*(Wid1*((SC1/20+Scref/400)*exp(-20*SC1/Scref)-((SC1+Ldrawn)/20+Scref/400)*exp(-20*(SC1+Ldrawn)/Scref))+Wid2*((SC2/20+Scref/400)*exp(-20*SC2/Scref)-((SC2+Ldrawn)/20+Scref/400)*exp(-20*(SC2+Ldrawn)/Scref))+Wid3*((SC3/20+Scref/400)*exp(-20*SC3/Scref)-((SC3+Ldrawn)/20+Scref/400)*exp(-20*(SC3+Ldrawn)/Scref))+Wid4*((SC4/20+Scref/400)*exp(-20*SC4/Scref)-((SC4+Ldrawn)/20+Scref/400)*exp(-20*(SC4+Ldrawn)/Scref))+Len5*((SC5/20+Scref/400)*exp(-20*SC5/Scref)-((SC5+Wdrawn)/20+Scref/400)*exp(-20*(SC5+Wdrawn)/Scref))+Len6*((SC6/20+Scref/400)*exp(-20*SC6/Scref)-((SC6+Wdrawn)/20+Scref/400)*exp(-20*(SC6+Wdrawn)/Scref))+Len7*((SC7/20+Scref/400)*exp(-20*SC7/Scref)-((SC7+Wdrawn)/20+Scref/400)*exp(-20*(SC7+Wdrawn)/Scref)))
    slist=[X1,X2,Y1,Y2,SCA,SCB,SCC]
    return slist
    
    
    
def createFile():
    cwdpath=os.getcwd()
    path=os.path.join(cwdpath,'Converted data')
    if not os.path.exists(path):
        os.makedirs(path)
    return path
def getFilename(sys_line):
    name=sys_line.split(',')[-1]
    out='ID_#'+name
    return out
    
    

if __name__=='__main__':
    printWait("\
*************************************************************************\n\
**  Please put the converter,WPE_tdt_def,data under the same directory  *\n\
**  Please set the Electrical Parameter Definiton in WPE_tdt_def file   *\n\
**    OUTPUT section or you can comment the unused Parameter            *\n\
**  N&P parts in original data will be converted to separated file      *\n\
*************************************************************************")
    findFile()
    failed=0
    input_value=raw_input('Please input Scref value Scref=')
    try:
        Scref=float(input_value)
    except:
        printError ('ERROR: invalid input, set Scref=3')
        Scref=3
    for i in range(0,len(convertlist)):
        try:
            convert(convertlist[i])
            print 
            printProcess ('Convert %s ...'%convertlist[i] )
            print 
        except:
            printError ('ERROR: Convert file %s filed\n'%convertlist[i])
            failed=failed+1
    printResult('All complete %d failed ...'%failed)
    raw_input('')