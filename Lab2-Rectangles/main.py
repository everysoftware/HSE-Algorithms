from benchmark import *
from rectangles_tree import *


def test_algorithms():
    benchmark()


def solve_contest():
    n = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    points = [list(map(int, input().split())) for _ in range(m)]
    print(*rectangles_tree(rectangles, points))


def main():
    test_algorithms()


main()
