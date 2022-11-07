from board import Board

"""
Main Runner File
"""

def boardSolOutput(puzzleString):
    """Currently prints output for one puzzle into txt file
    """
    
    solOutputArr = []
    solOutputArr.append("Initial Board Configuration: " + puzzleString + '\n')
    solOutputArr.append("!" + '\n' + Board.print_board(puzzleString))
    carFuelString = ', '.join(str(car) for car in Board.fuel_level(puzzleString))
    solOutputArr.append("Car fuel available: " + carFuelString + '\n')
    solOutputArr.append("Runtime: ")
    solOutputArr.append("Search path length: ")
    solOutputArr.append("Solution path length: ")
    solOutputArr.append("Solution path: ")

    with open('outputTEST.txt', 'w') as f:
        f.write("--------------------------------------------------------------------------------")
        f.write('\n')
        for line in solOutputArr:
            f.write(line)
            f.write('\n')
        f.write("--------------------------------------------------------------------------------")

#main function
if __name__ == '__main__':
    puzzle1 = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
    boardSolOutput(puzzle1)