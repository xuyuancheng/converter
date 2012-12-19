# -*- coding: utf-8 -*-
'''
Created on 12.17.2012
@author zhaiyt
'''
import os
import sys

class Converter(object):

    def __init__(self):
        self.part_list=[]
        self.raw_list=[]
        self.cdf=""

    def log(self, log_info, mode='cli'):
        '''
        output the log msg
        '''
        if mode == 'cli':
            print log_info

    # CLI only
    def findFile(self, post_fix=""):  
        '''
        Find the raw data file in current folder
        post_fix must be lower case
        '''
        cur_dir = os.getcwd()
        for root, dirs, files in os.walk(cur_dir):
            for fil in files:
                if fil.split('.')[-1] == 'cdf':
                    fil_path = os.path.join(root,fil)
                    self.cdf = fil_path
                elif fil.split('.')[-1] == 'py' or fil.split('.')[-1] == 'exe':
                    continue
                elif post_fix == "":
                    fil_path = os.path.join(root,fil)
                    self.raw_list.append(fil_path)
                elif fil.split('.')[-1].lower() == post_fix:
                    fil_path = os.path.join(root,fil)
                    self.raw_list.append(fil_path)

         

        raw_num = len(self.raw_list)
        if not raw_num:
            self.log("")
            self.log("No file find ,please put data file to current dirctory")
            raw_input()
            sys.exit()
        else:
            self.log("")
            self.log("%d files need to convert:" % raw_num)
            self.log("")
            for fil in self.raw_list:
                self.log(fil)
                self.log("")

    def isPartStart(self,line):
        pass

    def isPartEnd(self,line):
        pass
            
    def getPartList(self,content):
        '''
        devide the file content to part
        '''
        start=[]
        end=[]
        part_list=[]
        for i,line in enumerate(content):
            if self.isPartStart(line):
                start.append(i)

            if self.isPartEnd(line):
                end.append(i)

        # no end line 
        if end==[]:
            for i,start_index in enumerate(start):
                if i == len(start) - 1:
                    part = content[start_index:]
                    part_list.append(part)
                else:
                    part = content[start_index:start[i+1]]
                    part_list.append(part)

            return part_list
        else:
            if len(start) != len(end):
                self.log("Unmatched part line found!")
                return part_list
            for i, start_index in enumerate(start):
                part = content[start_index, end[i]]
                part_list.append(part)

            return part_list

    def convertPart(self,part):
        '''
        convert part process
        '''
        pass

    def readCdf(self):
        pass



                




