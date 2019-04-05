#!/usr/bin/env python3
####################################################################################################
# Script that performs a test of creating data then displaying an animation of the Earth and Moon  #
# Also tests that the program is able to add an object from file and the produce immediate output  #
####################################################################################################
import sys
sys.path.append("../SRC")

from AnimateSpace import AnimateSpace
from Space import Space

TIME_INTERVAL = 50
OVERALL_SIM_TIME = 2.628e+6 #A month
ENERGY_OUTPUT_FILE = "/dev/null" 
def main():
    space =Space(TIME_INTERVAL,ENERGY_OUTPUT_FILE) 
    space.addFromFile("../SRC/PlanetData/Earth moon.csv")
    a=AnimateSpace(space)
    data = space.simulatePeriodAndTrace(OVERALL_SIM_TIME)
    a.animateExistingData(data)
    
main()
