# Incomplete

t = int(input())
for i in range(t):
    n = input()
    list1 = [int(x) for x in input().split()].sorted()
    a = 0
    b = len(list1) - 1
    while 1:
        pass

def possible(l1: list):
    pairs = []
    while l1:
        
    greatest = l1.pop()
    pairs = []
    a = 0
    b = len(list1) - 1
    while a != b:
        sum_ab = list1[a] + list1[b]
        if sum_ab > greatest:
            b -= 1
        elif sum_ab < greatest:
            a += 1
        else:
            pairs.append((a, b))
            a += 1

