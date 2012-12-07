# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:43:44 2012

@author: zhaiyt
"""

import sys
import os
import shutil
import string
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtGui
import converter_ui
import statistical

class ConvertDlg( QDialog, converter_ui.Ui_converter):
    def __init__(self, parent = None ):
        super(ConvertDlg,self).__init__(parent)
        self.setupUi(self)
        self.Output_button.setEnabled(False)
        self.Convert_button.setEnabled(False)
        self.Result.setEnabled(False)
        self.redcol=PyQt4.QtGui.QColor(255,0,0)
        self.blackcol=PyQt4.QtGui.QColor(0,0,0)
        self.greencol=PyQt4.QtGui.QColor(0,100,0)
        self.bluecol=PyQt4.QtGui.QColor(240,160,0)
        
    @pyqtSignature("")
    def on_Input_button_clicked(self):
        source_file_path = QFileDialog.getOpenFileName()
        source_file_path = source_file_path.replace('/','\\')
        self.Input.setText(source_file_path)
        source_file_path=str(source_file_path)
        source_dir_path = os.path.dirname(source_file_path)
        if source_dir_path != "":
            default_path = os.path.join(source_dir_path,'Converted_data')
            self.Output.setText(default_path)
            self.Output_button.setEnabled(True)
            self.Convert_button.setEnabled(True)
        
    @pyqtSignature("")
    def on_Output_button_clicked(self):
        target_dir_path = QFileDialog.getExistingDirectory()
        target_dir_path = target_dir_path.replace('/','\\')
        if not str(target_dir_path) == "":
            self.Output.setText(target_dir_path)
   
    @pyqtSignature("")
    def on_Show_button_clicked(self):
        spec_file_path_list = QFileDialog.getOpenFileNames(self, self.tr("Select spec file"), QString(), self.tr("spec file(*.lspc *.gspc);;All File(*.*)"))
        self.show_obj = Show(spec_file_path_list)
        self.connect(self.show_obj,SIGNAL("plot(PyQt_PyObject)"),self.plot)
        self.show_obj.start() 

    @pyqtSignature("")
    def on_Convert_button_clicked(self):        
        input_path = self.Input.text()
        output_path = self.Output.text()
        
        input_path = str(input_path.replace('\\','\\\\'))
        output_path = str(output_path.replace('\\','\\\\'))
        
        rename = str(self.Rename.text())
        
        sigma = self.sigma.value()
        ratio = self.ratio.value()
        exist = 1
        
        if rename <>'' and rename.find(':')==-1:
            self.log.append("The input expression '%s' is invalid"%rename)
            exist = 0
        
        if not os.path.exists(input_path):
            if input_path == '':
                self.log.append('Please load the data file')
            else:
                self.log.append("%s doesn't exists!"%input_path)
            exist = 0
        if os.path.exists(output_path):
            try:
                shutil.rmtree(output_path)
            except:
                pass
        try:
            os.makedirs(output_path)
        except:
            pass
        if not os.path.exists(output_path):
            self.log.append("Can't create folder %s"%output_path)
            exist = 0
            
        if not exist:
            return

        self.log.append("Start...")
        self.convert(input_path,output_path,sigma,ratio,rename)
        self.Result.setEnabled(True)
        self.out_dir = output_path
            
    @pyqtSignature("")
    def on_Result_clicked(self):
        os.startfile(self.out_dir)

    def convert(self,input_path,output_path,sigma,ratio,rename):
        '''
        start to convert the file
        '''
        self.convert_obj = Convert(input_path,output_path,sigma,ratio,rename)
        self.connect(self.convert_obj, SIGNAL("log_append(PyQt_PyObject)"),self.log_append)
        self.convert_obj.start()

    def log_append(self, argv):
        color_dic={}
        color_dic['error']=self.redcol
        color_dic['warning']=self.bluecol
        color_dic['info']=self.greencol
        color_dic['']=self.blackcol
        if len(argv) == 0:
            return
        elif len(argv) == 2:
            if argv[1] in color_dic.keys():
                self.log.setTextColor(color_dic[argv[1]])  
                self.log.append(argv[0])
                self.log.setTextColor(self.blackcol)
        else:
            self.log.append(argv[0])

    def plot(self,filename):
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
        plt.show()
        plt.drawn()

class Convert(QThread):
    def __init__(self,input_path,output_path,sigma,ratio,rename):
        QThread.__init__(self,None)
        self.exiting = False
        self.in_path = input_path
        self.out_path = output_path
        self.sigma = sigma
        self.ratio = ratio
        self.rename = rename

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        #try:
        statistical.convert(self,self.in_path,self.out_path,self.sigma,self.ratio,self.rename)
        #except:
        #    self.emit(SIGNAL("log_append(PyQt_PyObject)"),['Convert file %s failed'%(os.path.basename(self.in_path)),'error'])

class Show(QThread):
    def __init__(self,spec_path_list):
        QThread.__init__(self,None)
        self.exiting = False
        self.spec_path_list = spec_path_list

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        for spec_file in self.spec_path_list:
            spec_file = spec_file.replace('/','\\')
            self.emit(SIGNAL("plot(PyQt_PyObject)"),str(spec_file))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConvertDlg()
    converter.show()
    app.exec_()
    
