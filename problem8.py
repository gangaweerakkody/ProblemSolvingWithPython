from os import listdir
from os.path import islife , join

files_list = [f for f in listdir('/home') if isfile(join('/home'.f))]