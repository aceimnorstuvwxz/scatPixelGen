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
            pos = (ix-hw, w-1-iy-hh)
            r,g,b,a = img.getpixel((ix,iy))
            if  a > ALPHA_THREHOLD:
                node = {}
                node['x'] = pos[0]
                node['y'] = pos[1]
                node['r'] = r
                node['g'] = g
                node['b'] = b
                jobj["data"].append(node)
            
    print jobj
    f = open(fn+'.sopx','w')
    f.write(json.dumps(jobj))
    f.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fn = sys.argv[1]
        gen(fn)
    else:
        print "png file as parameter..."
