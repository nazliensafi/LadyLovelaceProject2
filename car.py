from collections import *
from board import *

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

    def __repr__ (self):
        if self.orientation == 0:
            rep = 'Car(' + self.name + ', (' + str(self.x) + ', ' + str(self.y) \
                  + '), ' + str(self.length) + ', ' + "Horizontal" + ', ' + str(self.fuel) +  ')'
        else:
            rep = 'Car(' + self.name + ', (' + str(self.x) + ', ' + str(self.y) \
              + '), ' + str(self.length) + ', ' + "Vertical" + ', ' + str(self.fuel) +  ')'

        return rep



    # Need to add validation() method    
    def move(self, distance, direction):
        """
        If valid, Moves car to the given distance parameter, in particular direction
        """
        x, y = self.x, self.y #get the coord's
        if direction == "up":
            x = x - distance
        elif direction == "down":
            x = x + distance
        elif direction == "right":
            y = y + distance
        else:
            y = y - distance
        self.x = x    #set the new x
        self.y = y  #set the new y
    
    # levels of the search tree:
    # root of the search is the first state of the board (original 2D array)
    # 1st level: the car heads that can move
    # 2nd level: possible moves of each car

    def is_blocked(self):
        """

        :return: true if the calling car is not blocked on both sides by either cars or walls
        """

    # Reminder: x goes from 0 to 5, starting from the left
    #           y goes from 0 to 5, starting from the top
    #           e.g. 1st position on the grid ia [0][0] on the top left
    #           2nd position on the grid ia [5][5] on the bottom right
    def explore_moves(self, board):
        """
        given a car head checks if it can how many different moves are possible
        :return: (car_name, distance, direction) in a list of possible moves
        """
        if self.orientation == 0: # horizontal cars
            print()
            # check if it can move to the right and by how many positions
            if self.y + self.length != 5 and isinstance(board[self.x][self.y + self.length + 1], 'NoneType'):
                # check if it can move to the left and by how many positions
                print()
        elif self.orientation == 1: # vertical cars
            print()
            # check if it can move up and by how many positions
            # check if it can move down and by how many positions

        possible_moves =[]
        return possible_moves


    def goal(self):
        """

        :return: True if the A car's tail is at poaition [2][5]
        """
        if self.name == 'A' and self.x == 2 and self.y + self.length == 5:
            return True
