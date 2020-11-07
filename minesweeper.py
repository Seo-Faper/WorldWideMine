import random

width = 10
height = 10
k = 18


class MineSweeperMaking:
    def __init__(self):
        self.mapping = [[0 for i in range(width)] for j in range(height)]
        self.plant(self.mapping, k, 0)
        self.printMap = ""
        for i in range(height):
            for j in range(width):
                self.printMap += str(self.mapping[i][j]) + " "
            self.printMap += "\n"
        print(self.printMap)

    def plant(self, temp, mines, numbering):
        while numbering <= mines:
            x = random.randint(0, height-1)
            y = random.randint(0, width-1)
            if temp[x][y] == "*":
                return self.plant(temp, mines, numbering)
            else:
                temp[x][y] = "*"
                self.counting(temp, x, y)
                return self.plant(temp, mines, numbering + 1)
        return temp

    def counting(self, temp, x, y):
        stack = []
        que = []
        for i in range(3):
            for j in range(3):
                stack.append([x + i - 1, y + j - 1])
        for i in range(9):
            if stack[i][0] < 0 or stack[i][1] < 0 or stack[i][0] > height-1 or stack[i][1] > width-1:
                que.append(i)
        for i in reversed(range(len(que))):
            del stack[que[i]]
        for i in range(len(stack)):
            a = int(stack[i][0])
            b = int(stack[i][1])
            if temp[a][b] != "*":
                temp[a][b] += 1
        return temp


MineSweeperMaking()
