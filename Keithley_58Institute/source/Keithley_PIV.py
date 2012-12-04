# -*-coding: utf-8 -*-

import os
import sys
from time import ctime
import re
import string
from win32com.client import Dispatch
import win32com.client

global convertlist

def findFile():
    '''Find *.xls file in current directory'''
    global convertlist
    convertlist=[]
    flag=0
    
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for fil in files:
            splitename=os.path.splitext(fil)
            if splitename[-1]=='.xls' or splitename[-1]=='.xlsx':                                                   #may change if format change
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
        raw_input('No measured data found, please put data file or data folder to corrent directory')
        sys.exit()

def headCvt(meaname):
    global head

    #read device type from file name
    name=(os.path.basename(meaname)).upper()
    if name.find('NMOS')<>-1:
        dtype='NMOS'
    elif name.find('PMOS')<>-1:
        dtype='PMOS'
    else:
        print 'Can not get device type imformation from file name, set default NMOS'
        dtype='NMOS'

    #Get instance valuse:
    wflag=0
    lflag=0
    tflag=0
    templist=name.split('_')
    for i in range(0,len(templist)):
        if templist[i].startswith('W'):
            templist[i]=templist[i].strip('W')
            if templist[i].isdigit():
                wvalue=string.atof(templist[i])
                wflag=1
            else:
                pass
        elif templist[i].startswith('L'):
            templist[i]=templist[i].strip('L')
            if templist[i].isdigit():
                lvalue=string.atof(templist[i])
                lflag=1
            else:
                pass
        elif templist[i].startswith('T'):
            templist[i]=templist[i].strip('T')
            if templist[i].isdigit():
                tvalue=string.atof(templist[i])
                tflag=1
            else:
                pass
    if wflag==0:
        print 'Instance imformation W miss, set to default W=10'
        wvalue=10
    if lflag==0:
        print 'Instance imformation L miss, set to default L=10'
        lvalue=10
    if tflag==0:
        print 'Instance imformation T miss, set to default T=25'
        tvalue=25
    #Set input list
    inputliststr='Input{Vgs,Vds,Vbs}'
    #Set output list
    outputliststr='Output{Ids}'

    head=['ObjInfo{}',\
      'Version{2006.1}',\
      'ModelType{DC}',\
      'WorkingMode{Forward}',\
      'Delimitor{,}',\
      'DataType{%s}'%dtype,\
      'Instance{W=%s,L=%s,T=%s.}'%(wvalue,lvalue,tvalue),\
      inputliststr,\
      outputliststr]

def bodyCvt(meaname):
    global databody
    global calcbody
    
    excel=win32com.client.Dispatch('Excel.Application')
    try:
        excel.Visible=0
        excel.DisplayAlerts=0
    except:
        pass
    elxbook=excel.Workbooks.open(meaname)
    datasheet=elxbook.Worksheets('Data')
    calcsheet=elxbook.Worksheets('Calc')
    setingsheet=elxbook.Worksheets('Settings')

    
    inoutlist=[]
    #get curvenum
    curvenum=0
    i=1  
    while True:
        cell=datasheet.Cells(1,i).Value
        verify=datasheet.Cells(2,i).Value
        if cell==None:
            break
        else:
            cell=cell.upper()
            inoutlist.append(cell)
            if cell.find('ID')<>-1 and verify<>None and len(cell)<5:
                curvenum=curvenum+1
            i=i+1
    #get sweep input
    sweepflag=0
    for i in range(0,len(inoutlist)):
        if inoutlist[i].find('VD')<>-1 and len(inoutlist[i])<5:
            for j in range(2,5):
                if datasheet.Cells(j,(i+1)).Value<>datasheet.Cells(j+1,(i+1)).Value:
                    sweepflag=1
            if sweepflag==1:
                sweepinput='VD'
                listinput='VG'
            else:
                sweepinput='VG'
                listinput='VD'
            break
    #creat body
    databody=[]
    calcbody=[]
    #get group
    sweepinput_new=sweepinput.title()
    group='{Id_%s}'%sweepinput_new
    #get groupname
    listinputvaluelist=[]
    for i in range(0,len(inoutlist)):
        if inoutlist[i].find(listinput)<>-1 and len(inoutlist[i])<5:
            value=datasheet.Cells(2,(i+1)).Value
            listinputvaluelist.append(value)
            if len(listinputvaluelist)==curvenum:
                break
    if sweepinput=='VD':
        groupname='[Vds,'
        for i in range(0,len(listinputvaluelist)):      
            groupname=groupname+'Ids(Vgs=%s),'%listinputvaluelist[i]
    if sweepinput=='VG':
        groupname='[Vgs,'
        for i in range(0,len(listinputvaluelist)):
            groupname=groupname+'Ids(Vds=%s),'%listinputvaluelist[i]
    groupname=groupname+'Vbs=0]'
#############################
#datasheet convert
#############################
    #get sweepinput list
    sweeplist=[]
    for i in range(0,len(inoutlist)):
        if inoutlist[i].find(sweepinput)<>-1 and len(inoutlist[i])<5:
            j=2
            while True:
                value=datasheet.Cells(j,(i+1)).Value
                if value<>None:
                    sweeplist.append(value)
                    j=j+1
                else:
                    break
            break
    #get output list
    outlist=[]
    outnum=-1
    for i in range(0,len(inoutlist)):
        if inoutlist[i].find('ID')<>-1 and len(inoutlist[i])<5:
            outlist.append([])
            outnum=outnum+1
            if len(outlist)==curvenum+1:
                break
            else:
                j=2
                while True:
                    value=datasheet.Cells(j,(i+1)).Value
                    if value<>None:
                        outlist[outnum].append(value)
                        j=j+1
                    else:
                        break
    #get bodylist
    bodylist=[]
    for i in range(0,len(sweeplist)):
        templist=[]
        templist.append(str(sweeplist[i]))
        for j in range(0,curvenum):
            templist.append(str(outlist[j][i]))
        tempstr=','.join(templist)
        bodylist.append(tempstr)
    #getbody
    databody.append(group)
    databody.append(groupname)
    databody.extend(bodylist)


#############################
#calcsheet convert
#############################
    inoutlist=[]
    i=1  
    while True:
        cell=calcsheet.Cells(1,i).Value
        verify=calcsheet.Cells(2,i).Value
        if cell==None:
            break
        else:
            cell=cell.upper()
            inoutlist.append(cell)
            i=i+1
    #get sweepinput list
    if sweepinput=='VD':
        sweepinput='DRAINV'
        listinput='GATEV'
    if sweepinput=='VG':
        sweepinput='GATEV'
        listinput='DRAINV'
    sweeplist=[]
    for i in range(0,len(inoutlist)):
        if inoutlist[i].find(sweepinput)<>-1 and len(inoutlist[i])<11:
            j=2
            while True:
                value=calcsheet.Cells(j,(i+1)).Value
                if value<>None:
                    sweeplist.append(value)
                    j=j+1
                else:
                    break
            break
    #get output list
    outlist=[]
    outnum=-1
    for i in range(0,len(inoutlist)):
        if inoutlist[i].find('DRAINI')<>-1 and len(inoutlist[i])<11:
            outlist.append([])
            outnum=outnum+1
            if len(outlist)==curvenum+1:
                break
            else:
                j=2
                while True:
                    value=calcsheet.Cells(j,(i+1)).Value
                    if value<>None:
                        outlist[outnum].append(value)
                        j=j+1
                    else:
                        break
    #get bodylist
    bodylist=[]
    for i in range(0,len(sweeplist)):
        templist=[]
        templist.append(str(sweeplist[i]))
        for j in range(0,curvenum):
            templist.append(str(outlist[j][i]))
        tempstr=','.join(templist)
        bodylist.append(tempstr)
    #getbody
    calcbody.append(group)
    calcbody.append(groupname)
    calcbody.extend(bodylist)
#Close excel
    elxbook.Close()
    excel.Quit()
def link(datapath,calcpath):
    
    global head
    global databody
    global calcbody
    cvtdata=open(datapath,'w')
    headstr='\n'.join(head)
    bodystr='\n'.join(databody)
    cvtdata.writelines(headstr)
    cvtdata.writelines('\n')
    cvtdata.writelines(bodystr)
    cvtdata.close()
    cvtdata=open(calcpath,'w')
    headstr='\n'.join(head)
    bodystr='\n'.join(calcbody)
    cvtdata.writelines(headstr)
    cvtdata.writelines('\n')
    cvtdata.writelines(bodystr)
    cvtdata.close()

def cvt(meaname,datapath,calcpath):
    headCvt(meaname)
    bodyCvt(meaname)
    link(datapath,calcpath)

#############################################Combine Id_Vg and Id_Vd###################################3
def search():
    global pairs
    global pairs_index
    pairs_index=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    filelist=[]
    dirlist=[]
    index=[]
    for root,dirs,files in dircontent:
        files_n=files[:]
        for i in range(len(files)):
            files_n[i]=files[i].lower()
            findf=(files_n[i].find('idvg'))*(files_n[i].find('id_vg'))
            finds=(files_n[i].find('idvd'))*(files_n[i].find('id_vd'))
            if (findf<0 or finds<0) and files_n[i].endswith('dat'):
                filelist.append(files_n[i])
                dirlist.append(os.path.join(root,files[i]))
                index.append(-findf*finds)
    #then find the paires
    pairs=[]
    for i in range(len(filelist)):
        temp=filelist[i][0:index[i]]
        for j in range(i+1,len(filelist)):
            if filelist[j][0:index[i]]==temp and (filelist[j][(index[i]+4):]==filelist[i][(index[i]+4):] or filelist[j][(index[i]+5):]==filelist[i][(index[i]+5):]):
                templist=[dirlist[i],dirlist[j]]
                pairs.append(templist)
                pairs_index.append(index[i])
def combine():
    global pairs
    global pairs_index
    global combody
    global comdir
    if len(pairs)<>0:
        print 'Combine Id_Vg and Id_Vd data file'
    combody=[]
    comdir=[]
    for i in range(0,len(pairs)):
        f1=open(pairs[i][0],'r')
        f1con=f1.readlines()
        f1.close()
        f2=open(pairs[i][1],'r')
        f2con=f2.readlines()
        f2.close()
        # deal with the output problem
        templist=[]
        for k in range(0,len(f1con)):
            if f1con[k].find('Output')<>-1:
                begin=f1con[k].find('{')
                tempstr=f1con[k][begin:]
                tempstr=tempstr.strip('{}\n')
                templist.extend(tempstr.split(','))
        for k in range(0,len(f2con)):
            if f2con[k].find('Output')<>-1:
                begin=f2con[k].find('{')
                tempstr=f2con[k][begin:]
                tempstr=tempstr.strip('{}\n')
                templist.extend(tempstr.split(','))
        outputlist=list(set(templist))
        outputstr='Output{%s}\n'%(','.join(outputlist))
        # deal with the problem of order
        if (pairs[i][0].lower()).find('idvg')<>-1 or (pairs[i][0].lower()).find('id_vg')<>-1:
            startcon=f1con
            hangcon=f2con
        else:
            startcon=f2con
            hangcon=f1con
        for j in range(0,len(startcon)):
            if startcon[j].find('Output')<>-1:
                startcon[j]=outputstr
        tempcon=[]
        for j in range(0,len(hangcon)):
            if hangcon[j].startswith('{I') or hangcon[j].startswith('{i'):
                hangcon[j]='\n'+hangcon[j]
                tempcon.extend(hangcon[j:])
                break
        startcon.extend(tempcon)
        combody.append(startcon)
    #made name
        basename=os.path.basename(pairs[i][0])
        dirname=os.path.join('Converted data\\dc_combine','%s_dc'%basename[0:pairs_index[i]])
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        basename=basename[0:pairs_index[i]]+basename.split('_')[-1]
        path=os.path.join(dirname,basename)
        comdir.append(path)

def dchang():
    global combody
    global comdir
    search()
    combine()
    flag=1
    for i in range(0,len(comdir)):
        if os.path.exists(comdir[i]):
            comdir[i]=list(comdir[i])
            comdir[i].insert(-4,'(%s)'%flag)
            comdir[i]=''.join(comdir[i])
            flag=flag+1
        writepath=comdir[i]
        f=open(writepath,'w')
        f.writelines(combody[i])
        f.close()
            
                
if __name__=='__main__':
    findFile()
    for convertfile in convertlist:
        print "--Start to convert file %s --"%convertfile
        try:
            nametemp=os.path.basename(convertfile)
            name=nametemp.split('.')[0]          
            dirname=os.path.join('Converted data',name)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            datapath=os.path.join(dirname,(name+'_data'+'.dat'))
            calcpath=os.path.join(dirname,(name+'_calc'+'.dat'))

            cvt(convertfile,datapath,calcpath)
        except:
            print "ERROR:------Convert file %s failed-----------"%convertfile

    try:
        dchang()
    except:
        print "ERROR:------Combine id_vg id_vd data file failed-----------"
    raw_input('All complete... ')
        
