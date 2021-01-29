t = int(input())
output = []
for _ in range(t):
    n = int(input())
    moves = input()
    move_count = [1]
    lr_count = 1
    rl_count = 1
    i = 0
    for char in moves:
        if i % 2 == 0:
            if char == "L":
                lr_count += 1
                rl_count = 1
            else:
                lr_count = 1
                rl_count += 1
            move_count.append(lr_count)
        else:
            if char == "R":
                lr_count += 1
                rl_count = 1
            else:
                lr_count = 1
                rl_count += 1
            move_count.append(rl_count)
        i += 1
    lr_count = 0
    rl_count = 0
    i = 0
    for char in moves[::-1]:
        if i % 2 == 0:
            if char == "R":
                lr_count += 1
                rl_count = 0
            else:
                lr_count = 0
                rl_count += 1
            move_count[-i-2] += lr_count
        else:
            if char == "L":
                lr_count += 1
                rl_count = 0
            else:
                lr_count = 0
                rl_count += 1
            move_count[-i-2] += rl_count
        i += 1

    output.append(move_count)

for out in output:
    print(" ".join([str(x) for x in out]))