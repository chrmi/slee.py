from os import listdir
from os.path import isfile, join

def getFileNames():
    return [f for f in listdir('audio') if isfile(join('audio', f))]

