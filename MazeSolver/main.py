
from collections import deque

def solveMazeWithPath(maze):
    R, C = len(maze), len(maze[0])

    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'I':
                start = (r, c)
                break
        else:
            continue
        break
    else:
        return None

    queue = deque()
    queue.appendleft((start[0], start[1], 0, [start[0] * C + start[1]]))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == "S":
            return coord[2], [[i//C, i%C] for i in coord[3]] # Return path length, boxes on path

        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2] + 1, coord[3] + [nr * C + nc]))


mazeFile = input("Maze txt name: ")

with open(mazeFile) as f:
    maze = []
    for line in f:
        maze.append([i for i in line.strip("\n")])
    pathLen, pathItems = solveMazeWithPath(maze)
    print("Length of path:", pathLen)
    print("Path Items:", *pathItems)