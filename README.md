# Image_to_edulogo
Converts an image file into executable code in edulogo

Contents:
-
- Limitations
- Dependencies
    - Installing dependencies
- Installation
- Usage
- Setup inside Edulogo  

# Limitations
Since the script goes through all pixels in an image, it may take a while for some images to be converted.
This time depends on the amount of unique colors in the image.

This script has only been tested on macOS, as Edulogo is only available for mac.

Some images have an issue where the image is skewed, we are working on finding the cause of this issue, and fixing it.

The canvas in Edulogo is only 500x500, meaning any image with a larger size than that will be cropped to fit.

# dependencies:
**Python 3.13+**, The python interpeter.

**Pip 24+**, A package manager for python libraries.

**PILLOW**, An image processing library for python.

## Installing dependencies:
To install Python, go to [the python website](https://www.python.org) and download the latest version of python, then simply follow the instructions.

After installing python, make sure you also installed pip. to check if pip is installed, run the following command:
`pip --version`

If pip installed correctly you can skip the following steps.

Alternative pip install
-
Get the pip binary:
``curl https://bootstrap.pypa.io/get-pip.py > pip.py``.

Use the python interpeter to install pip:
``python pip.py``.

Confirm pip has installed by running `pip --version` again.

---

To install pillow, run the following command:

`pip install pillow`

> **Note**: If this command outputs an error, check if pip is installed correctly, and up to date.

> To update pip, run `pip install --upgrade pip`.

# Installation:
**Make sure you have installed all dependencies before using the script.**

Clone this repository and run the script using python:
```
git clone https://github.com/tetie12345/image_to_edulogo.git
cd image_to_edulogo
```

To run the script, use:
``
python edulogo.py <file>
``

**The script is now ready to be used.**

# Setup inside Edulogo:
Assuming you have edulogo installed, the setup is simple.

Create **5** procedures, and name them: s, r, e, m, and n.
and program them like so:

s:
``
setRGB :c :param
setpencolor :c
make "c :c + 1
fd -1
``.

e:
``
pu
rt 90
fd 1
rt 90
fd :param * -1
rt 180
pd
``.

n:
``
fd -1
``.

r:
``
setcolor :param
fd -1
``.

m:
``
fd 0 - :param
``.

And add 1 parameter to all except n.
> **Note**: keep the default parameter names.

# Usage:
python edulogo.py -[ho] <file>

flags:

    -h              brings up this menu
    -o <filename>   specify output file. default "out.txt"

> **note**: the -o flag overwrites the given file if it exists, without warning

The contents of the output file can now be copied into any setup edulogo project, (see previous paragraph for instructions on how to set up Edulogo).

To run the script, paste it into the EL editor, and hit cmd+R to run it.


# FAQ
When i try to run the the edulogo script, it gives an error.
- Make sure you created the correct procedures inside edulogo, the procedures tab is found under `window > show procedures`.

Running the python script gives an error.
- make sure you have the latest version of python, pip, and pillow installed.

The python script doesn't work / doesn't do anything.
- although quite optimal, the script can take up to 3 minutes to covert an image.
