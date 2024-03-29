# https://www.acmicpc.net/problem/1780

import sys

input = sys.stdin.readline

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

result = {-1: 0, 0: 0, 1: 0}


def is_consists_same_number(two_dimension):
    target_number = two_dimension[0][0]
    for row in two_dimension:
        for num in row:
            if target_number != num:
                return False
    return True


def logic(two_dimension, result):
    if is_consists_same_number(two_dimension):
        if two_dimension[0][0] == 0:
            result[0] += 1
        elif two_dimension[0][0] == 1:
            result[1] += 1
        else:
            result[-1] += 1
        return

    else:
        side = len(two_dimension) // 3

        for i in range(3):
            for j in range(3):
                logic([two_dimension[row][i * side: (i + 1) * side] for row in range(j * side, (j + 1) * side)], result)


logic(paper, result)

print(result[-1])
print(result[0])
print(result[1])
