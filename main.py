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
    b, g = board.strToBoard(board.readFile('goaltest.txt'))
    brd = b[0]
    grid = g[0]
    brds , grds = board.explore_moves(brd, grid)
    print(len(grds), "possible moves detected")
    #print(len(brds))
    # #  Uncomment to see the look-up table aka grid
    # for a_row in range(6):
    #     for a_col in range(6):
    #         print(lu[a_row][a_col], end =" ")
    #     print("\n")
    # if board.goal(b[0]):
    #     print("Goal reached")
    # else:
    #     print("Goal failed")


    # hn = 0
    # #get the position of A
    # i=0
    # for c in goaltest[0].cars:
    #     if (c.name!='A'):
    #         i+=1
    #     else:
    #         break
    #Ay = goaltest[0].cars[i].y + 1
    
    # #either the head or the tail of the A is at the exit(2,5)
    # if(Ay == 5 or Ay == 4):
    #     hn = 0
    # #check if any cars is positioned between A and the exit(2,5)
    # else:
    #     for c in goaltest[0].cars:
    #         #if the car is horizontal, then its x value is equal to Ax
    #         if c.orientation == 0:
    #             if(c.x == 2 and (c.y > Ay or (c.y+c.length-1)<= 5)):
    #                 hn+=1
    #             else:
    #                 continue
    #         #if the car is vertical, its y value is greater than Ay
    #         elif c.orientation == 1:
    #             if(c.y > Ay and ((c.x+c.length-1)==2 or 2==c.x)):
    #                 hn+=1
    #             else:
    #                 continue
    #print(i)

# TODO
# Car.py -> valide_move() method
# Car.py -> explore_move() method: 
#   part 1: if car = horizontal, allow left-right, check the head and tail of the car
#   part 2: if car = vertical, allow top-bottom, check the head and tail of the car

# Search algorithms (implementation and test)
# UCS
# GBFS h1, h2, h3, h4
# Algorithm A/A* h1, h2, h3, h4

#For submission
#50 sample questions
#output.txt after the test
#slides for presentation
# READ.Me for instructions on running the code
