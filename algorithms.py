# algorithms.py
import time
import tracemalloc
import heapq
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, maze):
    x, y = node
    return [
        (x + dx, y + dy)
        for dx, dy in directions
        if (x + dx, y + dy) in maze and maze[(x + dx, y + dy)] == 0
    ]

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path

# ── BFS ─────────────────────────────────────────────────────────
def bfs(start, goal, maze):
    metrics = {'time': [], 'memory': []}
    tracemalloc.start()
    start_time = time.time()

    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        metrics['time'].append(time.time() - start_time)
        metrics['memory'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if current == goal:
            break

        for neighbor in get_neighbors(current, maze):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    tracemalloc.stop()
    path = reconstruct_path(came_from, goal) if goal in came_from else []
    return path, metrics

# ── DFS ─────────────────────────────────────────────────────────
def dfs(start, goal, maze):
    metrics = {'time': [], 'memory': []}
    tracemalloc.start()
    start_time = time.time()

    stack = [start]
    came_from = {start: None}

    while stack:
        current = stack.pop()
        metrics['time'].append(time.time() - start_time)
        metrics['memory'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if current == goal:
            break

        for neighbor in get_neighbors(current, maze):
            if neighbor not in came_from:
                came_from[neighbor] = current
                stack.append(neighbor)

    tracemalloc.stop()
    path = reconstruct_path(came_from, goal) if goal in came_from else []
    return path, metrics

# ── A* ──────────────────────────────────────────────────────────
def a_star(start, goal, maze, heuristic):
    metrics = {'time': [], 'memory': []}
    tracemalloc.start()
    start_time = time.time()

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), start))
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        metrics['time'].append(time.time() - start_time)
        metrics['memory'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if current == goal:
            break

        for neighbor in get_neighbors(current, maze):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    tracemalloc.stop()
    path = reconstruct_path(came_from, goal) if goal in came_from else []
    return path, metrics

# ── GBFS ────────────────────────────────────────────────────────
def gbfs(start, goal, maze, heuristic):
    metrics = {'time': [], 'memory': []}
    tracemalloc.start()
    start_time = time.time()

    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    came_from = {start: None}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        metrics['time'].append(time.time() - start_time)
        metrics['memory'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if current == goal:
            break

        visited.add(current)

        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor))

    tracemalloc.stop()
    path = reconstruct_path(came_from, goal) if goal in came_from else []
    return path, metrics