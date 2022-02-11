#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图片转为turtle代码
Version : 0.1
Author  : yx
Date    : 2022-02-11
"""

from PIL import Image

f = open('test.py', 'w')

im = Image.open("1.jpg")
x, y = im.size
print(f'{x}px * {y}px')

f.write("import turtle\n\n\n")
f.write("canvasX = {}\n".format(x))
f.write("canvasY = {}\n".format(y))

f.write('''
def D(x, y):
    return x - canvasX // 2, - y + canvasY // 2
\n\nturtle.screensize(canvasX,canvasY, "white")
turtle.penup()
turtle.goto(D(0,0))
turtle.pendown()
turtle.pensize(1)
turtle.speed(0)
turtle.colormode(255)
turtle.delay(0)
turtle.tracer({},0)
turtle.hideturtle()
'''.format(x))

for y in range(im.size[1]):
    f.write("turtle.penup()\n")
    f.write("turtle.goto(D(0,{}))\n".format(y))
    f.write("turtle.pendown()\n")
    for x in range(im.size[0]):
        pix = im.getpixel((x, y))
        f.write("turtle.pencolor" + str(pix) + "\n")
        f.write("turtle.forward(1)\n")

f.write("turtle.done()\n")
