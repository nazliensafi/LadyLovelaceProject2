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

    def __init__(self, cars, width=6, height=6):
        """
        initializes a board boardObject with width and height 6
        """
        self.size = {'x': height, 'y': width}
        self.cars = cars

    def print_board(boardString):
        """ 
        Prints board to output in 2D array 
        """

        string=""
        if len(boardString) == 36:
            for i in range(0, len(boardString), 6):
                string+=boardString[i: i + 6]
                string+="\n"
        else: 
            new_str = str[0:35]
            for i in range(0, len(new_str), 6):
                string+=boardString[i: i + 6]
                string+="\n"
        return string
    
    def car_list(str):
        """ 
        returns a list of string with unique alphabet character representing each car
        """

        res = []
        car = ''.join(set(str))

        for c in car:
            if c == '.':
                continue
            elif c == '\n':
                continue
            else:
                res.append(c)

        return res
    
    # def fuel_level(boardString):
    #     """
    #     returns a list containing char representing cars and int representing fuel level
    #     """
    #     car_fuel = []
    #
    #     # if the original line does not contain specification of initial fuel_level
    #     if len(boardString) == 36:
    #         cars = Board.car_list(boardString)
    #         for c in cars:
    #             car_fuel.append(c+":"+str(100))
    #
    #     if len(boardString)>36:
    #         # the fuel-level specification is separated by a space
    #         new_str = boardString[37:]
    #         cars = Board.car_list(boardString[:35])
    #         for i in range(0, len(new_str), 3):
    #             if new_str[i] in cars:
    #                 car_fuel.append(new_str[i]+":"+ new_str[i+1])
    #
    #         # for cars without fuel-level specification, add 100
    #         for c in cars:
    #             if c in car_fuel:
    #                 continue
    #             else:
    #                 car_fuel.append(c+":"+str(100))
    #     return car_fuel

        """
        CREATE 2D ARRAY BOARD
        LIST OF VALID MOVES FUNCTION
        """

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

        # def get_coord(row_idx):
        #     def result((col_idx, value)):
        #         return (value, {'y': row_idx, 'x': col_idx})
        #     return result
        #
        # def flatten(l):
        #     return [item for sublist in l for item in sublist]
        #
        # puzzle_file = open(filename, 'r')
        # raw_board = [list(line.strip()) for line in puzzle_file]
        # coords_board = [map(get_coord(row_idx), enumerate(row))
        #                 for row_idx, row in enumerate(raw_board)]
        # cars_board = flatten([filter(lambda (c, v): c.isalpha(), list(row))
        #                       for row in list(coords_board)])
        # raw_cars = defaultdict(list)
        # for (k, v) in cars_board:
        #     raw_cars[k].append(v)
        # cars = []
        # for i in raw_cars:
        #     cars.append(Car.createFromBoardInfo(i, raw_cars[i]))
        # return Board(cars, len(raw_board), len(raw_board[0]))

    # def explore_moves(self):
    #     """Explore the state space of possible moves for a single car, this also checks whether we bump into a car or a wall"""
    #     board = self.game_board(self.cars)
    #     for car in self.cars:
    #         if car.orientation == Orientation.VERTICAL:
    #             # UP
    #             if car.coord['y'] - 1 >= 0 and board[car.coord['y'] - 1][car.coord['x']] == '.':
    #                 new_cars = deepcopy(self.cars)
    #                 new_car = [x for x in new_cars if x.name == car.name][0]
    #                 new_car.coord['y'] -= 1
    #                 yield [[[car.name, 'up']], Board(new_cars)]
    #             # DOWN
    #             if car.coord['y'] + car.length + 1 <= (self.size['x'] - 1) and board[car.coord['y'] + car.length + 1][car.coord['x']] == '.':
    #                 new_cars = deepcopy(self.cars)
    #                 new_car = [x for x in new_cars if x.name == car.name][0]
    #                 new_car.coord['y'] += 1
    #                 yield [[[car.name, 'down']], Board(new_cars)]
    #         else:
    #             # LEFT
    #             if car.coord['x'] - 1 >= 0 and board[car.coord['y']][car.coord['x'] - 1] == '.':
    #                 new_cars = deepcopy(self.cars)
    #                 new_car = [x for x in new_cars if x.name == car.name][0]
    #                 new_car.coord['x'] -= 1
    #                 yield [[[car.name, 'left']], Board(new_cars)]
    #             # RIGHT
    #             if car.coord['x'] + car.length + 1 <= (self.size['y'] - 1) and board[car.coord['y']][car.coord['x'] + car.length + 1] == '.':
    #                 new_cars = deepcopy(self.cars)
    #                 new_car = [x for x in new_cars if x.name == car.name][0]
    #                 new_car.coord['x'] += 1
    #                 yield [[[car.name, 'right']], Board(new_cars)]

    # def game_board(self, cars):
    #     """Given a set of cars, create a 2D array of the puzzle"""
    #     board = [['.' for col in range(self.size['x'])]
    #              for row in range(self.size['y'])]
    #     for car in cars:
    #         if car.orientation == Orientation.HORIZONTAL:
    #             x_start = car.coord['x']
    #             x_stop = car.coord['x'] + car.length
    #             for x in range(x_start, x_stop + 1):
    #                 board[car.coord['y']][x] = car.name
    #         else:
    #             y_start = car.coord['y']
    #             y_stop = car.coord['y'] + car.length
    #             for y in range(y_start, y_stop + 1):
    #                 board[y][car.coord['x']] = car.name
    #     return board
    #
    # def prettify(self, cars):
    #     """Printable version that represents the 2D array of the puzzle"""
    #     board = self.game_board(cars)
    #     output = ''
    #     for line in board:
    #         output += " ".join(line) + '\n'
    #     return output
    #
    # def goalTest(self):
    #     """Check if the red_car is free"""
    #     red_car = [car for car in self.cars if car.is_red_car][0]
    #     return red_car.coord['x'] + red_car.length == self.size['x'] - 1




def readfile(input_file):
    """ Reads an input file (where each line contains a puzzle, a comment started by a #, or an empty line)
        skips empty lines and lines and comments
        stores each puzzle in a list called puzzles_list
        then stores each puzzle from the list in a 6 by 6 2D array
    """
    input_file = open('input.txt', 'r')
    puzzles_list = list()
    puzzles_array = []
    car_length_dict = {}
    car_orient_dict ={}
    car_fuel_dict = {}
    #car = Car.__new__(Car)

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

        #collects car lengths in car_length_dict with keys : car chars
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
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

        puzzles_array.append(a)

    return puzzles_array

# determines if car A has reached (2,5) in the board
def goal(self):
    exited = False
    i = self.cars.index('A')
    if(self.cars[i].x == 2 and self.cars[i].y == 5):
        exited = True
    # add elif to check the position of the tail
    else:
        exited = False
    
    return exited
