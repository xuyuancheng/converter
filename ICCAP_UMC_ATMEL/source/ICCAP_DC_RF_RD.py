# -*-coding: utf-8 -*-

import os
import sys
from time import ctime
import re
import string
from rf_cvt import rfcvt
from dc_cvt import dccvt
from rd_cvt import rdcvt
from dc_hang import dchang

global convertlist

def findFile():
    '''Find *.mdm file in current directory'''
    global convertlist
    convertlist=[]
    flag=0
    
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for fil in files:
            splitename=os.path.splitext(fil)
            if splitename[-1]=='.mdm':                                                   #may change if format change
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
        raw_input('No .mdm file found, please put .mdm file or data folder to corrent directory')
        sys.exit()

def getHeader(cvtfile):
    '''Find how much header in cvtfile and return '''
    start=[]
    headerlist=[]
    f=open(cvtfile,'r')
    tempcontent=f.readlines()
    f.close()
    for i in range(0,len(tempcontent)):
        if tempcontent[i].find('BEGIN_HEADER')<>-1:
            start.append(i)
    for i in range(0,len(start)):
        if i<>(len(start)-1):
            temp=tempcontent[start[i]:start[i+1]]
        else:
            temp=tempcontent[start[i]:]
        while True:
            pop=temp.pop()
            if pop.find('END_DB')<>-1:
                temp.append(pop)
                headerlist.append(temp)
                break
    return headerlist

def typeJudge(header):
    '''judge the header's type'''
    out=[]
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
        output=temp[i].split()
        for k in range(0,len(output)):
            if output[k].isalpha():
                out.append(output[k])
                break
    if len(out)==1 and out[0]=='s':
        htype='RF'
    elif not 's' in out :
        htype='DC'
    else:
        htype='RD'
    return htype
                        
    

if __name__=='__main__':
    
    findFile()
    for convertfile in convertlist:
        try:
            print "--Start to convert file %s --"%convertfile
            nametemp=os.path.basename(convertfile)
            name=nametemp.split('.')[0]
            headerlist=getHeader(convertfile)
            for header in headerlist:
                htype=typeJudge(header)
                if htype=='DC':
                    try:
                        dcdir=os.path.join('Converted data',name)
                        if not os.path.exists(dcdir):
                            os.makedirs(dcdir)
                        i=1
                        while True:
                            if i==1:
                                dcpath=os.path.join(dcdir,(name+'_dc'+'.dat'))
                            else:
                                dcpath=os.path.join(dcdir,(name+'_dc(%s)'%(i-1)+'.dat'))
                            if os.path.exists(dcpath):
                                i=i+1
                            else:
                                break
                        dccvt(header,convertfile,dcpath)
                    except:
                        print "ERROR:------Convert DC part failed-----------"
                elif htype=='RF':
                    try:
                        rfdir=os.path.join('Converted data',name)
                        if not os.path.exists(rfdir):
                            os.makedirs(rfdir)
                        i=1
                        while True:
                            if i==1:
                                rfpath=os.path.join(rfdir,(name+'_rf'+'.sp2'))
                            else:
                                rfpath=os.path.join(rfdir,(name+'_rf(%s)'%(i-1)+'.sp2'))
                            if os.path.exists(rfpath):
                                i=i+1
                            else:
                                break
                        rfcvt(header,convertfile,rfpath)
                    except:
                        print "ERROR:------Convert RF part failed-----------"
                elif htype=='RD':
                    try:
                        rddir=os.path.join('Converted data',name)
                        if not os.path.exists(rddir):
                            os.makedirs(rddir)
                        i=1
                        while True:
                            if i==1:
                                rdpath=os.path.join(rddir,(name+'_rf_dc'+'.dat'))
                            else:
                                rdpath=os.path.join(rddir,(name+'_rf_dc(%s)'%(i-1)+'.dat'))
                            if os.path.exists(rdpath):
                                i=i+1
                            else:
                                break
                        rdcvt(header,convertfile,rdpath)
                    except:
                        print "ERROR:------Convert rf_dc part failed-----------"
        except:
                print "ERROR:------Convert file %s failed-----------"%convertfile
    try:
        dchang()
    except:
        print "ERROR:------Combine id_vg id_vd data file failed-----------"
    raw_input('All complete... ')

            
            
        
            
