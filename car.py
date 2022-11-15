from collections import *
from board import *

"""
Shows attributes of car, where it can move
and its coordinates
"""

#Coordinates = namedtuple('Position', 'y x')

class Car:
    """
    Attributes of car: name, position, length, orientation, and fuel level
    """
    # def __init__(self, **kwargs):
    #     for key, value in kwargs.items():
    #         if key == "name":
    #             self.name = value
    #         elif key == "x":
    #             self.x = value
    #         elif key == "y":
    #             self.y = value
    #         elif key == "length":
    #             self.length = value
    #         elif key == "_orientation":
    #             self.orientation = value # 0 for horizontal, 1 for vertical
    #         elif key == "fuel":
    #             self.fuel = value

    def __init__(self, name, x, y, length, orientation, fuel):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation
        self.fuel = fuel

    # def __repr__ (self):
    #     # if self._orientation == 0:
    #     #     orientation = "Horizontal"
    #     # else:
    #     #     orientation = "Vertical"
    #     #
    #     # rep = 'Car(' + self._name + ',' + str(self._x) + ',' + str(self._y) \
    #     #       + ',' + str(self._length) + ',' + orientation + ',' + str(self._fuel) +  ')'
    #     rep = 'Car(' + str(self.name) + ')'
    #     return rep

    #GETTERS:

    #name getter
    def name(self):
        return self._name

    #coord getter
    def coord(self):
        return self._coord

    #length getter
    def length(self):
        return self._length

    #orientation getter
    def orientation(self):
        return self._orientation

    #fuel_level getter
    def fuel(self):
        return self._fuel

    #x coord getter
    def x(self):
        return self._x
    #y coord getter
    def y(self):
        return self._y



    # Need to add validation() method    
    def move(self, distance, direction):
        """
        If valid, Moves car to the given distance parameter, in particular direction
        """
        x, y = self._coord.get("x"), self._coord.get("y") #get the coord's
        if direction == "up":
            x = x - distance
        elif direction == "down":
            x = x + distance
        elif direction == "right":
            y = y + distance
        else:
            y = y - distance
        self.coord(x, y)    #set the new coord's
    
    
    # def exploreNewPosition(self, distance):
    #     """
    #     Car possible position according to available distance
    #     """
    #     y, x = self.coord
    #     if distance > 0:
    #         y, x = self.end
    #     if self.isHorizontal:
    #         x += distance
    #     else:
    #         y += distance
    #     return Coordinates(y, x)
    #
    # def finalPosition(self):
    #     """
    #     Return car's final position
    #     """
    #     y, x = self.coord
    #     if self.isHorizontal:
    #         x += self.size - 1
    #     else:
    #         y += self.size - 1
    #     return Coordinates(y, x)
    #
    # end=property(finalPosition)