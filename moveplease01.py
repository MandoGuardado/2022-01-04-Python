#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/2022-01-04-Python/')
shutil.move('raynor.obj', 'Lab_21/')
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('Lab_21/kerrigan.obj', 'Lab_21/' + xname)


