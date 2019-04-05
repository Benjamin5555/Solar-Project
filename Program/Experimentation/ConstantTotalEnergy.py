#!/usr/bin/env python3
####################################################################################################
# This is a small script which basically simulates data in a file and plots the energies against   #
# time to show conservation overall and ensure that they are constant                              #
#                                                                                                  #
# Whilst this produces valid results to further provide analysis the txt output alongside          #
# spreadsheet software will be used due to my own experience being better with them than with      #
# MatPlotLib.                                                                                      #
#                                                                                                  #
# Is basically used as a quick test of valid output being produced                                 #
####################################################################################################
import sys
sys.path.append("../SRC")

from Space import Space
from matplotlib import pyplot as plt


PLANET_FILE ="../SRC/PlanetData/innerPlanets.csv"
ENERGY_OUTPUT = "../OUTPUT/CONSTANT ENERGY Copy SCHEME DATA.txt"
OVERALL_SIM_TIME = 3.154e+7
TIME_INTERVAL = 3600 
FILE_NAME = "../OUTPUT/CONSTANtENERGyTestOutputEnergies.png"

def getData():
    global testSpace,gPE,kE,tE,time
    #Setup stores for grav potential energy, Kinetic energy, total energy and time 
    # (not most efficient way of adding time to the graph and addmitedly it probably would have been
    # a better idea to read all of this from the produced file anyway rather than storing it)
    gPE = []
    kE = []
    tE = []


    time = []
    while testSpace.getTime()<=OVERALL_SIM_TIME:
        #Simulate until time period over
        testSpace.simulateInterval()
        gPE.append(testSpace.getSystemGPE())
        kE.append(testSpace.getSystemKineticEnergy())
        tE.append(testSpace.getTotalEnergy())
        time.append(testSpace.getTime())
        

def plotData(time,gPE,kE,tE):
    #Gets matplotlib to graph the produced data
    global testSpace
    
    plt.scatter(time,gPE,label = "Gravitational Potential")
    plt.scatter(time,kE,label = "Kinetic")
    plt.scatter(time,tE, label = "Total")
    plt.xlabel("Time /s")
    plt.ylabel("Energy /J")
    plt.legend()
    plt.savefig(FILE_NAME)


def main():
    global testSpace ,gPE,kE,tE,time
    testSpace = Space(TIME_INTERVAL,ENERGY_OUTPUT)
    testSpace.addFromFile(PLANET_FILE)
    getData()
    plotData(time,gPE,kE,tE)

main()


