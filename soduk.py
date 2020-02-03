import copy
class Solution:
    def judged(self,temp):
        for i in range(9):
            for j in range(9):
                for a in range(9):
                    if a != j and temp[i][a] == temp[i][j]:
                        return False
                    if a != i and temp[a][j] == temp[i][j]:
                        return False
                i1 = i//3
                j1 = j//3
                for a in [i1*3, i1*3+1, i1*3+2]:
                    for b in [j1*3, j1*3+1, j1*3+2]:
                        if a != i and b != j and temp[a][b] == temp[i][j]:
                            return False
        return True

    def getalist(self, temp):
        row = 0
        column = 0
        length = 0
        for a in range(2, 10):
            for i in range(9):
                for j in range(9):
                    if isinstance(temp[i][j], list) and len(temp[i][j]) == a:
                        row = i  # 单元行号
                        column = j  # 单元列号
                        length = a
                        return [i, j, a]
        return [-1, -1, -1]

    def printbyrow(self, lt):
        for i in lt:
            print(i)
        print("----------------------------------------------")

    def relative(self, i, j):
        lt = []
        for a in range(9):
            lt.append((a, j))
            lt.append((i, a))
        i1 = i // 3
        j1 = j // 3
        for a in [3*i1, 3*i1 + 1, 3*i1 + 2]:
            for b in [3*j1, 3*j1 + 1, 3*j1 + 2]:
                lt.append((a, b))
        st = set(lt)
        lt = list(st)
        lt.remove((i, j))
        return lt

    def delete(self, temp, a, b, value):
        count = 0
        if isinstance(temp[a][b], list):
            if value in temp[a][b]:
                temp[a][b].remove(value)
                count = count + 1
                # print("{}行{}列排除{}".format(a,b,value))
                if len(temp[a][b]) == 1:
                    temp[a][b] = temp[a][b].pop()
        return count

    def soluted(self, temp):
        for i in range(9):
            for j in range(9):
                if isinstance(temp[i][j], list):
                    return False
        True


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        temp = [list(list(i+1 for i in range(9)) for i in range(9)) for i in range(9)]
        slitch = [[list(list() for i in range(9)) for i in range(9)]]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    temp[i][j] = int(board[i][j])        # board数据类型转换以后放入matrix
        del slitch[0]
        slitch.append(temp)                         # 将matrix放入待解列表
        # 对matrix进行求解 首先进行按确定值排除
        # self.printbyrow(temp)
        switch = 1
        while not self.soluted(temp):
            if switch == 1:
                count = 0
                for i in range(9):
                    for j in range(9):
                        if isinstance(temp[i][j], int):
                            # 获取相关单元格列表relativelt
                            relativelt = self.relative(i, j)
                            # print("{}行 {}列消除列表为{}".format(i, j, relativelt))
                            for a in relativelt:
                                count = count + self.delete(temp, a[0], a[1], temp[i][j]) # 排除一次
                if count == 0:
                    print("矩阵已穷举")
                    self.printbyrow(temp)
                    switch = 2
            if switch == 2:
                del slitch[-1]
                # 找到一个分支列表 构造穷举
                [row, column, length] = self.getalist(temp)
                if [row, column, length] == [-1, -1, -1]:
                    if self.judged(temp):
                        print("求解成功！")
                        break
                    else:
                        print("求解失败 当前矩阵错误，删除最后一个待解矩阵")
                        print("矩阵队列还有{}个".format(len(slitch)))
                        for i in range(9):
                            for j in range(9):
                                temp[i][j] = slitch[-1][i][j]
                        print("重新取一个矩阵求解")
                print("增加{}个矩阵".format(length))
                for k in range(length):
                    slitch.append([list(list() for p in range(9)) for p in range(9)])
                    for i in range(9):
                        for j in range(9):
                            if i == row and j == column:
                                slitch[-1][i][j] = temp[i][j][k]
                            else:
                                slitch[-1][i][j] = temp[i][j]
                temp = copy.deepcopy(slitch[-1])

                switch = 1
                print("求解新矩阵")
                self.printbyrow(temp)
                print("待求解矩阵还有{}".format(len(slitch)))
                for i in range(len(slitch)):
                    self.printbyrow(slitch[i])

        # self.printbyrow(temp)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(temp[i][j])
        print(board)
        self.printbyrow(board)

test = Solution()
path = "C:\\Users\\Administrator\\Desktop\\soduk3.txt"
file = open(path, "r")
temp = (file.readlines())
board = eval(temp[0]) # board
test.solveSudoku(board)


