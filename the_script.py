#!/usr/bin/env python3
import vlc
import logging

print("Hello world")

p = vlc.MediaPlayer("/home/pi/music/auto/goodbye.mp3")
p.play()
while True:
    pass

logging.basicConfig(level=logging.ERROR, file='/var/log/goodbye.log')
logging.ERROR('message')
