# image_to_edulogo
converts an image file into executable code in edulogo

contents:
-
- support
- dependencies
    - installing dependencies
- installation
- usage
- setup inside EL

# support:
image_to_edulogo is **only** supported on unix based operating systems, and only tested on macOS

# dependencies:
**python 3.12+**, the python interpeter
**pip 24+**, a package manager for python libraries
**PILLOW**, an image processing library for python

## installing dependencies:
to install python, go to [the python website](https://www.python.org) and download the latest version of python, then simply follow the instructions

after installing python, make sure you also installed pip. to check if pip is installed, run the following command:
`pip --version`

if pip installed correctly you can skip the following steps.

alternative pip install
-
get the pip binary:
``curl https://bootstrap.pypa.io/get-pip.py > pip.py``

use the python interpeter to install pip:
``python pip.py``

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
cd image_to_edulogo
```

to run the script, use:
``
python edulogo.py <file>
``

**the script is now ready to be used**

# Setup inside EL:
assuming you have edulogo installed, the setup is simple.

create **4** procedures, and name them: s, r, e, and n
and program them like so:

s:
``
setRGB :c :param
setpencolor :c
make "c :c + 1
fd -1
``

e:
``
pu
rt 90
fd 1
rt 90
fd :param * -1
rt 180
pd
``

n:
``
fd -1
``

r:
``
setcolor :param
fd -1
``

and add 1 parameter to all except n.
> **note**, keep the parameters default name

# Usage:
python edulogo.py -[ho] <file>

flags:

    -h              brings up this menu
    -o <filename>   specify output file. default "out.txt"

> **note**, the -o flag overwrites the given file if it exists, without warning

the contents of the output file can now be copied into any setup edulogo project, (see previous paragraph for instructions on how to set up edologo)

to run the script, paste it into the EL editor, and hit cmd+R to run it


# FAQ
when i try to run the the edulogo script, it gives an error.
- make sure you created the correct procedures inside edulogo, the procedures tab is found under `window > show procedures`

running the python script gives an error
- make sure you have the latest version of python, pip, and pillow installed:
