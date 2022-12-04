from collections import *
import board

"""
Shows attributes of car, where it can move
and its coordinates
"""


class Car:
    """
    Attributes of car: name, position, length, orientation, and fuel level
    """

    def __init__(self, name, x, y, length, orientation, fuel):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation
        self.fuel = fuel

    def __repr__(self):
        if self.orientation == 0:
            rep = 'Car(' + self.name + ', (' + str(self.x) + ', ' + str(self.y) \
                  + '), ' + str(self.length) + ', ' + "Horizontal" + ', ' + str(self.fuel) +  ')'
        else:
            rep = 'Car(' + self.name + ', (' + str(self.x) + ', ' + str(self.y) \
                  + '), ' + str(self.length) + ', ' + "Vertical" + ', ' + str(self.fuel) +  ')'

        return rep
    
    def __eq__(self, other):
        return (self.x, self.y, self.name, self.fuel,self.orientation) == (other.x, other.y, self.name,self.fuel,self.orientation)
    
    # name getter
    def name(self):
        return self.name

    # length getter
    def length(self):
        return self.length

    # orientation getter
    def orientation(self):
        return self.orientation

    # fuel_level getter
    def fuel(self):
        return self.fuel

    # x coord getter
    def x(self):
        return self.x

    # y coord getter
    def y(self):
        return self.y

    # Need to add validation() method
    def move(self, distance, direction):
        """
        If valid, Moves car to the given distance parameter, in particular direction
        """
        x, y = self.x, self.y # get the coord's
        if direction == "up":
            x = x - distance
        elif direction == "down":
            x = x + distance
        elif direction == "right":
            y = y + distance
        else:
            y = y - distance
        self.x = x    # set the new x
        self.y = y  # set the new y




