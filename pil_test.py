#!/usr/bin/env python

from PIL import Image, PngImagePlugin

reserved = ('interlace', 'gamma', 'dpi', 'transparency', 'aspect')

im=Image.open('1.png')
meta = PngImagePlugin.PngInfo()
for k,v in im.info.iteritems():
    if k in reserved: continue
    meta.add_text(k, v, 0)
meta.add_text('wtf', 'asdfasdfzxcvzxcvzxcv', 0)

# and save
im.save('2.png', pnginfo=meta)
