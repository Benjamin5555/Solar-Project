#!/usr/bin/env python3
####################################################################################################
# Script that performs a test of creating and saveing an animation of the inner planets of the     #
# solar system                                                                                     #
# Also tests that the program is able to add an object from file                                   #
####################################################################################################
import sys
sys.path.append("../SRC")

from AnimateSpace import AnimateSpace
from Space import Space

TIME_INTERVAL = 15000
OVERALL_SIM_TIME = 0.5*3.154e+7 #1 Years
ENERGY_OUTPUT_FILE = "../OUTPUT/InnerPlanetsEnergyOut.csv"

def main():
    space =Space(TIME_INTERVAL,ENERGY_OUTPUT_FILE) 
    space.addFromFile("../SRC/PlanetData/innerPlanets.csv")

    
    a=AnimateSpace(space)
    data = space.simulatePeriodAndTrace(OVERALL_SIM_TIME)
    a.saveExistingDataAnimation(data)
    
    
    
main()
