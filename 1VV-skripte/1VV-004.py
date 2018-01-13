#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script takes the raw album cover image data and prepares it for later analysis.
Input is a folder with image files.
Output is another folder with image files.
Operations are resize to 500x500 pixels and binarization of the image (== 1 bit per pixel).
"""

import os
import glob
from os.path import join

# same package
from ZZ_HelperModules import basic_image_functions as bif, docfile

# ===============================
# Parameters
# ===============================

current_dir = os.path.dirname(os.path.abspath(__file__))
workdir, tail = os.path.split(current_dir)
sourcedatafolder = join(workdir, "0RD-daten", "0RD-003")
targetdatafolder = join(workdir, "2VV-daten", "2VV-004")
documentationfile = join(workdir, "2VV-daten", "2VV-004.txt")
docstring = __doc__


# ===============================
# Functions
# ===============================

# ===============================
# Main
# ===============================

def main(sourcedatafolder, targetdatafolder, documentationfile, docstring, tail):
    if not os.path.exists(targetdatafolder):
        os.makedirs(targetdatafolder)
    for file in glob.glob(sourcedatafolder + "/*"):
        basename, ext = os.path.basename(file).split(".")
        image = bif.load(file)
        image = bif.resize(image, 500, 500)
        image = bif.mode(image, "bw")
        bif.save(image, basename, targetdatafolder)
    docfile.write(sourcedatafolder, targetdatafolder, documentationfile, docstring, tail, __file__)


main(sourcedatafolder, targetdatafolder, documentationfile, docstring, tail)
