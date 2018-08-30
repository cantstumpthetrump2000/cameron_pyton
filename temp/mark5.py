#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

from math import cos, sin, pi, sqrt, atan2
d2r = pi/180



def circle_intersection_sympy( circle1, circle2):
    from sympy.geometry import Circle, Point
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    c1=Circle(Point(x1,y1),r1)
    c2=Circle(Point(x2,y2),r2)
    intersection = c1.intersection(c2)
    if len(intersection) == 1:
        intersection.append(intersection[0])
    p1 = intersection[0]
    p2 = intersection[1]
    print((p2))
    print(p2.evaluate)
    xs1,ys1 = p1.x,p1.y
    xs2,ys2 = p2.x,p2.y
    print((xs1,ys1),(xs2,ys2))
    #return (xs1,ys1),(xs2,ys2)


circle_intersection_sympy((0,0,50),(50,0,55))
