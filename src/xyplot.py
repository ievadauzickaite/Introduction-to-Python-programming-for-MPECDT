#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:48:02 2017

@author: id1917
"""
import numpy as np
import pylab

infile = open("../data/xy.dat", "r")

xlist = []
ylist = []

for line in infile:
    xi, yi = line.split()
    xlist.append(float(xi))
    ylist.append(float(yi))
  
x = np.array(xlist)
y = np.array(ylist)

pylab.plot(x,y)

print("max(xy) = {}, min(y) = {}.".format(max(y), min(y)))
    