from car import Car
from board import *
import time


def ucs(board):
    initial_state = board
    open = []
    closed = set()
    parentIndex = 0
    index = 0
    cost = 0
    goalstate = []

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    visited = (initial_state, parentIndex, index, cost)
    
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state

    while(visited != []):
        # find a list of next possible moves from the current state
        # #replace [] with a call to the function that checks all possible moves from the state in the visited queue and return a new Board
        # ex. nextMove = possibleMove(visited[0])
        nextMove = [] 
   
        
        #if there is no next move and we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            print("No solution")
            break #stop while loop

        # #if next move is found and we reach the goal, we finished the search
        # if (nextMove != []):
        #     for m in nextMove:
        #         if(m is goal):
        #            goalstate = (m, parentIndex+1, index+1, cost+1)
        #            visited.pop()
        #            stop = time.time()
        #            break

        #else, we do the following steps:
        else:
            #It always costs 1 to go from a parent node to the child node
            cost = cost+1

            #the new parent node is the child node from the previous loop
            parentIndex = index     
            
            #for each of the possible move we found (for each element of the array nextMove)
            #we create a new tuple to append to 'open' queue: (nextMove element, parent state, new cost)
            for m in nextMove:
                for n in open:
                    #verify if we have equivalent board already in open queue
                    if (n[0] != m):
                        open.append(m,parentIndex,index+1,cost)
                    #if we do, continue without adding, since the cost of the newly found state will be higher
                    elif(n[0] == m):
                        continue
            
            #empty nextMove
            nextMove.clear()
            #append the element from visited queue to closed queue
            closed.append(visited)
            #append next state in the 'open' queue to visited and delete the same element from the open queue
            visited = open[0]
            open.pop(0)


    #as result, we should display:
    runtime = stop-start

    #find the actual path by tracking the parent node
    path = [goalstate]
    currentNode = goalstate
    for node in closed:
        if (node[2] == currentNode[1]):
            path.insert(0, currentNode)
        else:
            continue
    
    #in output.txt file, write:
    # "Runtime :" + runtime + "seconds\n"
    # "Search path lenght: " + len(closed) + " states\n"
    # "Solution path lenght: "+(len(path)-1)+" moves\n" #-1 to not count the initial state
    # "Solution path : " #I'm not sure how to keep track of the actual moves made for the path :/
    # final Board object displayed as 2D matrix

