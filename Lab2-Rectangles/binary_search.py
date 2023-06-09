# индекс минимального элемента в отсортированном массиве, который строго больше x
# (стоит правее него)
def upper_bound(a, x, left=None, right=None, key=None):
    key = (lambda i: i) if key is None else key
    start = 0 if left is None else left
    end = (len(a) - 1) if right is None else right
    while start <= end:
        m = (start + end) // 2
        if key(a[m]) > x:
            end = m - 1
        else:
            start = m + 1
    return start


# индекс максимального элемента в отсортированном массиве, который меньше или равен x
# (стоит левее него)
def lower_bound(a, x, left=None, right=None, key=None):
    key = (lambda i: i) if key is None else key
    start = 0 if left is None else left
    end = (len(a) - 1) if right is None else right
    while start <= end:
        m = (start + end) // 2
        if key(a[m]) >= x:
            end = m - 1
        else:
            start = m + 1
    return start
