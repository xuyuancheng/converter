# -*- coding utf-8 -*-
'''
Created on 12.17.2012
@author zhaiyt
'''
import converter
import os
import sys
import re

def valueCvt(value_str):
    
    value_str = value_str.split('(')[0]

    if value_str.find('KHZ')<>-1:
        old_str = 'KHZ'
        new_str = '000'
    elif value_str.find('u')<>-1:
        old_str = 'u'
        new_str = 'e-06'
    else:
        return value_str.strip()
    value_str = value_str.replace(old_str,new_str)
    value_str = value_str.replace(' ','')
    value_str = "%0.2e"%float(value_str)
    return value_str

class Cgg(converter.Converter):

    def __init__(self):
        super(Cgg,self).__init__()
        self.ins_dic={}
        self.input_dic={}
        self.output_dic={}
        self.output_dir=""

        self.__partInit()
        self.head_list=['ObjInfo{}',\
                        'Version{2.0}',\
                        'ModelType{AC}',\
                        'DataType{d}',\
                        'Delimitor{,}',\
                        'Workingmode{FORWORD}',\
                        self.ins_str,\
                        self.input_str,\
                        self.output_str]

    def __partInit(self):
        self.input_list=[]
        self.output_list=[]
        self.x = ""
        self.output_name = ""
        self.sweep = ""
        self.sweep_value_list = []
        self.sweep_str_list = []
        self.const_str_list = []

        self.group_str=""
        self.graph_str=""

        self.ins_str = ""
        self.ins_name_str= ""
        self.input_str = ""
        self.output_str = ""

        self.value_dic={}

        self.body = []

    def isPartStart(self,line):
        line = line.lower()
        tmp_list = line.split(':')

        if len(tmp_list) == 2:
            if tmp_list[0].find('lot')<>-1:
                return True
            else:
                return False
        else:
            return False


    def __assembly(self):
        head = []
        self.head_list[-3] = self.ins_str
        self.head_list[-2] = self.input_str
        self.head_list[-1] = self.output_str

        head.extend(self.head_list)

        body=[]
        body.append(self.group_str)
        body.append(self.graph_str)
        
        for i in xrange(len(self.value_dic[self.x])):
            line_list = []
            line_list.append(self.value_dic[self.x][i])
            for sweep_str in self.sweep_str_list:
                line_list.append(self.value_dic[sweep_str][i])
            line_str = ','.join(line_list)
            body.append(line_str)

        head.extend(body)
        self.body = head[:]

    def __parse(self,part):
        self.__getInsStr(part)
        self.__getInOutStr(part)
        
        # parse the data section
        x_value_list = []
        output_value_list = []
        p = re.compile(r"-*\d")
        for line in part:
            tmp_list = line.split()
            m = p.match(tmp_list[0])
            # no sweep
            if m and self.sweep == "":
                x_value_list.append(tmp_list[0])
                output_value_list.append(tmp_list[1])
            # have sweep
            elif m:
                x_value = tmp_list[0]
                if x_value not in x_value_list:
                    x_value_list.append(x_value)
                sweep_value = tmp_list[1]
                if sweep_value not in self.sweep_value_list:
                    self.sweep_value_list.append(sweep_value)
                    sweep_str = "%s=%s"%(self.sweep, sweep_value)
                    self.sweep_str_list.append(sweep_str)
                    if output_value_list != []:
                        sweep_str = self.sweep_str_list[-2]
                        self.value_dic[sweep_str] = output_value_list
                    output_value_list = []
                output_value_list.append(tmp_list[-1])
        if self.sweep != "":
            self.value_dic[self.sweep_str_list[-1]] = output_value_list
        self.value_dic[self.x] = x_value_list

        if self.sweep == "":
            self.value_dic["="] = output_value_list


        # sweep string list
        if self.sweep_value_list == []:
            self.sweep_str_list.append("=")

        # group and graph string 
        self.group_str = "{%s_%s}"%(self.output_name,self.x)
        if self.sweep == "":
            self.graph_str = "[%s,%s(%s)]"%(self.x,self.output_name,self.const_str_list[0])
        else:
            graph_str_list=[]
            graph_str_list.append(self.x)
            
            if len(self.sweep) == 3:
                const_name = "V%s"%self.sweep[2]
                const_str = "%s=0"%const_name
                self.const_str_list.append(const_str)

            for sweep_str in self.sweep_str_list:
                if sweep_str == "=":
                    continue
                sweep_str = "%s(%s)"%(self.output_name,sweep_str) 
                graph_str_list.append(sweep_str)
            graph_str_list.extend(self.const_str_list)
            graph_str = ','.join(graph_str_list)
            self.graph_str = "[%s]"%graph_str

    def __output(self):
        output_path = os.path.join(self.output_dir, self.ins_name_str+'.dat')
        f=open(output_path,'w')
        f.writelines('\n'.join(self.body))
        f.close()
        

    def __getInsStr(self,part):
        ins_str_list=[]
        ins_name_list=[]
        for i,line in enumerate(part):
            tmp_list = line.split(":")
            if len(tmp_list) == 2:
                if tmp_list[0] in self.ins_dic.keys():
                    ins_name = self.ins_dic[tmp_list[0]]
                    ins_value_ori = tmp_list[1].strip()

                    #in case of L:     0.0481 u (estimated poly length )
                    ins_value_ori = ins_value_ori.split('(')[0]
                    ins_value_ori = ins_value_ori.replace(' ','')

                    ins_value = valueCvt(tmp_list[1])
                    ins_str = "%s=%s"%(ins_name,ins_value)
                    ins_name_str = "%s%s"%(ins_name,ins_value_ori)
                    ins_str_list.append(ins_str)
                    ins_name_list.append(ins_name_str)
        ins_str = ','.join(ins_str_list)
        ins_str = "Instance{%s}"%ins_str

        self.ins_str = ins_str

        self.ins_name_str = "_".join(ins_name_list)

    def __getInOutStr(self,part):
        # first get the input from the head
        data_key_str = ""
        const_name_list=[]
        p = re.compile(r"-*\d")
        for line in part:
            tmp_list = line.split()
            m = p.match(tmp_list[0])
            if not m and line.find(':')==-1:
                data_key_str = line
                break
            elif not m and line.find(':')<>-1:
                head_list = line.split(":")
                input_name = head_list[0]
                input_value = ''
                if input_name in self.input_dic.keys():
                    input_name = self.input_dic[input_name]
                    input_value = valueCvt(head_list[1])
                    const_name_list.append(input_name)
                    const_str = "%s=%s"%(input_name,input_value)
                    self.const_str_list.append(const_str)
                    
        tmp_list = data_key_str.split()
        self.x = tmp_list[0]
        if self.x in self.input_dic.keys():
            self.x = self.input_dic[self.x]
        self.input_list.append(self.x) 
        
        output_name = tmp_list[-1].split('(')[0]
        if output_name in self.output_dic.keys():
            output_name = self.output_dic[output_name]
        self.output_name = output_name
        self.output_str="Output{%s}"%output_name

        if len(tmp_list) == 3:
            self.sweep = tmp_list[1]
            if self.sweep in self.input_dic.keys():
                self.sweep = self.input_dic[self.sweep]
            self.input_list.append(self.sweep)
        self.input_list.extend(const_name_list)

        input_str = ','.join(self.input_list)
        self.input_str = "Input{%s}"%input_str


    def convertPart(self,part):
        part_new= [] 
        for i,line in enumerate(part):
            line = line.strip('\r,\n')
            if line!= "":
                part_new.append(line)

        self.__partInit()
        self.__parse(part_new)
        self.__assembly()
        self.__output()



    def readCdf(self):
        '''
        parse the cdf file
        '''
        all_list=[self.ins_dic,self.input_dic,self.output_dic]
        INSTANCE = 0
        INPUT =  1
        OUTPUT = 2
        if self.cdf == "":
            print "Can't find the cdf file"
            raw_input()
            sys.exit()
        elif not os.path.exists(self.cdf):
            print "Can't find the cdf file"
            raw_input()
            sys.exit()
        else:
            f=open(self.cdf,'r')
            content = f.readlines()
            f.close()
            
            #parse the content
            for i,line in enumerate(content):
                line = line.strip('\r,\n')
                if line.startswith('#') or line == "":
                    continue
                elif line.find('instance')<>-1:
                    index = INSTANCE
                    continue
                elif line.find('input')<>-1:
                    index = INPUT
                    continue
                elif line.find('output')<>-1:
                    index = OUTPUT
                    continue
                
                tmp_list = line.split(',')
                if len(tmp_list) == 1:
                    all_list[index][tmp_list[0]] = tmp_list[0]
                elif len(tmp_list) == 2:
                    all_list[index][tmp_list[0]] = tmp_list[1]


if __name__ == '__main__':
    cvt = Cgg()
    cvt.findFile()
    cvt.readCdf()
    cur_path = os.getcwd()
    for fil in cvt.raw_list:
        if fil.endswith('cdf'):
            continue
        cvt.part_list=[]
        cvt.output_dir = os.path.join(cur_path, os.path.basename(fil)+'.dat')
        if not os.path.exists(cvt.output_dir):
            os.mkdir(cvt.output_dir)
        f=open(fil,'r')
        content = f.readlines()
        f.close()
        part_list = cvt.getPartList(content)
        cvt.part_list.extend(part_list)

        for i,part in enumerate(part_list):
            file_sec = "%-30s"%("File:%s"%(os.path.basename(fil)))
            part_sec = "%s"%("Part:%d"%(i+1))
            print "%-50s"%(file_sec + part_sec),
            try:
                cvt.convertPart(part)
                print "         OK"
            except:
                print "         FAILED"
    raw_input()

