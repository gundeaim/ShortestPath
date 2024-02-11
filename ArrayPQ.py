class ArrayPQ(object):
    def __init__(self):
        self.list = []

    #returns boolean if there are no more elements in the queue
    def isEmpty(self):
        return len(self.list) == 0

    #takes a node and inserts it into the list
    #TC: O(1) SC: O(V)
    def insert(self, data):
        self.list.append(data) #appends to the list TC: O(1) #SC: O(1)

    #Total TC: O(|V|) SC: O(1)
    def deleteMin(self, distance):
        #sets intial variables
        minimumVal = float('inf') #SC: O(1) TC: O(1)
        minimumIndex = 0 #SC: O(1) TC: O(1)
        iteration = 0 #SC: O(1) TC: O(1)

        for node in self.list: #goes through all nodes in the list to find the one with
            # the lowest distance in the distance array TC: O(V) TC:O(1)
            distanceIndex = node.node_id #SC: O(1) TC: O(1)
            #updates shortest distance and the index found if it finds a distance that is smaller than the
            #previous distance found
            if distance[distanceIndex] < minimumVal: #SC: O(1) TC: O(1)
                minimumVal = distance[distanceIndex] #SC: O(1) TC: O(1)
                minimumIndex = iteration #SC: O(1) TC: O(1)
            iteration = iteration + 1 #SC: O(1) TC: O(1)
        nodeIndex = self.list[minimumIndex].node_id #SC: O(1) TC: O(1)
        del self.list[minimumIndex] #removes the minimum found from the PQ SC: O(1) TC: O(1)
        return nodeIndex #SC: O(1) TC: O(1)

    def decreaseKey(self, nodeIndex):
        pass #O(1) for both TC & SC

