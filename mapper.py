#!/usr/bin/env python

import sys
import os


for line in sys.stdin:
    line = line.strip()
    datas = line.split(";")
    if not "fixed acidity" in datas[0]:
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (datas[0], datas[1], datas[2], datas[3], datas[4], datas[5], datas[6], datas[7], datas[8], datas[9], datas[10], datas[11])
