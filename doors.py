from vertexPhysics import getNeighbour

def calcDoorsPositions(graph, points):
    doors = []
    for e in graph:
        doors.append(((points[e[0]][0]+points[e[1]][0])/2, (points[e[0]][1]+points[e[1]][1])/2, "D"))
    return doors