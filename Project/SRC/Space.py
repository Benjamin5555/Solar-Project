from Body import Body
from Probe import Probe
from Running import Running
import copy
import math
#TODO AUTO CALC TIME INTERVAL (i.e. to be ~1% of the shortest half )
class Space():
    def __init__(self,timeInterval,energyOutputFile="../OUTPUT/EnergyOutput.txt"):
        """
        Object which contains and simulates a collection of bodies motion
        """
        self.__timeInterval = float(timeInterval )#TODO Validation
        self.__bodies = []
        self.__time = 0
        self.__setEnergyOutput(energyOutputFile)

    def simulatePeriodAndTrace(self,period):
        """
        Perhaps data should be space rather than distance to keep time etc data 
        """
        self.__time =0 #Reset the time in case other simulations have occured
        data = []
        notify = Running()
        
        while (self.__time <= period):
            self.simulateInterval(self.__timeInterval)
            data.append(self.copyBodies()) 
        notify.join()
        return data

    def copyBodies(self):
        """
        Provides a new identical list of bodies, that is separate of the self.__bodies list and
        hence will not be changed by/during further simulation.
        
        """
        retList = []
        for body in self.__bodies:
            retList.append(body.copy())
        return retList
 
    def simulateInterval(self,timeInterval = None):
        """
        Simulates a time interval for the space object i.e. simulates the movement of all objects 
        over some time interval which can be given as a parameter or default use the objects 
        timeinterval defined at creation 
        TODO: THERE MAY BE ISSUES WITH THIS HOWEVER THIS CREATES THE EXPECTED BEHAVIOUR as discussed 
        in project report
        """
       
        if(timeInterval == None):
            timeInterval = self.__timeInterval


        for x in self.__bodies:
            
            x.simulate(timeInterval)
        
        self.__time=self.__time+ timeInterval
        self.writeSystemData() 

    def getBodies(self):
        """
        Returns all the bodies being simulated in the space object
        """
        return self.__bodies
    
    def getBody(self,name):
        """
        Returns a body that is associated with the name parameter given
        """
        for body in self.__bodies:
            if(body.getName()==name):
                return body
        ValueError("A body of the given name doesn't exist in this space")
        return None
    
    def getSystemKineticEnergy(self,bodies = None):
        """
        Returns the sum of the gravitational potential energy of all bodies within a system if no
        parameter is passed then uses the space's bodies to calculate
        """
        if (bodies == None):
            bodies = self.__bodies

        kE = 0
        for body in bodies:
            kE =kE+ body.getKineticEnergy()
        return kE

    def getSystemGPE(self,bodies = None):
        """
        Returns the sum of the gravitational potential energy of all bodies within a system if no
        parameter is passed then uses the space's bodies to calculate

        0.5* sum is used as GPE is a 'pair potential' and hence this term will correct the overall
        energy
        """
        if (bodies ==None):
            bodies = self.__bodies
        gPE = 0 
        for body in bodies:
            gPE = gPE +body.getGPE() 
        return gPE*0.5

    def getTotalEnergy(self,bodies = None):
        """
        Returns the sum of all energy of all bodies within a system if no parameter is passed then
        uses the space's bodies to calculate
        """
        if(bodies ==None):
            bodies = self.__bodies
        return self.getSystemGPE(bodies)+self.getSystemKineticEnergy(bodies)
    
    def addBody(self,bodyName,xPosition,yPosition,mass,radius,initialXVelocity,initialYVelocity):
        """
        Adds a body to the space to be simulated ensuring this doesn't cause an error
        """
        try:
            self.__bodies.append(Body(self.__bodies,bodyName,xPosition,yPosition,mass,radius,initialXVelocity,initialYVelocity))
        except ValueError:
            print("Body "+bodyName + "was not added to the system due to one of its parameters being invalid")
            return 

    def launchFromSurface(self,bodyName,launchBodyName,latitude,mass,radius,initialXVelocity,initialYVelocity):
        """
        Latitude should be given in degrees
        Launches a Probe object from the surface
        Angle given is polar coordinate angle for position
        Launches from just above a planet
        """
        latitude=math.radians(latitude)
        launchBody = self.getBody(launchBodyName)
        startPos = self.__calcLaunchPos(radius,launchBody,latitude)
        self.add(Probe(self.__bodies,bodyName,startPos[0],startPos[1],mass,radius,\
                           initialXVelocity+launchBody.getVelocity()[0],\
                           initialYVelocity+launchBody.getVelocity()[1]))
             
    def add(self,bodyToAdd):
        """
        Adds a body or related object to the space
        """
        if(isinstance(bodyToAdd,Body)):
            self.__bodies.append(bodyToAdd)    

    def __calcLaunchPos(self,probeRadius,launchBody,latitude):
        """
        Calculates the position on a body to launch from using the radius of the probe (prevent
        collisions between object being launched and where launched from) , the body object to
        launch from and latitude to launch at
        """
        planetPos = launchBody.getPos()
        
        planetRadius = launchBody.getRadius()
        surfacePos  =   (planetPos[0]+math.cos(latitude)*(planetRadius+probeRadius*1.05),\
                         planetPos[1]+math.sin(latitude)*(planetRadius+probeRadius*1.05))
        return surfacePos

    def addFromFile(self,filepath="PlanetData/innerPlanets.csv"):
        """
        Adds a collection of bodies to the space from a file
        Assumes fully specified file of form:
        (Name,xPos,yPos,Mass,Radius,initial X Velocity,initial Y Velocity)
        """
        file = open(filepath,"r")
        file.readline() #Disregard header 
        for line in file:
            data = line.split(",")
            self.addBody(\
                str(data[0]).strip(),\
                float(data[1]),\
                float(data[2]),\
                float(data[3]),\
                float(data[4]),\
                float(data[5]),\
                float(data[6]),\
            )

    def getTimeInterval(self):
        """
        Returns the time interval that has been used to  simulate
        """
        return self.__timeInterval
        
    def getTime(self):
        """
        Returns the overall time that has been simulated
        """
        return self.__time 

    def __str__(self):
        """
        Provides a string representation of the space object showing all bodies, their speed and
        their positions

        """
        retStr = ""
        for x in self.getBodies():
            retStr += str(x.getName())+"|"+str(x.getPos())+"|"+str(x.getSpeed())+"|"+"\n"
        return retStr

    def writeSystemData(self):
        """
        Writes the energies of the system to a file
        """
        f = open(self.__energyOutputFile,'a')
        f.write(str(self.getTime())+\
            ","+str(self.getTotalEnergy())+\
            ","+str(self.getSystemKineticEnergy())+\
            ","+str(self.getSystemGPE())+"\n")
        f.close()

    def __setEnergyOutput(self, energyOutputFile):
        """
        Sets the file that should be used to output energy information at each iteration and clears 
        it from any previous simulations
        """
        self.__energyOutputFile = energyOutputFile
        
        f = open(self.__energyOutputFile,'w')#Clears data stored in output file 
        f.close()

  
    def getOrbitalPeriodOfBody(self,BodyToDetermineName,moveAwayIntervals=500):
        """
        Calculates the orbital period of a body by determining time take to reach start position
        again  and returns in seconds.

        NOTE: Function may be unreliable due to not realising it needed to be a function until close 
        to deadline.
        TODO: Because there is no stopping condition, planets which are not on a stable orbit will 
        cause an infinite loop
        """

        #Used where this function is called when the simulation time is not at the start
        startTime = self.getTime()  
        
                                   
        #Setup parameters used to determine bodies year
        spaceToTestOn = copy.deepcopy(self) #To prevent losing current state of space
        bodyToDetermine = spaceToTestOn.getBody(BodyToDetermineName)
        
        bodyToDetermineStartPos = bodyToDetermine.getPos() #Record where the body started from

        

        endDistance = self.__getEndConditionForBodyYear(spaceToTestOn,\
                                                        bodyToDetermine,\
                                                        bodyToDetermineStartPos)
        
       
        while(not self.__determineIfPlanetInRangeOfStartPos(bodyToDetermine,bodyToDetermineStartPos,endDistance)):
            #Whilst the current position is not within range of the objects start position, continue simulating
            spaceToTestOn.simulateInterval()

        return spaceToTestOn.getTime() -startTime 
        #Returns testing space's current time corrected for when testing began

    def __getEndConditionForBodyYear(self,spaceToTestOn,bodyToDetermine,bodyToDetermineStartPos):
        """
        Calculates the end condition for determining a year for a given body, this value is the
         distance between the object and its start position to determine when a year is completed,
        where the distance to start considered completed  is 45% of the distance between intervals
         used because this was found to work for small and large orbits (Tested with Phobos around
        Mars and Earth around the sun)
        """
        spaceToTestOn.simulateInterval()

        return bodyToDetermine.calcDistanceBetween(bodyToDetermineStartPos)*0.45


    def __determineIfPlanetInRangeOfStartPos(self,bodyToDetermine,bodyToDetermineStartPos,endDistance):
        """
        Determine if a planet is within a range of its start position with a 100% tolerance to allow
        for slight variations in orbit and issues due to time intervals meaning it may never be at 
        start position again
        """
        return (bodyToDetermine.calcDistanceBetween(bodyToDetermineStartPos)<=endDistance)
            


