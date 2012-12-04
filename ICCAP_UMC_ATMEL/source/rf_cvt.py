# -*-coding: utf-8 -*-
import os


def headCvt(header,mdmname):
    global head
    head=[]
    general=[]
    frequency=[]
    bias=[]

    #read device type from file name

    name=(os.path.basename(mdmname)).upper()
    if name.startswith('N'):
        dtype=1
    elif name.startswith('P'):
        dtype=-1
    else:
        print 'Can not get device type imformation from file name, set default NMOS'
        dtype=1

    #get frequency information

    for i in range(0,len(header)):
        if header[i].find('ICCAP_INPUTS')<>-1:
            start=i
        elif header[i].find('ICCAP_OUTPUTS')<>-1:
            end=i
            break
    temp=header[(start+1):end]
    for i in range(0,len(temp)):
        output=temp[i].split()
        for k in range(0,len(output)):
            if output[k].find('freq')<>-1:
                if output[k+2]=='LIN':
                    startf=output[k+4]
                    endf=output[k+5]
                    potnum=output[k+6]
                elif output[k+2]=='LIST':
                    startf=output[k+5]
                    endf=output[-1]
                    potnum=output[k+4]

    #get bias imformation

    vslist=[]
    vblist=[]
    vdlist=[]
    vglist=[]
    for i in range(0,len(header)):
        if header[i].find('ICCAP_VAR')<>-1:
            biaslist=header[i].split()
            if 'vs' in biaslist:
                if len(vslist)<>0:
                    if biaslist[-1]<>vslist[-1]:
                        vslist.append(biaslist[-1])
                else:
                    vslist.append(biaslist[-1])
            if 'vb' in biaslist:
                if len(vblist)<>0:
                    if biaslist[-1]<>vblist[-1]:
                        vblist.append(biaslist[-1])
                else:
                    vblist.append(biaslist[-1])
            if 'vd' in biaslist:
                if len(vdlist)<>0:
                    if biaslist[-1]<>vdlist[-1]:
                        vdlist.append(biaslist[-1])
                else:
                    vdlist.append(biaslist[-1])
            if 'vg' in biaslist:
                if len(vglist)<>0:
                    if biaslist[-1]<>vglist[-1]:
                        vglist.append(biaslist[-1])
                else:
                    vglist.append(biaslist[-1])
    vs_len=len(vslist)
    vb_len=len(vblist)
    vg_len=len(vglist)
    vd_len=len(vdlist)
    biasnum=vs_len*vb_len*vg_len*vd_len
    vdlist_s=','.join(vdlist)
    vslist_s=','.join(vslist)
    vglist_s=','.join(vglist)
    vblist_s=','.join(vblist)
            
    general.extend(['**S parameter for multiple biases. Saved by RFPro for Windows(2) on 3/19/2003**',\
                    'PortNumber= 2',\
                    'User Name=Me',\
                    'Lot Name=Lot1',\
                    'Die Number= 1',\
                    'Device Number= 1',\
                    'Device Type= %d'%dtype,\
                    'Connect Type=',\
                    'Created Data=03-19-2003',\
                    'Temperature= 25',\
                    'Comment=Comments',\
                    'PolarType= 1',\
                    '0.0000025, 1.8E-07, 0, 0, 0.000001, 1E-10, 32, 1.52E-10, 1.52E-10, 0.00022, 0.00022, 1, 1, 1, 1, 1, 1, 1, 1,  1',\
                    'ExtraInfo= 0',\
                    'Z0= 50'])
    frequency.extend(['Start Frequency= %s'%startf,\
                      'Stop Frequency= %s'%endf,\
                      'Number of Points= %s'%potnum])
    bias.extend(['Total Biases= %d'%biasnum,\
                 'Bias1 Mode= 0',\
                 'Bias1#= %d'%vg_len,\
                 vglist_s,\
                 'Bias2 Mode= 0',\
                 'Bias2#= %d'%vd_len,\
                 vdlist_s,\
                 'Bias3 Mode= 0',\
                 'Bias3#= %d'%vs_len,\
                 vslist_s,\
                 'Bias4 Mode= 0',\
                 'Bias4#= %d'%vb_len,\
                 vblist_s])
    head.extend(general)
    head.extend(frequency)
    head.extend(bias)

def bodycvt(header):
    global body
    body=[]
    startlist=[]
    endlist=[]
    bodylist=[]
    for i in range(0,len(header)):
        if header[i].find('BEGIN_DB')<>-1:
            startlist.append(i)
        elif header[i].find('END_DB')<>-1:
            endlist.append(i)
    for i in range(0,len(startlist)):
        bodytemp=header[startlist[i]:endlist[i]]
        bodylist.append(bodytemp)
    for i in range(0,len(bodylist)):
        tempbody=[]
        tempbody.append('Bias#%d Voltages & Currents:'%(i+1))
        data=bodylist[i]
        for k in range(0,len(data)):
            if data[k].find('ICCAP_VAR')<>-1:
                inlist=data[k].split()
                if 'vs' in inlist:
                       vs=inlist[-1]
                elif 'vb' in inlist:
                       vb=inlist[-1]
                elif 'vd' in inlist:
                       vd=inlist[-1]
                elif 'vg' in inlist:
                       vg=inlist[-1]
        tempbody.append(' %s , %s , %s , %s , 0 , 2.093147E-10 , 0 , 0'%(vg,vd,vs,vb))
        tempbody.append('**Frequency         S11x                S11y                S12x                S12y                S21x                S21y                S22x                S22y')
        n=0
        for k in range(0,len(data)):
            if data[k].find('#freq')<>-1:
                n=k
            elif k>n and n<>0:
                templist=data[k].split()
                for i in range(-9,0):
                    templist[i]='%-20s'%templist[i]
                templist=templist[-9:]
                tempstr=''.join(templist)
                tempbody.append(tempstr)
        body.extend(tempbody)


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

def rfcvt(header,mdmname,path):
    headCvt(header,mdmname)
    bodycvt(header)
    link(path)
    

        

            
    
