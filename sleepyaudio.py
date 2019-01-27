import sleepystate
import vlc

p = vlc.MediaPlayer('audio/' + sleepystate.getPlayingTrack())
p.pause()
p.audio_set_volume(100)

def changeTrack():
    global p
    p.stop()
    p = vlc.MediaPlayer('audio/' + sleepystate.getPlayingTrack())
    p.pause()

def update():
    global p
    if sleepystate.isPaused():
        p.pause()
    else:
        p.play()
