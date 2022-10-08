#!/usr/bin/env python3
####################################################################################################
# Script that outputs the orbital periods of the planets in the solar system to file.              # 
# This is not included in the space class due to not being reliable for all objects that would be  # 
# in space e.g. objects that have no stable orbit.                                                 # 
####################################################################################################
import sys
sys.path.append("../src")

from AnimateSpace import AnimateSpace
from Space import Space

TIME_INTERVAL = 10000
OVERALL_SIM_TIME = 3.154e+7 #1 Years
OUTPUT_FILE = "../OUTPUT/OrbitalPeriodsOfBodies.csv"
ENERGIES_OUTPUT_FILE = "/dev/null"
PLANETS_TO_SIM_DATA = "../src/PlanetData/innerPlanets.csv"


def main():
    space =Space(TIME_INTERVAL,ENERGIES_OUTPUT_FILE) 
    space.addFromFile(PLANETS_TO_SIM_DATA)
    f = open(OUTPUT_FILE,'w')
    for x in space.getBodies():
        if(x.getName()=="Sun"):
 	# Skip over the sun as where simulated as has no stable orbit in this sim 
            continue
        
        f.write(x.getName()+","+str(space.getOrbitalPeriodOfBody(x.getName()))+"\n")
	#Write data to file
    f.close()
    
    
main()
