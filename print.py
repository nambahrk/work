
import win32api
import sys
import os
import time
 
def auto_print(path):
if __name__ == '__main__':
win32api.ShellExecute(0,"print",path,None,".",0)
print("Printed:"+path)
 
def file_check(path):
if os.path.isdir(path):
files = os.listdir(path)
for file in files:
file_check(path+"\\"+file)
 
else:
auto_print(path)
time.sleep(3)
 
print_path = r"./印刷用"
 
file_check(print_path)
 
print("Process finished")