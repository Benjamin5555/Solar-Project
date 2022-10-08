import unittest
import sys
# sys.path.append("../src")

from src.AnimateSpace import AnimateSpace
from src.Space import Space
from math import isclose, log10,floor


class test_space(unittest.TestCase):

    def __setupEnvironment(self):
        TIME_INTERVAL = 10000
        PLANET_DATA_FILE = "Program/src/PlanetData/innerPlanets.csv"
        space =Space(TIME_INTERVAL,"/dev/null") 
        space.addFromFile(PLANET_DATA_FILE)
        return space, TIME_INTERVAL

    def test_systemEnergyConservation(self):
        space,TIME_INTERVAL = self.__setupEnvironment()
        initEnergyOrderOfMagnitude = floor(log10(abs(space.getTotalEnergy())))
        space.simulateInterval()        
        assert initEnergyOrderOfMagnitude==floor(log10(abs(space.getTotalEnergy())))
        
    # def test_simulatePeriodAndTrace(self,period):
    def test_copyBodies(self):
        space,TIME_INTERVAL = self.__setupEnvironment()
        bodies_copy =space.copyBodies()
        assert not id(bodies_copy)==id(space.getBodies())
        foundMatch = True
        for body in space.getBodies():
            for body_copy in bodies_copy:
                if(body==body_copy):
                    foundMatch = True
                    break
            if(not foundMatch): #if no match found, break and assert false
                break        
        assert foundMatch

 
    # def test_simulateInterval(self,timeInterval = None):
    
    def test_getBodies(self):
        space,TIME_INTERVAL = self.__setupEnvironment()
        assert space.getBody("Sun").getName()=="Sun"
        assert space.getBody("MERCURY").getName()=="MERCURY"
        assert space.getBody("VENUS").getName()=="VENUS"
        assert space.getBody("EARTH").getName()=="EARTH"
        assert space.getBody("MARS").getName()=="MARS"

    def test_getBody(self):
        space,TIME_INTERVAL = self.__setupEnvironment()
        bodies = space.getBodies()
        foundMatch = False
        names = ["Sun","MERCURY","VENUS","EARTH","MARS"]
        for body in bodies:
            for name in names:
                if(body.getName()==name):
                    foundMatch = True
                    break
            if(not foundMatch): #if no match found, break and assert false
                break        
        assert foundMatch


    def test_getSystemKineticEnergy(self,bodies = None):
        space,TIME_INTERVAL = self.__setupEnvironment()
        bodies = space.getBodies()
        KE = 0
        for body in bodies:
            KE = KE + body.getKineticEnergy()
        assert KE == space.getSystemKineticEnergy()

        
    def test_getSystemGPE(self,bodies = None):
        TIME_INTERVAL = 10000
        PLANET_DATA_FILE = "Program/src/PlanetData/innerPlanets.csv"
        space =Space(TIME_INTERVAL,"/dev/null") 
        
        space.addFromFile(PLANET_DATA_FILE)
        space.simulateInterval()
        bodies = space.getBodies()
        GPE = 0 
        for body in bodies:
            GPE = GPE + 0.5*body.getGPE()
        assert GPE == space.getSystemGPE()

    def test_getTotalEnergy(self,bodies = None):
        space,TIME_INTERVAL = self.__setupEnvironment()
        bodies = space.getBodies()
        GPE = 0
        KE = 0 
        for body in bodies:
            GPE = GPE + 0.5*body.getGPE()
            KE = KE + body.getKineticEnergy()
        assert KE+GPE == space.getTotalEnergy()

    def test_addBody(self):
        space,TIME_INTERVAL = self.__setupEnvironment()
        space.addBody("PlanetX",50,-100,5000,20,1e3,1e1)
        testBody = space.getBody("PlanetX")
        assert testBody.getName() =="PlanetX"
        assert testBody.getPos()[0]==50
        assert testBody.getPos()[1]==-100
        assert testBody.getMass()==5000
        assert testBody.getRadius() == 20
        assert testBody.getVelocity()[0] == 1e3
        assert testBody.getVelocity()[1] == 1e1

    # def test_launchFromSurface(self,bodyName,launchBodyName,latitude,\
    # def test_add(self,bodyToAdd):
    # def test___calcLaunchPos(self,probeRadius,launchBody,latitude):
    # def test_addFromFile(self,filepath="PlanetData/innerPlanets.csv"):
    # def test_getTimeInterval(self):
    # def test_getTime(self):
    # def test___str__(self):
    # def test_writeSystemData(self):
    # def test___setEnergyOutput(self, energyOutputFile):
    def test_getOrbitalPeriodOfBody(self):
        TIME_INTERVAL = 10000
        YEAR_IN_SECONDS = 3.154e7
        THRESHOLD=1e6
        PLANET_DATA_FILE = "Program/src/PlanetData/innerPlanets.csv"
        PLANET_YEAR_TO_GET = "EARTH"
        space =Space(TIME_INTERVAL,"/dev/null") 
        space.addFromFile(PLANET_DATA_FILE)
        orbit_period = space.getOrbitalPeriodOfBody(PLANET_YEAR_TO_GET)
        assert (isclose(orbit_period,YEAR_IN_SECONDS,abs_tol=THRESHOLD))
    # def test___getEndConditionForBodyYear(self,spaceToTestOn,bodyToDetermine,bodyToDetermineStartPos):
    # def test___determineIfPlanetInRangeOfStartPos(self,bodyToDetermine,bodyToDetermineStartPos,endDistance):