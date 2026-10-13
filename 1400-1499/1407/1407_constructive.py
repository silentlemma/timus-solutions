def main():
    n = int(input())
    # a number of k digits 1 and 2 divisible by 2^k: put 1 or 2 in front of
    # the one for k - 1, whichever keeps one more factor 2
    value, digits, power = 0, [], 1
    for k in range(n):
        for d in (1, 2):
            if (value + d * power) % (2 << k) == 0:
                value += d * power
                digits.append(str(d))
                break
        power *= 10
    print("".join(reversed(digits)))


main()
