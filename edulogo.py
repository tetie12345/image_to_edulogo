from PIL import Image
from math import *
import sys
import os

flag = ""
argc = len(sys.argv)

for i in range(len(sys.argv)):
    if "-" in sys.argv[i]:
        flag = sys.argv[i]
        sys.argv.pop(i)

if argc < 2:
    print("missing arguments")
    print("for help using this tool, run:\n'python edulogo.py -h'")
    quit()

if flag == "-h":
    print("usage:\npython edulogo.py -[ho] <input file>")
    print("flags:")
    print(" -h            displays this message")
    print(" -o <file>     specify the output file")
    quit()

elif flag == "-o":
    pass

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

