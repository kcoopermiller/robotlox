import lupa
import numpy as np
from lupa import LuaRuntime
import random

class proceduralMatrix:
    def __init__(self):
        self.world = []
        self.options = ['wall', 'slab', 'bloc', 'nood']
        self.probs = [0.3, 0.2, 0.4, 0.1]
        self.n = 0

    def buildMatrix(self, n):
        self.n = n
        self.world = [[0 for x in range(n)] for y in range(n)]
        x = random.randrange(0, n*n)
        if x < n:
            self.world[int(x)][0] = 'char'
        else:
            a = int(x / n)
            b = int(x - (a*n))
            self.world[a][b] = 'char'

        y = random.randrange(0, n*n)
        while y == x:
            y = random.randrange(0, n*n)

        if y < n:
            self.world[int(y)][0] = 'flag'
        else:
            a = int(y / n)
            b = int(y - (a*n))
            self.world[a][b] = 'flag'

        for i in range(n):
            row = random.choices(options, weights = probs, k = n)
            for j in range(len(row)):
                if world[i][j] != 'char' and world[i][j] != 'flag':
                    world[i][j] = row[j]

    def isPath(self):
        visited = [[False for x in range(n)] for y in range(n)]
        flag = False
        for i in range(n):
            for j in range(n):
                if(self.world[i][j] == 'flag' and not visited[i][j]):
                    if(checkPath(self.world, i, j, visited)):
                        flag = True
                        break
        if(flag):
            print('yes')
        else:
            print('no')

    def isSafe(i, j, matrix):
        if(i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
            return True
        return False

    def checkPath(matrix, i, j, visited):
        if(isSafe(i, j, matrix) and matrix[i][j] != 'wall' and not visited[i][j]):
            visited[i][j] = True
            if(matrix[i][j] == 'flag'):
                return True

            up = checkPath(matrix, i - 1, j, visited)
            if(up):
                return True

            left = checkPath(matrix, i, j - 1, visited)
            if(left):
                return True

            down = checkPath(matrix, i + 1, j, visited)
            if(down):
                return True

            right = checkPath(matrix, i, j + 1, visited)
            if(right):
                return True

        return False
