#!/usr/bin/env python3
####################################################################################################
# Script that performs a live ('on the fly') animation of Mars and its surronding moons.           #
# Also tests that the program is able to add an object given values                                #
# Is effectivly the checkpoint5 Task                                                               #
####################################################################################################

import sys
sys.path.append("../src")
from AnimateSpace import AnimateSpace
from Space import Space
def main():
    space =Space(50) 
    space.addBody("Mars",0,0,6.4185e23,3390e3,0,0)
    space.addBody("Phobos",9.3773e6,0,1.06e16,11e3,0,2137.356443587166)
    space.addBody("Deimos",23460e3,0,1.8e15,6.2e3,0,1.3513e3)
    a=AnimateSpace(space)
    a.liveSim()
main()
