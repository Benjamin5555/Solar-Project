class Path():
    def __init__(self,xPos,yPos,radius=50,color='r',name=""):
        """
        Class providing a structure to store a data set and store the path taken by a body in (a) space (object)
        """
        self.xPositions = [xPos]
        self.yPositions = [yPos]
        self.size = radius/100
        self.color = color
        self.name = name

    def update(self,xPos,yPos):
        """
        Updates the path taken by an body, (i.e. adds a x and y position to the list of items)
        """
        self.xPositions.append(xPos)
        self.yPositions.append(yPos)
    
    def getXData(self):
        """
        Returns a list of data that is related to the x positions taken by the body along its path
        """
        return self.xPositions

    def getYData(self):
        """
        Returns a list of data that is related to the x positions taken by the body along its path
        """
        return self.yPositions
    
    def getPosData(self):
        """
        Returns a tuples of lists data that is related to the (x,y) positions taken
        by the body along its path
        """
        return (self.xPositions, self.yPositions)

    def getColor(self):
        """
        Returns the color used to represent the path in the animation graphic
        """
        return self.color
 
    def getSize(self):
        """
        Returns the size used to represent each data point on the path
        :return:
        """
        return self.size