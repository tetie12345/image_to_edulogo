#! /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
from PIL import Image
from math import *
import sys

if len(sys.argv) < 2:
    print("missing arguments")
    exit

img = Image.open(sys.argv[1])

width, height = img.size
img = img.convert("RGB")

pixels = img.load()

print(f'cs\npu\nsetposition [-{ceil(width/2)} {ceil(height/2)}]\npd\nmake "w {width}\nmake "c 0')

steps = 1
lastcolor = (-1, -1, -1)
colors = []

for i in range(width):
    for j in range(height):
        if (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]) == lastcolor:
            print("n")
            continue

        if (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]) in colors:
            print(f"r {colors.index((pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]))}")
        else:
            colors.append((pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]))
            print(f"s [{pixels[i,j][0]} {pixels[i,j][1]} {pixels[i,j][2]}]")
        lastcolor = (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2])
    print(f"e :w")

