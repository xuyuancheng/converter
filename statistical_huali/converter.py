# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:43:44 2012

@author: zhaiyt
"""

import sys
import os
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
            self.log.append("%s doesn't exists!"%input_path)
            exist = 0
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
        
        try:
            statistical.convert(input_path,output_path,sigma,ratio,rename,self.log,self.redcol,self.blackcol)
            self.Result.setEnabled(True)
            self.out_dir = output_path
        except:
            self.log.append("Convert file %s failed"%os.path.basename(input_path))
            
    @pyqtSignature("")
    def on_Result_clicked(self):
        os.startfile(self.out_dir)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConvertDlg()
    converter.show()
    app.exec_()
    