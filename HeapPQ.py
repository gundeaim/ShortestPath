import math


class HeapPQ(object):
    def __init__(self, S):
        h = [] #same as data items

    def makeHeap(self, S):
        for x in S: #run through the size given
            self.h[self.h + 1] = x #adds items to the Binary Heap
        for i in range (len(S) - 1, 0, -1): #range of length of S down to 0
           self.siftDown(self.h, self.h[i], i) #calls sift down to place them in correct order


    #returns boolean if there are no more elements in the queue TC: O(1) SC: O(1)
    def isEmpty(self):
        def isEmpty(self):
            return len(self.list) == 0

    # takes a node and inserts it into the list in the right spot based off distance
    # TC: O(log|V|) SC: O(V)
    def insert(self, x, data):
        cardinalityOfH = len(self.h) #TC:O(1) SC:O(1)
        self.bubbleUp(self.h, x, cardinalityOfH + 1) #TC: O(log|V|) SC: O(1)

    #will reorginaze nodes and then delete the previous root node
    #TC: O(log|V|) SC: O(1)
    def deleteMin(self, distance):
        cardinalityOfH = len(self.h)  #TC:O(1) SC:O(1)
        if cardinalityOfH == 0: #TC:O(1) SC:O(1)
            return None #TC:O(1) SC:O(1)
        else:
            x = self.h[0] #TC:O(1) SC:O(1)
            self.siftDown(self.h, self.h[cardinalityOfH], 1) #TC: O(log|V|) SC: O(1)
            return x #TC:O(1) SC:O(1)

    # will reorginaze nodes based on new key value
    #TC: O(log|V|) SC: O(1)
    def decreaseKey(self, x):
        inverseOfH = self.h #TC:O(1) SC:O(1)
        self.bubbleUp(self.h, x, inverseOfH) # rearranges heap based on new key TC: O(log|V|) SC: O(1)

    #will move an element up to it's new position in the binary heap
    #TC: O(log|V|) SC: O(1)
    def bubbleUp(self, h, x, i):
        p = math.ceil(i/2) #TC:O(1) SC:O(1) even though we are dividing we have fixed size for i
        while i != 1 and h[p] > h[x]: #TC: O(log|V|) SC: O(1)
            h[i] = h[p]  #TC:O(1) SC:O(1)
            i = p #TC:O(1) SC:O(1)
            p = math.ceil(i/2) #TC:O(1) SC:O(1) even though we are dividing we have fixed size for i
        h[i] = x #TC:O(1) SC:O(1)

    # TC: O(log|V|) SC: O(1)
    def siftDown(self, h, x, i):
        c = self.minchild(h, i) #TC:O(1) SC:O(1)
        while c != 0 and h[c] < h[x]:
            h[i] = h[c] #TC:O(1) SC:O(1)
            i = c #TC:O(1) SC:O(1)
            c = self.minchild(h, i) #TC: O(log|V|) SC: O(1)
        h[i] = x  #TC:O(1) SC:O(1)

    #finds the child with the lowest index TC: O(log|V|) SC: O(1)
    def minchild(self, h, i):
        if 2*i > len(h):
            return 0
        else:
            argmin = h[i]
            return argmin