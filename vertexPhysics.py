import time
import random
import gridprinter
from physics import Vector2, Body

debug = True

def getNeighbour(v, graph):
    neighbours = []
    for i in graph:
        if i[0] == v:
            neighbours.append(i[1])
        elif i[1] == v:
            neighbours.append(i[0])
    return neighbours

def printBodies(bodies, graph):
    points = []
    for b in bodies:
        v = b.position
        
        points.append((v.x, v.y, str(b.id)))
    lines = []
    
    for i in range(len(graph)):
        for j in getNeighbour(i, graph):
            lines.append(((bodies[i].position.y, bodies[i].position.x), (bodies[j].position.y, bodies[j].position.x)))

    gridprinter.printGrid(gridprinter.setPointsOnGrid(points, gridprinter.drawLines(lines)))

def updateBodies(bodies, delta):
    for b in bodies:
        b.update(delta)



def spring(distance, minDistance):
    return min(((distance - minDistance)/(minDistance))**3/3, 5)


def addImpulses(bodies, graph, minDistance = 5):
    for b in bodies:
        for b1 in bodies:
            if b != b1:
                if b.id in getNeighbour(b1.id, graph):
                    b.addImpulses((b.position - b1.position)*(spring(b.distance(b1), minDistance)))
                    b.speed = b.speed * 0.92

                b.addImpulses((b.position - b1.position)*(2/b.distance(b1))*-1)
                
bodies = []

def addVertexAsBodies(graph):
    el = 0
    for i in graph:
        if i[0] > el or i[1] > el:
            el = max(i[0], i[1])
    for i in range(el + 1):
        bodies.append(Body(random.uniform(-10, 10), random.uniform(-10, 10), i))


def drawDebug(iterationNum, bodies, graph):
    print(iterationNum)
    printBodies(bodies, graph)

def calcGraphVertexPosition(graph, iterations = 150, minDistance = 5):
    
    addVertexAsBodies(graph)

    for i in range(iterations):
        addImpulses(bodies, graph, minDistance)
        updateBodies(bodies, 0.1)
        if debug:
            drawDebug(i, bodies, graph)
        print(1)
    
    sortedBodies = sorted(bodies, key=lambda x: x.id)

    result = []

    xcenter = 0
    ycenter = 0
    for i in sortedBodies:
        xcenter += i.position.x
        ycenter += i.position.y
    xcenter /= len(sortedBodies)
    ycenter /= len(sortedBodies)


    for i in sortedBodies:
        result.append((i.position.x - xcenter, i.position.y - ycenter))
    
    return result
    
# calcGraphVertexPosition(graph, 100)


if __name__ == "__main__":
    addVertexAsBodies(graph)
    t = 0
    while True:
        addImpulses(bodies)
        updateBodies(bodies, 0.1)
        if debug:
            drawDebug(t, bodies, graph)
        t += 1