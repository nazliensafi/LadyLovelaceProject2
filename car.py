from collections import *
from board import *

"""
Shows attributes of car, where it can move
and its coordinates
"""

Coordinates = namedtuple('Position', 'y x')

class Car():
    """
    Attributes of car: name, position, size, orientation
    """
    def __init__(self, name='_', coord=Coordinates(0,0), size=1, isHorizontal=True):
        self.name = name
        self.coord = coord
        self.size = size
        self.isHorizontal = isHorizontal
        
    def exploreNewPosition(self, distance):
        """
        Car possible position according to available distance
        """
        y, x = self.coord
        if distance > 0:
            y, x = self.end
        if self.isHorizontal:
            x += distance
        else:
            y += distance
        return Coordinates(y, x)
    
    def move(self, distance):
        """
        Moves car to the given distance parameter
        """
        y, x = self.coord
        if self.isHorizontal:
            x += distance
        else:
            y += distance
        self.coord = Coordinates(y, x)
        
    def finalPosition(self):
        """
        Return car's final position
        """
        y, x = self.coord
        if self.isHorizontal:
            x += self.size - 1
        else:
            y += self.size - 1
        return Coordinates(y, x)

    end=property(finalPosition)