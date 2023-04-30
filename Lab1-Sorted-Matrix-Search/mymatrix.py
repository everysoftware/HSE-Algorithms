from searches import *


class MyMatrix:
    def __init__(self, rows=0, cols=0):
        self.rows, self.cols = rows, cols
        self.arr = None

    def fill(self, type_id):
        f = (lambda i, j: ((self.cols // self.rows * i + j) * 2)) if type_id == 0 else \
            (lambda i, j: ((self.cols // self.rows * i * j) * 2))
        self.arr = [[f(i, j) for j in range(self.cols)] for i in range(self.rows)]

    def print(self, file=None):
        for i in range(self.rows):
            print(*self.arr[i], file=file)

    def binary_search(self, target):
        for i in range(self.rows):
            search_res = binary_search(self.arr[i], target)
            if self.arr[i][search_res] == target:
                return i, search_res
        return -1, -1

    def ladder_search(self, target):
        i = 0
        j = self.cols - 1
        while i < self.rows and j >= 0:
            if self.arr[i][j] < target:
                i += 1  # идём вниз
            elif self.arr[i][j] > target:
                j -= 1  # идём влево
            else:
                return i, j
        return -1, -1

    def exp_search(self, target):
        i = 0
        j = self.cols - 1
        while i < self.rows and j >= 0:
            if self.arr[i][j] < target:
                i += 1
            elif self.arr[i][j] > target:
                # Определяем границы поиска
                start = 1
                while j - start >= 0 and self.arr[i][j - start] > target:
                    start *= 2
                finish = j - start // 2
                start = max(j - start, 0)
                if start == finish:
                    break
                # Запускаем бинарный на полученных границах
                j = binary_search(self.arr[i], target, (start, finish))
            else:
                return i, j
        return -1, -1
