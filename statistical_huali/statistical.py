# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:03:54 2012

@author: zhaiyt
"""
import os
import sys
import string
from PyQt4.QtCore import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

global convertlist
convertlist=[]

global keyoplist
keyoplist=[]

global instancelist
instancelist=[]

global d_type
d_type = 'NMOS'

def findFile():
    
    global convertlist
    convertlist=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for mem in files:
            if mem.split('.')[-1]=='dat' or mem.split('.')[-1]=='DAT':
                mem=os.path.join(root,mem)
                convertlist.append(mem)
    num=len(convertlist)
    if num==0:
        print
        raw_input('No file find ,please put data file to current dirctory')
        sys.exit()
    else:
        print
        print("%s files need to convert:" % num)
        print
        for hitfile in convertlist:
            print(hitfile)
            print
            
def isDataline(line):
    # to see if one line is a data line  like 'VTGM1_SPK017D_N12STR1SP3Y_9_d054\
                             #,,R,V,-8.433325E+01,+5.087684E-01,+5.008418E-01...' 
    temp_list = line.split(',')
    if len(temp_list) >= 5:
        try:
            float(temp_list[-2])
            return True
        except:
            return False       
    else:
        return False
        
def getDataFromline(line):
    # get the data section from a data line 
    temp_list = line.split(',')
    index = 0
    for i in range(0,len(temp_list)):
        try:
            float(temp_list[i])
            index = i
            break
        except:
            pass
    return temp_list[index:]
    
def deleteBadpoint(data_list,log):
    #delete the bad point in one list
    #if the sign of data is different from median                -->delete
    #if the data is deviate the median too large(<0.4,>2.5)      -->delete
    temp_list=[]
    ori_list=[]
    bad_index=[]
    for i in range(0,len(data_list)):
        try:
            value = float(data_list[i])
            temp_list.append(value)
        except:
            log.emit(SIGNAL("log_append(PyQt_PyObject)"),["WARNING: %s can't convert to float"%temp_list[i],'warning'])
            return False
    ori_list[:] = temp_list
    temp_list.sort()
    median = temp_list[len(temp_list)//2]
    
    for i in range(0,len(ori_list)):
        if ori_list[i]*median<0 or abs(ori_list[i])/abs(median)<0.4 or abs(ori_list[i])/abs(median)>2.5:
            bad_index.append(i)
        else:
            pass
    return bad_index
    
def deletePointoutsigma(data_list):
    pass
    
def outputGroup(head_list,log):
    #devide the data line to group
    #like VTGM1,VTGM2,VTGM_MIS should be devided to one group
    #the instance should be match also
    global keyoplist
    keyoplist=[]
    global instancelist
    instancelist=[]
    out_dic={}
    out_mark=[]

    for i in range(0,len(head_list)):
        temp_list = head_list[i].split('_')
        if temp_list[1] != 'MIS':
            kop = temp_list[0][:-1]
            instance = temp_list[-2] + '_' +temp_list[-1]
            mark = kop +'_'+ instance       
            if kop not in keyoplist:
                keyoplist.append(kop)
            if instance not in instancelist:
                instancelist.append(instance)
        else:
            continue
        if mark in out_mark:
            out_dic[mark].append(head_list[i])
        else:
            out_mark.append(mark)
            out_dic[mark]=[head_list[i]]
    keyoplist = list(set(keyoplist))
    for mark in out_dic.keys():
        if len(out_dic[mark]) != 2:
            log.emit( SIGNAL("log_append(PyQt_PyObject)"), ["WARNING: %s has %s"%(mark,','.join(out_dic[mark])),'warning'] )
            del out_dic[mark]
    for out_list in out_dic.values():
        out_list.sort(key=lambda out:out.split('_')[0][-1])
    return out_dic
    
def calstdev(valuelist):
    value_list=[]
    if len(valuelist)==0:
        return 0
    if type(valuelist[0])==str:
        for i in range(0,len(valuelist)):
            value_list.append(float(valuelist[i])) 
    else:
        value_list.extend(valuelist)
    totle1= 0 
    totle2= 0 
    for i in range(0,len(value_list)):
        totle1 = totle1+ value_list[i]**2
        totle2 = totle2+ value_list[i]
    n=len(value_list)
    stdev=((totle1*n - totle2**2)/(n*(n-1)))**0.5
    return stdev

def calmean(valuelist):
    value_list=[]
    for i in range(0,len(valuelist)):
        value_list.append(float(valuelist[i])) 
    total=0
    for i in range(0,len(valuelist)):
        total=total+value_list[i]
    mean=total/(len(valuelist))
    return mean

def output_gwat(line_dic,line_dic_del,output_dic,file_path,file_path_del,out_flag,ratio,log):
    global instancelist
    global keyoplist
    global d_type
    head=[ '#',\
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
           '#',\
           '# DATA section -- output data table with many variation data points',\
           '#',\
           '' ]
    head_str = '\n'.join(head)
    kop_str=(20*' ').join(keyoplist)+'\n'
    body_list=[]
    body_list_del=[]
    for instance in instancelist:
        temp_list = instance.split('_')
        w =str(float(temp_list[0].replace('d','.')))
        l =str(float(temp_list[1].replace('d','.')))
        title='.START_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)+kop_str
        tail='.END_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)
        section = []
        section_del =[]
        for i_kop,kop in enumerate(keyoplist):
            for out_list in output_dic.values():
                temp_list = out_list[0].split('_')
                cur_kop = temp_list[0][:-1]
                cur_instance = temp_list[-2] + '_' +temp_list[-1]
                mismatch = cur_kop + '_' + cur_instance
                if cur_kop == kop and cur_instance == instance:
                    first_list = line_dic[out_list[0]]
                    second_list = line_dic[out_list[1]]
                    if out_flag == 'gwat':
                        for i in range(0,len(first_list)):
                            if i_kop == 0:
                                section.append([])
                                section[-1].append(first_list[i])
                            else:
                                section[i].append(first_list[i])
                        for i in range(0,len(second_list)):
                            if i_kop == 0:
                                section.append([])
                                section[-1].append(second_list[i])
                            else:
                                section[i+len(first_list)].append(second_list[i])
                                
                        #output delete data points
                        first_list_del = line_dic_del[out_list[0]]
                        for i in range(0,len(first_list_del)):
                            if i_kop == 0:
                                section_del.append([])
                                section_del[-1].append(first_list_del[i])
                            else:
                                section_del[i].append(first_list_del[i])
                        second_list_del = line_dic_del[out_list[1]]
                        for i in range(0,len(second_list_del)):
                            if i_kop == 0:
                                section_del.append([])
                                section_del[-1].append(second_list_del[i])
                            else:
                                section_del[i+len(first_list_del)].append(second_list_del[i])
                        #output the median and mean value for gwat!
                        combin_list = first_list + second_list
                        mean_value = calmean(combin_list)
                        median_value = getMedian(combin_list)
                        ratio_control = mean_value/median_value
                        # if the ratio value out of the ratio_control (0.99 or 1.01 eg.) set text color red
                        color_str=''
                        if ratio_control<(1-ratio) or ratio_control>(1+ratio):
                            color_str = 'error'
                        
                        log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Kop:%s Instance:%s"%(kop,instance),color_str])
                        log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Mean Value:%s"%mean_value,color_str])
                        log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Median Value:%s"%median_value,color_str])
                        log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Ratio:%s%%"%(mean_value/median_value*100),color_str])
                        log.emit(SIGNAL("log_append(PyQt_PyObject)"),["-----------------------------------------------",color_str])
                    else:
                        global_list = first_list + second_list
                        mismatch_list = line_dic[mismatch]

                        stdev_global = calstdev(global_list)
                        median_global = getMedian(global_list)
                        stdev_mismatch = calstdev(mismatch_list)
                    
                        kop_lower = kop.lower()
                        if kop_lower.startswith('i'):
                            if  ( stdev_global**2 - ((stdev_mismatch*median_global)**2)/2 ) < 0 :
                                color_str='error'
                                log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Kop:%s Instance:%s"%(kop,instance),color_str])
                                log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Warning: the local variation is larger than the total variation!",color_str])
                                log.emit(SIGNAL("log_append(PyQt_PyObject)"),["-----------------------------------------------------------------",color_str])
                                gspec_value = 0
                            else:
                                gspec_value = ( stdev_global**2 - ((stdev_mismatch*median_global)**2)/2 )**0.5 
                        else:
                            if  ( stdev_global**2 - (stdev_mismatch**2)/2 ) < 0 :
                                color_str='error'
                                log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Kop:%s Instance:%s"%(kop,instance),color_str])
                                log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Warning: the local variation is larger than the total variation!",color_str])
                                log.emit(SIGNAL("log_append(PyQt_PyObject)"),["-----------------------------------------------------------------",color_str])
                                gspec_value = 0
                            else:
                                gspec_value = ( stdev_global**2 - (stdev_mismatch**2)/2 )**0.5 
                        if i_kop == 0:
                            section.append([])
                            section[-1].append(gspec_value)
                        else:
                            section[-1].append(gspec_value)
                    
        for i_section in range(0,len(section)):
            for j_data in range(0,len(section[i_section])):
                section[i_section][j_data] = "%-25s"%section[i_section][j_data]
            section[i_section] = ''.join(section[i_section])
        section_str = '\n'.join(section)
        body = title + section_str + '\n' +tail
        body_list.append(body)

        if out_flag == 'gwat':
            #output delete data points
            for i_section in range(0,len(section_del)):
                for j_data in range(0,len(section_del[i_section])):
                    section_del[i_section][j_data] = "%-25s"%section_del[i_section][j_data]
                section_del[i_section] = ''.join(section_del[i_section])
            section_str_del = '\n'.join(section_del)
            body_del = title + section_str_del + '\n' + tail
            body_list_del.append(body_del)

    f= open(file_path,'w')
    body = ''.join(body_list)
    f.writelines(head_str+body)
    f.close()

    if out_flag == 'gwat':
        f= open(file_path_del,'w')
        body = ''.join(body_list_del)
        f.writelines(body)
        f.close()
    
def output_lwat(line_dic,mismatch_list,file_path,out_flag = 'lwat'):
    # output the lwat file
    global instancelist
    global keyoplist
    global d_type
    head=[ '#',\
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
           '#',\
           '# DATA section -- output data table with many variation data points',\
           '#',\
           '' ]
    head_str = '\n'.join(head)
    kop_str=(20*' ').join(keyoplist)+'\n'
    body_list=[]
    for instance in instancelist:
        temp_list = instance.split('_')
        w =str(float(temp_list[0].replace('d','.')))
        l =str(float(temp_list[1].replace('d','.')))
        title='.START_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)+kop_str
        tail='.END_DATA|%s|W=%s|L=%s|T=25\n'%(d_type,w,l)
        section = []
        for i_kop,kop in enumerate(keyoplist):
            for mismatch in mismatch_list:
                temp_list = mismatch.split('_')
                cur_kop = temp_list[0]
                cur_instance = temp_list[-2] + '_' +temp_list[-1]
                if cur_kop == kop and cur_instance == instance:
                    first_list = line_dic[mismatch]
                    if out_flag == 'lwat':
                        for i in range(0,len(first_list)):
                            if i_kop == 0:
                                section.append([])
                                section[-1].append(first_list[i])
                            else:
                                section[i].append(first_list[i])
                    else:
                        stdev = '%0.6g'%calstdev(first_list)
                        if i_kop == 0:
                            section.append([])
                            section[-1].append(stdev)
                        else:
                            section[-1].append(stdev)
        for i_section in range(0,len(section)):
            for j_data in range(0,len(section[i_section])):
                section[i_section][j_data] = "%-25s"%section[i_section][j_data]
            section[i_section] = ''.join(section[i_section])
        section_str = '\n'.join(section)
        body = title + section_str + '\n' +tail
        body_list.append(body)
    if out_flag == 'lwat':
        f= open(file_path,'w')
    else:
        f= open(file_path,'w')
    body = ''.join(body_list)
    f.writelines(head_str+body)
    f.close()
    
def getMedian(data_list):
    # get the median value of one list
    temp_list=[]
    for i in range(0,len(data_list)):
        try:
            value=float(data_list[i])
            temp_list.append(value)
        except:
            pass
    temp_list.sort()
    return temp_list[len(temp_list)//2]

def findspecfile(output_dir):

    spec_list=[]
    for root,dirs,files in os.walk(output_dir):
        for fil in files:
            if fil.split('.')[-1].find('lspc')<>-1:
                spec_path = os.path.join(root,fil)
                spec_list.append(spec_path)
    return spec_list

def plot(filename, show_flag,log):
    f=open(filename)
    content=f.readlines()
    f.close()
    x=[]
    kop_list=[]
    find_flag = 0
    for i in range(0,len(content)):
        if content[i].startswith('.START_DATA'):
            find_flag= 1
            continue
        if find_flag:
            kop_list = content[i].split()
            break
    kop_value_list=[]
    for kop in kop_list:
        kop_value_list.append([])
    for i in range(0,len(content)):
        if content[i].startswith('.START_DATA'):
            temp_list=content[i].split('|')
            w_str=temp_list[-3].split('=')[-1]
            l_str=temp_list[-2].split('=')[-1]
            w=string.atof(w_str)
            l=string.atof(l_str)
            x.append(1/((w*l)**0.5))
            
            temp_list=content[i+2].split()
            for kop_index in xrange(len(kop_value_list)):
                kop_value_list[kop_index].append(string.atof(temp_list[kop_index]))

    x=np.array(x)
    for i in xrange(len(kop_value_list)):
        kop_value_list[i] = np.array(kop_value_list[i])
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)
    shape_list=['s','o','x','h']
    color_list=['b','r','g','k']
    for i in xrange(len(kop_value_list)):
        ax.plot(x,kop_value_list[i],shape_list[i],label=kop_list[i])
    ax.legend(bbox_to_anchor = (1, 0.28))
    ax.set_title(os.path.basename(filename))
    if show_flag<>0:
        plt.show()
        plt.close()
    else:
        png_path='.'.join(filename.split('.')[:-1]) + '.png'
        plt.savefig(png_path)
        plt.close()
        log.emit(SIGNAL("log_append(PyQt_PyObject)"),['plot %s...'%filename,'info'])
    
def convert(log,input_path,output_dir,sigma,ratio,rename):
    global d_type
    file_name = os.path.basename(input_path).split('.')[0]

    log.emit(SIGNAL("log_append(PyQt_PyObject)"),['Convert %s...'%os.path.basename(input_path),'info'])
    f=open(input_path,'r')
    content=f.readlines()
    f.close()
   
   
    rename_dic={}
    rename_list = rename.split(";")
    for i in range(len(rename_list)):
        temp_list=rename_list[i].split(':')
        for j in range(len(temp_list)):
            temp_list[j]=temp_list[j].strip()
        if len(temp_list) == 2:
            rename_dic[temp_list[0]] = temp_list[1]
            
    line_head=[]
    line_dic={}
    line_dic_del={}
    
    pre_kop = rename_dic.keys()
    
    for j, line in enumerate(content):
        line = line.strip('\r,\n')
        if(isDataline(line)):
            line_list=line.split(',')
            for i in range(0,len(pre_kop)):
                if line_list[0].find(pre_kop[i]) != -1:
                    line_list[0]=line_list[0].replace(pre_kop[i],rename_dic[pre_kop[i]])
            if line_list[0] in line_head:
                line_dic[line_list[0]].extend(getDataFromline(line))
            else: 
                line_head.append(line_list[0])
                line_dic[line_list[0]] = getDataFromline(line)
                
    output_dic=outputGroup(line_head,log)
    
    # get the type 'NMOS' or 'PMOS'
    for out_list in output_dic.values():
        temp_list = out_list[0].split('_')
        if temp_list[-3][0] == 'P' or temp_list[-3][0] == 'p':
            d_type = 'PMOS'
            break
        else:
            d_type = 'NMOS'
            break
 
    for instance in instancelist:
        ###################
        #pre processing
        ###################
        bad_index = []
        # get the bad index for one specfic instance
        for out_list in output_dic.values():
            for i_out in range(0,len(out_list)):
                temp_list = out_list[i_out].split('_')
                cur_instance = temp_list[-2] + '_' +temp_list[-1]
                if cur_instance == instance:
                    bad_index.extend(deleteBadpoint(line_dic[out_list[i_out]],log))
        bad_index=list(set(bad_index))

        # delete the bad points
        for out_list in output_dic.values():
            for i_out in range(0,len(out_list)):
                temp_list = out_list[i_out].split('_')
                cur_instance = temp_list[-2] + '_' +temp_list[-1]
                if cur_instance == instance:
                    data_list = line_dic[out_list[i_out]]
                    replace=[]
                    delete=[]
                    for i_data in range(0,len(data_list)):
                        if i_data not in bad_index:
                            replace.append(data_list[i_data])
                        else:
                            delete.append(data_list[i_data])
                            
                    line_dic[out_list[i_out]] = replace
                    line_dic_del[out_list[i_out]] = delete
                    
        ###################################
        #delete the points out of sigma    
        ###################################
        # get the bad index of points out of sigma
        bad_index = [] 
        for out_list in output_dic.values():
            for i_out in range(0,len(out_list)):
                temp_list = out_list[i_out].split('_')
                cur_instance = temp_list[-2] + '_' +temp_list[-1]
                if cur_instance == instance:
                    data_list = line_dic[out_list[i_out]]
                    stdev = calstdev(data_list)
                    mean = calmean(data_list)
                    for i_data in range(0,len(data_list)):
                        if sigma == 0:
                            pass
                        elif abs(float(data_list[i_data]) - mean) > sigma * abs( stdev ):
                            bad_index.append(i_data)
        bad_index=list(set(bad_index))
        
        # delete the data points out of sigma
        for out_list in output_dic.values():
            for i_out in range(0,len(out_list)):
                temp_list = out_list[i_out].split('_')
                cur_instance = temp_list[-2] + '_' +temp_list[-1]
                if cur_instance == instance:
                    data_list = line_dic[out_list[i_out]]
                    replace=[]
                    delete=[]
                    for i_data in range(0,len(data_list)):
                        if i_data not in bad_index:
                            replace.append(data_list[i_data])
                        else:
                            delete.append(data_list[i_data])
                    line_dic[out_list[i_out]] = replace
                    line_dic_del[out_list[i_out]].extend(delete)
    ##############################################################################################################
    # 1.  (value_n_1 - value_n_2 ) / value_list_median = lvwat_value_n
    # 2.  stdev of lvwat_value_list   -> lspc
    # 3.  value_1_list + value_2_list -> gwat_list
    # 4.  ((stdev of '3')**2  - ('2'**2)/2)**0.5  -> gspc
    ##############################################################################################################
    

    #first we should get the mismatch list then we can output the .gspec and lspec, lvwat

    #########################
    # Get the mismatch list
    #########################
    mismatch_list=[]
    for out_list in output_dic.values():
        temp_list = out_list[0].split('_')
        kop = temp_list[0][:-1]
        instance = temp_list[-2] + '_' +temp_list[-1]
        mark = kop +'_'+ instance 
        mismatch_list.append(mark)
        
        mis_list=[]
        # kop is I
        if (kop.upper()).startswith('I'):
            temp_list = line_dic[out_list[0]] + line_dic[out_list[1]]
            median = getMedian(temp_list)
            for i_data in range(0,len(line_dic[out_list[0]])):
                first = float(line_dic[out_list[0]][i_data])
                second = float(line_dic[out_list[1]][i_data])
                value = '%0.6e'%((first-second)/median)
                mis_list.append(value)
            line_dic[mark] = mis_list
        else:
            for i_data in range(0,len(line_dic[out_list[0]])):
                first = float(line_dic[out_list[0]][i_data])
                second = float(line_dic[out_list[1]][i_data])
                value = '%0.6e'%(first-second)
                mis_list.append(value)
            line_dic[mark] = mis_list


    gwat_file_name = os.path.join(output_dir,(file_name+'.gwat'))
    gwat_file_name_del = os.path.join(output_dir,(file_name+'_delete.txt'))
    out_flag = 'gwat'
    output_gwat(line_dic,line_dic_del,output_dic,gwat_file_name,gwat_file_name_del,out_flag,ratio,log)
    log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Output gwat file %s"%os.path.basename(gwat_file_name),'info'])

    gspec_file_path = os.path.join(output_dir,(file_name + '.gspc'))
    out_flag = 'gspc'
    output_gwat(line_dic,line_dic_del,output_dic,gspec_file_path,gwat_file_name_del,out_flag,ratio,log)
    log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Output gspec file %s"%os.path.basename(gspec_file_path),'info'])


    lwat_file_path = os.path.join(output_dir,(file_name + '.lvwat'))
    output_lwat(line_dic, mismatch_list,lwat_file_path)
    log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Output lwat file %s"%os.path.basename(lwat_file_path),'info'])
    
    lspec_file_path = os.path.join(output_dir,(file_name + '.lspc'))
    output_lwat(line_dic, mismatch_list,lspec_file_path,out_flag ='lspec')
    log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Output lspec file %s"%os.path.basename(lspec_file_path),'info'])

    spec_list=findspecfile(output_dir)
    for i in xrange(len(spec_list)):
        show_flag=0
        try:
            plot(spec_list[i],show_flag,log)
        except:
            log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Plot spec file %s failed"%os.path.basename(spec_list[i]),'error'])
    
    log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Success...",'info'])
    log.emit(SIGNAL("log_append(PyQt_PyObject)"),["Press result button to open result folder.",'info'])
