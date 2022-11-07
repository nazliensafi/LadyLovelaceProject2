"""
This module implements 'board' class.
"""
import numpy as np
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


    @staticmethod
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

        for line in input_file:
            if line.strip() and line[0]!='#': #if there line is not empty and doesn't start with #
                puzzles_list.append(line)

        input_file.close()

        #make a 2D array for each puzzle found
        for puzzle in puzzles_list:
            print(len(puzzle))
            print(puzzle)
            a = np.full((6, 6), '*', dtype='U1')
            k=0
            for a_row in range(6):
                for a_col in range(6):
                    a[a_row][a_col] = puzzle[k]
                    k += 1
            puzzles_array.append(a)

            for char in "ABCDEFGHIJKLMNOP":
                 count = 0
                 for k in range(36):
                    if char == puzzle[k]:
                        count += 1
                 if count == 0:
                    break
                 else:
                    car_length_dict[char] = count
        print(car_length_dict)
        print (puzzles_array[0])
        print (puzzles_array[1])


        return puzzles_array
    
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
    
    def fuel_level(boardString):
        """
        returns a list containing char representing cars and int representing fuel level
        """
        car_fuel = []

        # if the original line does not contain specification of initial fuel_level
        if len(boardString) == 36:
            cars = Board.car_list(boardString)
            for c in cars:
                car_fuel.append(c+":"+str(100))
        
        if len(boardString)>36:
            # the fuel-level specification is separated by a space
            new_str = boardString[37:]
            cars = Board.car_list(boardString[:35])
            for i in range(0, len(new_str), 3):
                if new_str[i] in cars:
                    car_fuel.append(new_str[i]+":"+ new_str[i+1])

            # for cars without fuel-level specification, add 100
            for c in cars:
                if c in car_fuel:
                    continue
                else:
                    car_fuel.append(c+":"+str(100))
        return car_fuel

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
        print(grid)
        #print(grid[0][3])
        

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
