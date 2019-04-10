#!/usr/bin/env python

import os
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))

libIdxFile = open("lib_index.txt", "w")

files = os.listdir('.')
for fileName in files:
    if fileName.endswith(".lib"):
        libIdxFile.write(fileName + '\n')

libIdxFile.close()
