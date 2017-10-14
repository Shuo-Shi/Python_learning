#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

dirdict = os.listdir()
current_path = os.getcwd()

key = 0
while key < len(dirdict):
    print(os.path.join(current_path,dirdict[key]))
    key += 1


