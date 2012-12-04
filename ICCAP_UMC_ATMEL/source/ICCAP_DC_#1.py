# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 17:45:56 2011

@author: Yiting
"""

import sys
import os

global convertlist
global instance
global datalist
global headstr

convertlist=[]
instance=[]
datalist=[]
headstr=[]

def findFile():
    '''Find file in current directory'''
    global convertlist
    convertlist=[]
    flag=0
    
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for fil in files:
            splitename=os.path.splitext(fil)
            if (splitename[-1].strip('.,-,m')).isdigit():                                                  #may change if format change
                fil=os.path.join(root,fil)
                convertlist.append(fil)
                flag=1
    if flag==1:
        num=len(convertlist)
        print
        print "%s files need to convert:" % num
        print 
        for hitfile in convertlist:
            print hitfile
    else:
        print
        raw_input('No measured data file found, please put data file or data folder to corrent directory')
        sys.exit()
        
def devide(convertfile):
    global instance
    global datalist
    instance=[]
    datalist=[]
    index=-1
    f=open(convertfile,'r')
    content=f.readlines()
    f.close()
    for i in range(0,len(content)):
        if content[i].find('Lot')<>-1:
            instance.append([[],[],[]])
            index=index+1
        elif content[i].find('Wdrawn')<>-1:
            instance[index][0].append(content[i])
        elif content[i].find('Ldrawn')<>-1:
            instance[index][1].append(content[i])
        elif content[i].find('Temp')<>-1:
            instance[index][2].append(content[i])
        elif content[i].find('VD')<>-1:
            j=i
            while True: 
                j=j+1
                templist=content[j].split()
                if len(templist)>=2:
                    start=j
                    break
                else:
                    pass
            j=i
            while True:
                j=j+1
                if j==len(content):
                    end=j
                    break
                elif content[j].find('Lot')<>-1:
                    end=j
                    break
            datalist.append(content[start:end])
            for w in range(0,len(datalist[-1])):
                if len(datalist[-1][-1])<4:
                    del datalist[-1][-1]
            

def body_cvt(databody):
    bodytemp=[]
    vdlist=[]
    vglist=[]
    vblist=[]
    for i in range(0,len(databody)):
        templist=databody[i].split()
        vdlist.append(templist[0])
        vglist.append(templist[1])
        vblist.append(templist[3])
    vdlist=trip(vdlist)
    vglist=trip(vglist)
    vblist=trip(vblist)
    d=len(vdlist)
    g=len(vglist)
    b=len(vblist)
    templist=[d,g,b]
    templist.sort()
    if templist==[d,g,b]:
        linearlist=vblist
        listlist=vglist
        steplist=vdlist
        linearflag='Vb'
        listflag='Vg'
        stepflag='Vd'
        linearindex=3
        listindex=1
        stepindex=0
    elif templist==[d,b,g]:
        linearlist=vglist
        listlist=vblist
        steplist=vdlist
        linearflag='Vg'
        listflag='Vb'
        stepflag='Vd'
        linearindex=1
        listindex=3
        stepindex=0
    elif templist==[g,d,b]:
        linearlist=vblist
        listlist=vdlist
        steplist=vglist
        linearflag='Vb'
        listflag='Vd'
        stepflag='Vg'
        linearindex=3
        listindex=0
        stepindex=1
    elif templist==[g,b,d]:
        linearlist=vdlist
        listlist=vblist
        steplist=vglist
        linearflag='Vd'
        listflag='Vb'
        stepflag='Vg'
        linearindex=0
        listindex=3
        stepindex=1
    elif templist==[b,d,g]:
        linearlist=vglist
        listlist=vdlist
        steplist=vblist
        linearflag='Vg'
        listflag='Vd'
        stepflag='Vb'
        linearindex=1
        listindex=0
        stepindex=3
    elif templist==[b,g,d]:
        linearlist=vdlist
        listlist=vglist
        steplist=vblist
        linearflag='Vd'
        listflag='Vg'
        stepflag='Vb'
        linearindex=0
        listindex=1
        stepindex=3

    #group information
    outputlist=['Id','Ig','Is','Ib']
    grouplist=[]
    sgrouplist=[]
    for output in outputlist:
        groupstr='{%s_%s}'%(output,linearflag)
        grouplist.append(groupstr)
        
        sgrouplist.append([])
        sgroup=[linearflag]
        templist=[]
        for i in range(0,len(listlist)):
            tempstr=output+'(%s=%s)'%(listflag,listlist[i])
            templist.append(tempstr)
        endlist=[]
        for i in range(0,len(steplist)):
            sgrouplist[-1].append([])
            endlist.append('%s=%s'%(stepflag,steplist[i]))
            sgrouplist[-1][i].extend(sgroup)
            sgrouplist[-1][i].extend(templist)
            sgrouplist[-1][i].append(endlist[-1])
            sgrouplist[-1][i].append('Vs=0.000')
    for i in range(0,len(sgrouplist)):
        for j in range(0,len(sgrouplist[i])):
            sgrouplist[i][j]=','.join(sgrouplist[i][j])
    #data information
    data_list=[]
    datalist_temp=[]
    Idlist=[]
    Iglist=[]
    Islist=[]
    Iblist=[]


    for i in range(0,len(databody)):
        templist=databody[i].split()
        Idlist.append(templist[4])
        Iglist.append(templist[5])
        Islist.append(templist[6])
        Iblist.append(templist[7])
    for x in range(0,len(steplist)):
        datalist_temp.append([])
        datalist_temp[-1].append([])
        datalist_temp[-1].append([])
        datalist_temp[-1].append([])
        datalist_temp[-1].append([])
        for i in range(0,len(linearlist)):
            templist=[]
            templist1=[]
            templist2=[]
            templist3=[]
            templist.append(linearlist[i])
            templist1.append(linearlist[i])
            templist2.append(linearlist[i])
            templist3.append(linearlist[i])
            for j in range(0,len(listlist)):
                templist.append(Idlist[i+x*(len(linearlist)*len(listlist))+j*(len(linearlist))])
                templist1.append(Iglist[i+x*(len(linearlist)*len(listlist))+j*(len(linearlist))])
                templist2.append(Islist[i+x*(len(linearlist)*len(listlist))+j*(len(linearlist))])
                templist3.append(Iblist[i+x*(len(linearlist)*len(listlist))+j*(len(linearlist))])
            tempstr=','.join(templist)
            tempstr1=','.join(templist1)
            tempstr2=','.join(templist2)
            tempstr3=','.join(templist3)
            datalist_temp[-1][-4].append(tempstr)
            datalist_temp[-1][-3].append(tempstr1)
            datalist_temp[-1][-2].append(tempstr2)
            datalist_temp[-1][-1].append(tempstr3)
    for j in range(0,4):    
        for i in range(0,len(steplist)):
            data_list.append(datalist_temp[i][j])
      
    #creat body
    data_index=0
    for i in range(0,len(grouplist)):
        bodytemp.append(grouplist[i])
        for k in range(0,len(sgrouplist[0])):
            sgrouplist[i][k]='['+sgrouplist[i][k]+']'
            bodytemp.append(sgrouplist[i][k])
            bodytemp.extend(data_list[data_index])
            data_index=data_index+1
    return bodytemp

def head_cvt(head):
    global headstr
    wvalue=(head[0][0].split())[-1]
    lvalue=(head[1][0].split())[-1]
    tvalue=(head[2][0].split())[-1]
    headtemp=['ObjInfo{}',\
      'Version{2006.1}',\
      'ModelType{DC}',\
      'WorkingMode{Forward}',\
      'Delimitor{,}',\
      'DataType{NMOS}',\
      'Instance{W=%s,L=%s,T=%s}'%(wvalue,lvalue,tvalue),\
      'Input{Vd,Vg,Vs,Vb}',\
      'Output{Id,Ig,Is,Ib}']
    tempstr='W%s_L%s_T%s'%(wvalue,lvalue,tvalue)+'.dat'
    headstr.append(tempstr)
    return headtemp
    
    
    
    
def trip(plist):
    setlist=[plist[0]]
    for i in range(1,len(plist)):
        if plist[i] in setlist:
            pass
        else:
            setlist.append(plist[i])
    return setlist

def makedir(name):
    dcdir=os.path.join('Converted data',name)
    if not os.path.exists(dcdir):
        os.makedirs(dcdir)
    return dcdir
        
                

        

if __name__=='__main__':
    
    findFile()
    for i in range(0,len(convertlist)):
        try:
            dcdir=makedir(os.path.basename(convertlist[i]))
            bodylist=[]
            headlist=[]
            headstr=[]
            devide(convertlist[i])
            body_cvt(datalist[-1])
    
            for i in range(0,len(datalist)):
                try:
                    bodylist.append(body_cvt(datalist[i]))
                except:
                    bodylist.append([])
            for i in range(0,len(instance),2):
                try:
                    headlist.append(head_cvt(instance[i]))
                except:
                    headlist.append([])
            for i in range(0,len(headlist)):
                try:
                    dc=[]
                    dc.extend(headlist[i])
                    dc.extend(bodylist[2*i])
                    dc.extend(bodylist[2*i+1])
                    tempstr='\n'.join(dc)
                    try:
                        path=os.path.join(dcdir,headstr[i])
                        f=open(path,'w')
                        f.writelines(tempstr)
                        f.close()
                    except:
                        pass
                except:
                    print "one file failed"
        except:
            pass

    raw_input('All conplete')
    