from rectangles import *


def test_rectangles():
    n = int(input())
    rect = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    points = [list(map(int, input().split())) for _ in range(m)]
    print(*rectangles_naive(n, rect, m, points))
    print(*rectangles_map(n, rect, m, points))


def main():
    test_rectangles()


main()
