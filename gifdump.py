#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
(C) 2015 Arisecbf
'''

import sys
from pylab import*
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageSequence
import json
import random
import time


def gen(fn):
    img = Image.open(fn)
    cnt = 0
    for frame in ImageSequence.Iterator(img):
        frame.save(("%s.%d.png"%(fn,cnt)), "PNG")
        cnt = cnt+1
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fn = sys.argv[1]
        print fn
        gen(fn)
    else:
        print "gif file as parameter..."
