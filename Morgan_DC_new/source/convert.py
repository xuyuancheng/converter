# -*- coding: utf-8 -*-
'''
@auther: zhaiyt
'''
#
# 1 find file
# 2 open file and parse to several parts
# 3 convete every part
# 4 for every part, generate the head then converet the body
#
import os
import sys
from shellcolor import *



global convert_list
convert_list=[]
def findFile():
    '''Find data file to conveter'''
    global convert_list
    convert_list=[]

    current_dir= os.getcwd()
    dircontent = os.walk(current_dir)
    file_num = 0
    for root,dirs,files in dircontent:
        file_num = file_num + len(files)
        for fil in files:
            fil_name = os.path.join(root,fil)
            convert_list.append(fil_name)
    if file_num==0:
        print
        raw_input("No data file found, please put data file to current dirctory!")
        sys.exit()
    else:
        print 
        print "%s files need to convert:"%file_num
        print
        for hitfile in convert_list:
            print hitfile

def parse(content):
    ''' parse the data file and devide it to several parts'''
    ins_info_start=-1
    ins_info_end =-1
    bias_info_no =-1

    bias_info_no_list=[]  # to find the body part
    ins_info_start_list=[]

    part=[]
    part_list=[]
    for i in range(len(content)):
        content[i]= content[i].strip('\r,\n')
        if content[i].find('Lot')<>-1:
            ins_info_start = i
            ins_info_start_list.append(i)
        elif content[i].find('Numpts')<>-1:
            ins_info_end = i+1
        elif content[i].find('VD')<>-1 and content[i].find('ID')<>-1:
            bias_info_no = i
            bias_info_no_list.append(i)
        if ins_info_start != -1 and ins_info_end != -1 and bias_info_no != -1:
            part.append(content[ins_info_start:ins_info_end])
            part.append(content[bias_info_no])
            part_list.append(part)
            part=[]
            ins_info_start=ins_info_end=bias_info_no=-1
    for i in range(len(part_list)):
        if i <> len(part_list) -1:
            part_list[i].append(content[(bias_info_no_list[i]+1):ins_info_start_list[i+1]])
        else:
            part_list[i].append(content[(bias_info_no_list[i]+1):])
    return part_list



def convert(data_path):
    f=open(data_path,'r')
    content = f.readlines()
    f.close()

    # part_list=[ part, part, part...]
    # part=[instance_info, bias_info, data_body]
    part_list=parse(content)
    # for every part in the part_list , parse its instance message
    part_dic={}
    key_str_list=[]
    for part in part_list:
        ins_info = part[0]
        #generate the key str
        for line in ins_info:
            temp_list = line.split()
            if line.find('Lot')<>-1:
                lot =temp_list[-1]
            elif line.find('Wafer')<>-1:
                wafer=temp_list[-1]
            elif line.find('Chip') <>-1:
                chip=temp_list[-1]
            elif line.find('Wdrawn') <>-1:
                w=temp_list[-1]
            elif line.find('Ldrawn') <>-1:
                l=temp_list[-1]
            elif line.find('Temp') <>-1:
                t=temp_list[-1]
        key_str = "%s_%s_%s_W%s_L%s_T%s"%(lot,wafer,chip,w,l,t)
        part[0] = key_str
        if key_str in key_str_list:
            part_dic[part[0]].append(part[1:])
        else:
            key_str_list.append(key_str)
            part_dic[part[0]]=[part[1:]]

    #convert every part
    for key in part_dic.keys():
        body,polar = body_cvt(part_dic[key]) 
        head = head_cvt(key,polar)
        name = key

        if not os.path.exists('.\converted_data'):
            os.mkdir('.\converted_data')
        dir_name = os.path.join('.\converted_data',os.path.basename(data_path))
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        file_path = os.path.join(dir_name, name)
        f=open(file_path+'.dat','w')
        f.writelines(head + body)
        f.close()


def head_cvt(key,polar):
    '''generate the head'''
    out="{Id,Ig,Is,Ib}"                          #maybe open a interface
    key_list = key.split('_')
    for ins in key_list:
        if ins.startswith('W'):
            w=ins[1:]
        elif ins.startswith('L'):
            l=ins[1:]
        elif ins.startswith('T'):
            t=ins[1:]
    it_str = "W=%s,L=%s,T=%s"%(w,l,t)
    head=['ObjInfo{DataType=%s}'%polar,\
          'Instance{%s}'%it_str,\
          'Input{Vgs,Vds,Vbs}',\
          'Output%s'%out,\
          'ModelType{DC}',\
          'Delimitor{,}',\
          'DataType{%s}'%polar]
    
    return '\n'.join(head);

def body_cvt(part_list):
    ''' convert the body '''
    out_list=['Id','Ig','Is','Ib']
    input_list=['Vds','Vgs','Vbs']
    
    part_group_list=[]
    for part in part_list:
        bias_dic={}
        body_ori=part[-1]
        body_content=[]
        for i in range(len(body_ori)):
            temp_list = body_ori[i].split()
            if len(temp_list) <4:
                pass
            else:
                body_content.append(body_ori[i])
        bias_list=part[0]
        temp_list=part[0].split()
        
        ## assert there has four input and the third one is Vs=0
        col_1=[]
        col_2=[]
        col_3=[]
        for i in range(len(body_content)):
           temp_list=body_content[i].split()
           col_1.append(temp_list[0])
           col_2.append(temp_list[1])
           col_3.append(temp_list[3])
        col_1=list(set(col_1)) 
        col_2=list(set(col_2))
        col_3=list(set(col_3))
        col_1.sort()
        col_2.sort()
        col_3.sort()

        sweep_list=[col_1,col_2,col_3]

        sort_dic={}
        sort_dic[len(col_1)]=0
        sort_dic[len(col_2)]=1
        sort_dic[len(col_3)]=2
        length_list=[len(col_1),len(col_2),len(col_3)]
        length_list.sort()
        sort_list=[sort_dic[length_list[0]],sort_dic[length_list[1]],sort_dic[length_list[2]]]
        

        #judge the polar type 
        x_sweep_list = sweep_list[sort_list[-1]]
        positive_num=0
        negtive_num=0

        for x_value in x_sweep_list:
            try:
                value=float(x_value)
                if value < 0:
                    negtive_num = negtive_num + 1
                else:
                    positive_num = positive_num + 1
            except:
                pass

        if negtive_num > positive_num:
            polar = 'PMOS'
        else:
            polar = 'NMOS'

        #generate the mask stirng for every line 
        body_dic = {}
        new_sort_list=[]
        for mem in sort_list:
            if mem == 2:
                mem = 3
            new_sort_list.append(mem)
        for line in body_content:
            temp_list=line.split()
            mask="%s,%s,%s"%(temp_list[new_sort_list[-1]],temp_list[new_sort_list[-2]],temp_list[new_sort_list[-3]])
            body_dic[mask]=temp_list[4:8]
        
        group_str_list=[]
        for out in out_list:
            if input_list[sort_list[-1]].endswith('s'):
                group_input = input_list[sort_list[-1]][:-1]
            else:
                group_input = input_list[sort_list[-1]]
            group_str="{%s_%s}"%(out,group_input)
            graph_str_list=[]
            for p_sweep_value in sweep_list[sort_list[0]]:
                x_sweep = input_list[sort_list[-1]]
                y_sweep = input_list[sort_list[1]]
                p_sweep = input_list[sort_list[0]]
                temp_list=[]
                for y_sweep_value in sweep_list[sort_list[1]]:
                    if polar == 'PMOS':
                        if y_sweep_value.startswith('-'):
                            y_sweep_value=y_sweep_value[1:]
                        else:
                            y_sweep_value='-'+y_sweep_value
                    temp_list.append( "%s(%s=%s)"%(out,y_sweep,y_sweep_value) )
                temp_str = ','.join(temp_list) 
                if polar == 'PMOS':
                    if p_sweep_value.startswith('-'):
                        p_sweep_value_reverse = p_sweep_value[1:]
                    else:
                        p_sweep_value_reverse = '-'+p_sweep_value
                graph_str='[%s,'%x_sweep + temp_str + ',%s=%s]'%(p_sweep,p_sweep_value_reverse)
                
                out_index = out_list.index(out)
                graph=[]
                for x_value in sweep_list[sort_list[-1]]:
                    if polar == 'PMOS':
                        if x_value.startswith('-'):
                            x_value_reverse = x_value[1:]
                        else:
                            x_value_reverse = '-'+x_value
                    line_list=[]
                    line_list.append(x_value_reverse)
                    for y_value in sweep_list[sort_list[1]]:
                        mask = '%s,%s,%s'%(x_value,y_value,p_sweep_value)
                        try:
                            line_value = body_dic[mask][out_index];
                            if polar == 'PMOS':
                                if line_value.startswith('-'):
                                    line_value = line_value[1:]
                                else:
                                    line_value = '-'+line_value
                            line_list.append(line_value)
                        except:
                            line_list=[]
                            break
                    line_str = ','.join(line_list)
                    graph.append(line_str)
                graph_str=graph_str+'\n'+'\n'.join(graph)
                graph_str_list.append(graph_str)
            group_str=group_str+'\n'+'\n'.join(graph_str_list)
            group_str_list.append(group_str)
        part_group_list.append(group_str_list)
        
        body=''
        if len(part_group_list) !=2 :
            for group_str_list in part_group_list:
                group_str = '\n'.join(group_str_list)
                body=body+'\n'+group_str
        else:
            for i in range(len(part_group_list[0]) + len(part_group_list[1])):
                if i%2 == 0:
                    group_str=part_group_list[0][i//2]
                    body=body+'\n'+ group_str
                elif i%2 != 0:
                    group_str=part_group_list[1][i//2]
                    body=body+'\n'+group_str

            
    return body,polar

if __name__ == '__main__':
    findFile()
    for data in convert_list:
        try:
             convert(data)
             print "convert %-50s"%data,
             printWait( "[OK]\n" )
        except:
            print "convert %-50s"%data,
            printError( "[Failed]\n")
    raw_input("Finish...")   
