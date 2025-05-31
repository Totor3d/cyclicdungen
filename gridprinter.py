import os
import time
import math

void = " "

size = 60
zoom = 2

delay = 0.01

def getPosOnGrid(x, y):
    return (size//2+(math.floor(x))//zoom, size//2+(math.floor(y))//zoom)

def printGrid(grid):
    for i in grid:
        print(*i)
    time.sleep(delay)


def setPointsOnGrid(points, grid = None):
    if not grid:
        grid = [[void for x in range(size)] for y in range(size)]
    
    for x, y, s in points:
        try:
            gx, gy = getPosOnGrid(x, y)
            grid[gx][gy] = s
        except IndexError:
            pass
    return grid

def drawRectanglesOnGrid(rectangles, grid = None):
    if not grid:
        grid = [[void for x in range(size)] for y in range(size)]
    
    for x, y, w, h in rectangles:
        w = math.floor(w)
        h = math.floor(h)
        try:
            for i in range(w):
                grid[size//2+(math.floor(x) + i - w//2)//zoom][size//2+(math.floor(y) - h//2)//zoom] = "#"
            for i in range(w):
                grid[size//2+(math.floor(x) + i - w//2)//zoom][size//2+(math.floor(y) + h//2)//zoom] = "#"
            for i in range(h):
                grid[size//2+(math.floor(x) - w//2)//zoom][size//2+(math.floor(y) + i - h//2)//zoom] = "#"
            for i in range(h):
                grid[size//2+(math.floor(x) + w//2)//zoom][size//2+(math.floor(y) + i - h//2)//zoom] = "#"
            
        except IndexError:
            pass
    
    return grid

def drawLines(points, s="o", grid = None):
    if not grid:
        grid = [[void for x in range(size)] for y in range(size)]
    for p in points:
        point1 = p[0]
        point2 = p[1]
        x1, y1 = getPosOnGrid(point1[0], point1[1])
        x2, y2 = getPosOnGrid(point2[0], point2[1])

        
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        
        err = dx - dy
        
        while True:
            if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[0]):
                grid[y1][x1] = s
            
            if x1 == x2 and y1 == y2:
                break
            
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
    
    return grid
