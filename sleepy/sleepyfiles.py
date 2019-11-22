from os import listdir
from os.path import isfile, join

def getFileNames():
    return [f for f in listdir('/home/pi/slee.py/audio') if isfile(join('/home/pi/slee.py/audio', f))]

