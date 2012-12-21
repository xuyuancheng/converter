# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:06:50 2012

@author: zhaiyt
"""
import sys
import os

global convertlist
convertlist=[]
global attrlist
attrlist=[]

def Findfile():
    '''Find data file to convert'''
    global convertlist
    convertlist=[]
    global attrlist
    attrlist=[]
    
    currentdir = os.getcwd()
    dircontent = os.walk(currentdir)
    flag = 0
    for root,dirs,files in dircontent:
        for fil in files:
            splitename = fil.split('.')[-1]
            if splitename == "data":
                fil = os.path.join(root,fil)
                convertlist.append(fil)
                flag = 1
            elif splitename == "attr":
                fil = os.path.join(root,fil)
                attrlist.append(fil)
    if flag == 1:
        num = len(convertlist)
        print 
        print "%s files need to convert:" % num
        print
        for hitfile in convertlist:
            print hitfile
            
    else:
        print 
        raw_input("No data file found, please put data file to current directory")
        sys.exit()
        
def headconvert(attrfile):
    global convertlist
    f=open(attrfile,'r')
    attr=f.readlines()
    f.close()
    
    np=''
    it_str=''
    out=''
    
    w=''
    l=''
    t=''
       
    b4_instance = ['as','as','ps','pd','nrs','nrd','sa','sb','sd','rdc','rsc',
                   'm','nf','min','trnqsmod','acnqsmod','rbodymod','rgatemod',
                   'geomod','rgeomod','stimod','rbdb','rbsb','rbpb','rbps',
                   'rbpd','sca','scb','scc','sc','xgw','ngcon','delvto','mulmu0',
                   'delk1','delnfct','delk2','deltox','delrsh','mulvsat','mulid0']
       
    other_it_list=[]
    for i in range(0,len(attr)):
        it_name,it_value=paseVarLine(attr[i])
        if it_name == '':
            continue
        elif it_name == 'WIDTHDRAWN':
            w=it_value
        elif it_name == 'LENGTHDRAWN':
            l=it_value
        elif it_name == 'DEVTYPE':
            np=it_value
    # replace NDEV by m ( m is HSPICE compatible instant)
        else:
            if it_name == 'NDEV':
                it_name = 'm'
            lower_name = it_name.lower()
            if lower_name in b4_instance:
                other_it = '%s=%s'%(it_name,it_value.strip("\""))
                other_it_list.append(other_it)
    
    head = []
    attr_dir = os.path.dirname( attrfile )
    for i in range(0,len(convertlist)):
        data_dir = os.path.dirname(convertlist[i])
        if data_dir.find('Converted_data') != -1:
            print "Skip %s"%convertlist[i]
            continue
        # change the graph constant
        body_list=[]
        for j in range(0,2):
            if attr_dir == data_dir:
                try:
                    out,t,graph_constant,body=bodyconvert(convertlist[i],j)
                    body_list.append(body)
                except:
                    print "Convert %s failed, graph constant: %s"%(convertlist[i],graph_constant)
                    continue
                it_str = "W=%s,L=%s,T=%s"%(w,l,t)
                other_it_str = ','.join(other_it_list)
                it_str = it_str + ',' + other_it_str
                #head def
                head=['ObjInfo{DataType=%s}'%np,\
                      'Instance{%s}'%it_str,\
                      'Input{Vgs,Vds,Vbs}',\
                      'Output%s'%out,\
                      'ModelType{DC}',\
                      'Delimitor{,}',\
                      'DataType{%s}'%np]
            else:
                continue
     
            if head == []:
                continue
            convert_dir = os.path.join(os.path.dirname(attr_dir),'converted_data',os.path.basename(attr_dir))
            if not os.path.exists(convert_dir):
                os.makedirs(convert_dir)
            
            head_str = '\n'.join(head)
            body_str = '\n'.join(body)
            content = head_str + '\n' + body_str        
            
            convert_data_path = os.path.join(convert_dir, os.path.basename(convertlist[i]))
            convert_data_path = convert_data_path.replace('.data','_%s.dat'%graph_constant)
            f= open(convert_data_path,'w')
            f.writelines(content)
            f.close()
            
            print "Success graph_constant: %s, %s"%(graph_constant,convertlist[i])
            
            if j==1 and len(body_list) == 2:
                new_body = body_list[0] + body_list[1]
                head_str = '\n'.join(head)
                body_str = '\n'.join(new_body)
                content = head_str + '\n' + body_str        
                
                convert_data_path = os.path.join(convert_dir, os.path.basename(convertlist[i]))
                convert_data_path = convert_data_path.replace('.data','.dat')
                f= open(convert_data_path,'w')
                f.writelines(content)
                f.close()
                print "Success: %s"%(convertlist[i])
            
def bodyconvert(datafile, time):
    f=open(datafile,'r')
    content=f.readlines()
    f.close()
    t= ''
    key_list=[]
    key_dic={}
    data_section = 0   #not found yet
    data_index = 0
    # find the t info
    # find the key info
    for i in range(0,len(content)):
        if content[i].startswith('VAR'):
            it_name,it_value = paseVarLine(content[i])
            if it_name == '':
                continue
            elif it_name == "T":
                t = it_value
        elif content[i].startswith('KEY'):
            temp_list= content[i].split('=')
            if len(temp_list) != 2:
                continue
            key_str = temp_list[-1].strip("\n,\"")
            key_list = key_str.split()
            for mem in key_list:
                key_dic[mem]=[]
        elif content[i].find("=") == -1:
            temp_list = content[i].split()
            if len(temp_list) > 3:
                data_section = 1 #have found
                data_index = i
                break
    #convert the data section, file in the key dic
    if data_index == 0 or data_section == 0:
        print "Can't find the data section of %s"%datafile
        return
    else:
        for i in range(data_index,len(content)):
            content[i] = content[i].strip('\r,\n')
            data_list=content[i].split()
            if len(data_list) != len(key_list):
                print "The data section doesn't match with the key definition in %s."%datafile
                return 
            else:
                for j in range(0,len(data_list)):
                    key_dic[key_list[j]].append(data_list[j])
  
    #parse the key dic find out the x_axis,y_axis,sweep etc.
    v_dic={}                  
    for i in range(0,len(key_list)):
        if key_list[i].startswith("V") or key_list[i].startswith("v"):
            data_column = key_dic[key_list[i]]
            for j in range(0,len(data_column)):
                data_column[j] = float(data_column[j])
            data_column = list(set(data_column))
            data_column.sort()
            key_dic[key_list[i]] = data_column
            v_dic[len(data_column)] = key_list[i]
    sort_list = v_dic.keys()
    sort_list.sort()
    
    if len(sort_list) != 3:
        print "The output is not {Vds,Vgs,Vbs} in data %s"%datafile
        return
    x_axis = v_dic[sort_list[-1]]
    if time == 0:
        sweep_1st = v_dic[sort_list[-2]]
        sweep_2nd = v_dic[sort_list[-3]]
    elif time == 1:
        sweep_1st = v_dic[sort_list[-3]]
        sweep_2nd = v_dic[sort_list[-2]]
    
    x_axis_index = key_list.index(x_axis)
    sweep_1st_index = key_list.index(sweep_1st)
    sweep_2nd_index = key_list.index(sweep_2nd)
        
    i_list = ['IS','ID','IG','IB']
    out_list=[]
    for i in range(0,len(key_list)):
        temp_key = key_list[i].upper()
        if temp_key in i_list:
            out_list.append(key_list[i])
    outstr_list=[]
    for out in out_list:
        outstr_list.append(out.capitalize())
    
    outstr = ','.join(outstr_list)
    outstr = '{%s}'%outstr    
    
    # devide the output data to group by mark
    mark_list=[]
    mark_dic={}
    for i in range(data_index,len(content)):
        match_mark = getmark(content[i],sweep_1st_index,sweep_2nd_index)
        
        temp_list = content[i].split()
        if match_mark not in mark_list:
            mark_list.append(match_mark)
            mark_dic[match_mark]=[]
            for mem in out_list:
                mark_dic[match_mark].append([])
        for i_out in range(0,len(out_list)):
            out = out_list[i_out]
            out_index = key_list.index(out)
            mark_dic[match_mark][i_out].append(temp_list[out_index])
            
    #begin to generate the body 
    #group string is like {Id_Vg}
    body_list=[]
    for out in out_list:
        out_index = out_list.index(out)
        group_str ='{%s_%s}'%(out.capitalize(),x_axis.capitalize())
        body = [group_str]
        for i_2nd in key_dic[sweep_2nd]:
            sweep_str_2nd  = "%s=%0.3f"%(sweep_2nd.capitalize(),i_2nd)
            sweep_str_list=[x_axis.capitalize()] 
            for i_1st in key_dic[sweep_1st]:
                sweep_str = "%s(%s=%0.3f)"%(out.capitalize(),sweep_1st.capitalize(),i_1st)
                sweep_str_list.append(sweep_str)
            sweep_str_list.append(sweep_str_2nd)
            graph_str='[%s]'%(','.join(sweep_str_list))
            
            body_data = []
            miss_list = []
            
            for i_x,x_value in enumerate(key_dic[x_axis]):
                body_line_list=[str(x_value)]
                for i_1st in key_dic[sweep_1st]:
                    current_mark='_'.join([str(i_1st),str(i_2nd)])
                    if current_mark not in mark_dic.keys():
                        miss_list.append(i_1st)
                        continue
                    elif i_x >= len(mark_dic[current_mark][out_index]):
                        break
                    else:
                        body_line_list.append(mark_dic[current_mark][out_index][i_x])
                if ( len(body_line_list) == 1 ):
                    continue
                body_line = ','.join(body_line_list)
                body_data.append(body_line)
            
            miss_list=list(set(miss_list))
                
            if miss_list != []:
                temp_list = graph_str.split(',')
                new_list=[]

                for sweep1_str in temp_list:
                    find = 0
                    for mem in miss_list:
                        miss_str = '%s=%0.3f'%(sweep_1st.capitalize(),mem)
                        if sweep1_str.find(miss_str) != -1:
                            find = 1
                    if find == 0:
                        new_list.append(sweep1_str)
                graph_str = ','.join(new_list)
            body.append(graph_str)
            body.extend(body_data)
        body_list.extend(body)
        
    return outstr,t,sweep_2nd,body_list
                    
def getmark(line,sweep1_index,sweep2_index):
    # to see if one data line is match current group_str and graph_str
    temp_list = line.split()
    mark = '_'.join([str(float(temp_list[sweep1_index])),str(float(temp_list[sweep2_index]))])
    return mark
                          
def paseVarLine(varline):
    temp_list=varline.split('=')
    if len(temp_list) <2:
        return '',''
    it_name=temp_list[-2]
    it_value=temp_list[-1]
    it_value=it_value.strip("\n,\"")
    name_list=it_name.split('__')
    it_name = name_list[-1]
    if len(name_list) < 2 and it_name != 'T':
        return '',''
    return it_name,it_value
      
if __name__ == "__main__":
    Findfile()
    if len(attrlist) == 0:
        print
        raw_input("Can't find '.attr' file!")
        sys.exit()
    for i in range(0,len(attrlist)):
        try:
            headconvert(attrlist[i])
        except:
            print "Can't parse the attr file %s"%attrlist[i]
    raw_input("Press any key to quit...")
        
                
