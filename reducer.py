#!/usr/bin/env python

import sys

count = 0
sum = {"fixed acidity": 0.,
       "volatile acidity": 0.,
       "citric acid": 0.,
       "residual sugar": 0.,
       "chlorides": 0.,
       "free sulfur dioxide": 0.,
       "total sulfur dioxide": 0.,
       "density": 0.,
       "pH": 0.,
       "sulphates": 0.,
       "alcohol": 0.,
       "quality": 0.}

for line in sys.stdin:
    line = line.strip()
    datas = line.split()
    sum["fixed acidity"] += float(datas[0])
    sum["volatile acidity"] += float(datas[1])
    sum["citric acid"] += float(datas[2])
    sum["residual sugar"] += float(datas[3])
    sum["chlorides"] += float(datas[4])
    sum["free sulfur dioxide"] += float(datas[5])
    sum["total sulfur dioxide"] += float(datas[6])
    sum["density"] += float(datas[7])
    sum["pH"] += float(datas[8])
    sum["sulphates"] += float(datas[9])
    sum["alcohol"] += float(datas[10])
    sum["quality"] += float(datas[11])
    count += 1

print "fixed acidity mean\tvolatile acidity mean\tcitric acid mean\tresidual sugar mean\tchlorides mean\tfree sulfur dioxide mean\ttotal sulfur dioxide mean\tdensity mean\tpH mean\tsulphates mean\talcohol mean\tquality mean"
print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (float(sum["fixed acidity"])/float(count), float(sum["volatile acidity"])/float(count), float(sum["citric acid"])/float(count), float(sum["residual sugar"])/float(count), float(sum["chlorides"])/float(count), float(sum["free sulfur dioxide"])/float(count), float(sum["total sulfur dioxide"])/float(count), float(sum["density"])/float(count), float(sum["pH"])/float(count), float(sum["sulphates"])/float(count),float(sum["alcohol"])/float(count), float(sum["quality"])/float(count))