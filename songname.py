#!/usr/bin/env python3
import vlc

p = vlc.MediaPlayer("/home/pi/FOLDER/SONGNAME.mp3")
p.play()
while True:
    pass
