# Given BST and a target value, 
# write a function to find the closest value to the target value contained in BST 

#ask each node.
#Are you by far the closest node? 
#Tell me: left or right

def findClosestValueInBst(tree, target):
    return helper(tree, target, float("inf"))
def helper(tree, target, closest_candidate):
    #base case
    if tree is None:
        return closest_candidate
    #when to update the closest_candidate
    if abs(tree.value-target) < abs(closest_candidate-target):
        closest_candidate=tree.value
    #how to decide traverse direction: left or right
    if target < tree.value:
        return helper(tree.left, target, closest_candidate)
    elif target > tree.value:
        return helper(tree.right, target, closest_candidate)
    else:
        return closest_candidate


#iterative solution
def findClosestValueInBst(tree, target):
    return helper(tree, target, float("inf"))
def helper(tree, target, closest_candidate):
    currentNode=tree
    while currentNode:
        if abs(target-closest_candidate) > abs(target-currentNode.value):
            closest_candidate=currentNode.value
        if target < currentNode.value:
            currentNode=currentNode.left
        elif target > currentNode.value:
            currentNode=currentNode.right
        else:
            break
    return closest_candidate


#Check if a tree is a valid BST

#from top to bottom check if current node is None
#check if its left tree is valid BST and check if its right tree is BST
# This is an input class. Do not edit.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#divide and conquer
#validate any node's left and right trees
#each node has a minimal value and maximum value
#left node < direct parent
#updating min and max when traversing the tree
#gradually narrow down the min and max of node.
#T: O(N) need to traverse every node in the tree
#S: O(log(N)) using space on call stack O(D), D is the depth of the tree.

def validateBst(tree):
    return helper(tree, float("-inf"),float("inf"))
def helper(tree, min, max):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    #check subtrees validity
    leftIsValid=helper(tree.left, min, tree.value)
    rightIsValid=helper(tree.right,tree.value,max)
    return leftIsValid and rightIsValid