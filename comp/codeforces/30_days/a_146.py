chars = set()
for char in input():
    chars.add(char)
if len(chars) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")