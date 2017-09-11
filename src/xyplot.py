#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:48:02 2017

@author: id1917
"""
import numpy as np
import pylab

xy_dat = open("../data/xy.dat", "r")

x = []
y = []

for line in xy_dat:
    # xy = tuple(map(float, line.split()))
    # x.append(xy[0])
    # y.append(xy[1])
    
    xi, yi = line.split()
    x.append(float(xi))
    y.append(float(yi))
  
x = np.array(x)
y = np.array(y)

pylab.plot(x,y)
pylab.show()

print("max(xy) = {}, min(y) = {}.".format(max(y), min(y)))
    