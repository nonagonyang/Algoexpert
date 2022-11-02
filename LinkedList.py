# Remove duplicates from a sorted linked list

#find the next distinct node
#curentNode's next pointer points to the nextDistinct
#move currentNode to nextDistince

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) Time: look through all the nodes only once
#O(1) Space: keep the nextDistinctNode moving until find a disctinct value
#1->1->3->4->4->4->5->6->6
#*  x  *
def removeDuplicatesFromLinkedList(linkedList):
    currentNode=linkedList
    while currentNode is not None:
        nextDistinctNode=currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            #keep moving forward until find a distinct value
            nextDistinctNode=nextDistinctNode.next
        #once the nextDistinct value is found, connect them with next pointer
        currentNode.next=nextDistinctNode
        #move currentNode to the position of nextDistinctNode and keep moving forward
        currentNode=nextDistinctNode
    return linkedList



#remove Kth node from the end of a singlely linked list
#use two pointers: firt make sure these two pointers have a distance of k
#then move these two pointers together, when the fast pointer reaches the None node, the slow one is at Kth position from the end
#We need to know the node before the node we want to remove
#otherwise we don't have a way to remove the node we want to remove
#Another thing learnt is that how to remove head of a linkedlist
#update the value of head with the value of head.next
#remove head.next node
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    slow=head
    fast=head
    counter=1
    #inclusive
    while counter <= k:
        fast=fast.next
        counter +=1
    if fast is None:
        #remove head
        #update the value of head, and remove the node after head node
        head.value=head.next.value
        head.next=head.next.next
        return
    # this while loop will break if fast.next is at None
    # and the slow pointer is at the node before the node we want to remove
    while fast.next is not None:
        #move two pointers together
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next



#Sum of two linkedlists
#use linkedlist to represent integer
# 1->2->3 means 321
# 1->4 means 41
#return 1->6->3
#node, value, linkedlist
#linkedlist can be represented by its head
#having a head of a linkedlist means having the whole linkedlist accessible
#create a new linkedlist needs LinkedList class and value to be inserted into the new linkedlist

#Time: O(max(L1,L2))
#Space: O(max(L1,L2))
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    #keep modifying this variablle
    carry=0
    dummy=LinkedList(None)
    currentNode=dummy
    
    #head is bascially the linkedlist itself
    #the linkedlist is bascially the head
    nodeOne=linkedListOne
    nodeTwo=linkedListTwo
    
    while nodeOne is not None or nodeTwo is not None or carry !=0:
        valueOne= nodeOne.value if nodeOne is not None else 0
        valueTwo= nodeTwo.value if nodeTwo is not None else 0
        sumOfValues=valueOne + valueTwo + carry
        newValue=sumOfValues%10
        newNode=LinkedList(newValue)
        currentNode.next=newNode
        currentNode= newNode
        
        carry=sumOfValues // 10
        nodeOne=nodeOne.next if nodeOne is not None else None
        nodeTwo=nodeTwo.next if nodeTwo is not None else None

    return dummy.next



#Construct a doubly linked list with a bunch of methods
#make sure you reuse the methods
#insertion, removal O(1), grab head, grab tail are all constant time operation.
#traverse takes O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
#5
    def setHead(self, node):
        if self.head is None:
            self.head=node
            self.tail=node 
            return
        self.insertBefore(self.head, node)

#6       

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        self.insertAfter(self.tail,node)

#7    

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)    
        nodeToInsert.next=node
        nodeToInsert.prev=node.prev 
        if node.prev is None:
            self.head=nodeToInsert
        else:
            node.prev.next=nodeToInsert
        node.prev=nodeToInsert
            
#8
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert== self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev=node
        nodeToInsert.next=node.next 
        if node.next is None:
            self.tail= nodeToInsert
        else:
            node.next.prev=nodeToInsert
        node.next=nodeToInsert

    
#9    
    def insertAtPosition(self, position, nodeToInsert):
        if position ==1:
            self.setHead(nodeToInsert)
            return
        #traverse until we arrive the position
        node=self.head
        currentPosition=1
        while node is not None and currentPosition != position:
            node=node.next
            currentPosition +=1
        if node is not None:
            self.insertBefore(node,nodeToInsert)
        else:
            self.setTail(nodeToInsert)
            
        
#4
    def removeNodesWithValue(self, value):
        #find the node with the value in the linkedlist
        #remove the node
        node=self.head
        while node is not None:
            #keep track of the node to be removed
            nodeToRemove=node
            #keep track of the pointer 
            node=node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
                     
#3 Remove, update surrounding pointers first then delete the toBeRemoved value's pointers later         

    def remove(self, node):
        #deal with situtations where we will remove head, update new head
        #deal with situations where we will remove tail, update new tail
        if node==self.head:
            self.head =self.head.next
        if node == self.tail:
            self.tail=self.tail.prev
        self.removeNodePointers(node)
              
#1
    def containsNodeWithValue(self, value):
        #traverse the linkedlist to find a node has the targeted value
        node =self.head
        while node is not None and node.value !=value:
            node=node.next
        return node is not None
        
 #2   
    def removeNodePointers(self, node):
        #update the pointers of surrounding node
        #remove the node pointers
        if node.prev is not None:
            node.prev.next=node.next
        if node.next is not None:
            node.next.prev=node.prev
        node.prev=None
        node.next=None
        #now our node is completely alone
        