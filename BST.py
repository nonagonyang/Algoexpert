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




#How to traverse a BST: use recursion!!!

#inorder traverse
#traverse(left)
#array.append(currentValue)
#traverse(right)

#T: O(N)
#S: O(N)+O(D)=> O(N)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left,array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array
   

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array




#Reconstruct a min-height BST based on a sorted array
#a min height BST is a most balanced BST
#we just need to keep finding middle value and make the middle value as the root
# we do not even need to use the provided insert method.

def minHeightBst(array):
    return helper(array, 0, len(array)-1)
def helper(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx= (startIdx + endIdx) // 2
    bst= BST(array[midIdx])
    bst.left=helper(array,startIdx, midIdx-1)
    bst.right=helper(array, midIdx+1, endIdx)
    return bst
    


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)




#find the kth largest value
#since we are trying to find the largest value, 
#we'd probably better do a reverse in order traverse
#we know inorder traverse will give us a sorted array
#the only difficulty is to keep track of where are we in terms of traverse
#are we at the nth node visted?
#what is the latest value we just visited? so if n=k, we can return the visited value
#A new knowledge for me is to keep track of the nth and latest visted node in a class
#it is like a travel log

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


#perform a reversed inorder traverse
#track the number we have visited
#no need for the space of array
#T: O(D+K)
#S: O(H)
class TreeInfo:
    def __init__(self, numVistedNodes,latestVistedNodeValue):
        self.numVistedNodes= numVistedNodes
        self.latestVistedNodeValue= latestVistedNodeValue
        

def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, None)
    reverseInOrderTraverse(tree,k,treeInfo)
    return treeInfo.latestVistedNodeValue
    
def reverseInOrderTraverse(node,k, treeInfo):
    if node is None or treeInfo.numVistedNodes >=k:
        return 
    reverseInOrderTraverse(node.right, k,treeInfo)
    if treeInfo.numVistedNodes < k:
        treeInfo.numVistedNodes += 1
        treeInfo.latestVistedNodeValue = node.value
        reverseInOrderTraverse(node.left,k,treeInfo)


#Reconstruct BST based on pre_order traverse.
