# -*- coding: utf-8 -*-
# See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp
# for information on Windows APIs.

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.

FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.



#  See http:http://lcs.syr.edu/faculty/morphet/screen.cpp

#define FOREGROUND_BLACK   (0)
#define FOREGROUND_WHITE   (FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
#define FOREGROUND_YELLOW  (FOREGROUND_RED | FOREGROUND_GREEN)
#define FOREGROUND_MAGENTA (FOREGROUND_RED | FOREGROUND_BLUE)
#define FOREGROUND_CYAN    (FOREGROUND_GREEN | FOREGROUND_BLUE)
#define BACKGROUND_BLACK   (0)
#define BACKGROUND_WHITE   (BACKGROUND_RED | BACKGROUND_GREEN | BACKGROUND_BLUE)
#define BACKGROUND_YELLOW  (BACKGROUND_RED | BACKGROUND_GREEN)
#define BACKGROUND_MAGENTA (BACKGROUND_RED | BACKGROUND_BLUE)
#define BACKGROUND_CYAN    (BACKGROUND_GREEN | BACKGROUND_BLUE)

import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_cmd_text_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool
# set_cmd_text_color
def resetColor():
    """"""
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
#

def printError(mess):
    """
    
    """
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
    print(mess)
    resetColor()
#
def printProcess(mess):
    """
    
    """
    set_cmd_text_color(FOREGROUND_GREEN | FOREGROUND_BLUE)
    print(mess)
    resetColor()
#
def printResult(mess):
    """
    
    """
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_BLUE| FOREGROUND_INTENSITY)
    print(mess)
    resetColor()
#
def printWait(mess):
    """
    
    """
    set_cmd_text_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    print(mess)
    resetColor()
#

def tprintList():
    """
    
    """
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_INTENSITY)
#
def tprintTip():
    """
     raw_input 
    """
    set_cmd_text_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
#
def MainEnter():
    """"""
    printError('error')
    printProcess('wait.......')
    printResult('result...')
    printWait('wati again...')
    li=['a','b','c','d']
    tprintList()
    for i,v in enumerate(li):print '%s.%s' %(i+1,v)
    resetColor(); tprintTip()
    s=raw_input("""
    
    """)
    printResult(''+s)

if __name__=='__main__':
    MainEnter()