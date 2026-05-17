# config_maze.py
import random

width  = 10
height = 10
start  = (0, 0)
goal   = (9, 9)

def initialize_path(path, width, height):
    i, j = 0, 0
    for i in range(0, height // 2):
        path.append((i, j))
    for j in range(0, int(width / 2)):
        path.append((i, j))
    for i in range(0, height // 2):
        path.append((i, j))
    for j in range(width // 2, width - 1):
        path.append((0, j))
    for i in range(0, height):
        path.append((i, width - 1))
    return path

def generate_maze(width, height, path, start, goal):
    maze = {}
    for y in range(height):
        for x in range(width):
            maze[(y, x)] = random.choice([0, 1])
    for coord in path:
        maze[coord] = 0
    maze[start] = 0
    maze[goal]  = 0
    return maze