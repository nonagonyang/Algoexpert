#Branch Sums
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums=[]
    helper(root, 0, sums)
    return sums

def helper(node, runningSum,sums):
    if node is None:
        return
    newRunningSum=runningSum+node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return 
    helper(node.left, newRunningSum, sums)
    helper(node.right,newRunningSum, sums)
    



#Given a binary tree, calculate sum of each node's depth
#each node's depth is how many edges it needs travel to arrive root node. 

# compute each node's depth and add them together
# each node's depth depends on its parent's depth
# one way to think about this question is to have parent passing down depth to its children
# f(node, depth)=depth+ f(node.left, depth+1)+ f(node.right, depth+1)
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth+nodeDepths(root.left, depth+1)+ nodeDepths(root.right, depth+1)
   

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Given a bianry tree, return a mirroring or inverted binary tree
#swap every right node with left node

#Solution1
#Iterative soloutin using breadth first search
#in order to do breadth first search, we use a queue to
#keep track of which node we should explore the next
#start from the root
#swap its children
#start from the root's left and swap its children
def invertBinaryTree(tree):
    queue=[tree]
    while len(queue):
        current=queue.pop(0)
        if current is None:
            continue
        swapLeftRight(current)
        queue.append(current.left)
        queue.append(current.right)
def swapLeftRight(tree):
    tree.left, tree.right=tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Solution2
def invertBinaryTree(tree):
    if tree is None:
        return 
    swapLeftRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    
def swapLeftRight(tree):
    tree.left, tree.right= tree.right, tree.left
    
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Given a binary tree, return its diameter
#diameter is the length of the longest path
#a path is a collection of connected nodes
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter
    
def getTreeInfo(tree):
    if tree is None: 
        return TreeInfo(0,0)
        
    leftTreeInfo=getTreeInfo(tree.left)
    rightTreeInfo=getTreeInfo(tree.right)
    
    longestPathThroughRoot=leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar=max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter=max(maxDiameterSoFar, longestPathThroughRoot)
    currentHeight=1+max(leftTreeInfo.height, rightTreeInfo.height)
    return TreeInfo(currentDiameter, currentHeight )
class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter=diameter
        self.height=height