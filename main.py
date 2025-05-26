import vertexPhysics
import rectsPhysics
import physics
import gridprinter

graph = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (3, 6), (4, 5), (4, 6), (6, 5), (6, 0)]
positions = vertexPhysics.calcGraphVertexPosition(graph, 100, 20)





rects = []

for i in positions:
    rects.append(physics.Rectangle(physics.Vector2(i[0], i[1]), physics.Vector2(10, 10)))

rectsPositions = rectsPhysics.calcRectsPosition(rects)

points = []
for i in range(len(positions)):
    points.append((rectsPositions[i].position.x, rectsPositions[i].position.y, i))



rectsForPrint = []

for i in rectsPositions:
    rectsForPrint.append((i.position.x, i.position.y, i.size.x, i.size.y))

grid = gridprinter.drawRectanglesOnGrid(rectsForPrint)
grid = gridprinter.setPointsOnGrid(points, grid)

gridprinter.printGrid(grid)
