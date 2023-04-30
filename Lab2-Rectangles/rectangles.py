from binary_search import *


# O(N^2)
def rectangles_naive(n, rect, m, points):
    result = []
    for i in range(m):
        k = 0
        for j in range(n):
            x1, y1, x2, y2 = rect[j]
            if x1 <= points[i][0] < x2 and y1 <= points[i][1] < y2:
                k += 1
        result.append(k)
    return result


class AlgorithmOnMap:
    def __init__(self, n, rectangles):
        self.all_x = []
        self.all_y = []
        self.compressed_x = {}
        self.compressed_y = {}
        self.map = []
        self.rectangles_count = n
        self.rectangles = rectangles
        self.compress_rectangles()
        self.create_map()

    def create_mapper(self, mapper_type):
        mapper = self.compressed_x if mapper_type == 0 else self.compressed_y
        keys = self.all_x if mapper_type == 0 else self.all_y
        new_coord = 0
        for i in range(len(keys)):
            mapper[keys[i]] = new_coord
            new_coord += 2

    def compress_rectangles(self):
        self.compressed_x, self.compressed_y = {}, {}
        self.all_x, self.all_y = [], []
        for i in range(self.rectangles_count):
            x1, y1, x2, y2 = self.rectangles[i]
            self.all_x += [x1, x2]
            self.all_y += [y1, y2]
        self.all_x, self.all_y = sorted(set(self.all_x)), sorted(set(self.all_y))
        self.create_mapper(0)
        self.create_mapper(1)

    def create_map(self):
        self.map = [[0] * (2 * len(self.compressed_y)) for _ in range(2 * len(self.compressed_x) + 1)]
        for i in range(self.rectangles_count):
            x1, y1, x2, y2 = self.rectangles[i]
            compressed_lower_point = (self.compressed_x[x1], self.compressed_y[y1])
            compressed_upper_point = (self.compressed_x[x2], self.compressed_y[y2])
            for j in range(compressed_lower_point[0], compressed_upper_point[0]):
                for k in range(compressed_lower_point[1], compressed_upper_point[1]):
                    self.map[j][k] += 1

    def compress_coord(self, coord_type, coord):
        mapper = self.compressed_x if coord_type == 0 else self.compressed_y
        keys = self.all_x if coord_type == 0 else self.all_y
        if coord in mapper:
            return mapper[coord]
        key = upper_bound(keys, coord)
        if 0 < key < len(keys):
            return mapper[keys[key]] - 1
        else:
            return -1

    def count(self, point):
        x, y = point
        compressed_point = (self.compress_coord(0, x), self.compress_coord(1, y))
        if compressed_point[0] < 0 or compressed_point[1] < 0:
            return 0
        return self.map[compressed_point[0]][compressed_point[1]]

    def execute(self, m, points):
        result = []
        for i in range(m):
            result.append(self.count(points[i]))
        return result


# O(N^3) + O(logN)
def rectangles_map(n, rect, m, points):
    al = AlgorithmOnMap(n, rect)
    return al.execute(m, points)
