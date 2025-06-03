import random
from vertexPhysics import getNeighbour

import networkx as nx
import matplotlib.pyplot as plt

n = 0

class Room:

    def __init__(self, difficulty = 0, neighbours = []):
        global n
        self.identifier = n
        n += 1
        self.difficulty = difficulty

    def toString(self):
        return str(self.identifier) + " - " + str(self.difficulty)

def allRoomsFromGraph(roomsGraph):
    rooms = []
    for i in roomsGraph:
        if i[0] not in rooms:
            rooms.append(i[0])
        if i[1] not in rooms:
            rooms.append(i[1])
    return rooms

def setIdentifiers(rooms):
    for i in range(len(rooms)):
        rooms[i].identifier = i

def getCandidates(roomsGraph):
    candidates = []
    rooms = allRoomsFromGraph(roomsGraph)
    for room in rooms:
        if len(getNeighbour(room, roomsGraph)) == 2 and room.identifier != 0 and room.identifier != 1:
            candidates.append(room)
    return candidates

def roomsGraphToNumGraph(roomsGraph):
    numGraph = []
    for i in roomsGraph:
        numGraph.append((i[0].identifier, i[1].identifier))
    
    return numGraph

def preparePlace(roomsGraph, candidate):
    global n

    resultRoomsGraph = []
    for i in roomsGraph:
        if i[0] != candidate and i[1] != candidate:
            resultRoomsGraph.append(i)
        else:
            if i[0] == candidate:
                B = i[1]
                sourceRoom = i[0]
            if i[1] == candidate:
                A = i[0]
                sourceRoom = i[1]

    return (resultRoomsGraph, A, B, sourceRoom)
    

def rule1(roomsGraph, A, B, sourceRoom):
    resultRoomsGraph = roomsGraph

    room1 = Room(sourceRoom.difficulty)
    room2 = Room(sourceRoom.difficulty)

    roomsGraph.append((A, room1))
    roomsGraph.append((room1, B))
    roomsGraph.append((A, room2))
    roomsGraph.append((room2, B))

    return resultRoomsGraph

def rule2(roomsGraph, A, B, sourceRoom):
    resultRoomsGraph = roomsGraph

    room1 = Room(sourceRoom.difficulty/2)
    room2 = Room(sourceRoom.difficulty/2)

    roomsGraph.append((A, room1))
    roomsGraph.append((room1, room2))
    roomsGraph.append((room2, B))


    return resultRoomsGraph

def debugPrint(graph):
    graphWithStr = []
    for i in graph:
        graphWithStr.append((i[0].toString(), i[1].toString()))
    G = nx.Graph()
    G.add_edges_from(graphWithStr)
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue", alpha=0.8)
    
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.5, edge_color="gray")
    
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def createPlan(difficulty = 100, iterations = 5):
    
    startRoom = Room()
    finishRoom = Room()

    rootRoom = Room(difficulty)
    
    graph = [(startRoom, rootRoom), (rootRoom, finishRoom)]

    for i in range(iterations):
        candidate = random.choice(getCandidates(graph))
        preparedPlaceGraph, A, B, sourceRoom = preparePlace(graph, candidate)
            
        print(len(getNeighbour(candidate, graph)))
        if random.randint(0, 10) < 7:
            graph = rule1(preparedPlaceGraph, A, B, sourceRoom)
        else:
            graph = rule2(preparedPlaceGraph, A, B, sourceRoom)
    setIdentifiers(allRoomsFromGraph(graph))
    print(roomsGraphToNumGraph(graph))
    debugPrint(graph)
    
    return roomsGraphToNumGraph(graph)


if __name__ == "__main__":
    createPlan()
