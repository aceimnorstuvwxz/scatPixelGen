#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
(C) 2015 Arisecbf
'''

import sys
from pylab import*
from scipy.io import wavfile
from PIL import Image, ImageDraw
import json
import random
import time

'''
255整型
'''

ALPHA_THREHOLD = 50

def isExist(img, x, y):
    if (x >= 0 and x < img.size[0] and y >= 0 and y < img.size[1]):
        r,g,b,a = img.getpixel((x,y))
        if (a > ALPHA_THREHOLD):
            return 1
    return 0

def gen(fn):
    img = Image.open(fn)
    w,h = img.size
    hw = int(w/2)
    hh = int(h/2)
    jobj = {}
    jobj["data"] = []
    
    print 'size=', img.size
    for ix in xrange(w):
        for iy in xrange(h):
            pos = (ix-hw, h-1-iy-hh)
            r,g,b,a = img.getpixel((ix,iy))
            if  a > ALPHA_THREHOLD:
                node = {}
                node['x'] = pos[0]
                node['y'] = pos[1]
                node['r'] = r
                node['g'] = g
                node['b'] = b
                node['T'] = isExist(img, ix, iy+1)
                node['B'] = isExist(img, ix, iy-1)
                node['L'] = isExist(img, ix-1, iy)
                node['R'] = isExist(img, ix+1, iy)
                jobj["data"].append(node)
            
#     print jobj
    f = open(fn+'.sopx','w')
    f.write(json.dumps(jobj))
    f.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fn = sys.argv[1]
        gen(fn)
    else:
        print "png file as parameter..."
