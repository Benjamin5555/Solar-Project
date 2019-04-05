#!/usr/bin/env python3
####################################################################################################
# Provides a command line script that can be used to produce a probe path for a probe of simlar    #
# size and mass to those used in NASA's Viking Missions                                            # 
# (SOURCE https://www.nasa.gov/redplanet/viking.html)                                              #
####################################################################################################
from AnimateSpace import AnimateSpace
from Space import Space
import sys
def main():
    space =Space(int(sys.argv[4]),sys.argv[5]) 
    space.addFromFile("PlanetData/innerPlanets.csv")


    space.launchFromSurface("PROBE","EARTH",int(sys.argv[1]),3000,3,int(sys.argv[2]),int(sys.argv[3]))

    a=AnimateSpace(space)
    

    data = space.simulatePeriodAndTrace(3.154e+7*0.5)#yr = 3.154e+7

    a.saveExistingDataAnimation(data,"../OUTPUT/ProbeAnimation "+sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]+" "+sys.argv[4]+".mp4")
    

    
main()
