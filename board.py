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

    def create_grid(boardString):
        """
        return 2D array of the board
        """
        boardAsList = list(boardString)
        grid = [boardAsList[j:j + 6] for j in range(0, len(boardAsList), 6)]
        return grid




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

        Returns an array of Board objectcs called resulting_boards
         and an array of 2D arrays (look-up grids) calles resulting_grids
    """

    resulting_boards = []
    resulting_grids = [] 

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
        lu = np.empty((6, 6), dtype='str') # look-up board to use as a helper in explore_moves

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
                    lu[a_row][a_col] = puzzle[k]
                    print(".", end =" ")
                else:
                    car = Car.__new__(Car) #create an empty Car object
                    car.name = puzzle[k] #set the car name
                    lu[a_row][a_col] = puzzle[k]
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

        # Uncomment to see the look-up table aka grid
        # for a_row in range(6):
        #     for a_col in range(6):
        #         print(lu[a_row][a_col], end =" ")
        #     print("\n")

        # build the resulting array of Boards
        for c in car_name:
            new_car = Car(c, car_coord_dict.get(c)[0], car_coord_dict.get(c)[1], car_length_dict.get(c), car_orient_dict.get(c), car_fuel_dict.get(c))
            #print(new_car)
            resulting_cars+=[(new_car)]

        resulting_grids.append(lu)
        resulting_boards+=[Board(resulting_cars, 6, 6)]

        # for cars in resulting_cars:
        #     resulting_boards.append(Board(cars, 6, 6))

    return resulting_boards, resulting_grids


def explore_moves(b, g):
    """
    given a board of car objects, checks how many different moves are possible
     e.g.
     move 1: B left 1 and the respective board
     move 2: B left 2 and the respective board
     move 3: C up 1 and the respective board
     :return:  list of boards and the move that made it different from the parent board
    """
    cars = b.cars
    grid = g
    new_boards = []
    new_grids = []

    for car in cars:
        x, y, length = car.x, car.y, car.length
        if car.orientation == 0:  # horizontal cars
            # if positions to the left of the HEAD is empty
            step_l = step_r = 1
            for i in range(y):
                if grid[x][y-step_l] == '.':
                    print(car.name, "left", step_l)
                    step_l += 1

            for j in range(5-y+length):
                # if positions to the right of the TAIL is empty
                if y+length-1+step_r <= 5 and grid[x][y+length-1+step_r] == '.':
                    print(car.name, "right", step_r)
                    step_r += 1

        elif car.orientation == 1: # vertical cars
            # if positions up from the HEAD is empty
            step_u = step_d = 1
            for i in range(x):
                if grid[x-step_u][y] == '.':
                    print(car.name, "up", step_u)
                    step_u += 1

            # if positions down from the TAIL is empty
            for j in range(5-x+length):
                if x+length-1+step_d <= 5 and grid[x+length-1+step_d][y] == '.':
                    print(car.name, "down", step_d)
                    step_d += 1

    return new_boards


def goal(self):
    """
    given a board of cars checks if the A car's tail is at position [2][5]
    since A is always horizontal we don't need to check for a vertical case
    since if tail reaches the exit a solution is found, we only need to check the tail
    :return: True if the A car's tail is at position [2][5]
    """
    cars = self.cars  # get the cars attribute of the calling board
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

# #H4: heuristic of our choice
# def h4(self):
#     """
#        The distance of A's head from the exit + the number of cars blocking A
#        H4 is admissible:
#        - A must traverse the distance between himself and the exit
#        - All cars blocking A from the exit must be moved at least once to allow A to traverse to the exit
#     """
#     hn = 0
#     #the number of cars blocking A = value of h1(n)
#     ha = h1(self)

#     # #the distance of the red car from the exit

#     #find the index of A in the list of cars
#     i=0
#     for c in self.cars:
#         if(c.name != 'A'):
#             i+=1
#         else:
#             break

#     #using the index, determine the coordinate of A's edge
#     Alength=self.cars[i].length
#     Ay=self.cars[i].y+Alength-1
#     Ax=self.cars[i].x

#     #verify if A is at the exit
#     if(Ax == 2 and Ay == 5):
#         hn = 0

#     blockingA=[]
#     #find cars blocking A
#     else:
#         for c in self.cars:
#             #skip A
#             if(c.name != 'A'):
#                 #if the car is horizontal and blocking, then its x value is equal to Ax and y value greater than Ay
#                 if c.orientation == 0:
#                     if(c.x==Ax and c.y > Ay):
#                         blockingA+=[c.name]
#                     else:
#                         continue
#                 #if the car is vertical and blocking, its y value is greater than Ay, and its x value is equal to Ax or x+length surpasses 2 when x < 2
#                 elif c.orientation == 1:
#                     if((c.x == Ax and c.y>Ay) or (c.x<=2 and (c.x+c.length-1 >= 2) and c.y>Ay)):
#                         blockingA+=[c.name]


#     # #the coordinate y of A's head
#     # Ay = self.cars[i].y + 1

#     # #distance from the exit
#     # hd = 5 - Ay

#     # #final h4(n) value
#     # hn = ha + hd


#     return hn

def h4(self):
    """
       H4(n) = the number of cars blocking the cars blocking A
       H4 is admissible:
       - All cars blocking the cars blocking A must be moved before the cars blocking A can move
       - After moving those cars, the cars blocking A still must be moved
       - Thus, h4(n) would always be smaller than the actual cost to reach goal
    """

    hn=0
    blockingA = []
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
                        blockingA += [c]
                    else:
                        continue

                #if the car is vertical and its y value is greater than Ay, then it only blocks one position
                elif c.orientation == 1:
                    if(c.y > Ay and (c.x==Ax or (c.x==1 and c.length>=2) or (c.x==0 and c.length>=3))):
                        blockingA += [c]
                    else:
                        continue

    for i in range(len(blockingA)):
        coordx = blockingA[i].x
        coordy = blockingA[i].y
        lengthb = blockingA[i].length
        for c in self.cars:
            if(blockingA[i].name != c.name and c.name !='A'):
                #if the car [i] is horizontal, we skip, as the number of the cars blocking is already counted in h1(n)
                if blockingA[i].orientation == 0:
                    continue
                #if the car [i] is vertical, count the number of cars blocking car[i]
                elif blockingA[i].orientation == 1:
                    #if the car is horizontal, then it only blocks car[i] if its head or tail blocks car[i]'s head or tail
                    if c.orientation == 0:
                        if((coordx-1 == c.x and c.y<=coordy and c.y+c.length-1 >=coordy) or (coordx+lengthb == c.x and c.y <= coordy and c.y+c.length-1 >=coordy)):
                            hn+=1
                     #if the car is vertical then it only blocks car[i] if its x coordinate is at the head or the tail of car[i]
                    elif c.orientation == 1:
                        if(((c.x == (coordx+lengthb)) and c.y == coordy) or (c.x+c.length-1)==(coordx-1) and c.y == coordy):
                            hn+=1


    return hn

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
