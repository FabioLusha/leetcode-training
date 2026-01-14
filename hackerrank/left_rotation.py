def rotateLeft(d, arr):
    d = d % len(arr)
    result = arr[d:] + arr[:d]

    return result
