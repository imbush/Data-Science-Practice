def main():
    in_string = input()
    counts = [0] * 26
    for c in in_string:
        counts[ord(c) - 65] += 1

    palindrome = ""
    middle = ""
    for i in range(26):
        if counts[i] % 2 == 1:
            if middle:
                print("NO SOLUTION")
                return
            middle = chr(65 + i)
        palindrome += (counts[i] // 2) * chr(65 + i)
    print(palindrome + middle + palindrome[::-1])

main()
