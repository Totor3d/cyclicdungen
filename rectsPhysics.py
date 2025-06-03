from physics import Vector2, Rectangle, Body, addGravityForces
from vertexPhysics import getNeighbour
import gridprinter
import math

debug = True


def addForces(bodies, power):
    for b in bodies:
        b.addImpulses((bodies[len(bodies)//2].position - b.position)*-1)

def calcRectsPosition(rects, iterations = 150, graph = []):

    bodies = []

    for i in range(len(rects)):
        bodies.append(Body(rects[i].position.x, rects[i].position.y, i))
    addForces(bodies, 500)
    for iteration in range(iterations):
        
        for i in bodies:
            i.update(0.005)
        for i in range(len(rects)):
            for j in range(len(rects)):
                if rects[i].isItColliding(rects[j]):
                    # rects[i].grow = False
                    # rects[j].grow = False
                    # rects[i].size = rects[i].size * (1/1.001)
                    if i != j:
                        #bodies[i].powerInfluence = 1
                        #bodies[i].speed = bodies[i].speed * 0.998

                        x = bodies[i].position.x
                        y = bodies[i].position.y
                        
                        x1 = rects[j].size.x
                        y1 = rects[j].size.y
                        

                        #if abs(x/y) < abs(x1/y1):
                        # bodies[i].speed.y = 0
                        # bodies[i].speed.x = 0
                        mid = (bodies[i].speed + bodies[j].speed) * 0.5
                        bodies[i].speed = mid
                        bodies[j].speed = mid
                # else:
                #     bodies[i].powerInfluence = 1
                #     bodies[i].speed = bodies[i].speed * 1
                # else:
                #     rects[i].grow = True
                
                # if rects[i].grow:
                #     rects[i].size = rects[i].size * 1.001
            bodies[i].speed = bodies[i].speed * 0.995

            rects[i].position = bodies[i].position

        if debug:
            rectsTransforms = []
            for i in rects:
                rectsTransforms.append((i.position.x, i.position.y, i.size.x, i.size.y))

            lines = []
    
            for i in range(len(graph)):
                for j in getNeighbour(i, graph):
                    lines.append(((bodies[i].position.y, bodies[i].position.x), (bodies[j].position.y, bodies[j].position.x)))
            
            points = []
            for i in range(len(rects)):
                points.append((rects[i].position.x, rects[i].position.y, i))
            gridprinter.printGrid(gridprinter.setPointsOnGrid(points, gridprinter.drawRectanglesOnGrid(rectsTransforms, gridprinter.drawLines(lines))))
    
    xcenter = 0
    ycenter = 0
    for i in rects:
        xcenter += i.position.x
        ycenter += i.position.y
    xcenter /= len(rects)
    ycenter /= len(rects)

    for r in rects:
        r.position.x -= xcenter
        r.position.y -= ycenter 

    return rects