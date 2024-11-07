# Created by tetie12345 on 10-03-2024

from PIL import Image
from math import ceil
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
    print(" -o <file>     specify the output file, default = out.txt")
    quit()

if flag[0] == "-o":
    if argc > flag[1] + 1:
        outputFile = sys.argv[flag[1]]
        sys.argv.pop(flag[1])
    else:
        print("missing arguments")
        quit()

if not os.path.isfile(sys.argv[1]):
    if os.path.isdir(sys.argv[1]):
        print(f"path '{sys.argv[1]}' is a directory")
    print(f"no such file: '{sys.argv[1]}'")
    quit()

outputFile = outputFile.removesuffix("/")

img = Image.open(sys.argv[1])

width, height = img.size
img = img.convert("RGB")

pixels = img.load()

if os.path.isfile(outputFile): os.remove(outputFile)

with open(outputFile, "x") as file:

    file.write(f'cs pu setposition [-{ceil(width/2)} {ceil(height/2)}] pd make "w {height} make "c 0 ')

    steps = 1
    lastcolor = (-1, -1, -1)
    colors = []
    nCount = 0

    for i in range(width):
        for j in range(height):
            print(f"{round(((width*i+j)/(width*height))*100, 3)}% done     ", end = "\r")
            color = (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2])
            if color == lastcolor:
                nCount += 1
                continue
            elif nCount == 1:
                file.write(f"n ")
                nCount = 0
            elif nCount > 1:
                file.write(f"m {nCount} ")
                nCount = 0

            if color in colors:
                file.write(f"r {colors.index(color)} ")
            else:
                colors.append(color)
                file.write(f"s [{pixels[i,j][0]} {pixels[i,j][1]} {pixels[i,j][2]}] ")
            lastcolor = color
        if nCount == 1:
            file.write("n ")
        elif nCount > 1:
            file.write(f"m {nCount} ")
        nCount = 0
        file.write(f"e :w ")
