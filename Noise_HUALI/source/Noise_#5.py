# -*-coding: utf-8 -*-

import os
import sys
import string
import re

global convertlist
global convertgroup
global head
global body
global bodylist
global frequency
global measured_data_list
global vglist
global vdlist
global index

body=[]
bodylist=[]
head=[]
convertlist=[]
convertgroup={}
measured_data_list=[]
frequency=['[Frequency Selection]']
vglist=[]
vdlist=[]
index=[]

def findFile():
    '''Find *.csv file in current directory'''
    global convertlist
    convertlist=[]
    flag=0
    
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for fil in files:
            splitename=os.path.basename(fil).lower()
            if splitename=='noise.csv':                                  #may change if format change
                fil=os.path.join(root,fil)
                convertlist.append(fil)
                flag=1
    if flag==1:
        num=len(convertlist)
        print
        print "%s files need to convert:" % num
        print 
#        for hitfile in convertlist:
#            print hitfile
    else:
        print
        raw_input('No .csv file found, please put .csv file or data folder to corrent directory')
        sys.exit()
 
def makeDir(folder_name,file_name):
    '''Make result dir'''
    file_name=file_name+'.noi'
    temp1=os.getcwd()
    temppath=os.path.join(temp1,'Converted data')     #file directory
    if folder_name <> '':
        path=os.path.join(temppath,folder_name)
    else:
        path=temppath
    if not os.path.exists(path):
        os.makedirs(path)
    data_path = os.path.join(path,file_name)
    return data_path

def headCvt(cvtfile,w_value,l_value,runtime,times,samp_value_list):
    global head
    global frequency
    global measured_data_list
    global vglist
    global vdlist
    global index
    general=[]
    bias=[]
    measured_data=[]
    '''Get head imformation'''
    #get imformation from filename
    temppath=os.path.dirname(cvtfile)
    filename=os.path.basename(temppath)
    filelist=filename.split('_')
    #print filelist
    dtype=0
    vgflag=0
    for i in range(0,len(filelist)):
        tempstr=filelist[i].upper()
        if tempstr=='NMOS':
            dtype=1
        elif tempstr=='PMOS':
            dtype=-1
        elif tempstr.endswith('V'):
            if vgflag==0:
                vglist.append(tempstr.strip('V'))
                vgflag=1
            else:
                vdlist.append(tempstr.strip('V'))
    if dtype==0:
        dtype=1
    content=open(cvtfile,'r')
    lines=content.readlines() 
    content.close()
    measured_data.extend([[],[]])
    cflag=0
    measured_data[0]='[Measured Data] (Vrd, Ird, Vg, Ig, Beta, Gm, Gd, tRd, tRb, fRd, fRb, Amp, Vp, Vn, Sampling Noise...)'
    measure_key=['Vrd', 'RealId', 'Vg', 'Ig', 'Beta', 'Gm', 'Gd', 'tRd', 'tRb', 'fRd', 'fRb', 'Amp', 'Vp', 'Vn']
    temp_key=[]
    temp_value=[]
    spling=[]
    sid_flag = 3
    for line in lines:
        line=line.strip('\n')
        line=line.strip('\r')
        if line.find('Temperature')<>-1:
            temp=line.split(',')
            temperature=temp[1].strip('\n')
            temperature=string.atof(temperature)-273.15
        elif line.find('#CALC')<>-1:
            cflag=1
#        elif cflag==1:
#            temp=line.split(',')
#            measured_data[0].append(temp[0])
#            measured_data[1].append(temp[1].strip('\n'))
#            count=count+1
#        if count==5:
#            measured_data[0]='[Measured Data] ('+','.join(measured_data[0])+')'
#            measured_data[1]=','.join(measured_data[1])
#            break
        elif cflag==1:
            temp=line.split(',')
            if len(temp)==2:# and temp[1].isdigit():        #check if this line is a measure data define line                
                temp_key.append(temp[0])
                temp_value.append(temp[1])
            elif line.startswith('Freq[Hz]'):
                for i in range(0,len(temp)):
                    if temp[i].find('Sid')<>-1:
                        sid_flag=i
            elif len(temp)==6: # and temp[0].isdigit():   #check if this line is a data line
#                if temp[0]=='100':
#                    spling.append(temp[sid_flag])
#                elif temp[0]=='1000':
#                    spling.append(temp[sid_flag])
                try:
                    f_value=float(temp[0])
                    if f_value in samp_value_list:
                        spling.append(temp[sid_flag])
                except:
                    pass
    
    measured_data[1]=(len(measure_key))*['0']        # initial the measured value except sampling (the last one)
    for i in range(0, len(temp_key)):
        if temp_key[i] in measure_key:
            key_index=measure_key.index(temp_key[i])
            measured_data[1][key_index] = temp_value[i]
    measured_data[1].extend(spling)
    measured_data[1][0]=vdlist[-1]
    measured_data[1][2]=vglist[-1]
    measured_data[1]=','.join(measured_data[1])
            
    if runtime==0:
        measured_data_list.extend(measured_data)
    else:
        measured_data_list.append(measured_data[1])
    if runtime==times-1:
        vglist_new=(list(set(vglist)))
        vdlist_new=(list(set(vdlist)))
        vglist_new.sort()
        vdlist_new.sort()
        
        # resort the order according to the bias
        for i in range(0,len(vdlist_new)):
            for j in range(0,len(vglist_new)):
                templist=[]
                for w in range(0,len(vdlist)):
                    if vdlist[w]==vdlist_new[i]:
                        templist.append(w)
                for k in range(0,len(templist)):
                    if vglist[templist[k]]==vglist_new[j]:
                        index.append(templist[k])
                        
        # resort the measured_data_list according to the index 
        temp_list=measured_data_list[1:]
        measured_data_list_new=[]
        measured_data_list_new.append(measured_data_list[0])
        for i in range(0,len(index)):
            measured_data_list_new.append(temp_list[index[i]])
        
        general.extend(['*Multiple-bias noise file(Text). Created by NoisePro2.0.0',\
              '*Any comment typed here will be recorded into the NoisePro setup file and Noise Data Files.',\
              '[General Information]',\
              'User Name=XXX',\
              'Lot Name=XXX',\
              'Device Name=#10',\
              'Created Date=XXX',\
              'temperature= %s'%temperature,\
              'Device Type= 1 ',\
              'Tox= 1000',\
              'drawnL= %s'%l_value,\
              'drawnW= %s'%w_value,\
              'Xj= 0.5 ',\
              'polarType= %d '%dtype,\
              '[Additonal Instaneces: 6]',\
              'Nrd= 0',\
              'Nrs= 0',\
              'Ad= 0',\
              'As= 0',\
              'Pd= 0',\
              'Ps= 0' ])
        bias.extend(['[Bias Selection]',\
                    'Port1 Enabled=True',\
                    'Port1 Mode= 0 ',\
                    'Port1 Bias Number= %d'%len(vdlist_new),\
                    '%s'%(','.join(vdlist_new)),\
                    'Port2 Enabled=True',\
                    'Port2 Mode= 0',\
                    'Port2 Bias Number= %d'%len(vglist_new),\
                    '%s'%(','.join(vglist_new)),\
                    'Port3 Enabled=True',\
                    'Port3 Mode= 0',\
                    'Port3 Bias Number= 1',\
                    '0',\
                    'Port4 Enabled=True',\
                    'Port4 Mode= 0',\
                    'Port4 Bias Number= 1',\
                     '0' ])
        head.extend(general)
        head.extend(frequency)
        head.extend(bias)
        head.extend(measured_data_list_new)

def headCvt_fre(cvtfile,runtime,samp_value_list):
    global frequency
    if runtime==0:
        fre=[]
        flag=0
        content=open(cvtfile,'r')
        lines=content.readlines()
        content.close()
        for j in range(0,len(lines)):
            if flag<>0 and len(lines[j])>=flag:
                temp=lines[j].split(',')
                temp_list=list(temp[0])
                digit_flag=0
                for k in range(0,len(temp_list)):
                    if temp_list[k].isdigit() or temp_list[k]=='.':
                        pass
                    else:
                        digit_flag=1
                if digit_flag==0: 
                        fre.append(temp[0])
            if lines[j].find('Freq[Hz]')<>-1:
                flag=1
    
        start_fre='Start frequency= '+fre[0]
        stop_fre='Stop frequency= '+fre[-1]
        point_num='Noise point Number= %s'%len(fre)
        sampling=[]
        sampling_num=len(samp_value_list)
        sampling_num_str='Sampling Number= %d'%sampling_num
        sampling.append(sampling_num_str)
        for i in range(0,len(samp_value_list)):
            sampling_value_str='Sampling Frequency# %d= %f'%(i+1,samp_value_list[i])
            sampling.append(sampling_value_str)
        frequency.append('[Frequency Selection]')
        frequency.append(start_fre)
        frequency.append(stop_fre)
        frequency.append(point_num)
        frequency.extend(sampling)
    else:
        pass
    
def bodyCvt(cvtfile,runtime):
    global body  
    flag=0
    content=open(cvtfile,'r')
    lines=content.readlines()
    content.close()
    tflag1=0
    tflag2=0
    if runtime==0:
        for j in range(0,len(lines)):
            if flag<>0: #and len(lines[j])>=flag:
                templist=[]
                temp=lines[j].split(',')
                if len(temp) >= flag:
                    templist.append(temp[0])
                    templist.append(temp[flag])
                    bodylist.append([])
                    bodylist[tflag1].extend(templist)
                    tflag1=tflag1+1
                else:
                    continue
            if lines[j].find('Freq[Hz]')<>-1:
                temp=lines[j].split(',')
                for i in range(0,len(temp)):
                    if temp[i].find('Sid')<>-1:
                        flag=i


    else:
        for j in range(0,len(lines)):
            if flag<>0: # and len(lines[j])>=flag:
                temp=lines[j].split(',')
                if len(temp) >= flag:
                    bodylist[tflag2].append(temp[flag])
                    tflag2=tflag2+1
                else:
                    continue
            if lines[j].find('Freq[Hz]')<>-1:
                temp=lines[j].split(',')
                for i in range(0,len(temp)):
                    if temp[i].find('Sid')<>-1:
                        flag=i            
 
def link(path):
    global head
    global body
    global bodylist
    bodystrlist=['[Noise Spectrum]']
    for i in range(0,len(bodylist)):
        bodystrlist.append(','.join(bodylist[i]))
    cvtdata=open(path,'w')
    headstr='\n'.join(head)
    bodystr='\n'.join(bodystrlist)
    cvtdata.writelines(headstr)
    cvtdata.writelines('\n')
    cvtdata.writelines(bodystr)
    cvtdata.close()
    
def devide():
    global convertlist
    global convertgroup
    group_name_list=[]
#    #match the N/P type folder name
#    polar='[n,p]\d+'
#    polar_match=re.compile(polar)
    temp_path=os.getcwd()
    cwd_list=temp_path.split('\\')
    instance='[\w_]*[0-9d]+_[0-9d]+'
    instance_match=re.compile(instance)
    instance_name=''
    for i in range(0,len(convertlist)):
        temp_list=convertlist[i].split('\\')
        temp_list=temp_list[len(cwd_list):]
        
        instance_index = None        
        for j in range(0,len(temp_list)):
            temp_list[j]=temp_list[j].lower()
#            match_result_polar=polar_match.match(temp_list[j])
            match_result_instance=instance_match.match(temp_list[j])
#            if match_result_polar != None:
#                polar_name=match_result_polar.group()
            if match_result_instance != None:
                instance_name=match_result_instance.group()
                instance_index = j
#        if polar_name == '':
#            polar_name='N-P-unknown'
        if instance_name == '':
            instance_name='W-unknown_L-unknown'
        
        if len(temp_list) <= 3 :    #if the level foler is 3 so all the files
                                   #need to convert are blong to the same group
            polar_name=''
        elif instance_index != None:
            polar_name = temp_list[instance_index-1]
        else:
            polar_name='_'.join(temp_list[:-3])

        
        group_name=polar_name+'$'+instance_name
        if group_name in group_name_list:
            convertgroup[group_name].append(convertlist[i])
        else:
            group_name_list.append(group_name)
            convertgroup[group_name]=[convertlist[i]]
        
def getSampling():
    ''' get the sampling frequency from user input'''
    print 
    print '**************************************************************************'
    print "If you want set the Sampling Frequency as 100 and 1000, input '100 1000' "
    input_samp=raw_input('Please input the Sampling Frequency:')
    samp_list=[]
    samp_list=input_samp.split()
    samp_value_list=[]
    for i in range(0,len(samp_list)):
        try:
            samp_f=float(samp_list[i])
            samp_value_list.append(samp_f)
        except:
            print '''"%s" this input maybe incorrect!'''%samp_list[i]
            getSampling()
    return samp_value_list
    
    
def golden_gen():
    '''
    generate the glden file from all die files
    '''
    golden_dic = golden_devide()
    for group in golden_dic.values():
        group2file(group)
    
def golden_devide():
    '''
    devide the die files to group
    '''
    global convertlist
    name_key_list=[]                   #has member like NMOS_Vg_0.4V_2.5V_RL100KOhm_RS0Ohm
    golden_dic={}
    for i in range(0,len(convertlist)):
        temp_list = convertlist[i].split('\\')
        if 'golden_data' in temp_list:
            continue
        name_key = temp_list[-2] + temp_list[-4]
        if name_key not in name_key_list:
            name_key_list.append(name_key)
            golden_dic[name_key]=[]
            golden_dic[name_key].append(convertlist[i])
        else:
            golden_dic[name_key].append(convertlist[i])
    return golden_dic
    
def group2file( golden_group ):
    '''
    generate all file in one group to one file
    '''
    if len(golden_group)<=1:
        return
    golden_neck={}
    golden_head=[]
    golden_body={}
    for i_file,g_file in enumerate(golden_group):
        f=open(g_file, 'r')
        content=f.readlines()
        f.close()
        record_flag=0
        data_flag = 0
        if i_file == 0 :  #first file
            for i_line in range(0,len(content)):
                line = content[i_line]
                if line.find('#CALC')<>-1:
                    head_index = i_line
                    golden_head = content[:head_index+1]
                    record_flag = 1
                    continue
                
                if line.find('Freq[Hz]')<>-1:
                    data_flag = 1
                    body_index = i_line
                    
                if record_flag == 1 and data_flag == 0:
                    temp_list = line.split(',')
                    if len(temp_list) == 2:     #this line may have key message like gm, realid
                        temp_list[-1]=temp_list[-1].strip('\n\r')
                        try:
                            key_value=float(temp_list[-1])
                            golden_neck[temp_list[0]]=(i_line,[])
                            golden_neck[temp_list[0]][-1].append(key_value)
                        except:
                            golden_neck[i_line]=line
                    else:
                        golden_neck[i_line]=line
                        
                if data_flag == 1:
                    if i_line == body_index:       #freq line
                        golden_neck[i_line]=line
                    else:
                        line=line.strip('\n\r')
                        temp_list=line.split(',')
                        if len(temp_list) > 1: #data line
                            data_list=[]
                            for i_data in range(1,len(temp_list)):
                                try:
                                    temp_value=float(temp_list[i_data])
                                    data_list.append([temp_value])
                                except:
                                    break
                            try:
                                temp_value = float(temp_list[0])
                                golden_body[temp_value]=data_list
                            except:
                                pass
                                              
        else:   #other files in group
            for i_line in range(0,len(content)):
                line = content[i_line]
                if line.find('#CALC')<>-1:
                    record_flag=1
                if line.find('Freq[Hz]')<>-1:
                    body_index = i_line
                    data_flag=1
                if record_flag == 1 and data_flag == 0:
                    temp_list = line.split(',')
                    if len(temp_list) == 2:     #this line may have key message like gm, realid
                        temp_list[-1]=temp_list[-1].strip('\n\r')
                        try:
                            key_value=float(temp_list[-1])
                            if temp_list[0] in golden_neck.keys():
                                golden_neck[temp_list[0]][-1].append(key_value)
                        except:
                            pass
                if data_flag==1:
                    if i_line != body_index:
                        line=line.strip('\n\r')
                        temp_list=line.split(',')
                        if len(temp_list) > 1:
                            try:
                                first_value = float(temp_list[0])
                            except:
                                continue
                            if first_value in golden_body.keys():
                                for i_data in range(1,len(temp_list)):
                                    try:
                                        temp_value = float(temp_list[i_data])
                                    except:
                                        break
                                    golden_body[first_value][i_data-1].append(temp_value)
        
    #### find the median value
    golden_neck_new={}
    golden_body_new={}
    for index,key in enumerate(golden_neck.keys()):
        if type(golden_neck[key]) == type(()):
            median=get_median(golden_neck[key][-1])
            if median != 'NULL':
                golden_neck_new[golden_neck[key][0]]='%s,%g\r\n'%(key,median)
            else:
                golden_neck_new[golden_neck[key][0]]='%s,%s\r\n'%(key,median)
        elif type(golden_neck[key]) == type(''):
            golden_neck_new[key] = golden_neck[key]
            
    key_list=golden_body.keys()
    key_list.sort()
    for index,key in enumerate(key_list):
        if type(golden_body[key]) == type([]):
            temp_list=[str(key)]
            for group in golden_body[key]:
                median = get_median(group)
                if median != 'NULL':
                    temp_list.append('%s'%median)
                else:
                    temp_list.append(median)
            golden_body_new[index] = ','.join(temp_list) + '\r\n'
            
    ######construct the output 
    golden_neck_list=[]
    golden_body_list=[]    
    
    key_list=golden_neck_new.keys()
    key_list.sort()
    for key in key_list:
        golden_neck_list.append(golden_neck_new[key])
        
    key_list=golden_body_new.keys()
    key_list.sort()
    for key in key_list:
        golden_body_list.append(golden_body_new[key])
        
    golden_content = golden_head + golden_neck_list + golden_body_list
    ####### create the dir
    golden_file_path = golden_dir(golden_group)
    if golden_file_path != '':
        print golden_file_path
        f=open(golden_file_path,'w')
        f.writelines(golden_content)
        #add the '*'
        f.write('*\r\n')
        f.close()
          
def golden_dir(golden_group):
    '''
    create the golden data path
    '''
    if len(golden_group)>1:
        temp_list_1=golden_group[0].split('\\')
        temp_list_2=golden_group[1].split('\\')
    for i in range(0,len(temp_list_1)):
        try:
            if temp_list_1[i] != temp_list_2[i]:
                temp_list_1[i]='golden_data'
        except:
            return ''
    dir_path = '\\'.join(temp_list_1[:-1])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return '\\'.join(temp_list_1)
                    
def get_median(g_list):
    ''' get the median of one list'''
    #print g_list
    g_list.sort()
    mid = len(g_list)/2
    if len(g_list) == 0:
        return 'NULL'
    median = g_list[mid]
    return median
    
if __name__=='__main__':
    convertlist_new=[]
    #collect all the noise.csv data path 
    findFile()
    try:
        print 'Generate the golden data ...'
        golden_gen()
    except:
        print 'Generate the golden data failed ...'
    
    #find file again
    findFile()    
    #parse the path and divide them to groups by different N/P type and W/L values
    devide() 
    #get the user define sampling frequency 
    samp_value_list=getSampling()
    for i in range(0,len(convertgroup.keys())):
        key=convertgroup.keys()[i]
        split_list=key.split('$')
        polar_str=split_list[0]
        temp_list=split_list[1].split('_')
        if temp_list[-2]=='W-unknown':
            w_value='100'
        else:
            w_value=temp_list[-2].replace('d','.')
            w_value=str(float(w_value))
        if temp_list[-1]=='L-unknown':
            l_value='100'
        else:
            l_value=temp_list[-1].replace('d','.')
            l_value=str(float(l_value))
        convertlist_group=convertgroup[key]
        try:
            # refresh all the global variable first
            index=[]
            vglist=[]
            vdlist=[]
            measured_data_list=[]
            convertlist_new=[]
            body=[]
            bodylist=[]
            head=[]
            frequency=[]
            for j in range(0,len(convertlist_group)): 
                headCvt_fre(convertlist_group[j],j,samp_value_list)
                headCvt(convertlist_group[j],w_value,l_value,j,len(convertlist_group),samp_value_list)
            for j in range(0,len(index)):
                convertlist_new.append(convertlist_group[index[j]])
            for j in range(0,len(convertlist_new)):
                bodyCvt(convertlist_new[j],j)
            datapath=makeDir(polar_str,split_list[1])
            link(datapath)
            print('%s complete... '%key)
        except:
            print('%s failed... '%key)
    raw_input('All complete... ')

