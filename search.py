from car import Car
from board import *
import time

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
    explored = 0

    #to calculate the runtime
    start = time.time()

    # initialize visited
    sourceNode = (initial_state, grd, parentIndex, index, cost, valid)
    visited = sourceNode
    # print("Initial Game Board")
    # print(board.brdToGrd(initial_state))
    # print()

    #get next possible moves
    nextMove, nextGrid = board.explore_moves(brd, grd)

    # print("The number of child nodes: ")
    # print(len(nextMove))

    while(foundGoal == False):
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            foundGoal = True
            solution = False
            break

        elif(board.goal(visited[0])==True):
            stop = time.time()
            # print("TRUE: Solution found")
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
                    #print("TRUE: Goal is Found")
                    #print(g)
                    solution = True
                    index = index + 1
                    goalstate = (b, g, parentIndex-1, index, cost,valid)
                    visited = []
                    foundGoal = True
                    break

                #The next move is not a goal state
                else:
                    #print("FALSE: Goal is not Found")
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
                                #print("***Board already in closed queue***Skipping")
                                break
                            else: 
                                brdInClosed = False
                    
                    #if Closed queue is empty
                    else:
                        brdInClosed = False

                    brdFound = brdInClosed
                    #if same node was found in Closed Queue, we don't add the board to the open list, so brdFound = True
                    # if(brdFound==True):
                    #     print("Moving to the next possible moves")
                    if(brdFound == False):
                        #if Open Queue is empty, add the board as the first node
                        if(open == []):
                            #print("Adding the first element to Open Queue")
                            #print(g)
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
                                    #print("Board already in Open Queue")
                                    if(open[k][4]> cost):
                                        #print("Found lower cost, keep current node in open and pop the previous node")
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
                                #print("Adding the following child node in the Open Queue")
                                #print(g)
                                index = index + 1
                                nextOpen = (b, g, parentIndex,index,cost,valid)
                                open.append(nextOpen)
            #end of for loop to verift all child node  
            #after verifying each child node        
            #empty nextMove
            if(solution == False):
                nextMove = []
                nextGrid = []
                #print("delete NextMove array")
                #append the element from visited queue to closed queue
                closed+=[visited]
                #print("append visited node to Closed Queue")
                #append next state in the 'open' queue to visited and delete the same element from the open queue
                if(open == []):
                    #print("Open Queue Empty, No solution")
                    stop = time.time()
                    foundGoal = True
                else :
                    if(open[0][5] == False):
                        closed+=[open[0]]
                        open.pop(0)
                        visited = open[0]
                        #print("The next node in visited:")
                        #print(visited[1])
                        explored = explored + 1
                        open.pop(0)
                        #print("Open queue first element popped, current lenght:")
                        #print(len(open))
                        nextMove, nextGrid = board.explore_moves(visited[0], visited[1]) 
                        #print("Open Node into the visited queue")
                    else:
                        visited = open[0]
                        #print("The next node in visited:")
                        #print(visited[1])
                        explored = explored + 1
                        open.pop(0)
                        #print("Open queue first element popped, current lenght:")
                        #print(len(open))
                        nextMove, nextGrid = board.explore_moves(visited[0], visited[1]) 
                        #print("Open Node into the visited queue")
            
            elif(solution == True):
                foundGoal = True

    runtime = stop - start

    #if solution = True, find path
    #find the actual path by tracking the parent node
    if(solution == True and closed != []):
        # for node in closed:
        #     print(node[1])
        #     print(node[2], node[3], node[4])
        currentNode = goalstate
        # print(goalstate[2], goalstate[3], goalstate[4])
        while(currentNode[3] != 0):
            for node in closed:
                #the index of the node = the parent node's index of current node
                if (node[3] == currentNode[2]):
                    path.insert(0, currentNode)
                    currentNode = node
                    break
        
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, sourceNode)
        pl = (len(path)-1)
        #print("Solution path length: %.1d" % (len(path)-1))
        # for p in path:
        #     print(p[2], p[3], p[4])
        #     print(p[1])
            
    elif(solution == True and closed == []):
        path = [goalstate]
        #print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)

    elif(solution == False):
        #print("No Solution found")
        pl = 0
    
    return runtime, path, pl, explored
    
def gbfs_h1(brd,grd):
    
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False
    
    path = []
    explored = 0

    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state
    source = (brd, grd, parentIndex, idx, board.h1(brd))
    visited = source


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #if there are children nodes from the current node
        if (nextMove != []):
            
            #parentIndex = the current node's index
            parentIndex = visited[3]


            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h1(b)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n) of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % i)
                                break #end iteration
                            #if h(n) of the node in OPEN queue is equal to the h(n) of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i+1, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % (i+1))
                                break #end iteration
                                continue
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n) is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h)
                        open+=[child]
                        # print("Adding to the end of OPEN Queue")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
                # print("Moved next node in OPEN to VISITED")
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed!=[]):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)

        # print("The length of the path: %.1d" % (len(path)-1))
        pl = len(path)-1
    
    elif(found == True and closed == []):
        path = [goalstate]
        #print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)

    else:
        # print("No Solution is found")
        pl = 0

    return runtime, path, pl, explored

def gbfs_h2(brd,grd):
    
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False

    path = []
    explored = 0 

    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state
    source = (brd, grd, parentIndex, idx, board.h2(brd))
    visited = source


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #if there are children nodes from the current node
        if (nextMove != []):
            
            #parentIndex = the current node's index
            parentIndex = visited[3]


            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h2(b)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n) of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i, child)
                                added = True
                                break #end iteration
                            #if h(n) of the node in OPEN queue is equal to the h(n) of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i+1, child)
                                # print("Added child node to OPEN")
                                added = True
                                break #end iteration
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n) is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h)
                        open+=[child]
                        # print("Added child node to OPEN")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed!=[]):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)

        # print("The length of the path: %.1d" % (len(path)-1))
        pl = len(path)-1
    
    elif(found == True and closed == []):
        path = [goalstate]
        #print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)

    else:
        # print("No Solution is found")
        pl = 0
    
    return runtime, path, pl, explored

def gbfs_h3(brd,grd,ld):
    
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False

    path = []
    explored = 0

    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state
    source = (brd, grd, parentIndex, idx, board.h3(brd, ld))
    visited = source


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #if there are children nodes from the current node
        if (nextMove != []):
            
            #parentIndex = the current node's index
            parentIndex = visited[3]


            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h3(b, ld)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n) of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i, child)
                                added = True
                                break #end iteration
                            #if h(n) of the node in OPEN queue is equal to the h(n) of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i+1, child)
                                # print("Added child node to OPEN")
                                added = True
                                break #end iteration
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n) is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h)
                        open+=[child]
                        # print("Added child node to OPEN")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed!=[]):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)

        # print("The length of the path: %.1d" % (len(path)-1))
        pl = len(path)-1
    
    elif(found == True and closed == []):
        path = [goalstate]
        #print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)

    else:
        # print("No Solution is found")
        pl = 0

    return runtime, path, pl, explored
    
def gbfs_h4(brd,grd):
    
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False

    path = []
    explored = 0

    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state
    source = (brd, grd, parentIndex, idx, board.h4(brd))
    visited = source


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #if there are children nodes from the current node
        if (nextMove != []):
            
            #parentIndex = the current node's index
            parentIndex = visited[3]


            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h4(b)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n) of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i, child)
                                added = True
                                break #end iteration
                            #if h(n) of the node in OPEN queue is equal to the h(n) of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h):
                                child = (b, g, parentIndex, idx, h)
                                open.insert(i+1, child)
                                # print("Added child node to OPEN")
                                added = True
                                break #end iteration
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n) is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h)
                        open+=[child]
                        # print("Added child node to OPEN")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed!=[]):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)

        # print("The length of the path: %.1d" % (len(path)-1))
        pl = len(path)-1
    
    elif(found == True and closed == []):
        path = [goalstate]
        #print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)

    else:
        # print("No Solution is found")
        pl = 0
    
    return runtime, path, pl, explored


# A Star algorithm
def astar_h1(brd,grd):
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False
    cost = 0
    valid = True
    path = []
    explored = 0
    
    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state, initialise the visited board
    source = (brd, grd, parentIndex, idx, cost, valid, board.h1(brd))
    visited = source
    # print("Initial Game Board")
    # print(board.brdToGrd(brd))
    #print()


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #calculate cost for every move
        if (nextMove != []):
            if(closed == []):
                cost=1
            elif(visited[3] == 1):
                cost = 2
            else:
                cost = closed[parentIndex][4]+1

            #parentIndex = the current node's index
            parentIndex = visited[3]

            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h1(b)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        #print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n)+cost of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i, child)
                                added = True
                                #print("Adding to the OPEN Queue at index %.1d" % i)
                                break #end iteration
                            #if h(n)+cost of the node in OPEN queue is equal to the h(n)+cost of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i+1, child)
                                added = True
                                #print("Adding to the OPEN Queue at index %.1d" % (i+1))
                                break #end iteration
                            # if h(n)+cost of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n)+cost is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h+cost)
                        open+=[child]
                        #print("Adding to the end of OPEN Queue")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h+cost)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
                #print("Moved next node in OPEN to VISITED")
            else:
                stop = time.time()
                #print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed != []):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)

        # print("The length of the path: %.1d" % (len(path)-1))
        # print(path)
        pl = len(path) - 1
    elif(found == True and closed == []):
        path = [goalstate]
        # print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)
    else:
        # print("No Solution is found")
        pl = 0
    
    return runtime, path, pl, explored
        
def astar_h2(brd,grd):
    
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False
    cost = 0
    valid = True
    path = []
    
    explored = 0

    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state, initialise the visited board
    source = (brd, grd, parentIndex, idx, cost, valid, board.h2(brd))
    visited = source
    # print("Initial Game Board")
    # print(board.brdToGrd(brd))
    # print()


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #calculate cost for every move
        if (nextMove != []):
            if(closed == []):
                cost=1
            elif(visited[3] == 1):
                cost = 2
            else:
                cost = closed[parentIndex][4]+1

            #parentIndex = the current node's index
            parentIndex = visited[3]

            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h2(b)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n)+cost of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % i)
                                break #end iteration
                            #if h(n)+cost of the node in OPEN queue is equal to the h(n)+cost of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i+1, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % (i+1))
                                break #end iteration
                                continue
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n)+cost is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h+cost)
                        open+=[child]
                        # print("Adding to the end of OPEN Queue")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h+cost)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
                # print("Moved next node in OPEN to VISITED")
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed != []):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)
        pl = len(path)-1
        # print("The length of the path: %.1d" % (len(path)-1))
    
    elif(found == True and closed == []):
        path = [goalstate]
        # print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)
    
    else:
        pl = 0
        # print("No Solution is found")
    
    return runtime, path, pl, explored
        
def astar_h3(brd,grd,ld):
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False
    cost = 0
    valid = True
    path = []

    explored = 0
    
    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state, initialise the visited board
    source = (brd, grd, parentIndex, idx, cost, valid, board.h3(brd, ld))
    visited = source
    # print("Initial Game Board")
    # print(board.brdToGrd(brd))
    # print()


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #calculate cost for every move
        if (nextMove != []):
            if(closed == []):
                cost=1
            elif(visited[3] == 1):
                cost = 2
            else:
                cost = closed[parentIndex][4]+1

            #parentIndex = the current node's index
            parentIndex = visited[3]

            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h3(b, ld)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n)+cost of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % i)
                                break #end iteration
                            #if h(n)+cost of the node in OPEN queue is equal to the h(n)+cost of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i+1, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % (i+1))
                                break #end iteration
                                continue
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n)+cost is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h+cost)
                        open+=[child]
                        # print("Adding to the end of OPEN Queue")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h+cost)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
                # print("Moved next node in OPEN to VISITED")
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    #find the actual path by tracking the parent node
    if(found == True and closed !=[]):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)

        pl=len(path)-1
        # print("The length of the path: %.1d" % (len(path)-1))
    
    elif(found == True and closed == []):
        path = [goalstate]
        # print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)
    
    else:
        pl = 0
        # print("No Solution is found")     
    
    return runtime, path, pl, explored

def astar_h4(brd,grd):
    open = []
    closed = []
    finished = False
    found = False
    res = False
    o_res = False
    added = False
    addOpen = False
    vopen = False
    cost = 0
    valid = True
    path = []
    
    explored = 0

    #index in the closed set to keep track of the path
    parentIndex = 0
    idx = 0

    #to calculate the runtime
    start = time.time()

    #each node passed in the queues = a tuple where the elements are: (board, parent state's index, cost)
    #current configuration: visited = [(S, 0, 0)], open = [], closed = () 
    # S = initial game state, initialise the visited board
    source = (brd, grd, parentIndex, idx, cost, valid, board.h4(brd))
    visited = source
    # print("Initial Game Board")
    # print(board.brdToGrd(brd))
    # print()


    while(not finished):

        #verify if the state in visited is a goal state
        if(board.goal(visited[0]) == True):
            stop = time.time()
            # print("TRUE: Goal Found")
            goalstate = visited
            finished = True
            found = True
            break #stop while loop

        # if current node is not a goal state,
        # find a list of next possible moves from the current state in visited
        nextMove, nextGrid = board.explore_moves(visited[0], visited[1])
   
        #if there is no next move even though we did not reach the goal, there is no solution
        if(nextMove == []):
            stop = time.time()
            # print("No solution")
            finished = True
            found = False
            break #stop while loop

        #calculate cost for every move
        if (nextMove != []):
            if(closed == []):
                cost=1
            elif(visited[3] == 1):
                cost = 2
            else:
                cost = closed[parentIndex][4]+1

            #parentIndex = the current node's index
            parentIndex = visited[3]

            #for each children node:
            for i in range(len(nextMove)):
                b = nextMove[i]
                g = nextGrid[i]
                h = board.h4(b)

                #verify if the children node is in goal state
                if(board.goal(b) == True):
                    # print("TRUE: Goal state found")
                    goalstate = (b, g, parentIndex, idx+1, 0)
                    closed+=[goalstate]
                    visited = []
                    stop = time.time()
                    finished = True
                    found = True
                    break

                #if the children node is not in goal state, must add it into open queue
                else:
                    #verify whehter the children node is already in the closed queue
                    for node in closed:
                        ng = node[1]
                        for k in range(6):
                            for j in range(6):
                                if(ng[k][j] == g[k][j]):
                                    res = True
                                else:
                                    res = False
                                    break #stop inner for loop if inequality
                            if(res == False):
                                break #stop outer for loop in case of inequality
                        if(res == True):
                            break #stop iteration over CLOSED queue

                    #after the grid check on all nodes of CLOSED, if res = False, then verify OPEN Queue
                    if(res == False):
                        vopen = True
                    else:
                        # print("***Board Already in CLOSED Queue***Skipping")
                        vopen = False

                    #verifying open queue
                    if(vopen == True):                
                        for node in open:
                            ng = node[1]
                            nh = node[4]
                            for k in range(6):
                                for j in range(6):
                                    if(ng[k][j] == g[k][j]):
                                        o_res = True
                                    else:
                                        o_res = False
                                        break #stop inner for loop if inequality
                                if(o_res == False):
                                    break #stop outer for loop in case of inequality
                            
                            if(o_res == True):
                                break #stop iteration over OPEN queue in case of equality

                        #after grid check on all nodes of OPEN queue, if o_res = False, then we can add the new child node to the Open
                        if(o_res == False):
                            addOpen = True
                        
                        #if o_res = True, then the same node is already in OPEN queue
                        else:
                            addOpen = False

                    #Adding child node into OPEN queue depending on h(n)
                    if(addOpen == True and vopen == True):
                        for i in range(len(open)):
                            nh = open[i][4]
                            #if h(n)+cost of the node in OPEN queue is greater, then place the child node before 
                            if(nh > h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % i)
                                break #end iteration
                            #if h(n)+cost of the node in OPEN queue is equal to the h(n)+cost of the child node
                            #place the child node after, since the path to the child node is longer
                            elif(nh == h+cost):
                                child = (b, g, parentIndex, idx, h+cost)
                                open.insert(i+1, child)
                                added = True
                                # print("Adding to the OPEN Queue at index %.1d" % (i+1))
                                break #end iteration
                                continue
                            # if h(n) of the child node is greater, continue iteration 
                            else:
                                added = False
                                continue
                    
                    #if the child node's h(n)+cost is the greatest, append as the last element of the OPEN queue
                    if(added == False and addOpen == True and vopen == True):
                        child =(b, g, parentIndex, idx, h+cost)
                        open+=[child]
                        # print("Adding to the end of OPEN Queue")
                    
                    #if the same node is already in OPEN queue, the path of the child node will be longer
                    # child node appended in CLOSED Queue
                    elif(addOpen == False and vopen == True):
                        idx = len(closed)
                        child = (b, g, parentIndex, idx, h+cost)
                        closed += [child]
                        added = True
                        break #end iteration

            #after verifying each child node
            #empty list of children nodes
            nextMove.clear()
            nextGrid.clear()

            #index of the next visited node will be the length of the current CLOSED queue (before appending the next node)
            idx = len(closed)

            #append the current(visited) node to CLOSED queue
            closed.append(visited)

            if(open != []):
                #append next node in the OPEN queue to visited and delete the same element from the OPEN queue
                bd = open[0][0]
                gd = open[0][1]
                pd = open[0][2]
                hd = open[0][4]
                visited = (bd, gd, pd, idx, hd)
                explored = explored + 1
                open.pop(0)
                # print("Moved next node in OPEN to VISITED")
            else:
                stop = time.time()
                # print("OPEN queue empty. No solution")
                finished = True
                found = False


    #as result, we should display:
    runtime = stop-start
    # print("Runtime: %.3f s" % runtime)
    
    #find the actual path by tracking the parent node
    if(found == True and closed != []):
        path = [goalstate]
        currentNode = goalstate
        while(currentNode[3] != 0):
            #get the state at the index of the parent node of the current node
            i = currentNode[2]
            path.insert(0, closed[i])
            currentNode = closed[i]
    
        #lastly, we insert the initial_state in the beginning of the path
        path.insert(0, source)
        pl = len(path)-1
        # print("The length of the path: %.1d" % (len(path)-1))
    
    elif(found == True and closed == []):
        path = [goalstate]
        # print("The length of the path:  %.1d" % (len(path)))
        pl = len(path)
    
    else:
        pl = 0
        # print("No Solution is found")     
    
    return runtime, path, pl, explored