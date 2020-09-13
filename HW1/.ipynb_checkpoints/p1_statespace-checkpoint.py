################################################################################
#
# Course: CS 540, fall 2020
# Homework: HW1
# Date 9/13/2020
# Name: Samuel Kruse
#
################################################################################
#returns a copy of state which fills the jug corresponding to the 
#index in which (0 or 1) to its maximum capacity. Do not modify state.

def copy(state):
    sn = [0,0]
    sn[0] = state[0]
    sn[1] = state[1]
    return sn

def fill(state, max, which):
    s1 = copy(state)
    s1[which] = max[which]
    return s1

 # — returns a copy of state which empties the jug corresponding to the
#index in which (0 or 1). Do not modify state.
def empty(state, max, which):
    s1 = copy(state)
    s1[which] = 0
    return s1
    
 #— returns a copy of state which pours the contents of the jug at index 
#source into the jug at index dest, until source is empty or dest is full. Do not modify state. xfer is shorthand for transfer.
def xfer(state, max, source, dest):
    s1 = copy(state)
    sumDest = s1[source] + s1[dest]
    if sumDest >= max[dest]:
        s1[source] = sumDest - max[dest]
        s1[dest] = max[dest]
    else:
        s1[dest] = sumDest
        s1[source] = 0
    
    return s1

#— prints the list of unique successor states of the current state in any order. 
#This function will generate the unique successor states of the current state by applying fill, empty, xfer operations on the current state. (Note: You have to apply an operation at every step for generating a successor state.)
def succ(state, max):
    s0 = copy(state)
    stateSpace = []
    
    
    if s0[0] != max[0]:
        s = fill(s0,max,0)
        stateSpace.append(s)
        
    s1 = fill(s0,max,1)
    if s1 not in stateSpace and s0[1] != max[1]:
        stateSpace.append(s1)

    s2 = empty(s0, max,0)
    if s2 not in stateSpace and s0[0] != 0:
        stateSpace.append(s2)
        
    s3 = empty(s0, max,1)    
    if s3 not in stateSpace and s0[1] != 0:
        stateSpace.append(s3)
        
    s4 = xfer(s0, max, 1, 0)    
    if s4 not in stateSpace and s0[1] != 0:
        stateSpace.append(s4)
        
    s5 = xfer(s0, max, 0, 1)
    if s5 not in stateSpace and s0[0] != 0:
        stateSpace.append(s5)

    for states in stateSpace:
        print(states)
    
