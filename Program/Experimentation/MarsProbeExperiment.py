#!/usr/bin/env python3
####################################################################################################
#############################    SCRIPT DETAILS AND AIMS    ########################################
####################################################################################################
# Script to produce values which can be used to determine parameters which will potentially be a   # 
# viable path for a object (the probe) launched from the surface of one body (the launch body)     #
# toward another (the target body).                                                                #
#                                                                                                  #
# As this script performs minimal functionality and required a very large number of parameters it  #
# was most simple to write it in this way and change paramters by changing the file itself, this   #
# is also down to it being much of a work in progress where changes were made frequently in an     #
# attempt to more quickly produce values which were more valid and hence did not allow for the     #
# planning that would go into a class file                                                         #
####################################################################################################

import sys
sys.path.append("../src")
import time
import math
import Running
import Space


####################################################################################################
#############################    EXPERIMENTAL PARAMETERS    ########################################
####################################################################################################
# The paramters in use are setup for a path between Earth and Mars, unknown paramters such as mass #
# for Earth and Mars are sourced from "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"           #
# Parameters for the probe are based roughly on that of the probes used in NASA's Viking mission   #
# detailed:https://www.nasa.gov/redplanet/viking.html                                              #
# Changing the below paramters can be used to get data on plotting paths for any bodies in a space #
#                                                                                                  #
# NOTE: All Launch paramters must be integers due to them being used as a loop                     #
####################################################################################################

PROBE_NAME = "PROBE"
PROBE_MASS = 3000
PROBE_RADIUS = 3
LAUNCH_NAME = "EARTH"
TARGET_NAME = "MARS"
TIME_INTERVAL = 5000
TIME_TO_SIM = 3.154e+7*(3/4) # three quaters of a year
OUTPUT_PATH = "../OUTPUT/iterateOverLaunchParameters"\
                +time.strftime("%a, %d %b %Y %H:%M:%S",time.gmtime())+".csv"
PLANET_DATA = "../src/PlanetData/innerPlanets.csv"
ENERGY_OUT_FILE = "/dev/null" #Disregards the (large) amount of energy data produced
LOW_INITIAL_X_VELOCITY= 9500
LOW_INITIAL_Y_VELOCITY=  2000 
HIGH_INITIAL_X_VELOCITY= 10500
HIGH_INITIAL_Y_VELOCITY= 3000
INTERVAL_X_VELOCITY = 1000
INTERVAL_Y_VELOCITY = 1000
INITIAL_HIGH_LATITUDE = -45 
INITIAL_LOW_LATITUDE =-55
INTERVAL_LATITUDE = 1

####################################################################################################

def iterateOverLaunchParameters():
    """
    Goes through the specified launch parameter ranges using specfied intervals to produce a 
    closest distance to the target body for each combination of values
    """
    n=Running.Running() 
    f = open(OUTPUT_PATH,'w')
    for launchPosAngle in range(INITIAL_LOW_LATITUDE, INITIAL_HIGH_LATITUDE, INTERVAL_LATITUDE):
        iterateOverVel(f,launchPosAngle)
    f.close()   
    n.join()

def iterateOverVel(f,launchPosAngle):
    """
    Iterates over the specified velocities producing a closest distance to the target body for each
    of them
    """
    for xVel in range(LOW_INITIAL_X_VELOCITY,HIGH_INITIAL_X_VELOCITY,INTERVAL_X_VELOCITY):
        for yVel in range(LOW_INITIAL_Y_VELOCITY,HIGH_INITIAL_Y_VELOCITY,INTERVAL_Y_VELOCITY):
            space=Space.Space(TIME_INTERVAL,ENERGY_OUT_FILE) 
                #Generate new space object with unchanging initial conditions and add planets to it
            space.addFromFile(PLANET_DATA) 

            #Add the new probe whose launch parameters are to be tested
            space.launchFromSurface(PROBE_NAME,LAUNCH_NAME,launchPosAngle,\
                                    PROBE_MASS,PROBE_RADIUS,xVel,yVel)

            #Write experimental parameters to file and get the closest position to target
            f.write(str(launchPosAngle)+","+\
                    str(xVel)+","+\
                    str(yVel)+","+
                    str(getClosestPos(space,TIME_TO_SIM))+"\n")  

  

def getClosestPos(space,timeToSim):
    """
    Simple runner that runs to a specific time or until the probe has collided with something 
    (afterwhich non reliable data can be collected) and reports the closest distance to the target 
    that was reached.
    """
    probe = space.getBody(PROBE_NAME)
    target = space.getBody(TARGET_NAME)
    closestPos = probe.calcDistanceBetween(target.getPos()) 

    
    while(space.getTime() < timeToSim and probe.checkCollided() == False): 
    # IF over given time to simulate or has collided with an object then stop gathering data for 
    # current launch parameter otherwise keep going and check that this position is not closer to 
    # the target than before  
      
        space.simulateInterval()                                          
        probe = space.getBody(PROBE_NAME)
        target = space.getBody(TARGET_NAME)
        closestPos = updateClosestPos(closestPos,probe,target)
    return closestPos
        
def updateClosestPos(currentClosest,probe,mars):
    """
    If current position of probe is closer than the recorded closest position, update the closest
    position with the current position
    """
    distance = probe.calcDistanceBetween(mars.getPos())
    if(distance<currentClosest):
        return distance
    else:
        return currentClosest
            

iterateOverLaunchParameters() #Actual call to do experiment
