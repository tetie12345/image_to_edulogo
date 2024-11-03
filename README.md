# image_to_edulogo
converts an image file into executable code in edulogo

contents:
-
- dependencies
    - installing dependencies
- installation
    - setup
- usage


# dependencies:
**python 3.12+**, the python interpeter
**pip 24+**, a package manager for python libraries
**PILLOW**, an image processing library for python

## installing dependencies:
to install python, go to [the python website](www.python.org) and download the latest version of python, then simply follow the instructions

after installing python, make sure you also installed pip. to check if pip is installed, run the following command:
`pip --version`

if pip installed correctly you can skip the following steps.

if pip did not install
-
get the pip binary:
`curl  https://bootstrap.pypa.io/get-pip.py > pip.py`

use the python interpeter to install pip:
`python pip.py`

confirm pip has installed by running `pip --version` again

---

to install pillow, rune the following command:
`pip install pillow`

> **note** if this command outputs an error, check if pip is installed correctly, and up to date
> to update pip, run `pip install --upgrade pip`

# Installation:
**make sure you have installed all dependencies before using the script.**

clone this repository and run the script using python:
```
git clone https://github.com/tetie12345/image_to_edulogo.git
cd image_to_edulogo.git
python edulogoV2.py
```





s:

setRGB :c :param
setpencolor :c
make "c :c + 1
fd -1

e:

pu
rt 90
fd 1
rt 90
fd :param * -1
rt 180
pd

n:

fd -1

r:

setcolor :param
fd -1
