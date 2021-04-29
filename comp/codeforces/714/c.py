t = int(input())
dig_storage = [0] * (20 + 2 * 10 ** 5)
dig_storage[0] = 1

digits = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1, 20 + 2 * 10 ** 5):
    nines = digits[9]
    for dig in range(8, -1, -1):
        digits[dig + 1] = digits[dig]
    digits[0] = nines
    digits[1] = (digits[1] + nines) % 1000000007
    dig_storage[i] = dig_storage[i-1] + nines

for _ in range(t):
    n, operations = input().split()
    operations = int(operations)
    output = 0
    for char in n:
        output += dig_storage[operations + int(char)] % 1000000007
    print(output)
