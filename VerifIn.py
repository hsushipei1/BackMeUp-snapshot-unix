#!~/Software/python-stack/bin/python  
#-*- coding: utf-8 -*-
import os, ntpath, sys

"""
顯示使用者剛才輸入的內容，並讓使用者選擇是否繼續還是重新輸入。
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def VeryifyInput(DirToBeBackup,FilExtList,BkupPath):
	print"""\
-----------------------------------------------------------
# Please verify your inputs
-----------------------------------------------------------
@ Absolute path to the directory you want to make a backup
=> %r

@ List of file extensions
=> %r

@ Path to save your backup
=> %r

# Hit ENTER to continute or CTRL-C to quit."""\
 %(DirToBeBackup,FilExtList,BkupPath)

	opt2 = raw_input(">")

