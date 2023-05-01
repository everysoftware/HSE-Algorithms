from binary_search import lower_bound, upper_bound


class Node:
    def __init__(self, left=None, right=None, summa=0):
        self.left = left
        self.right = right
        self.summa = summa

    def copy(self):
        return Node(self.left, self.right, self.summa)

    def find_quantity(self, left, right, target):
        if right - left == 1:
            return self.summa
        m = (left + right) // 2
        if target < m:
            if self.left is None:
                return self.summa
            return self.summa + self.left.find_quantity(left, m, target)
        else:
            if self.right is None:
                return self.summa
            return self.summa + self.right.find_quantity(m, right, target)

    def add_node(self, left, right, x, is_left):
        if left >= x or right <= x:
            return self
        if self.left is None:
            self.left = Node()
        if self.right is None:
            self.right = Node()
        if right <= x <= left:
            node = self.copy()
            node.summa += 1 if is_left else -1
            return node
        m = (left + right) // 2
        node = self.copy()
        node.left = self.left.add_node(left, m, x, is_left)
        node.right = self.right.add_node(m, right, x, is_left)
        return node


class AlgorithmOnTree:
    def __init__(self, rectangles):
        self.compressed_x = []
        self.compressed_y = []
        self.roots = []
        self.compressed_roots = []
        self.rectangles = rectangles
        self.compress_rectangles()
        self.build_tree()

    def compress_rectangles(self):
        for rect in self.rectangles:
            x1, y1, x2, y2 = rect
            self.compressed_x += [x1, x2]
            self.compressed_y += [y1, y2]
        self.compressed_x = sorted(set(self.compressed_x))
        self.compressed_y = sorted(set(self.compressed_y))

    def build_tree(self):
        root = Node()
        sides = []
        for rect in self.rectangles:
            x1, y1, x2, y2 = rect
            sides.append([
                lower_bound(self.compressed_x, x1),
                lower_bound(self.compressed_y, y1),
                True
            ])
            sides.append([
                lower_bound(self.compressed_x, x2),
                lower_bound(self.compressed_y, y2),
                False
            ])
        sides.sort(key=lambda i: i[0])
        for side in sides:
            x, y, is_lower = side
            root = root.add_node(
                0,
                len(self.compressed_y),
                y,
                is_lower
            )
            self.roots.append(root)
            self.compressed_roots.append(x)

    def count(self, point):
        x, y = point
        if x < self.compressed_x[0] or y < self.compressed_y[0] or \
                x > self.compressed_x[-1] or y > self.compressed_y[-1]:
            return 0
        compressed_x_pos = upper_bound(self.compressed_x, x) - 1
        compressed_y_pos = upper_bound(self.compressed_y, y) - 1
        pos = upper_bound(self.compressed_roots, compressed_x_pos) - 1
        return self.roots[pos].find_quantity(0, len(self.compressed_y), compressed_y_pos)

    def execute(self, points):
        return [self.count(point) for point in points]


def rectangles_tree(rectangles, points):
    algo = AlgorithmOnTree(rectangles)
    return algo.execute(points)
