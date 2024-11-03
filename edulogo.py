from PIL import Image
from math import *
import sys
import os

flag = ("", "")
argc = len(sys.argv)
i = 0
outputFile = "out.txt"

while i < len(sys.argv):
    if "-" in sys.argv[i]:
        flag = (sys.argv[i], i)
        sys.argv.pop(i)
    i+=1

if argc < 2:
    print("missing arguments")
    print("for help using this tool, run:\n'python edulogo.py -h'")
    quit()

if flag[0] == "-h":
    print("usage:\npython edulogo.py -[ho] <input file>")
    print("flags:")
    print(" -h            displays this message")
    print(" -o <file>     specify the output file")
    quit()

print(flag)
if flag[0] == "-o":
    print(argc)
    if argc > flag[1] + 1:
        outputFile = sys.argv[flag[1]]
        sys.argv.pop(flag[1])
    else:
        print("missing arguments")
        quit()

img = Image.open(sys.argv[1])

width, height = img.size
img = img.convert("RGB")

pixels = img.load()

if os.path.isfile(outputFile): os.remove(outputFile)

with open(outputFile, "x") as file:

    file.write(f'cs\npu\nsetposition [-{ceil(width/2)} {ceil(height/2)}]\npd\nmake "w {width}\nmake "c 0\n')

    steps = 1
    lastcolor = (-1, -1, -1)
    colors = []

    for i in range(width):
        for j in range(height):
            if (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]) == lastcolor:
                file.write("n\n")
                continue

            if (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]) in colors:
                file.write(f"r {colors.index((pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]))}\n")
            else:
                colors.append((pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]))
                file.write(f"s [{pixels[i,j][0]} {pixels[i,j][1]} {pixels[i,j][2]}]\n")
            lastcolor = (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2])
        file.write(f"e :w\n")

