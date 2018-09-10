# Assignment 1
import math

#################################
# Problem 1
#################################
# Objectives:
# (1) Write a recursive function to compute the nth fibonacci number

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib2(n)
    pass

def fib2(n):
    return fib(n-1) + fib(n-2)
    pass

#################################
# Problem 2
#################################
# Objectives:
# (1) Write a function which returns a list of the first and last items in a given list

def firstLast(n):
    if len(n) == 0: return n
    elif len(n) == 1: return n
    else: return [n[0],n[len(n) - 1]]
    pass




#################################
# Problem 3
#################################
# Objectives:
# (1) Write a function which takes a matrix and returns the transpose of that matrix
# Note: A matrix is represented as a 2-d array: [[1,2,3],[4,5,6],[7,8,9]]


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        if rows < cols:
            temp = [[0 for x in range(rows)] for y in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    if i < len(matrix):
                        temp[j][i] = matrix[i][j]
                return temp
    temp = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            temp[j][i] = matrix[i][j]
    return temp
    pass





#################################
# Problem 4
#################################
# Objectives:
# (1) Write a function which takes two points of the same dimension, and finds the euclidean distance between them
# Note: A point is represented as a tuple: (0,0)

def euclidean(p1,p2):
    if len(p1) == 3: return math.sqrt(((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2))
    else: return math.sqrt(((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))
    pass





#################################
# Problem 5
#################################

# A Node is an object
# - value : Number
# - children : List of Nodes
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


exampleTree = Node(1,[Node(2,[]),Node(3,[Node(4,[Node(5,[]),Node(6,[Node(7,[])])])])])



# Objectives:
# (1) Write a function to calculate the sum of every node in a tree (iteratively)

def sumNodes(root):
    if len(root.children) == 0:
        return root.value
    else:
        sum = root.value
        list1 = []
        list1.append(root.children)
        i = 0
        while True:
            for x in list1[i]:
                sum = sum + x.value
                list1.append(x.children)
            i += 1
            if i == len(list1):
                break
        return sum
    pass

# (2) Write a function to calculate the sum of every node in a tree (recursively)

def sumNodesRec(root):
    sum = 0
    if len(root.children) == 0:
        sum += root.value
        return sum
    else:
        sum += root.value + sumNodesRec2(root)
        return sum
    pass
def sumNodesRec2(root):
    sum = 0
    for x in root.children:
        sum += sumNodesRec(x)
    return sum
    pass






#################################
# Problem 6
#################################
# Objectives:
# (1) Write a function compose, which takes an inner and outer function
# and returns a new function applying the inner then the outer function to a value

def compose(f_outer, f_inner):
    return lambda x: f_outer(f_inner(x))
    pass





#################################
# Bonus
#################################
# Objectives:
# (1) Create a string which has each level of the tree on a new line

def treeToString(root):
    string = ""
    if len(root.children) == 0:
        string += str(root.value)+ "\n"
    else:
        string += str(root.value) + "\n"
        list1 = []
        temp = []
        list1.append(root.children)
        i = 0
        while True:
            for x in list1[i]:
                temp.append(x.value)
                list1.append(x.children)
            i += 1
            if len(temp) > 0:
                string += ''.join(str(e) for e in temp) + "\n"
            temp = []
            if i == len(list1):
                break
    return string
    pass

