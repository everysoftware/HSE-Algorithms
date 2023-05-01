class BruteForceAlgorithm:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def count(self, point):
        x, y = point
        k = 0
        for rect in self.rectangles:
            x1, y1, x2, y2 = rect
            if x1 <= x < x2 and y1 <= y < y2:
                k += 1
        return k

    def execute(self, points):
        return [self.count(point) for point in points]


# O(N^2)
def rectangles_naive(rectangles, points):
    alg = BruteForceAlgorithm(rectangles)
    return alg.execute(points)
