DIGIT = 9  # the largest digit


def main():
    digits = [int(c) for c in input().strip()]
    k = len(digits)
    # the rightmost digit that can grow by one while the digits after it give
    # one back; the smallest such change gives the next number
    after = 0  # the sum of the digits after position i
    for i in range(k - 1, -1, -1):
        if digits[i] < DIGIT and after > 0:
            digits[i] += 1
            rest = after - 1
            # the smallest tail with this sum: the digits pushed to the right
            for j in range(k - 1, i, -1):
                digits[j] = min(DIGIT, rest)
                rest -= digits[j]
            print("".join(map(str, digits)))
            return
        after += digits[i]
    print(-1)


main()
