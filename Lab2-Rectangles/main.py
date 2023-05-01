from rectangles_naive import *
from rectangles_map import *
from rectangles_tree import *


def test_rectangles():
    n = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    points = [list(map(int, input().split())) for _ in range(m)]
    print(*rectangles_naive(rectangles, points))
    print(*rectangles_map(rectangles, points))
    print(*rectangles_tree(rectangles, points))


def main():
    test_rectangles()


main()
