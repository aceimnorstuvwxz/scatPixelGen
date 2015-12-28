#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
(C) 2015 ARISECBF
'''

import sys
from pylab import*
from scipy.io import wavfile
from PIL import Image, ImageDraw
import json
import random
import time
import math

def gen():
    textfile = open("marchingcubes.txt", "r")
    lines = textfile.readlines();
#     print lines
    for line in lines:
#         print line
        numbers = line.split()
        for num in numbers:
            if num != ",":
                print num, ",",
        print ""
    pass
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        gen();
    else:
        print "imgcutout xxx.png x0 x1 y0 y1"
