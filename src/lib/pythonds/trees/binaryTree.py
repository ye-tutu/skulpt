# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 

class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.
    """    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self,):
        return self.key

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)


    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def printexp(self):
        if self.leftChild:
            print('(')
            self.leftChild.printexp()
        print(self.key)
        if self.rightChild:
            self.rightChild.printexp()
            print(')')

    def postordereval(self):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        res1 = self.leftChild.postordereval() if self.leftChild else None
        res2 = self.rightChild.postordereval() if self.rightChild else None
        return opers[self.key](res1,res2) if res1 and res2 else self.key

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    if tree.leftChild:
        print('(')
        printexp(tree.getLeftChild())
    print(tree.getRootVal())
    if tree.rightChild:
        printexp(tree.getRightChild())
        print(')') 

def printexp(tree):
    sVal = ""
    if tree:
        sVal = f'({printexp(tree.getLeftChild())}'
        sVal += str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())  #// \label{peleft}
        res2 = postordereval(tree.getRightChild()) #// \label{peright}
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2) #// \label{peeval}
        else:
            return tree.getRootVal()

def height(tree):
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.leftChild),height(tree.rightChild))

# t = BinaryTree(7)
# t.insertLeft(3)
# t.insertRight(9)
# inorder(t)
# import operator
# x = BinaryTree('*')
# x.insertLeft('+')
# l = x.getLeftChild()
# l.insertLeft(4)
# l.insertRight(5)
# x.insertRight(7)
# print(printexp(x))
# print(postordereval(x))
# print(height(x))
