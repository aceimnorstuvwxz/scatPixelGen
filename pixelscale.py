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
KLSD 的 TGA 资源图片的每个Pixel 是9X9的，所以这里需要缩放回去。
缩放并不需要对齐，而是在 X,Y 方向都分别以3为 step 采样即可。

'''
def pixelscale(fn, n):
    img = Image.open(fn)
    w,h = img.size
    nw,nh = int(w/n),int(h/n)
    print w,h,nw,nh
    
    img_out = Image.new("RGBA", (nw,nh), color=(0,0,0,0))
    draw = ImageDraw.Draw(img_out)
    for xx in xrange(nw):
        for yy in xrange(nh):
            rr,gg,bb,aa = 0,0,0,0
            for i in xrange(n):
                for j in xrange(n):
                    r,g,b,a = img.getpixel((xx*n+i, yy*n+j))
                    rr,gg,bb,aa = rr+r,gg+g,bb+b,aa+a
            n2 = n*n
            draw.point((xx,yy), (int(rr/n2),int(gg/n2),int(bb/n2),int(aa/n2)))
    img_out.save(("%s.ps.png"%fn), 'PNG')
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        fn = sys.argv[1]
        n = int(sys.argv[2])
        print fn
        pixelscale(fn,n)
    else:
        print "klsdtga xxx.png xxxout.png"
