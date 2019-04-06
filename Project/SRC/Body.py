import math

GravConst = 6.67408E-11  

class Body():
    def __init__(self,bodies,name,x,y,mass,radius,vx=0,vy=0):
        """
        Class to represent a body in space and its interaction with other objects in this space
        """
        self._pos = (x,y)
        self._name = name
        self._velocity = (vx,vy)
        self._mass = mass
        self._bodies = bodies
        self._radius = radius
        self._acceleration  = self.calcAccOnBody()
        self._collided = False

    def simulate(self,timeInterval=0.5):
        """
        Simulates the motion of the body over an time interval
        """
        stepForwardAccel = self.calcAccOnBody()
        #Becomes the next value of acceleration from the acceleration property stored in the body
        # i.e. a(t-1) = self.acceleration , a(t) = stepForwardAcceleration
        self.calcNewPosition(timeInterval,stepForwardAccel)
        self.calcNewVelocity(timeInterval,stepForwardAccel)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Main Calculations used to define simulation behaviour
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    def calcNewPosition(self,timeInterval,stepForwardAccel):
        """
        Calculates the position of the object from its old position over a given time interval
        """
        beemanTerms = self.__beemanPosTerm(timeInterval,stepForwardAccel)

        self._pos =    (self._pos[0]+self._velocity[0]*timeInterval+beemanTerms[0],\
                         self._pos[1]+self._velocity[1]*timeInterval+beemanTerms[1])
        
    def __beemanPosTerm(self,timeInterval,stepForwardAccel):
        """
        Helper function to improve clarity of the calcNewPosition method and break down the Beeman 
        integration method
        """
        return ((1/6)*(4*stepForwardAccel[0]-self._acceleration[0])*(timeInterval**2),\
                (1/6)*(4*stepForwardAccel[1]-self._acceleration[1])*(timeInterval**2))

    def calcNewVelocity(self,timeInterval,stepForwardAccel):
        """
        Calculates the velocity of the object from its old velocity given a time interval
        """
        beemanTerm = self.__beemanVelTerm(timeInterval,stepForwardAccel)

        self._velocity = (self._velocity[0]+ beemanTerm[0],\
                           self._velocity[1]+ beemanTerm[1])

    def __beemanVelTerm(self,timeInterval,stepForwardAccel):
        """
        Helper function to improve clarity of the calcNewVelocity method and break down the Beeman
         integration method
        as well as handling the updating of acceleration variables
        """
        stepBackAccel = self._acceleration      #= a(t-1)
        self._acceleration = stepForwardAccel   #= a(t)
        stepForwardAccel = self.calcAccOnBody() #= a(t+1)

        return (1/6*(2*stepForwardAccel[0]+5*self._acceleration[0]-stepBackAccel[0])*timeInterval,\
                1/6*(2*stepForwardAccel[1]+5*self._acceleration[1]-stepBackAccel[1])*timeInterval)

    def calcNewPositionE(self,timeInterval):
        """
        Calculates the position of the object from its old position over a given time interval
        """
        self._pos =  (self._pos[0]+self._velocity[0]*timeInterval,\
                self._pos[1]+self._velocity[1]*timeInterval)
        
    def calcNewVelocityE(self,timeInterval):
        """
        Calculates the velocity of the object from its old velocity given a time interval
        """
        intAccel = self.calcAccOnBody()
        
        self._velocity = (self._velocity[0]+ (intAccel[0])*timeInterval,\
                           self._velocity[1]+ (intAccel[1])*timeInterval)

    def calcAccOnBody(self):
        """
        Returns the magnitude of acceleration acting on the body due to other bodies in the space
        it occupies
        """
        forceV = self.calcForceonBody()
        return (forceV[0]/self._mass,forceV[1]/self._mass)

    def calcForceonBody(self):
        """
        Calculates and returns the magnitude of acceleration acting on the body due to all other 
        bodies in the space it occupies
        """
        totForceX = 0
        totForceY = 0
        for body in self._bodies:
            if(self == body): #Check valid to calculate on 
                continue
            if(self.calcDistanceBetween(body.getPos())<=self._radius+body.getRadius()):
                #If this body, or the other body has been involved in a collision then they cannot 
                # be reliably simulated and hence should not be whilst this is true and marked that 
                # this has occured for the future
                self._collided = True
                continue

            forceTotal = self.calcMagOfForceFromBody(body) 
            theta = self.calculateAngleFromX(body)            
            forceX = forceTotal*math.cos(theta)
            forceY = forceTotal*math.sin(theta)

            totForceX += forceX
            totForceY += forceY
        return (totForceX,totForceY)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Caclulations helper functions to simplify overall code
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def calcMagOfForceFromBody(self,body):
        """
        Returns the overall force acting on the object
        """
      
        return -1*(GravConst*self._mass*body.getMass())/(self.calcDistanceBetween(body.getPos())**2)

    def calculateAngleFromX(self,body):
        """
        Calculates the angle between the force acting on the body and the x axis so that force can
        be broken into components
        """
        return math.atan2(self.calcYdisplacment(body.getPos()[1]),\
                          self.calcXdisplacment(body.getPos()[0]))

    def calcDistanceBetween(self,pointPos):
        """
        Calculates the distance between this object and a given point
        """
        return math.sqrt((self._pos[0]-pointPos[0])**2+(self._pos[1]-pointPos[1])**2)
        
    def calcXdisplacment(self,x):
        """
        Calculates displacment in x between this object and a position along the x axis
        """
        return self._pos[0] - x

    def calcYdisplacment(self,y):
        """
        Calculates displacment in y between this object and a position along the y axis
        """
        return self._pos[1] - y
    
    def getSpeed(self):
        """
        Calculates the overall speed of the body
        """
        return math.sqrt((self._velocity[0]**2+self._velocity[1]**2))

    def getKineticEnergy(self):
        return 0.5* self._mass *abs(self.getSpeed())**2 

    def getGPE(self):
        """
        Uses existing force magnitude calculation to determine the GPE on a body
        TODO Would maybe be more efficient to have a method for GPE being used by both rather than 
        the force equation used for both (Adds a multiply then divied step that could be removed for
        GPE calculation)
        """ 
        totalGPE = 0 
        for body in self._bodies:
            if(self == body or\
               self.calcDistanceBetween(body.getPos())<=self._radius+body.getRadius()): 
                #Check valid to calculate on 
                continue
            else:
                totalGPE = totalGPE +self.calcMagOfForceFromBody(body) \
                           * self.calcDistanceBetween(body.getPos()) 
                           # Uses that F = U/r where r is distance between so F*r = U  
        return totalGPE

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Various getters and setters used to control input
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def __str__(self):
        """
        Returns information about the body when string required
        """
        return self._name  +"||Pos :"+ str(self._pos)+"||Vel :"+str(self._velocity)
    

    def copy(self):
        return Body(self._bodies,\
                self._name,\
                self._pos[0],\
                self._pos[1],\
                self._mass,\
                self._radius,\
                self._velocity[0],\
                self._velocity[1])


    def __eq__(self, other):
        """
        Provides proper equivalence checking
        """
        if isinstance(other, self.__class__):
            return self._name == other._name
        else:
            return False

    def __ne__(self, other):
        """
        Provides proper equivalence checking
        """
        return not self.__eq__(other)

    def getMass(self):
        """
        Returns bodies mass
        """
        return self._mass

    def getPos(self):
        """
        Returns objects x,y position within its space object
        """
        return self._pos

    def getVelocity(self):
        """
        Returns a tuple representing the bodies velocity at a certain point in time
        """
        return self._velocity

    def getRadius(self):
        """
        Returns the objects radius
        """
        return self._radius

    def getName(self):
        return self._name
   
    def checkCollided(self):
        """
        Checks if a body has collided with (any) other at the current iteration 
        """
        return self._collided

