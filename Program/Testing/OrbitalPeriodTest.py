#!/usr/bin/env python3
####################################################################################################
# Provides a test that the class is able to calculate a year for a body using the Earth as an      # 
# example. OUTPUTS IN SECONDS                                                                      # 
####################################################################################################
import sys
sys.path.append("../SRC")

from AnimateSpace import AnimateSpace
from Space import Space

TIME_INTERVAL = 10000
PLANET_DATA_FILE = "../SRC/PlanetData/innerPlanets.csv"
PLANET_YEAR_TO_GET = "EARTH"
def main():
    space =Space(TIME_INTERVAL,"/dev/null") 
    space.addFromFile(PLANET_DATA_FILE)
    print(space.getOrbitalPeriodOfBody(PLANET_YEAR_TO_GET))
main()
