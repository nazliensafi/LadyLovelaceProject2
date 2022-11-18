import board
import car

"""
Main Runner File
"""

# def boardSolOutput(puzzleString):
#     """Currently prints output for one puzzle into txt file
#     """
#
#     solOutputArr = []
#     solOutputArr.append("Initial Board Configuration: " + puzzleString + '\n')
#     solOutputArr.append("!" + '\n' + Board.print_board(puzzleString))
#     carFuelString = ', '.join(str(car) for car in Board.fuel_level(puzzleString))
#     solOutputArr.append("Car fuel available: " + carFuelString + '\n')
#     solOutputArr.append("Runtime: ")
#     solOutputArr.append("Search path length: ")
#     solOutputArr.append("Solution path length: ")
#     solOutputArr.append("Solution path: ")
#
#     with open('outputTEST.txt', 'w') as f:
#         f.write("--------------------------------------------------------------------------------")
#         f.write('\n')
#         for line in solOutputArr:
#             f.write(line)
#             f.write('\n')
#         f.write("--------------------------------------------------------------------------------")

#main function
if __name__ == '__main__':
    # puzzle1 = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
    # boardSolOutput(puzzle1)
    # print(Board.create_grid(puzzle1)[0][3])
    # board = Board.readfile('input.txt')

    goaltest = board.readfile('goaltest.txt')
    if board.goal(goaltest[0]):
        print("Goal reached")
    else:
        print("Goal failed")


# TODO
# Board.py -> read unique alphabets in the list from the input text to determine what cars are in the puzzle
# Car.py -> valide_move() method
# Car.py -> explore_move() method: 
#   part 1: if car = horizontal, allow left-right, check the head and tail of the car
#   part 2: if car = vertical, allow top-bottom, check the head and tail of the car
# Board.py -> goals() method: check if head or tail of A is in position (2,5) 
# Search algorithms
# UCS
# GBFS h1, h2, h3, h4
# Algorithm A/A* h1, h2, h3, h4