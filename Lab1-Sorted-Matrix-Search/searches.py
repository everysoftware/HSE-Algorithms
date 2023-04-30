def binary_search(arr, target, bounds=None):
    if bounds is None:
        low, high = 0, len(arr) - 1
    else:
        low, high = bounds
    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        elif guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return high
