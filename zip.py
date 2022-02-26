import zipfile
import os

#zipファイルが格納されているフォルダのパス
path = 'C:\Users\hirok\Downloads\sample'
output = 'C:\Users\hirok\Downloads\sample\解凍'

#ファイル名を取得
files = os.listdir(path)

#ひとつずつ解凍
for i in files:
    #zipファイル名のフォルダがなければ新しく作る
    if not os.path.isdir(output + i):
        os.mkdir(output + i)
    #解凍
    zf = zipfile.ZipFile(path + i)
    zf.extractall(output + i)