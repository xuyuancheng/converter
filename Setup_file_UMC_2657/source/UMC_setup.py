# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:45:56 2012

@author: zhaiyt
"""

import os
import sys
import shutil
from shellcolor import *

#xml
import xml.dom.minidom
import codecs


global convertlist
convertlist=[]

#global model info
global device_info
device_info=[]
global instance_info
instance_info=''
global node_info
node_info=''

def findFile():
    global convertlist
    convertlist=[]
    currentdir=os.getcwd()
    dircontent=os.walk(currentdir)
    for root,dirs,files in dircontent:
        for mem in files:
            if mem.split('.')[-1]=='txt':
                mem=os.path.join(root,mem)
                convertlist.append(mem)
                
    num=len(convertlist)
    if num==0:
        print
        raw_input('No file find ,please put data file to current dirctory')
        sys.exit()
    else:
        print
        printWait("%s files need to convert:" % num)
        print
        print 
        for hitfile in convertlist:
            printWait(hitfile)
            print
            
            
def modelType(convertfile_path): 
    model=''
    file_name=os.path.basename(convertfile_path)
    file_name=file_name.split('.')[0]
    try:
        f=open(convertfile_path,'r')
    except:
        printError("Can't open file %s"%file_name)
        sys.exit()
    content=f.readlines()
    f.close()
    key_list=['bsim3','bsim4','bsim6','bsimpd','hvmos','gp_bjt','mextram','ldmos','diode','hicum','hisim2',\
                  'psp','mextram503','bsimsoi','rpi_atft','res','rpi_ptft','hisim_hv','bsim_cmg','bsim_img']
    for i in range(0,len(content)):
        #if a instance line
        temp_list=content[i].split()
        if temp_list==[]:
            continue
        elif temp_list[0].isdigit():
            for j in range(0,len(temp_list)):
                temp_list[j]=temp_list[j].lower()
                if temp_list[j] in key_list:
                    model=temp_list[j]
                    break
                else:
                    pass
    if model=='':
        printError("Can't find the model type info in file %s"%file_name)
        sys.exit()
    return model
    
def parserModel(model_type):
    global sdn_head
    global device_info
    device_info=[]
    global instance_info
    instance_info=''
    global node_info
    node_info=''
    
    dom=xml.dom.minidom.parseString(sdn_head)
    root=dom.documentElement
    model_list=root.getElementsByTagName('MODEL')
    for model in model_list:
        model_name=model.getAttribute('name')
        if model_name==model_type:
            device_list=model.getElementsByTagName('DEVICE_TYPE')
            for device in device_list:
                device_type=device.getAttribute('name')
                device_info.append(device_type)
            instance_list=model.getElementsByTagName('INSTANCE')
            instance_info=instance_list[0].getAttribute('name')
            node_list=model.getElementsByTagName('NODES')
            node_info=node_list[0].getAttribute('name')
            break
        else:
            continue
    if device_info==[] or instance_info=='' or node_info=='':
        printError("Parse the model defination failed")
        sys.exit()
        
def parserRaw(convertfile,model_type): 
    global sdn_head
    global dev_head
    file_name=os.path.basename(convertfile)
    file_name=file_name.split('.')[0]
    try:
        f=open(convertfile,'r')
    except:
        printError("Can't open file %s"%file_name)
        sys.exit()
    content=f.readlines()
    f.close()
    
    plan_map=''
    total_num=''
    time=''
    device_line=[]
    for i in range(0,len(content)):
        content[i]=content[i].strip('\n')
        content_up=content[i].upper()
        if content_up.startswith('PLAN_MAP'):
            temp_list=content_up.split('=')
            plan_map=temp_list[1].strip(' ')
        elif content_up.startswith('TOTAL_SUBDIE'):
            temp_list=content_up.split('=')
            total_num=temp_list[1].strip(' ')
        elif content_up.startswith('TIME'):
            temp_list=content_up.split('=')
            time=temp_list[1].strip(' ')
        else:
            temp_list=content[i].split()
            if temp_list==[]:
                continue
            else:
                if temp_list[0].isdigit():
                    for j in range(0,len(temp_list)):
                        if model_type in temp_list:
                            device_line.append(content[i])
                            break
    #modify the sdn and dev head
    dom=xml.dom.minidom.parseString(sdn_head)
    root_sdn=dom.documentElement
    
    dom_dev=xml.dom.minidom.parseString(dev_head)
    root_dev=dom_dev.documentElement
    if plan_map=='':
        printWait("WARNING: Can't find the plan_map info in file %s"%file_name)
    else:
        #plan_map
        map_list=root_sdn.getElementsByTagName('PLAN_MAP')
        map_node=_textnode(dom,plan_map)
        map_list[0].appendChild(map_node)
    if total_num=='':
        printWait("WARNING: Can't find the total number info in file %s"%file_name)
    else:
        #total_num
        num_list=root_sdn.getElementsByTagName('TOTAL_SUBDIE')
        num_node=_textnode(dom,total_num)
        num_list[0].appendChild(num_node)
    if time=='':
        printWait("WARNING: Can't find the time info in file %s"%file_name)
    else:
        #time
        time_list=root_sdn.getElementsByTagName('DATE')
        time_node=_textnode(dom,time)
        time_list[0].appendChild(time_node)
        
    #model type
    model_type_list=root_dev.getElementsByTagName('MODEL')
    type_node=_textnode(dom,model_type)
    model_type_list[0].appendChild(type_node)
    sdn_head=root_sdn.toxml()
       
    if device_line==[]:
        printError("ERROR: Can't find the device info in file %s"%file_name)
        sys.exit()
    return device_line
    
def _textnode(dom,value):
    value = value.replace('&', '&amp;')
    value = value.replace('<', '&lt;')
    text  = dom.createTextNode(value)
    return text
    
def dev_parser(line):
    global device_info
    global instance_info
    global node_info
    global dev_section
    global polar
    
    node_list=node_info.split('|')
    node_len=len(node_list)
    instance_list=instance_info.split('|')
    instance_len=len(instance_list)
    
    line_list=line.split()
    dom_section=xml.dom.minidom.parseString(dev_section)
    root_section=dom_section.documentElement
    root_section.setAttribute('NAME',line_list[1])
    index=0
    for i in range(0,len(line_list)):
        line_list[i]=line_list[i].lower()
        if line_list[i] in device_info:
            polar=line_list[i]
            index=i
            break
    if index==0:
        printError("Can't find Device_Type info in %s"%line)
        return
    else:
        try: 
            setup=line_list[index+1]
            setup_list=root_section.getElementsByTagName('SETUP_FILE')
            setup_list[0].setAttribute('NAME',setup)
            instance_start=index+2+node_len
            instance_end=instance_start+instance_len
            instance_device_list=line_list[instance_start:instance_end]
            for i in range(0,len(instance_device_list)):
                if instance_device_list[i]<>'N/A':
                    instance_name=instance_list[i].split('(')[0]
                    instance_value=instance_device_list[i]
                    instance_node=_setnode('INSTANCE',instance_name,instance_value)
                    feed  = dom_section.createTextNode('\n') 
                    root_section.insertBefore(instance_node,setup_list[0])
                    root_section.insertBefore(feed,setup_list[0])
            node_device_list=line_list[index+2:index+2+node_len]
            for i in range(0,len(node_device_list)):
                node_tag=_setnode('NODE',node_list[i],node_device_list[i])
                root_section.appendChild(node_tag)
                feed  = dom_section.createTextNode('\n') 
                root_section.appendChild(feed)
        except IndexError:
            printError("Node or instance defination doesn't match with sdn")
            sys.exit()
        return polar,root_section
            
    

def _setnode(node_type,node_name,node_value):
    node_str='''<%s %s="%s"/>'''%(node_type,node_name,node_value)
    dom_node=xml.dom.minidom.parseString(node_str)
    root_node=dom_node.documentElement
    return root_node

def sdn_parser(line,model):
    global device_info
    global instance_info
    global node_info
    global sdn_section
    
    node_list=node_info.split('|')
    node_len=len(node_list)
    instance_list=instance_info.split('|')
    instance_len=len(instance_list)
    
    line_list=line.split()
    dom_section=xml.dom.minidom.parseString(sdn_section)
    root_section=dom_section.documentElement
    root_section.setAttribute('index',line_list[0])
    device=root_section.getElementsByTagName('DEVICE')[0]
    
    index=0
    for i in range(0,len(line_list)):
        line_list[i]=line_list[i].lower()
        if line_list[i] in device_info:
            polar=line_list[i]
            index=i
            break
    device.setAttribute('device_type',polar)
    if index==0:
        printError("Can't find Device_Type info in %s"%line)
        return
    else:
        try:
            instance_l=[]
            instance_start=index+2+node_len
            instance_end=instance_start+instance_len
            instance_device_list=line_list[instance_start:instance_end]
            for i in range(0,len(instance_device_list)):
                if instance_device_list[i]<>'N/A':
                    instance_l.append(instance_device_list[i])
                else:
                    instance_l.append('')
            instance_str='|'.join(instance_l)
            device.setAttribute('instance_value',instance_str)
            device.setAttribute('instance_name',instance_info)
            node_device_list=line_list[index+2:index+2+node_len]
            for i in range(0,7-len(node_device_list)):
                node_device_list.append('')
                node_list.append('NA')
            node_device_str='|'.join(node_device_list)
            node_str='|'.join(node_list)
            device.setAttribute('pin_value',node_device_str)
            device.setAttribute('pin_name',node_str)
            setup=line_list[index+1]
            device.setAttribute('setup_file_name',setup)
            
            device.setAttribute('model_name',model)
            device.setAttribute('name',line_list[1])
            if line_list[-1].find('Comments:')<>-1:
                comment_str=line_list.split(':')[-1]
                device.setAttribute('comments',comment_str)
            else:
                device.setAttribute('comments',"")
        except IndexError:
            printError("Node or instance defination doesn't match with sdn")
            sys.exit()
    return root_section
                
def _createTagele(dom,tagname,value):
    tag = dom.createElement(tagname)
    value = value.replace('&', '&amp;')
    value = value.replace('<', '&lt;')
    text  = dom.createTextNode(value)
    tag.appendChild(text)
    return tag

def _createAttr(dom,attrname,value):
    attr_node=dom.createAttribute(attrname)
    attr_node.value=value
    return attr_node
                            
                            
global sdn_head
sdn_head='''<SUBDIE_NAMING>
<DATE></DATE>
<PLAN_MAP></PLAN_MAP>
<TOTAL_SUBDIE></TOTAL_SUBDIE>
<MODEL name="bsim3">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Nrs()|Nrd()|SA(m)|SB(m)|m()|RDC()|RSC()|sca()|scb()|scc(v)|sc(m)"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="bsim4">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Nrs()|Nrd()|Sa(m)|Sb(m)|Sd(m)|Rdc()|Rsc()|m()|nf()|min()|trnqsmod()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="bsim6">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|AS(m2)|AD(m2)|PS(m)|PD(m)|NF()|NRS()|NRD()|MINZ()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="bsimpd">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|M()|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Nrs()|Nrd()|Nrb()|Rth0()|Cth0()|Nbc()|Nseg()|Pdbcp()|Psbcp()|Agbcp()"/>
<NODES name="D|G|S|E|P"/>
</MODEL>
<MODEL name="hvmos">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Nrs()|Nrd()|NqsMod()|m()|ls()|ld()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="gp_bjt">
<DEVICE_TYPE name="npn"/>
<DEVICE_TYPE name="pnp"/>
<DEVICE_TYPE name="lpnp"/>
<INSTANCE name="AREA(m2)|AREAB(m2)|AREAC(m2)|T(c)|M()"/>
<NODES name="C|B|E|S"/>
</MODEL>
<MODEL name="mextram">
<DEVICE_TYPE name="npn"/>
<DEVICE_TYPE name="pnp"/>
<INSTANCE name="T(c)|area(m2)|m()|region()"/>
<NODES name="C|B|E|S|DT"/>
</MODEL>
<MODEL name="ldmos">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Ae(m2)|Pe(m)|Nrs()|Nrd()|m()|RDC()|RSC()|Rth0()|Cth0()|Nseg()|lov()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="diode">
<DEVICE_TYPE name="d"/>
<INSTANCE name="Area()|Pj()|pg()|T(c)|m()|W(m)|L(m)|LM(m)|LP(m)|WM(m)|WP(m)"/>
<NODES name="J|S"/>
</MODEL>
<MODEL name="hicum">
<DEVICE_TYPE name="npn"/>
<DEVICE_TYPE name="pnp"/>
<INSTANCE name="t(c)|area(m2)|m()|region()|self_heating()"/>
<NODES name="C|B|E|S|T"/>
</MODEL>
<MODEL name="hisim2">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|m()|As(m2)|Ad(m2)|Ps(m)|Pd(m)|nrs(1)|nrd(1)|corbnet()|rbpb()|rbpd()|rbps()|rbdb()|rbsb()|corg()|ngcon()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="psp">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|absource(m2)|abdrain(m2)|lssource(m)|lsdrain(m)|lgsource(m)|lgdrain(m)|As(m2)|Ad(m2)|Ps(m)|Pd(m)|sa(m)|sb(m)|sd(m)|sca()|scb()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="mextram503">
<DEVICE_TYPE name="npn"/>
<DEVICE_TYPE name="pnp"/>
<INSTANCE name="T(c)|area(m2)|m()|region()"/>
<NODES name="C|B|E|S"/>
</MODEL>
<MODEL name="bsimsoi">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="W(um)|L(um)|T(c)|m()|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Nrs()|Nrd()|Nrb()|Rth0()|Cth0()|Nbc()|Nseg()|Pdbcp()|Psbcp()|Agbcp()"/>
<NODES name="D|G|S|E|P"/>
</MODEL>
<MODEL name="rpi_atft">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<INSTANCE name="W(um)|L(um)|T(c)|m()"/>
<NODES name="D|G|S"/>
</MODEL>
<MODEL name="res">
<DEVICE_TYPE name="r"/>
<INSTANCE name="T(c)|M()|W(m)|L(m)|SCALE()|R(ohm)|C(f)|AC(ohm)|TC1(1/deg)|TC2(1/deg^2)|TC1c(1/deg)|TC2c(1/deg^2)|region()"/>
<NODES name="R|S|B"/>
</MODEL>
<MODEL name="rpi_ptft">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<INSTANCE name="W(um)|L(um)|AD(um2)|AS(um2)|PD(um)|PS(um)|NRD()|NRS()|T(c)|m()|Rth()|Cth()|Nseg()"/>
<NODES name="D|G|S"/>
</MODEL>
<MODEL name="hisim_hv">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="w(um)|l(um)|T(c)|as(m)|ad(m)|ps(m)|pd(m)|nrs()|nrd()|dtemp(c)|corbnet()|rbpb(ohm)|rbpd(ohm)|rbps(ohm)|rbdb(ohm)|rbsb(ohm)|corg()|ngcon()"/>
<NODES name="D|G|S|B|E"/>
</MODEL>
<MODEL name="bsim_cmg">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<DEVICE_TYPE name="d"/>
<INSTANCE name="L(m)|TFIN(m)|FPITCH(m)|NF()|NFIN()|NGCON()|T()|D(m)|AS()|ASEO()|ASEJ()|AD()|ADEO()|ADEJ()|PS1()|PSEO()|PSEJ()|PD1()"/>
<NODES name="D|G|S|B"/>
</MODEL>
<MODEL name="bsim_img">
<DEVICE_TYPE name="nmos"/>
<DEVICE_TYPE name="pmos"/>
<INSTANCE name="L()|W()|NF()|T()|AS()|AD()|PS()|PD()|NRS()|NRD()"/>
<NODES name="D|FG|S|BG"/>
</MODEL>
</SUBDIE_NAMING>
<!--BSIMPro+ Sub-die Naming Data-->''' 

global dev_head
dev_head='''<!--BSIMProPlus Device Window setup file-->
<DEVICE_WND_SETUP_FILE>
<DATE VALUE="2012/4/2 ?? 11:21:10"/>
<MODEL NAME="bsim3"/>
</DEVICE_WND_SETUP_FILE>'''

global dev_section
dev_section='''<DEVICE NAME="N_08_r.dat">
<SETUP_FILE NAME="d:\\bsimprop\\bsim3\\bsim3nmos.set"/>
</DEVICE>'''
global sdn_section
sdn_section='''<SUBDIE index="1">
<DEVICE name="10X10_Nmos" comments="" model_name="bsim3" device_type="nmos" setup_file_name="C:\\ran\\job\\UMC\\20100317_auto_measure\\NMOSiv6_LVG.set" instance_name="W(um)|L(um)|T(c)|As(m2)|Ad(m2)|Ps(m)|Pd(m)|Nrs()|Nrd()|SA(m)|SB(m)|m()|RDC()|RSC()|sca()|scb()|scc(v)|sc(m)" instance_value="10|10|25|||||||||||||||" pin_name="D|G|S|B|N/A|N/A|N/A" pin_value="1|2|3|4|||"></DEVICE>
</SUBDIE>'''

def saveFile(dom, file_name):
    try:
        f=file(file_name,'w')
        writer = codecs.lookup('utf-8')[3](f)
        dom.writexml(writer,encoding='utf-8')
        writer.close()
    except:
        error_message="Unexpected exception when saving the file %s"%file_name
        printError(error_message)
        sys.exit()
def make_dir(convert_file):
    try:
        current_path=os.getcwd()
        file_name=os.path.basename(convert_file).split('.')[0]
        dir_path=os.path.join(current_path,file_name)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)
        else:
            os.makedirs(dir_path)
    except:
        printError("Unexcept exception when delete or make %s's result folder, please check if the file's name has illegal characters\
or make sure the files are not in used"%file_name)
        sys.exit()
    return dir_path
        
if __name__=='__main__':
    printWait("\
*************************************************************************\n\
**  Please put the converter,data under the same directory              *\n\
**  Support converting data with different device types                 *\n\
*************************************************************************")  
    findFile()
    failed=0
    for i in range(0,len(convertlist)):
        try:
            model=modelType(convertlist[i])
            parserModel(model)
            device_line=parserRaw(convertlist[i],model)
            
            dom_sdn=xml.dom.minidom.parseString(sdn_head)
            root_sdn=dom_sdn.documentElement
            
            dom_dev=xml.dom.minidom.parseString(dev_head)
            root_dev=dom_dev.documentElement
            
            dev_polar_list=[]        
            for device_type in device_info:
                polar_head='''<MODEL_TYPE_SECTION TYPE="nmos">
<TOTAL_DEVICE COUNT="20"/>
</MODEL_TYPE_SECTION>'''
                dom_polar=xml.dom.minidom.parseString(polar_head)
                root_polar=dom_polar.documentElement
                root_polar.setAttribute('TYPE',device_type)
                dev_polar_list.append(dom_polar)
            count=[0]*len(dev_polar_list)
                
            for j,line in enumerate(device_line):
                try:
                    #create dev file
                    polar,device_section=dev_parser(line)
                    polar_index=device_info.index(polar)
                    count[polar_index]=count[polar_index]+1
                    root_polar=dev_polar_list[polar_index].documentElement
                    root_polar.appendChild(device_section)
                    feed=dev_polar_list[polar_index].createTextNode('\n')
                    root_polar.appendChild(feed)
                except:
                    printError("Failed to convert .dev file, line index %d"%j)
                
                #create sdn file
                try:
                    sdn_device_section=sdn_parser(line,model)
                    root_sdn.appendChild(sdn_device_section)
                    feed=dom_sdn.createTextNode('\n')
                    root_sdn.appendChild(feed)
                except:
                    printError("Failed to convet .sdn file, line index %d"%j)
            for j in range(0,len(count)):
                if count[j]==0:
                    continue
                else:
                    root_polar=dev_polar_list[j].documentElement
                    count_list=root_polar.getElementsByTagName("TOTAL_DEVICE")
                    count_list[0].setAttribute('COUNT',str(count[j]))
                    root_dev.appendChild(root_polar)
                    feed=dom_dev.createTextNode('\n')
                    root_dev.appendChild(feed)
                
            file_name=os.path.basename(convertlist[i]).split('.')[0]
            dir_path=make_dir(convertlist[i])
            try:
                sdn_path=os.path.join(dir_path,file_name+'.sdn')
                saveFile(dom_sdn,sdn_path)
            except:
                printError("Failed to save the file %s"%(file_name+'.sdn'))
            try:
                dev_path=os.path.join(dir_path,file_name+'.dev')
                saveFile(dom_dev,dev_path)
            except:
                printError("Failed to save the file %s"%(file_name+'.dev'))
        except:
            printError ('ERROR: Convert file %s filed\n'%convertlist[i])
            failed=failed+1
    printResult('All complete %d failed ...'%failed)
    raw_input('')
        
    
            
        
        
    

