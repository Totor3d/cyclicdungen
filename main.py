import vertexPhysics
import rectsPhysics
import physics
import gridprinter
import doors
import mapPlanner

graph = mapPlanner.createPlan()

#graph = [(0, 1), (1, 2), (2, 0), (3, 4), (3, 6), (4, 6), (6, 5), (6, 0)]
positions = vertexPhysics.calcGraphVertexPosition(graph, 200, 15)





rects = []

for i in positions:
    rects.append(physics.Rectangle(physics.Vector2(i[0], i[1]), physics.Vector2(8, 8)))

rectsPositions = rectsPhysics.calcRectsPosition(rects, 300, graph)

points = []
for i in range(len(positions)):
    points.append((rectsPositions[i].position.x, rectsPositions[i].position.y, i))



rectsForPrint = []

for i in rectsPositions:
    rectsForPrint.append((i.position.x, i.position.y, i.size.x, i.size.y))

grid = gridprinter.drawRectanglesOnGrid(rectsForPrint)
grid = gridprinter.setPointsOnGrid(points, grid)

doors = doors.calcDoorsPositions(graph, points)
grid = gridprinter.setPointsOnGrid(doors, grid)

gridprinter.printGrid(grid)
