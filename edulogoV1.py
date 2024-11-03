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

print(f'cs\npu\nsetposition [-{ceil(width/2)} {ceil(height/2)}]\npd\nmake "w {width}')

steps = 1
lastcolor = (-1, -1, -1)

for i in range(width):
    for j in range(height):
        if (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]) == lastcolor:
            print("n")
            continue

        print(f"s [{pixels[i,j][0]} {pixels[i,j][1]} {pixels[i,j][2]}]")
        lastcolor = (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2])
    print(f"e :w")

