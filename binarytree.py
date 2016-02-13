# Binary search tree implementation
# Author: SmushBall
# Date: Feb 11, 2016
# Some good reasons to use Binary tree
# -- When Input data size is unknown
# -- Input data is highly dynamic with significant number of insertins/deletions

# Issues: When a BST is constructed and modieifed, it may become unbalanced.




class BinaryNode:
    def __init__(self, value = None):
        """ create binary node """
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        """ Add a new node to the tree containing this tree """
        if val <= self.value: # Check that value is left than root node. If yes , it goes left side
            if self.left:
                self.left.add(val) # Check that left node exists
            else:
                self.left = BinaryNode(val) # create left node as it doesn't exist      
        else:
            if self.right: # If right node exists, then add under it
                self.right.add(val)
            else:
                self.right = BinaryNode(val) # right node doesn't exist, so create it   


class BinaryTree:
    def __init__(self): # This is a constructor called when an object is initiated
        """Create empty binary tree"""
        self.root = None 

    def add(self, value):
        """ Insert value into proper location in binary tree """
        if self.root is None: # if root node is not there , then add a root node
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    
    def contains(self, target):
        """ check whether bst contains target value"""
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False        



import random
from time import time

def performance(): 
    """ Demostrate execution performance """
    n = 1024
    while n <= 65536:
        bt = BinaryTree()
        for i in range(n):
            bt.add(random.randint(i,n))        
        now = time()
        x = random.randint(1,n)
        bt.contains(x)
        print("The random number is {}".format(x)) 
        print(n, (time() - now)*1000)

        n *= 2   