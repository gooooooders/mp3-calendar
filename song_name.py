#!/usr/bin/env python3
import vlc
import logging

p = vlc.MediaPlayer("/home/pi/music/auto/goodbye.mp3")
p.play()
while True:
    pass

logging.warn('message')
