from car import Car
from board import *
import time

def ucs(brd,grid):
    initial_state = brd
    open = []
    closed = []
    parentIndex = 0
    index = 0
    cost = 0
    notFound = False
    foundGoal = False
    
    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    visited = (initial_state, [], parentIndex, index, cost)
    print(board.brdToGrd(initial_state))
    # find a list of next possible moves from the current state
    # #replace [] with a call to the function that checks all possible moves from the state in the visited queue and return a new Board
    # ex. nextMove = possibleMove(visited[0])
    nextMove, nextGrid = board.explore_moves(brd, grid)
    print(len(nextMove))
    
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state

    while(foundGoal == False):

        #if there is no next move and we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            print("No solution")
            foundGoal = True
            break #stop while loop

        if (nextMove != []):
            cost+=1
            # the new parent node is the state-node in the visited, so we get the index
            parentIndex = visited[3]

            for i in range(len(nextMove)):
                m = nextMove[i]
                g = nextGrid[i]
                #if next move is found and we reach the goal, we finished the search
                print(board.goal(m))
                if(board.goal(m)):
                   goalstate = (m, g, parentIndex, index+1, cost)
                   visited.clear()
                   stop = time.time()
                   foundGoal = True
                   break

                #else, we do the following steps:
                else:
                    print("Next Move is not Goal")
                    #for each of the possible move we found (for each element of the array nextMove)
                    #we create a new tuple to append to 'open' queue: (nextMove element, parent state, index, new cost)
                    if open == []:
                        nextOpen = (m, g, parentIndex,index+1,cost)
                        open.append(nextOpen)
                        print("appending first element in open queue")
                    else:
                        for n in open:
                            check = (n[0].cars == m.cars)
                            #verify if we have equivalent board already in open queue
                            #if we do, continue without adding, since the cost of the newly found state will be higher
                            if (check == True):
                                notFound = False
                                print("same board found in open queue")
                                break
                            elif(check==False):
                                notFound = True
                        
                        for n in closed:
                            check = (n[0].cars == m.cars)
                            #verify if we have equivalent board already in open queue
                            #if we do, continue without adding, since the cost of the newly found state will be higher
                            if (check == True):
                                notFound = False
                                print("same board found in closed queue")
                                break
                            elif(check==False):
                                notFound = True
                        
                        if(notFound == True):
                            nextOpen = (m, g, parentIndex,index+1,cost)
                            open.append(nextOpen)
                            print("appending next element in open")
                        elif(notFound==False):
                            print("board already in the open queue")

            #after verifying each child node        
            #empty nextMove
            nextMove.clear()
            nextGrid.clear()
            print("delete NextMove array")
            #append the element from visited queue to closed queue
            closed.append(visited)
            print("append visited node to closed queue")
            #append next state in the 'open' queue to visited and delete the same element from the open queue
            visited = open[0]
            print(open[0][1])
            open.pop(0)
            print("new visited, open queue first element popped")
            # nextMove, nextGrid = board.explore_moves(visited[0], visited[1]) 
            # print("Open Node into the visited queue")


    #as result, we should display:
    runtime = stop-start

    # #find the actual path by tracking the parent node
    # path = [goalstate]
    # currentNode = goalstate
    # while(currentNode != initial_state):
    #     for node in closed:
    #         #the index of the node = the parent node's index of current node
    #         if (node[3] == currentNode[2]):
    #             path.insert(0, currentNode)
    #             currentNode = node
    #             break
    #         else:
    #             continue
    
    # #lastly, we insert the initial_state in the beginning of the path
    # path.insert(0, initial_state)
    
    print("Runtime: " + runtime)
    # print("Solution path length: " + (len(path)-1))
    #in output.txt file, write:
    # "Runtime :" + runtime + "seconds\n"
    # "Search path lenght: " + len(closed) + " states\n"
    # "Solution path lenght: "+(len(path)-1)+" moves\n" #-1 to not count the initial state
    # "Solution path : " #I'm not sure how to keep track of the actual moves made for the path :/
    # final Board object displayed as 2D matrix

#TODO
def gbfs_h1(board):
    initial_state = board
    open = []
    closed = []

    #index in the closed set to keep track of the path
    parentIndex = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state
    visited = (initial_state, parentIndex, board.h1())


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

        if (nextMove != []):
            
            parentIndex+=1

            for m in nextMove:
                #if next move is found and we reach the goal, we finished the search
                if(m is goal()):
                   goalstate = (m, parentIndex, 0)
                   visited.pop()
                   stop = time.time()
                   break

                #else, we do the following steps:
                else:
                    #for each of the possible move we found (for each element of the array nextMove)
                    #calculate the value of h1()
                    hn = m.h1()
                    #find the right index where to insert the new m
                    i = 0
                    for n in open:
                        if(n[2] < hn):
                            i+=1
                        else:
                            open.insert(i, m)


            #after verifying each child node        
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
    while(currentNode != initial_state):
        #get the state at the index of the parent node of the current node
        i = currentNode[1]
        path.insert(0, closed[i])
        currentNode = closed[i]
    
    #lastly, we insert the initial_state in the beginning of the path
    path.insert(0, initial_state)
    
    #in output.txt file, write:
    # "Runtime :" + runtime + "seconds\n"
    # "Search path lenght: " + len(closed) + " states\n"
    # "Solution path lenght: "+(len(path)-1)+" moves\n" 
    # ** -1 to not count the initial state
    # "Solution path : " #I'm not sure how to keep track of the actual moves made for the path :/
    # final Board object displayed as 2D matrix


# A Star algorithm: calclate for heuristic and cost 
def astar(board):
    initial_state = board
    open = []
    closed = []

    #index in the closed set to keep track of the path
    parentIndex = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state
    visited = (initial_state, parentIndex, board.h1())


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

        if (nextMove != []):
            
            parentIndex+=1

            for m in nextMove:
                #if next move is found and we reach the goal, we finished the search
                if(m is goal()):
                   goalstate = (m, parentIndex, 0)
                   visited.pop()
                   stop = time.time()
                   break

                #else, we do the following steps:
                else:
                    #for each of the possible move we found (for each element of the array nextMove)
                    #calculate the value of h1()
                    hn = m.h1()
                    #find the right index where to insert the new m
                    i = 0
                    for n in open:
                        if(n[2] < hn):
                            i+=1
                        else:
                            open.insert(i, m)
            #after verifying each child node        
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
    while(currentNode != initial_state):
        #get the state at the index of the parent node of the current node
        i = currentNode[1]
        path.insert(0, closed[i])
        currentNode = closed[i]
    
    #lastly, we insert the initial_state in the beginning of the path
    path.insert(0, initial_state)
