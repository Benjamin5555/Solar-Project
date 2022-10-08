from src.Body import Body

class Probe(Body):
    def __init__(self, bodies, name, x, y, mass, radius, vx=0, vy=0):
        """
        Class Providing the functionality of a body however with additional functionality that
        maybe required of a manmade space probe/object


        """
        super().__init__(bodies, name, x, y, mass, radius, vx=vx, vy=vy)

    
    def isInRange(self,body,distance):
        """
        Determines if a body is close by to a target to within a specified distance
        """
        return (self.calcDistanceBetween(body.getPos())<=distance)

    def copy(self):
        """
        Copies the probe object to create a new separate but equivalent object
        """
        return Probe(self._bodies, self._name, self._pos[0], self._pos[1],\
                     self._mass, self._radius, self._velocity[0], self._velocity[1])





    def __eq__(self, other):
        """
        Ensures that equivalences are properly performed i.e. two objects are considered the same if
        they are same type and have same name
        """
        if isinstance(other, self.__class__):
            return self._name == other._name
        else:
            return False

    def __ne__(self, other):
        """
        Ensures that equivalences are properly performed
        """
        return not self.__eq__(other)
