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
import math

'''
从 某图片中扣出一部分
注意 x1,y1所在是不包含的。
坐标从左上角开始

'''
def cutout(fn, fn_out, x0, x1, y0, y1):
    img = Image.open(fn)
    w,h = img.size
    #check size
    if x0 > x1 or y0 > y1 or x1 > w or y1 > h:
        print "cut position is out of image"
        return
    
    ow = x1-x0
    oh = y1-y0
    img_out = Image.new("RGBA", (ow,oh), color=(0,0,0,0))
    draw = ImageDraw.Draw(img_out)
    for xx in xrange(ow):
        for yy in xrange(oh):
            draw.point((xx,yy), img.getpixel((x0+xx, y0+yy)))
    img_out.save(fn_out, 'PNG')
    
if __name__ == "__main__":
    if len(sys.argv) == 7:
        fn = sys.argv[1]
        fn_out = sys.argv[2]
        x0 = int(sys.argv[3])
        x1 = int(sys.argv[4])
        y0 = int(sys.argv[5])
        y1 = int(sys.argv[6])
        print fn,x0,x1,y0,y1
        cutout(fn,fn_out,x0,x1,y0,y1)
    else:
        print "imgcutout xxx.png x0 x1 y0 y1"
