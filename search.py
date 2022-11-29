from car import Car
from board import *
import time

# def ucs(brd,grid):
#     initial_state = brd
#     open = []
#     closed = []
#     parentIndex = 0
#     index = 0
#     cost = 0
#     notFound = False
#     foundGoal = False
    
#     #to calculate the runtime
#     start = time.time()

#     #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
#     visited = (initial_state, [], parentIndex, index, cost)
#     print(board.brdToGrd(initial_state))
#     # find a list of next possible moves from the current state
#     # #replace [] with a call to the function that checks all possible moves from the state in the visited queue and return a new Board
#     # ex. nextMove = possibleMove(visited[0])
#     nextMove, nextGrid = board.explore_moves(brd, grid)
#     print(len(nextMove))
    
#     #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
#     # S = initial game state

#     while(foundGoal == False):

#         #if there is no next move and we did not reach the goal, there is no solution
#         if(nextMove == []):
#             stop = time.time()
#             print("No solution")
#             foundGoal = True
#             break #stop while loop

#         if (nextMove != []):
#             cost+=1
#             # the new parent node is the state-node in the visited, so we get the index
#             parentIndex = visited[3]

#             for i in range(len(nextMove)):
#                 m = nextMove[i]
#                 g = nextGrid[i]
#                 #if next move is found and we reach the goal, we finished the search
#                 print(board.goal(m))
#                 if(board.goal(m)):
#                    goalstate = (m, g, parentIndex, index+1, cost)
#                    visited.clear()
#                    stop = time.time()
#                    foundGoal = True
#                    break

#                 #else, we do the following steps:
#                 else:
#                     print("Next Move is not Goal")
#                     #for each of the possible move we found (for each element of the array nextMove)
#                     #we create a new tuple to append to 'open' queue: (nextMove element, parent state, index, new cost)
#                     if open == []:
#                         nextOpen = (m, g, parentIndex,index+1,cost)
#                         open.append(nextOpen)
#                         print("appending first element in open queue")
#                     else:
#                         for n in open:
#                             check = (n[0].cars == m.cars)
#                             #verify if we have equivalent board already in open queue
#                             #if we do, continue without adding, since the cost of the newly found state will be higher
#                             if (check == True):
#                                 notFound = False
#                                 print("same board found in open queue")
#                                 break
#                             elif(check==False):
#                                 notFound = True
                        
#                         for n in closed:
#                             check = (n[0].cars == m.cars)
#                             #verify if we have equivalent board already in open queue
#                             #if we do, continue without adding, since the cost of the newly found state will be higher
#                             if (check == True):
#                                 notFound = False
#                                 print("same board found in closed queue")
#                                 break
#                             elif(check==False):
#                                 notFound = True
                        
#                         if(notFound == True):
#                             nextOpen = (m, g, parentIndex,index+1,cost)
#                             open.append(nextOpen)
#                             print("appending next element in open")
#                         elif(notFound==False):
#                             print("board already in the open queue")

#         #after verifying each child node        
#         #empty nextMove
#         nextMove.clear()
#         nextGrid.clear()
#         print("delete NextMove array")
#         #append the element from visited queue to closed queue
#         closed.append(visited)
#         print("append visited node to closed queue")
#         #append next state in the 'open' queue to visited and delete the same element from the open queue
#         visited = open[0]
#         print(open[0][1])
#         open.pop(0)
#         print("new visited, open queue first element popped")
#         # nextMove, nextGrid = board.explore_moves(visited[0], visited[1]) 
#         # print("Open Node into the visited queue")


#     #as result, we should display:
#     runtime = stop-start

#     # #find the actual path by tracking the parent node
#     # path = [goalstate]
#     # currentNode = goalstate
#     # while(currentNode != initial_state):
#     #     for node in closed:
#     #         #the index of the node = the parent node's index of current node
#     #         if (node[3] == currentNode[2]):
#     #             path.insert(0, currentNode)
#     #             currentNode = node
#     #             break
#     #         else:
#     #             continue
    
#     # #lastly, we insert the initial_state in the beginning of the path
#     # path.insert(0, initial_state)
    
#     print("Runtime: " + runtime)
#     # print("Solution path length: " + (len(path)-1))
#     #in output.txt file, write:
#     # "Runtime :" + runtime + "seconds\n"
#     # "Search path lenght: " + len(closed) + " states\n"
#     # "Solution path lenght: "+(len(path)-1)+" moves\n" #-1 to not count the initial state
#     # "Solution path : " #I'm not sure how to keep track of the actual moves made for the path :/
#     # final Board object displayed as 2D matrix

def ucs(brd, grd):
    initial_state = brd
    open = []
    closed = []
    parentIndex = 0
    index = 0
    cost = 0
    valid = True
    brdFound = False
    brdInClosed = False
    foundGoal = False
    solution = False
    path = []

    #to calculate the runtime
    start = time.time()

    # initialize visited
    sourceNode = (initial_state, grd, parentIndex, index, cost, valid)
    visited = sourceNode
    print("Initial Game Board")
    print(board.brdToGrd(initial_state))
    print()

    #get next possible moves
    nextMove, nextGrid = board.explore_moves(brd, grd)

    print("The number of child nodes: ")
    print(len(nextMove))

    while(foundGoal == False):
        if(nextMove == []):
            stop = time.time()
            print("No solution")
            foundGoal = True
            solution = False
            break

        elif(board.goal(visited[0])==True):
            stop = time.time()
            print("TRUE: Solution found")
            solution=True
            goalstate = visited
            visited = []
            foundGoal = True
            break

        else:
            if(closed == []):
                cost=1
            elif(visited[3] == 1):
                cost = 2
            else:
                cost = closed[parentIndex][4]+1

            parentIndex = int(visited[3])
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                valid = True

                #the next move is the goal state
                if(board.goal(b) == True):
                    stop = time.time()
                    print("TRUE: Goal is Found")
                    print(g)
                    solution = True
                    index = index + 1
                    goalstate = (b, g, parentIndex-1, index, cost,valid)
                    visited = []
                    foundGoal = True
                    break

                #The next move is not a goal state
                else:
                    print("FALSE: Goal is not Found")
                    #verify if next move is already in closed
                    if (closed != []):
                        for n in closed:
                            brdFound = False
                            ng = n[1]
                            for l in range(6):
                                for j in range(6):
                                    if(g[l][j] == ng[l][j]):
                                        res = True
                                    else:
                                        res = False
                                        break
                                if(res==False):
                                    break
                            if(res):
                                brdInClosed = True
                                print("***Board already in closed queue***Skipping")
                                break
                            else: 
                                brdInClosed = False
                    
                    #if Closed queue is empty
                    else:
                        brdInClosed = False

                    brdFound = brdInClosed
                    #if same node was found in Closed Queue, we don't add the board to the open list, so brdFound = True
                    if(brdFound==True):
                        print("Moving to the next possible move")
                    else:
                        #if Open Queue is empty, add the board as the first node
                        if(open == []):
                            print("Adding the first element to Open Queue")
                            print(g)
                            nextOpen = (b, g, parentIndex,index,cost, valid)
                            open.append(nextOpen)
                        
                        else:
                            for k in range(len(open)):
                                ng = open[k][1]
                                #for every node in the Open Queue, verify any board with the same board/grid: res = True if same board was found
                                for l in range(6):
                                    for j in range(6):
                                        if(g[l][j] == ng[l][j]):
                                            res = True
                                        else:
                                            res = False
                                            break
                                    if(res == False):
                                        break
                                
                                if(res):
                                    print("Board already in Open Queue")
                                    if(open[k][4]> cost):
                                        print("Found lower cost, keep current node in open and pop the previous node")
                                        brdFound = False
                                        valid = True
                                        notvalid = False
                                        open[k][4] = notvalid
                                        closed += [open[k]]
                                        open.pop(k)
                                    else:
                                        brdFound = True
                                    break
                                else: 
                                    brdFound = False
                            
                            #if board was not found after running through all the boards in Open Queu, add the new board to the Open Queue
                            if(brdFound==False):
                                print("Adding the following child node in the Open Queue")
                                print(g)
                                index = index + 1
                                nextOpen = (b, g, parentIndex,index,cost,valid)
                                open.append(nextOpen)
            #end of for loop to verift all child node  
            #after verifying each child node        
            #empty nextMove
            if(solution == False):
                nextMove = []
                nextGrid = []
                print("delete NextMove array")
                #append the element from visited queue to closed queue
                closed+=[visited]
                print("append visited node to Closed Queue")
                #append next state in the 'open' queue to visited and delete the same element from the open queue
                if(open == []):
                    print("Open Queue Empty, No solution")
                    stop = time.time()
                    foundGoal = True
                else :
                    if(open[0][5] == False):
                        closed+=[open[0]]
                        open.pop(0)
                        visited = open[0]
                        print("The next node in visited:")
                        print(visited[1])
                        open.pop(0)
                        print("Open queue first element popped, current lenght:")
                        print(len(open))
                        nextMove, nextGrid = board.explore_moves(visited[0], visited[1]) 
                        print("Open Node into the visited queue")
                    else:
                        visited = open[0]
                        print("The next node in visited:")
                        print(visited[1])
                        open.pop(0)
                        print("Open queue first element popped, current lenght:")
                        print(len(open))
                        nextMove, nextGrid = board.explore_moves(visited[0], visited[1]) 
                        print("Open Node into the visited queue")
            elif(solution == True):
                foundGoal = True

    runtime = stop - start

    print("Runtime: %.3f s" % runtime)
    #if solution = True, find path
    #find the actual path by tracking the parent node
    if(solution == True):
        # for node in closed:
        #     print(node[1])
        #     print(node[2], node[3], node[4])
        # currentNode = goalstate
        print(goalstate[2], goalstate[3], goalstate[4])
        while(currentNode[3] != 0):
            for node in closed:
                #the index of the node = the parent node's index of current node
                if (node[3] == currentNode[2]):
                    path.insert(0, currentNode)
                    currentNode = node
                    break
        
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, sourceNode)
        
        print("Solution path length: %.1d" % (len(path)))
        for p in path:
            print(p[2], p[3], p[4])
            print(p[1])

    elif(solution == False):
        print("No Solution found")
#     # if solution = False, print("No Solution")
#     #in output.txt file, write:
#     # "Runtime :" + runtime + "seconds\n"
#     # "Search path lenght: " + len(closed) + " states\n"
#     # "Solution path lenght: "+(len(path)-1)+" moves\n" #-1 to not count the initial state
#     # "Solution path : " #I'm not sure how to keep track of the actual moves made for the path :/
#     # final Board object displayed as 2D matrix
    

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
