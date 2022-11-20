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

    # DEVELOPER THOUGHTS
    # levels of the search tree:
    # root of the search is the first state of the board (original 2D array)
    # 1st level: the car heads that can move
    # 2nd level: possible moves of each car

    def explore_moves(self, board):
        """
        given a board of car objects, checks how many different moves are possible
        e.g.
        move 1: B left 1 and the respective board
        move 2: B left 2 and the respective board
        move 3: C up 1 and the respective board
        :return:  list of boards and the move that made it different from the parent board
        """
        cars = board.cars
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

    # def goal(self):
    #     """
    #     :return: True if the A car's tail is at poaition [2][5]
    #     """
    #     if self.name == 'A' and self.x == 2 and self.y + self.length == 5:
    #         return True
