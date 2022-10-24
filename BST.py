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