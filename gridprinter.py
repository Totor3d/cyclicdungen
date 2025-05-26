import os
import time
import math

size = 60
zoom = 2

delay = 0.01


def printGrid(grid):
    for i in grid:
        print(*i)
    time.sleep(delay)


def setPointsOnGrid(points, grid = None):
    if not grid:
        grid = [["." for x in range(size)] for y in range(size)]
    
    for x, y, s in points:
        try:
            grid[size//2+(math.floor(x))//zoom][size//2+(math.floor(y))//zoom] = s
        except IndexError:
            pass
    return grid

def drawRectanglesOnGrid(rectangles, grid = None):
    if not grid:
        grid = [["." for x in range(size)] for y in range(size)]
    
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