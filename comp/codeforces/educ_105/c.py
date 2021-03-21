def max_pts(boxes: list, pos: list) -> int:
    if not boxes or not pos:
        return 0
    if boxes[0] > pos[-1]:
        return 0
    dynamo = []
    for i in range(1, len(pos)):
        dynamo.append(pos[i] - pos[i-1])
    i = len(boxes) - 1
    j = k = len(pos) - 1
    dist = 1
    maximum = 1
    while i > 0 and j > 0:
        while boxes[i] > pos[j]:
            i -= 1
        while pos[j] > boxes[i]:
            j -= 1
            dist += pos[j+1] - pos[j]
            while dist > i:
                dist -= dynamo[k-1]
                k -= 1
            maximum = max(j - k + 1, maximum)
    return maximum


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        neg_a = []
        neg_b = []
        pos_a = []
        pos_b = []
        while a[i]:
            if i < 0:
                i += 1

        for i in b:
            if i < 0:
                neg_b.append(-i)
            else:
                pos_b.append(i)
        print(max_pts(pos_a, pos_b) + max_pts(list(reversed(neg_a)), list(reversed(neg_b))))
