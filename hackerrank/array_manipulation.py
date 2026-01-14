# This Solution uses the Difference Array algorithm to update a range
def arrayManipulation(n, queries):
    result = [0] * n

    for query in queries:
        a, b, k = query

        # 0-based indexing in python
        a -= 1
        b -= 1

        result[a] += k

        if b + 1 < n:
            result[b + 1] -= k

    maxVal = 0
    currentVal = 0

    for i in result:
        currentVal += i
        maxVal = currentVal if currentVal > maxVal else maxVal

    return maxVal
