from src.Space import Space
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches
from src.Path import Path
from random import random


class AnimateSpace():
    def __init__(self,space,data = None,timeInterval =None):
        """
        Object will simulate and animate for a collection of bodies for a given space object.
        For each body it will plot position and also plot the position on a scatter plot which acts
        to show the path taken.
        """
        self.space = space
        if (timeInterval == None):
            self.timeInterval = self.space.getTimeInterval()
        else:
            self.timeInterval = timeInterval
        
        self.__bodies = self.space.getBodies()

        self.__setupAnimator()
        


    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Functions related to setting up and starting (i.e. calling matplotlibs funcAnimate)
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def __setupAnimator(self):
        """
        Sets up figure that will be made animated i.e. labels and objects that will be used
        """
        self.fig = plt.figure()
        self.ax  = plt.axes()
        self.ax.set_xlabel('x \m')
        self.ax.set_ylabel('y \m')
        self.__setupBodyGraphics()
    

    
    def liveSim(self):
        """
        Runs matplotlibs animation function for the space animation 
        """
        anim =FuncAnimation(self.fig, self.__animateLive, interval= 1)
        plt.show()


    def saveExistingDataAnimation(self,data,name = "../OUTPUT/output.mp4"):
        """
        When given a set (list) of already produced data about the bodies in a space over the whole
        simulation, will save an animated graphic representing the space over time
        """
        self.dataSet = data
        anim =FuncAnimation(self.fig,self.__animateData,interval= 100,frames = len(self.dataSet))
        anim.save(name,writer='ffmpeg')

    def animateExistingData(self,data):
        """
        When given a set (list) of already produced data about the bodies in a space over the whole 
        simulation, will display an animated graphic representing the space over time
        """
        self.dataSet = data
        anim =FuncAnimation(self.fig,self.__animateData,interval= 1,frames = len(self.dataSet),repeat = True)
        plt.show()


    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Functions related to generation of each frame of the animation i.e. animate which will be run 
    by funcAnimate to produce a frame. 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    def __animateData(self,i):
        """
        Provides the iterative animate function when animating a dataset by setting the 
        self.__bodies property to the dataset at the animation index (i) which will become a frame 
        of the final animation
        """
        self.__bodies = self.dataSet[i]
        self.__updateAxes()


    def __animateLive(self, i):
        """
        Method run to generate each frame of the matplotlib animation 
        """
        self.space.simulateInterval()
        print(self.space.getSystemGPE(),self.space.getSystemKineticEnergy())
        return self.__updateAxes()
 

    def __setupBodyGraphics(self):
            """
            Sets up the various graphics that will represent bodies used in the function
            Uses a patches circle to represent each planet, each is given a random colour
            """
            self.bodyGraphics = []
            self.paths = []
            for body in self.__bodies :
                color = (random()*1,random()*1,random()*1) #Gets a random colour for each body 
                self.bodyGraphics.append(patches.Circle(body.getPos(),body.getRadius(),\
                                                        label=body.getName(),color = color))
                self.ax.add_patch(self.bodyGraphics[-1])
                self.paths.append(Path(body.getPos()[0],body.getPos()[1],\
                                       self.bodyGraphics[-1].get_linewidth(),color))

                
    def __updateAxes(self):
            """
            Method which updates the axes and plotted data on the graph for each animated frame
            For each body goes through and updates the patches position, also plots the position 
            on a scatter which acts to show the path taken

            TODO Potentially could have added a time output to the figure however this would only 
            work with live sim and as such has not been implemented, would be done by adding 
            self.__timeText.set_text("T = "+str()) within the for loop
            """
            self.ax.clear()

            for i in range(len(self.bodyGraphics)):
                bodyNewPos = self.__bodies[i].getPos()
                self.bodyGraphics[i].center = bodyNewPos[0],bodyNewPos[1]
                self.ax.add_patch(self.bodyGraphics[i])
                self.paths[i].update(bodyNewPos[0],bodyNewPos[1])

                self.ax.scatter(self.paths[i].getXData(),\
                                self.paths[i].getYData(),\
                                c=[[self.paths[i].getColor()[0],\
                                    self.paths[i].getColor()[1],\
                                    self.paths[i].getColor()[2]]],\
                                s=self.paths[i].getSize())  
                            #The unpacking of the tuple into 1*1 2D array was required by matplotlib 
                            #to add a colour unlike for a patch which just accepts a tuple
            self.ax.legend()




    

                      
