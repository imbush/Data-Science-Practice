# Incomplete

from turtle import right


t = int(input())

for _ in range(t):
    stuff = [int(x) for x in input().split()]
    s = input()
    k = stuff[0]

    left_dist = []
    right_dist = []
    for i in range(0, len(s)):
        if s[i] == 1:
            left_dist.append(i)
            right_dist.insert(0, len(s)-i-1)

    num_ones = len(left_dist)
    num_moved = 0
    steps_taken = 0
    left_one = -1
    right_one = len(s)
    i = 0
    j = len(s) - 1
    while num_moved < num_ones and steps_taken < k:
        i = left_one + 1
        j = right_one - 1
        if not (0 <= i <= j < len(s)):
            break
        while s[i]
    print(s)


def swap(s, i, j):
    a = s[i]
    b = s[j]
    s[i] = b
    s[j] = a
    return s
