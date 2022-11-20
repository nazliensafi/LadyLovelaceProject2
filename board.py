"""
This module implements 'board' class.
"""
import numpy as np
from car import *


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


def readFile(filename):
    """ Reads an input file (where each line contains a puzzle, a comment started by a #, or an empty line)
        skips empty lines and lines and comments
        stores each puzzle as a string in an array called puzzles
        each string represents the initial state of a game

        Returns puzzles
    """
    puzzles = []
    input_file = open(filename, 'r')
    # extracts puzzles in 1D and stores them in puzzles_list
    for line in input_file:
        # if line is not empty and doesn't start with #
        if line.strip() and line[0] != '#':
            puzzles+=[line]
    
    input_file.close()

    return puzzles

def strToBoard(puzzleArr):
    """ Reads an array containing strings representing the initial state of a game
        and creates a Board object with each string

        Returns an array of Board objectcs 
    """
    
    #car = Car.__new__(Car)

    # resulting array = an array of Board objects where each Board object represent the initial state of one game
    resulting_boards = []

    # make a 2D array for each puzzle found in the input file and initialize car objects
    for puzzle in puzzleArr:
        resulting_cars = []
        car_length_dict = {}
        car_orient_dict ={}
        car_fuel_dict = {}
        car_name = []

        #To delete after testing the readfile()
        print("puzzle string: " + puzzle)
        a = np.empty((6, 6), dtype=object)

        #list of unique car names
        prob = puzzle[0:36]
        uniqueCar = ''.join(set(prob))
        for c in uniqueCar:
            if c == '.':
                continue
            elif c == '\n':
                continue
            else:
                car_name.append(c)
        
        # collects car lengths in car_length_dict with keys : car chars
        for char in car_name:
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

        # collects car orientation in car_orint_dict with keys : car chars
        for i in range(35):
            if puzzle[i] == puzzle[i+1]:
                car_orient_dict[puzzle[i]] = 0
            else:
                car_orient_dict[puzzle[i+1]] = 1

        del car_orient_dict['.']
        print("\nCar Orientation Dictionary: ")
        print(car_orient_dict)

        # returns a dictionary called car_fuel_dict containing char representing cars and int representing fuel level
        # if the original puzzle does not contain specification of initial fuel_level
        if len(puzzle) == 36:
            for c in puzzle:
                car_fuel_dict[c] = 100

        if len(puzzle) > 36:
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


        k = 0
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
                        car_coord_dict[puzzle[k]] = (a_row, a_col)
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

        # puzzles_array.append(a)

        # build the resulting array of Boards
        for c in car_name:
            new_car = Car(c, car_coord_dict.get(c)[0], car_coord_dict.get(c)[1], car_length_dict.get(c), car_orient_dict.get(c), car_fuel_dict.get(c))
            #print(new_car)
            resulting_cars+=[(new_car)]

        #print(resulting_cars)
        resulting_boards+=[Board(resulting_cars, 6, 6)]
        
        # for cars in resulting_cars:
        #     resulting_boards.append(Board(cars, 6, 6))

    return resulting_boards


def goal(self):
    """
    given a board of cars checks if the A car's tail is at position [2][5]
    since A is always horizontal we don't need to check for a vertical case
    since if tail reaches the exit a solution is found, we only need to check the tail
    :return: True if the A car's tail is at position [2][5]
    """
    cars = self.cars
    print(type(self))
    for car in cars:
        if car.name == 'A' and car.x == 2 and car.y + car.length - 1 == 5:
            return True

# # determines if car A has reached (2,5) in the board
# def goal(self):
#     exited = False
#     i=0
#     for Car in self.cars:
#         if Car.name != 'A':
#             i += 1
#         else:
#             break
#
#     if(self.cars[i].x == 2 and self.cars[i].y == 5):
#         exited = True
#     # add elif to check the position of the tail
#     #case when A is horizontal
#     elif(self.cars[i].orientation == 0):
#         if(self.cars[i].x + self.cars[i].length == 2 and self.cars[i].y == 5):
#             exited = True
#         else:
#             exited = False
#     #case when A is vertical
#     elif(self.cars[i].orientation == 1):
#         if(self.cars[i].x == 2 and self.cars[i].y + self.cars[i].length == 5):
#             exited = True
#         else:
#             exited = False
#     else:
#         exited = False
#
#     return exited

#Heuristic functions
#H1: the number of vehicles blocking A
def h1(self):
    """
        given a board, read the coordinates of each car's position to determine
        the number of the vehicles blocking A from the exit(2,5)

        return the number of vehicles blocking A
    """
    #result to return
    hn = 0

    #find the index of A in the list of cars    
    i=0
    for c in self.cars:
        if (c.name!='A'):
            i+=1
        else:
            break

    #using the index, determine the coordinate of A's edge
    Alength=self.cars[i].length
    Ay=self.cars[i].y+Alength-1
    Ax=self.cars[i].x
    
    #verify if A is at the exit
    if(Ax == 2 and Ay == 5):
        hn = 0
    
    #check if any cars is positioned between A and the exit(2,5)
    else:
        for c in self.cars:
            #skip A
            if(c.name != 'A'):
                #if the car is horizontal and blocking, then its x value is equal to Ax and y value greater than Ay
                if c.orientation == 0:
                    if(c.x==Ax and c.y > Ay):
                        hn+=1
                    else:
                        continue
                #if the car is vertical and blocking, its y value is greater than Ay, and its x value is equal to Ax or x+length surpasses 2 when x < 2
                elif c.orientation == 1:
                    if((c.x == Ax and c.y>Ay) or (c.x<=2 and (c.x+c.length-1 >= 2) and c.y>Ay)):
                        hn+=1
    
    return hn

#H2: the number of positions blocked (regardless of vehicle number)
def h2(self):
    """
        given a board, verify the number of cars blocking row 2

        return the number of vehicles blocking the row 2
    """
    hn = 0

    #find the index of A in the list of cars
    i=0
    for c in self.cars:
        if(c.name != 'A'):
            i+=1
        else:
            break

    Ay = self.cars[i].y + 1

    #using the index, determine the coordinate of A's edge
    Alength=self.cars[i].length
    Ay=self.cars[i].y+Alength-1
    Ax=self.cars[i].x

    #either the head or the tail of A is at the exit(2,5)
    if(Ax == 2 and Ay == 5):
        hn = 0

    #if A is not in exit, check if any vehicle is blocking coordinate (2, y) between A and exit
    else:
        for c in self.cars:
            #skip A
            if(c.name != 'A'):
                #if the car is horizontal, at coordinate x = 2 and y > Ay, then its length is included in h(n)
                if c.orientation == 0:
                    if(c.x == 2 and (c.y > Ay or (c.y+c.length-1)<= 5)):
                        hn = hn + c.length
                    else:
                        continue
                
                #if the car is vertical and its y value is greater than Ay, then it only blocks one position
                elif c.orientation == 1:
                    if(c.y > Ay and (c.x==Ax or (c.x==1 and c.length>=2) or (c.x==0 and c.length>=3))):
                        hn+=1
                    else:
                        continue

    return hn

#H3: the value of h1 * lamda (value of choice > 1)
def h3(self, ld):
    hx = h1(self)
    hn = hx*ld
    return hn

#H4: heuristic of our choice


#Method to draw 2D board based on cars coordinate
def drawBoard(self):
    board2D = [['.' for i in range(6)] for j in range(6)]
    boardToPrint = []

    for c in self.cars:
        char = c.name
        #if car is horizontal
        if c.orientation == 0:
            for i in range(c.length):
                board2D[c.x][c.y+i] = char
        elif c.orientation == 1:
            for i in range(c.length):
                board2D[c.x+i][c.y] = char
    
    for i in range(6):
        str = ""
        for j in range(6):
            str = str + board2D[i][j] + " "
        boardToPrint+=[str]
    
    for line in boardToPrint:
        print(line)