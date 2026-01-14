#!/bin/python3


def dynamicArray(n, queries):
    arr = [list() for _ in range(n)]
    answers = []

    lastAnswer = 0
    for query in queries:
        q_type, x, y = query

        if not 0 < q_type < 3:
            raise Exception("Unexpected Query Type")

        idx = (x ^ lastAnswer) % n
        if q_type % 2 == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers
