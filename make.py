"""
list.txtを改行して用意する。
同階層でこのファイルを実行する。
"""

import os

with open('list.txt', 'r') as f:
    FolderList = f.read().split("\n")

for i in FolderList:
    os.mkdir(i)
