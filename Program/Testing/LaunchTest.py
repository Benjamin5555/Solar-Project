#!/usr/bin/env python3
####################################################################################################
# Script that allows easy and quick visulisation of the start position of a body when launching    #
# from a body.                                                                                     #
####################################################################################################
import sys
sys.path.append("../src")
import math
from AnimateSpace import AnimateSpace
from Space import Space

####################################################################################################
PROBE_LAT = -90
PROBE_MASS = 3 
PROBE_RADIUS = 20000


def main():
    space =Space(50) 
    space.addBody("MARS",0,0,6.4185e23,3390e3,0,0)
    space.launchFromSurface("TEST","MARS",PROBE_LAT,PROBE_MASS,PROBE_RADIUS,0,0)
    a=AnimateSpace(space)
    a.liveSim()
    
main()
