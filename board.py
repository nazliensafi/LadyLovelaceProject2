"""
This module implements 'board' class.
"""
import numpy as np
from car import Car
class Board(object):
    """Setting up the playing board

    Attributes:
        cars: list of cars on the play board
        size: size of the board
    """
    #
    # def __init__(self, cars, width=6, height=6):
    #     """
    #     initializes a board boardObject with width and height 6
    #     """
    #     self.size = {'x': height, 'y': width}
    #     self.cars = cars
    #
    # def print_board(boardString):
    #     """
    #     Prints board to output in 2D array
    #     """
    #
    #     string=""
    #     if len(boardString) == 36:
    #         for i in range(0, len(boardString), 6):
    #             string+=boardString[i: i + 6]
    #             string+="\n"
    #     else:
    #         new_str = str[0:35]
    #         for i in range(0, len(new_str), 6):
    #             string+=boardString[i: i + 6]
    #             string+="\n"
    #     return string

    def create_grid(boardString):
        """
        return 2D array of the board
        """
        boardAsList = list(boardString)
        grid = [boardAsList[j:j + 6] for j in range(0, len(boardAsList), 6)]
        return grid
    
    def valid_moves(boardString):
        """
        returns a list of possible moves, their new position, new fuel
        eg, [[B, up, (0,1), 100], [C, down, (3,2), 30]]
        """


def readfile(input_file):
    """ Reads an input file (where each line contains a puzzle, a comment started by a #, or an empty line)
        skips empty lines and lines and comments
        stores each puzzle in a list called puzzles_list
        then stores each puzzle from the list in a 6 by 6 2D array
    """
    input_file = open('input.txt', 'r')
    puzzles_list = list()
    unique_chars = []
    puzzles_array = []
    car_length_dict = {}
    car_orient_dict ={}
    car_fuel_dict = {}

    #extracts puzzles and stores them in puzzles_list
    for line in input_file:
        if line.strip() and line[0]!='#': #if there line is not empty and doesn't start with #
            puzzles_list.append(line)

    input_file.close()

    #make a 2D array for each puzzle found in the input file and initialize car objects
    for puzzle in puzzles_list:
        #print(len(puzzle))
        print("puzzle string: " + puzzle)
        a = np.empty((6, 6), dtype=object)


        #returns a list of string with unique alphabet character representing each car
        car = ''.join(set(puzzle))
        for c in car:
            if c == '.':
                continue
            elif c == '\n':
                continue
            else:
                unique_chars.append(c)

        #collects car lengths in car_length_dict with keys : car chars
        for char in unique_chars:
            car_count = 0
            for k in range(36):
                if char == puzzle[k]:
                    car_count += 1
            if car_count == 0:
                break
            else:
                car_length_dict[char] = car_count

        print("\nCar Length Dictionary: ")
        print(car_length_dict)

        #collects car orientation in car_orint_dict with keys : car chars
        for i in range(35):
            if puzzle[i] == puzzle[i+1]:
                car_orient_dict[puzzle[i]] = 0
            else:
                car_orient_dict[puzzle[i+1]] = 1

        del car_orient_dict['.']
        print("\nCar Orientation Dictionary: ")
        print(car_orient_dict)

        #returns a dictionary called car_fuel_dict containing char representing cars and int representing fuel level
        #if the original puzzle does not contain specification of initial fuel_level
        if len(puzzle) == 36:
            for c in puzzle:
                car_fuel_dict[c] = 100

        if len(puzzle)>36:
            # the fuel-level specification is separated by a space
            new_str = puzzle[37:]
            cars = puzzle[:35]
            for i in range(0, len(new_str), 3):
                if new_str[i] in cars:
                    car_fuel_dict[new_str[i]] = int(new_str[i+1])
            # for cars without fuel-level specification, add 100
            for c in cars:
                if c in car_fuel_dict.keys():
                    continue
                else:
                    car_fuel_dict[c] = 100

        del car_fuel_dict['.']
        print("\nCar Fuel Dictionary: ")
        print(car_fuel_dict)

        print("puzzle in 2D")

        #instantiate Car objects in a 6 by 6 2D array of Cars
        #create car_coord_dict
        k=0
        chars = []
        car_coord_dict = {}
        for a_row in range(6):
            for a_col in range(6):
                if puzzle[k] == ".":
                    print(".", end =" ")
                else:
                    car = Car.__new__(Car) #create an empty Car object
                    car.name = puzzle[k] #set the car name
                    car.length = car_length_dict.get(puzzle[k]) #set the car length
                    car.orientation = car_orient_dict.get(puzzle[k]) #set the car orientation
                    car.fuel = car_fuel_dict.get(puzzle[k]) #set the car fuel
                    a[a_row][a_col] = car
                    if puzzle[k] not in chars:
                        car.x, car.y = a_row, a_col
                        car_coord_dict[puzzle[k]] = (str(a_row), str(a_col))
                        chars += puzzle[k]
                    print(a[a_row][a_col].name,   end =" ")
                k += 1
            print("\n")

        print("\nCar Coordinate Dictionary: ")
        print(car_coord_dict)

        # Uncomment to check if the Car objects are properly instantiated
        # for a_row in range(6):
        #     for a_col in range(6):
        #          if isinstance(a[a_row][a_col], Car) and isinstance(a[a_row][a_col].x, int):
        #              print(a[a_row][a_col])
        print(type(a[0][5]))
        puzzles_array.append(a)

    #list of 2Darrays filled with car objects that represent each puzzle
    return puzzles_array
