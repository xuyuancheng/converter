# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 09:33:07 2012

@author: zhaiyt

"""

import os
import sys
import string
from shellcolor import *

global convertlist
convertlist=[]
global cj_gate_iv_namestr

def findFile():
    
    global convertlist
    convertlist=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for mem in files:
            if mem.split('.')[-1]<>'exe':
                mem=os.path.join(root,mem)
                convertlist.append(mem)
    num=len(convertlist)
    if num==0:
        print
        raw_input('No file find ,please put data file to current dirctory')
        sys.exit()
    else:
        print
        print "%s files need to convert:" % num
        print 
        for hitfile in convertlist:
            print hitfile
        
def convert(cvtfile):
    headline=[]
    headline_index=[]
    global cj_gate_iv_namestr
    temp=open(cvtfile,'r')
    content=temp.readlines()
    for i in range(0,len(content)):
        content[i]=content[i].strip('\n')
        flag=0
        templist=content[i].split(',')
        temp=templist[0].split('_')
        goldenhead=['VJG','CJG','VJIV','IJ','VBIAS','VBIASDIO','CJ','VGSCGC','CGC','VBSSTEP']
        for mem in goldenhead:
            if temp[0]==mem or temp[0].startswith('D'):
                flag=1
        if len(temp)>2 and flag==1:
            headline.append(templist[0])
            headline_index.append(i) 
#############################################################################
    for i in range(0,len(headline)):
        name=[]
        type_flag=''
        templist=headline[i].split('_')
        if templist[0]=='VJIV':
            name.append('IV')
            type_flag='iv'
        elif templist[0]=='VBIAS'or templist[0]=='VBIASDIO':
            name.append('CV')
            type_flag='cv'
        elif templist[0]=='VJG':
            name.append('CJGATE')
            type_flag='cj_gate'
        elif templist[0]=='VGSCGC':
            name=[[],[]]
            name[0].append('CJGATE')
            type_flag='cj_gate_cviv'
        else:
            continue
   #instance 
        t=cvtfile.split('.')[-1]
        area=templist[-2]
        area=area.replace('d','.')
        area_f=string.atof(area)
        area_f=area_f*1e-12
        pj=templist[-1]
        pj=pj.replace('d','.')
        pj_f=string.atof(pj)
        pj_f=pj_f*1e-6
        templist=templist[1:]
        instancelist=[area_f,pj_f,t]
        if type_flag=='cj_gate_cviv':
            namestr=[]
            name[0].append('_'.join(templist))
            namestr.append('_'.join(name[0]))
            namestr[0]=namestr[0]+'.%s'%t
        else:
            name.append('_'.join(templist))
            namestr='_'.join(name)
            namestr=namestr+'.%s'%t
    #create head
        if type_flag=='cj_gate_cviv':
            headstr=[]
            headstr.append(headcvt(instancelist,'cj_gate'))
            headstr.append(headcvt(instancelist,'iv'))

        else:
            headstr=headcvt(instancelist,type_flag)
    #create body
        if type_flag<>'':
            if type_flag=='cj_gate_cviv':
                bodystr=[]
                bodystr.append(bodycvt('cj_gate_cv',headline_index,headline,i,content))
                bodystr.append(bodycvt('cj_gate_iv',headline_index,headline,i,content))
                namestr.append(cj_gate_iv_namestr+'.%s'%t)
            else:
                bodystr=bodycvt(type_flag,headline_index,headline,i,content)
        if bodystr=='':
            continue
        else:
    #create file
            directory=createFile(cvtfile)
            root=os.getcwd()
            rootpath=os.path.join(root,directory)
            if  type_flag=='cj_gate_cviv':
                for j in range(0,len(namestr)):
                    writepath=os.path.join(rootpath,namestr[j])
                    if bodystr[j]<>'':
                        writeFile(writepath,headstr[j],bodystr[j])
            else:
                writepath=os.path.join(rootpath,namestr)
                writeFile(writepath,headstr,bodystr)

   # for i in range(0,len(headline_index),2):
       # print headline_index[i]    
def creatFolder():
    pass
def headcvt(instance,type_flag):
    head=[]
    biasstr=''
    if type_flag=='iv':
        modeltype='DC'
        output='Ij'
        groupstr='{Ij_Vj}'
        biasstr='[Vj,Ij(f=0.)]'
    if type_flag=='cv':
        biasstr='[Vj,Cj(f=0.)]'
    if type_flag=='cv' or type_flag=='cj_gate':
        modeltype='AC'
        output='Cj'
        groupstr='{Cj_Vj}'
    head.extend(['Objinfo{}',\
                 'ModelType{%s}'%modeltype,\
                 'DataType{D}',\
                 'Delimitor{,}',\
                 'Workingmodel{FORWARD}',\
                 'Instance{Area=%e,Pj=%e,T=%s}'%(instance[0],instance[1],instance[2]),\
                 'Input{Vj,f}',\
                 'Output{%s}'%output ,\
                 groupstr
                 ])
    if biasstr<>'':
        head.append(biasstr)
    headstr='\n'.join(head)
    return headstr        
        
def bodycvt(typeflag,h_list,hl_list,k,con):
    body=[]
    right=[]
    global cj_gate_iv_namestr
    if typeflag<>'cj_gate' and typeflag<>'cj_gate_cv' and typeflag<>'cj_gate_iv':
        left=con[h_list[k]:h_list[k+1]]
        if k<>len(h_list)-2:
            right=con[h_list[k+1]:h_list[k+2]]
        else:
            right=con[h_list[k+1]:]
    else:
        left=con[h_list[k]:h_list[k+1]]
        for i in range(k+1,len(hl_list)):
            templist=hl_list[i].split('_')
            if templist[0]=='VGSCGC' or templist[0]=='VJG':
                break
            else:
                if templist[0] == 'D1':
                    cj_gate_iv_namestr=hl_list[i]
                if ((templist[0]=='CGC' and templist[1]=='F1' and typeflag=='cj_gate_cv') or templist[0]=='CJG') and i<>len(hl_list)-1:
                    right.extend(con[h_list[i]:h_list[i+1]])
                elif templist[0] == 'D1' and typeflag=='cj_gate_iv' and i<>len(hl_list)-1:
                    right.extend(con[h_list[i]:h_list[i+1]])
                elif ((templist[0]=='CGC' and templist[1]=='F1' and typeflag=='cj_gate_cv') or templist[0]=='CJG') and i==len(hl_list)-1:
                    right.extend(con[h_list[i]:])
                elif templist[0] == 'D1' and typeflag=='cj_gate_iv' and i==len(hl_list)-1:
                    right.extend(con[h_list[i]:h_list[i+1]])
                if templist[0]=='CJG':
                    biasstr='[Vj,Cj(f=0.)]'
                else:
                    biasstr='[Vj,Cj(f=1e+05)]'
#        if len(biaslist)<>0:
#            for i in range(0,len(biaslist)):
#                if biaslist[i]=='F1':
#                    biaslist[i]='Cj(f=1E+05)'
#                elif biaslist[i]=='F2':
#                    biaslist[i]='Cj(f=0.)'
#                else:
#                    biaslist[i]='Cj(f=0.)'
#            biaslist.insert(0,'[Vj')
#            biasstr=','.join(biaslist)+']'
    if len(left)==0 or len(right)==0:
        return ''
    for i in range(0,len(left)):
        templist=left[i].split(',')
        if templist[0]=='1':
            for j in range(1,len(templist)):
                if templist[j]<>'':
                    body.append([])
                    #strip the left's '+' which starts with '+'
                    if templist[j].startswith('+'):
                        templist[j]=templist[j].lstrip('+')
                    #revise the bias for cv
#                    if typeflag<>'iv' and string.atof(templist[j])>=0:
#                        if templist[j].startswith('+'):
#                            templist[j]='-'+templist[j].lstrip('+')
#                        elif not templist[j].startswith('-'):
#                            templist[j]='-'+templist[j]
                    body[-1].append(templist[j])
                else:
                    break
    for i in range(0,len(right)):
        templist=right[i].split(',')
        if templist[0]=='1':
            for j in range(1,len(templist)):
                if templist[j]<>'':
                    body[j-1].append(templist[j])
                else:
                    break
    flag_num=0
    for i in range(0,len(body)):
        if i==0:
            continue
        else:
            skip=string.atof(body[i][0])-string.atof(body[i-1][0])
            if skip==0:
                flag_num=i-1
                break
    if flag_num<>0:
        body=body[0:flag_num]
    for i in range(0,len(body)):     
        body[i]=','.join(body[i])
    if  typeflag=='cj_gate' or typeflag=='cj_gate_cv':
        body.insert(0,biasstr)
    bodystr='\n'.join(body)
    return bodystr

def createFile(filename):
    cwdpath=os.getcwd()
    basepath=filename.strip(cwdpath)
    path=os.path.join('Converted data',basepath)
    if not os.path.exists(path):
        os.makedirs(path)
    return path
   
def writeFile(path,head,body):
    f=open(path,'w')
    f.writelines(head)
    f.writelines('\n')
    f.writelines(body)
    f.close()     
    
    
if __name__=='__main__':
    findFile()
    failed=0
    for i in range(0,len(convertlist)):
  #      try:
        convert(convertlist[i])
        print 
        printProcess ('Convert %s ...'%convertlist[i] )
        print 
   #     except:
 #           printError ('ERROR: Convert file %s filed'%convertlist[i])
  #          failed=failed+1
    printResult('All complete %d failed ...'%failed)
    raw_input('')