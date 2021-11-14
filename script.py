import os
import sys

extension1 = input('File extension: ')
extension2 = input('Extension you want: ')
folder = input('Enter your file path: ')

for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.' + extension1, '.' + extension2)
    output = os.rename(infilename, newname)
