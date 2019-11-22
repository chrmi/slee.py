import sleepyfiles

tracks = sleepyfiles.getFileNames()

previousTrack = tracks[0]
selectedTrack = tracks[1] 
nextTrack = tracks[2]

selected = 1
playing = 1
paused = True 

def getPreviousTrack():
    if selected < 1:
        return tracks[len(tracks) - 1]
    else:
        return tracks[selected - 1]

def getSelectedTrack():
    return tracks[selected]

def getNextTrack():
    if selected == len(tracks) - 1:
        return tracks[0]
    else:
        return tracks[selected + 1]

def getPlayingTrack():
   return tracks[playing] 

def selectNext():
    global selected
    if selected == len(tracks) - 1:
        selected = 0
    else:
        selected = selected + 1

def selectPrevious():
    global selected
    if selected > 0:
        selected = selected - 1
    else:
        selected = len(tracks) - 1

def playSelected():
    global playing
    global selected
    playing = selected

def pause():
    global paused
    paused = True

def unpause():
    global paused
    paused = False

def isPaused():
    return paused 
