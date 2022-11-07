from collections import *
from board import *

"""
Shows attributes of car, where it can move
and its coordinates
"""

Coordinates = namedtuple('Position', 'y x')

class Car():
    """
    Attributes of car: name, position, length, orientation
    """
    def __init__(self, name, coord, length, orientation):
        self.name = name
        self.coord = Coordinates(0,0)
        self.length = 2
        self.orientation = orientation
        
    def move(self, distance, direction):
        """
        If valid, Moves car to the given distance parameter, in particular direction
        """
        y, x = self.coord
        if direction == "up":
            x = x - distance
        elif direction == "down":
            x = x + distance
        elif direction == "right":
            y = y + distance
        else:
            y = y - distance
        self.coord = Coordinates(y, x)
        
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