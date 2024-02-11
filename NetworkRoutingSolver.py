#!/usr/bin/python3
import ArrayPQ
import HeapPQ
from CS312Graph import *
import time


class NetworkRoutingSolver:
    def __init__( self, distance=[], prev=[]):
        self.distance = distance
        self.prev = prev
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network


    def getShortestPath( self, destIndex ):
        self.dest = destIndex

        #initial variable setup
        path_edges = []
        total_length = 0
        currIndex = destIndex
        if self.prev[currIndex] is None: #this means the point isn't reachable from S
            return
        else:
            #while loop moves backwards from destination point until it hits the start node
            while currIndex != self.source:
                #finds the correct neighbour based on the index listed in prev array
                for neighbour in self.network.nodes[self.prev[currIndex]].neighbors:
                    if neighbour.dest.node_id == currIndex:
                        edge = neighbour
                # add found edge to the list of edges
                path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
                #adds edge length just found to total length
                total_length += edge.length
                currIndex = self.prev[currIndex] #updates index we are at
            return {'cost':total_length, 'path':path_edges}

    def dijkstrasAlgorithm(self, use_heap):
        self.prev.clear() #clear class arrays used from problem to problem
        self.distance.clear()
        use_heap = False #set which PQ we use
        if use_heap:
            PQ = HeapPQ.HeapPQ()
        else:
            PQ = ArrayPQ.ArrayPQ()
        for node in self.network.nodes:
            self.distance.append(float('inf')) #place all nodes in distance array
            self.prev.append(None) #place all nodes in previous array
            if node.node_id == self.source:
                self.distance[node.node_id] = 0 #set S node distance to 0
            PQ.insert(node) #insert each node into the priority Queue

        #while loop finds distance from S to every node
        while not PQ.isEmpty():
            nodeIndex = PQ.deleteMin(self.distance) #deletes node with smallest distance from the PQ.
            #checks each neighbour for the shortest path from the current node
            for neighbor in self.network.nodes[nodeIndex].neighbors:
                #updates shortest distance if it finds a neighbour with a distance smaller than previous
                #distance found
                if self.distance[neighbor.dest.node_id] > self.distance[nodeIndex] + neighbor.length:
                    self.distance[neighbor.dest.node_id] = self.distance[nodeIndex] + neighbor.length
                    self.prev[neighbor.dest.node_id] = nodeIndex
                    PQ.decreaseKey(nodeIndex)
        return self.distance, self.prev



    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        self.dijkstrasAlgorithm(use_heap)
        t2 = time.time()
        return (t2-t1)

