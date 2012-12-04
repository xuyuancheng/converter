# -*-coding: utf-8 -*-
import os
import string


def headCvt(header,mdmname):
    global head
    
    #read device type from file name
    name=(os.path.basename(mdmname)).upper()
    if name.startswith('N'):
        dtype='NMOS'
    elif name.startswith('P'):
        dtype='PMOS'
    else:
        print 'Can not get device type imformation from file name, set default NMOS'
        dtype='NMOS'
        
    #get instance values
    print 'Instance imformation W,L,T miss, set to default W=1.2,L=0.45,T=25'
    wvalue=1.2
    lvalue=0.45
    tvalue=25
    
    #get inputlist
    inputlist=[]
    for i in range(0,len(header)):
        if header[i].find('ICCAP_INPUTS')<>-1:
            start=i
        elif header[i].find('ICCAP_OUTPUTS')<>-1:
            end=i
    temp=header[(start+1):end]
    for i in range(0,len(temp)):
        inputs=temp[i].split()
        if inputs[0]=='freq':
            pass
        else:
            inputlist.append(inputs[0])
    inputliststr=','.join(inputlist)

    #get outputlist
    outputlist=[]
    for i in range(0,len(header)):
        if header[i].find('ICCAP_OUTPUTS')<>-1:
            start=i
        elif header[i].find('ICCAP_VALUES')<>-1:
            end=i
            break
        elif header[i].find('END_HEADER')<>-1:
            end=i
            break
    temp=header[(start+1):end]
    for i in range(0,len(temp)):
        outputs=temp[i].split()
        if outputs[0]=='s':
            pass
        else:
            outputlist.append(outputs[0])
    outputliststr=','.join(outputlist)
           
    head=['ObjInfo{}',\
          'Version{2006.1}',\
          'ModelType{DC}',\
          'WorkingMode{Forward}',\
          'Delimitor{,}',\
          'DataType{%s}'%dtype,\
          'Instance{W=%s,L=%s,T=%s.}'%(wvalue,lvalue,tvalue),\
          'Input{%s}'%inputliststr,\
          'Output{%s}'%outputliststr]
def bodycvt(header):
    global body
    body=[]
    startlist=[]
    endlist=[]
    bodylist=[]
    outputlist=[]
    newbodylist=[]
    #read every data part to list
    for i in range(0,len(header)):
        if header[i].find('BEGIN_DB')<>-1:
            startlist.append(i)
        elif header[i].find('END_DB')<>-1:
            endlist.append(i)
    for i in range(0,len(startlist)):
        bodytemp=header[startlist[i]:endlist[i]]
        bodylist.append(bodytemp)
    #get big grouplist 
    biggrouplist=[]
    for i in range(0,len(header)):
        if header[i].find('#')<>-1:             #according '#' judge main input
            temp=header[i].split()
            maininput=(temp[0].strip('#')).lower()
            for k in range(1,len(temp)):
                if temp[k].find(':s')==-1:
                    tempstr='{%s_%s}'%(temp[k],maininput)
                    biggrouplist.append(tempstr)
                    outputlist.append(temp[k])
                else:
                    pass
            break
    #get small grouplist
    smallgrouplist=[]
    smallgroup=[]
    for i in range(0,len(header)):
        if header[i].find('ICCAP_INPUTS')<>-1:
            start=i
        elif header[i].find('ICCAP_OUTPUTS')<>-1:
            end=i
            break
    independentlist=[]
    unchangelist=[]
    temp=header[(start+1):end]
    for i in range(0,len(temp)):
        if temp[i].find('LIN')<>-1 or temp[i].find('LIST')<>-1:
            templist=temp[i].split()
            if templist[0]<>maininput:
                independentlist.append(templist[0])
        else:
            templist=temp[i].split()
            if templist[0]=='freq':
                pass
            else:
                unchangelist.append('%s=%s'%(templist[0],templist[-1]))
    #if have only one independent       
    if len(independentlist)==1:
        for i in range(0,len(temp)):
            if temp[i].find ('LIN')<>-1:
                templist=temp[i].split()
                if templist[0]<>maininput:
                    num=templist.index('LIN')
                    changelist=[]
                    rangenum=string.atoi(templist[num+4])
                    for i in range(0,rangenum):
                        changelist.append(str(string.atof(templist[num+2])+i*(string.atof(templist[-1]))))
                    keynum=len(changelist)                                                                  #important variable
                    for i in range(0,len(biggrouplist)):
                        smallgrouplist.append([])
                        smallgroup.append([])
                        smallgroup[i].append(maininput)
                        for k in range(0,len(changelist)):
                            tempstr=outputlist[i]+'(%s=%s)'%(independentlist[0],changelist[k])
                            smallgroup[i].append(tempstr)
                        smallgroup[i].extend(unchangelist)
                        smallgrouplist[i].append('['+','.join(smallgroup[i])+']')
            elif temp[i].find ('LIST')<>-1:
                templist=temp[i].split()
                if templist[0]<>maininput:
                    num=templist.index('LIST')
                    changelist=templist[(num+3):]
                    keynum=len(changelist)                                                                  #important variable
                    for i in range(0,len(biggrouplist)):
                        smallgroup.append([])
                        smallgrouplist.append([])
                        smallgroup[i].append(maininput)
                        for k in range(0,len(changelist)):
                            tempstr=outputlist[i]+'(%s=%s)'%(independentlist[0],changelist[k])
                            smallgroup[i].append(tempstr)
                        smallgroup[i].extend(unchangelist)
                        smallgrouplist[i].append('['+','.join(smallgroup[i])+']')      
                
    #if have not only one independent
    independentvalue=100
    if len(independentlist)>1:
        for i in range(0,2):
            data=bodylist[i]
            for k in range(0,len(data)):
                if data[k].find('ICCAP_VAR')<>-1:
                    templist=data[k].split()
                    if templist[1]==independentlist[0]:
                        if i==1 and independentvalue<>templist[2]:
                            mainindependent=independentlist[0]
                            unmainindependent=independentlist[1]
                        elif i==0:
                            independentvalue=templist[2]
                        else:
                            mainindependent=independentlist[1]
                            unmainindependent=independentlist[0]
        for i in range(0,len(temp)):
            if temp[i].find(mainindependent)<>-1:
                if temp[i].find('LIN')<>-1:
                    templist=temp[i].split()
                    num=templist.index('LIN')
                    mainchangelist=[]
                    for i in range(0,string.atoi(templist[num+4])):
                        mainchangelist.append(str(string.atof(templist[num+2])+i*(string.atof(templist[-1]))))
                    keynum=len(mainchangelist)                                                                  #importtant variable
                elif temp[i].find('LIST')<>-1:
                    templist=temp[i].split()
                    num=templist.index('LIST')
                    mainchangelist=templist[(num+3):]
                    keynum=len(mainchangelist)                                                                  #importtant variable
            elif temp[i].find(unmainindependent)<>-1:
                if temp[i].find('LIN')<>-1:
                    templist=temp[i].split()
                    num=templist.index('LIN')
                    unmainindependentlist=[]
                    for i in range(0,templist[num+4]):
                        unmainchangelist.append(str(string.atof(templist[num+2])+i*(string.atof(templist[-1]))))
                elif temp[i].find('LIST')<>-1:
                    templist=temp[i].split()
                    num=templist.index('LIST')
                    unmainchangelist=templist[(num+3):]
        for i in range(0,len(biggrouplist)):
            smallgrouplist.append([])
            for k in range(0,len(unmainchangelist)):
                wait=[]
                wait.append(maininput)
                unmain='%s=%s'%(unmainindependent,unmainchangelist[k])
                for j in range(0,len(mainchangelist)):
                    tempstr=outputlist[i]+'(%s=%s)'%(mainindependent,mainchangelist[j])
                    wait.append(tempstr)
                wait.append(unmain)
                wait.extend(unchangelist)
                smallgrouplist[i].append('['+','.join(wait)+']')
    #creat body data list
    count=0
    for m in range(0,len(outputlist)):
        flag=m+1
        for i in range(0,len(bodylist)):
            data=bodylist[i]
            for k in range(0,len(bodylist[i])):
                if data[k].find('#')<>-1:
                    start=k
            tempdata=data[start+1:]
            if count==keynum:
                count=0
            if count==0:
                newbodylist.append([])
                for j in range(0,len(tempdata)):
                    templist=tempdata[j].split()
                    tempstr=templist[0]+','+templist[flag]
                    newbodylist[-1].append(tempstr)
                count=count+1
                    
            else:
                for j in range(0,len(tempdata)):
                    templist=tempdata[j].split()
                    newbodylist[-1][j]=newbodylist[-1][j]+','+templist[flag]
                count=count+1

    #write body
    for i in range(0,len(biggrouplist)):
        body.append(biggrouplist[i])
        for j in range(0,len(smallgrouplist[i])):
            body.append(smallgrouplist[i][j])
            for k in range(0,len(newbodylist[j])):
                body.append(newbodylist[j][k])
                    
                
               
def link(path):
    global head
    global body
    cvtdata=open(path,'w')
    headstr='\n'.join(head)
    bodystr='\n'.join(body)
    cvtdata.writelines(headstr)
    cvtdata.writelines('\n')
    cvtdata.writelines(bodystr)
    cvtdata.close()
def rdcvt(header,mdmname,path):
    headCvt(header,mdmname)
    bodycvt(header)
    link(path)

