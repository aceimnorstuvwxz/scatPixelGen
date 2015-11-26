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
layerput 画板.png  x0,y0 贴图.png    x1,y1,w,h  输出.png
在画板的 x0,y0位置贴上 贴图中的 x1,y1,w,h 定义的一部分。  
'''
def layerput(fn_board, x0, y0, fn_texture, x1, y1, w, h, fn_out):
    img_board = Image.open(fn_board)
    img_texture = Image.open(fn_texture)
    draw = ImageDraw.Draw(img_board)

    for xx in xrange(w):
        for yy in xrange(h):
            draw.point((x0+xx, y0+yy), img_texture.getpixel((x1+xx,y1+yy)))
    
    img_board.save(fn_out, 'PNG')
    
if __name__ == "__main__":
    '''layerput 画板.png  x0,y0 贴图.png    x1,y1,w,h  输出.png'''
    if len(sys.argv) == 10:
        fn_board = sys.argv[1]
        fn_texture = sys.argv[4]
        fn_out = sys.argv[9]
        x0 = int(sys.argv[2])
        y0 = int(sys.argv[3])
        x1 = int(sys.argv[5])
        y1 = int(sys.argv[6])
        w = int(sys.argv[7])
        h = int(sys.argv[8])
        layerput(fn_board, x0, y0, fn_texture, x1, y1, w, h, fn_out)
    else:
        print '''layerput 画板.png  x0,y0 贴图.png    x1,y1,w,h  输出.png'''
