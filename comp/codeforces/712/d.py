n = int(input())
i = 0
n_sqr = n * n
even = 1
odd = 0
if n % 2 == 0:
    while i < n_sqr:
        a = int(input())
        if a == 3:
            if even < n_sqr:
                print(2, even // n + 1, even % n + 1, flush=True)
                if (even // n) % 2 == 0 and n - even % n < 3:
                    even += 1
                elif (even // n) % 2 == 1 and n - even % n < 3:
                    even += 3
                else:
                    even += 2
                # return 2 in next even place
            else:
                print(1, odd // n + 1, odd % n + 1, flush=True)
                if (odd // n) % 2 == 0 and n - odd % n < 3:
                    odd += 3
                elif (odd // n) % 2 == 1 and n - odd % n < 3:
                    odd += 1
                else:
                    odd += 2
                # return 1 in next odd place
        elif a == 2:
            if odd < n_sqr:
                print(1, odd // n + 1, odd % n + 1, flush=True)
                if (odd // n) % 2 == 0 and n - odd % n < 3:
                    odd += 3
                elif (odd // n) % 2 == 1 and n - odd % n < 3:
                    odd += 1
                else:
                    odd += 2
                # return 1 in next odd place
            else:
                print(3, even // n + 1, even % n + 1, flush=True)
                if (even // n) % 2 == 0 and n - even % n < 3:
                    even += 1
                elif (even // n) % 2 == 1 and n - even % n < 3:
                    even += 3
                else:
                    even += 2
                # return 3 in next even place
        else:
            if even < n_sqr:
                print(2, even // n + 1, even % n + 1, flush=True)
                if (even // n) % 2 == 0 and n - even % n < 3:
                    even += 1
                elif (even // n) % 2 == 1 and n - even % n < 3:
                    even += 3
                else:
                    even += 2
                # retun 2 in next even place
            else:
                print(3, odd // n + 1, odd % n + 1, flush=True)
                if (odd // n) % 2 == 0 and n - odd % n < 3:
                    odd += 3
                elif (odd // n) % 2 == 1 and n - odd % n < 3:
                    odd += 1
                else:
                    odd += 2
                # return 3 in next odd place
        i += 1
else:
    while i < n_sqr:
        a = int(input())
        if a == 3:
            if even < n_sqr:
                print(2, even // n + 1, even % n + 1, flush=True)
                even += 2
                # return 2 in next even place
            else:
                print(1, odd // n + 1, odd % n + 1, flush=True)
                odd += 2
                # return 1 in next odd place
        elif a == 2:
            if odd < n_sqr:
                print(1, odd // n + 1, odd % n + 1, flush=True)
                odd += 2
                # return 1 in next odd place
            else:
                print(3, even // n + 1, even % n + 1, flush=True)
                even += 2
                # return 3 in next even place
        else:
            if even < n_sqr:
                print(2, even // n + 1, even % n + 1, flush=True)
                even += 2
                # retun 2 in next even place
            else:
                print(3, odd // n + 1, odd % n + 1, flush=True)
                odd += 2
                # return 3 in next odd place
        i += 1