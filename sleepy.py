import time

import sleepyio
import sleepydisplay
import sleepyaudio

while True:
    sleepyio.update()
    sleepydisplay.update()
    sleepyaudio.update()
    time.sleep(.05)
