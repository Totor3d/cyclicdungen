import time
import random
import gridprinter
from physics import Vector2, Body

debug = True


def printBodies(bodies):
    points = []
    for b in bodies:
        v = b.position
        points.append((v.x, v.y, str(b.id)))
    gridprinter.printGrid(gridprinter.setPointsOnGrid(points))

def updateBodies(bodies, delta):
    for b in bodies:
        b.update(delta)



def getNeighbour(v, graph):
    neighbours = []
    for i in graph:
        if i[0] == v:
            neighbours.append(i[1])
        elif i[1] == v:
            neighbours.append(i[0])
    return neighbours

def spring(distance, minDistance):
    return min((distance - minDistance)**3/(100*minDistance), 5)


def addImpulses(bodies, graph, minDistance = 5):
    for b in bodies:
        for b1 in bodies:
            if b != b1:
                if b.id in getNeighbour(b1.id, graph):
                    b.addImpulses((b.position - b1.position)*(spring(b.distance(b1), minDistance)))
                    b.speed = b.speed * 0.92
                else:
                    b.addImpulses((b.position - b1.position)*(1/b.distance(b1))*-1)
                
bodies = []

def addVertexAsBodies(graph):
    el = 0
    for i in graph:
        if i[0] > el or i[1] > el:
            el = max(i[0], i[1])
    for i in range(el + 1):
        bodies.append(Body(random.randint(-10, 10), random.randint(-10, 10), i))

def calcGraphVertexPosition(graph, iterations = 100, minDistance = 5):
    
    addVertexAsBodies(graph)

    for i in range(iterations):
        addImpulses(bodies, graph, minDistance)
        updateBodies(bodies, 0.1)
        if debug:
            print(i)
            printBodies(bodies)
    
    result = []
    for i in sorted(bodies, key=lambda x: x.id):
        result.append((i.position.x, i.position.y))
    
    return result
    
# calcGraphVertexPosition(graph, 100)


if __name__ == "__main__":
    addVertexAsBodies(graph)
    t = 0
    while True:
        addImpulses(bodies)
        updateBodies(bodies, 0.1)
        if debug:
            print(t)
            printBodies(bodies)
        t += 1