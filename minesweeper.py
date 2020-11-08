import random

width = 10
height = 10
mine = 18


class MineSweeperMaker:
    def __init__(self):
        self.keep_going = True
        self.mapping = [[[0] for i in range(width)] for j in range(height)]
        self.plant(self.mapping, mine, 0)
        for i in range(height):
            for j in range(width):
                self.mapping[i][j].append("X")
        while self.keep_going:
            x, y = map(int, input().split())
            self.clicking(self.mapping, x, y)

    def plant(self, temp, mines, numbering):
        while numbering <= mines:
            x = random.randint(0, height-1)
            y = random.randint(0, width-1)
            if temp[x][y] == ["*"]:
                return self.plant(temp, mines, numbering)
            else:
                temp[x][y] = ["*"]
                self.counting(temp, x, y)
                return self.plant(temp, mines, numbering + 1)
        return temp

    def counting(self, temp, x, y):
        stack = []
        for i in range(3):
            for j in range(3):
                stack.append([x + i - 1, y + j - 1])
        for i in reversed(range(9)):
            if stack[i][0] < 0 or stack[i][1] < 0 or stack[i][0] > height-1 or stack[i][1] > width-1:
                del stack[i]
        for i in range(len(stack)):
            a = int(stack[i][0])
            b = int(stack[i][1])
            if temp[a][b][0] != "*":
                temp[a][b][0] += 1
        return temp

    def chain(self, temp, x, y):
        temp[x][y][1] = temp[x][y][0]
        stack = []
        for i in range(3):
            for j in range(3):
                stack.append([x + i - 1, y + j - 1])
        for i in reversed(range(9)):
            if stack[i][0] < 0 or stack[i][1] < 0 or stack[i][0] > height-1 or stack[i][1] > width-1 or\
                    (stack[i][0] == x and stack[i][1] == y):
                del stack[i]
        for i in range(len(stack)):
            a = int(stack[i][0])
            b = int(stack[i][1])
            if temp[a][b][0] == 0 and temp[a][b][1] == "X":
                temp[a][b][1] = temp[a][b][0]
                self.mapping = temp
                self.chain(temp, a, b)
            elif temp[a][b][0] != "*":
                temp[a][b][1] = temp[a][b][0]
                self.mapping = temp

    def printing(self):
        print_map = ""
        for i in range(height):
            for j in range(width):
                print_map += str(self.mapping[i][j][1]) + " "
            print_map += "\n"
        return print_map

    def clicking(self, temp, x, y):
        if temp[x][y][0] == "*":
            self.keep_going = False
            print("Game over")
        else:
            self.chain(temp, x, y)
            print(self.printing())


game = MineSweeperMaker
game()
