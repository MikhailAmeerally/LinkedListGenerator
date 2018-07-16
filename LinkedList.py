import random

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def addNext(self,nextNode):
        self.next = nextNode
    
    def hasNext(self):
        return self.next != None

    def changeValue(self, newValue):
        self.value = newValue


def generateRandomList(ofLength = 5, rangeFrom = 1, rangeTo = 10):

        firstNode = Node(0)
        if rangeFrom > rangeTo:
            rangeFrom, rangeTo = rangeTo, rangeFrom

        if ofLength <= 0:
            return
        pointer = firstNode
        for i in range(ofLength):
            a = random.randint(rangeFrom,rangeTo)
            pointer.changeValue(a)
            pointer.addNext(Node(0))
            pointer = pointer.next;


        return firstNode

def traverse(LinkedList):
    cpy = LinkedList
    while cpy.hasNext():
        print(cpy.value)
        cpy = cpy.next
    print("None")
    
