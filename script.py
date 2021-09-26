import os
import sys

extension1 = input('Extensión de los archivos: ')
extension2 = input('Extension que desea: ')
folder = input('Ingrese su ruta: ')
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(extension1, extension2)
    output = os.rename(infilename, newname)
