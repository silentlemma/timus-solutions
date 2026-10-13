def main():
    n = int(input())
    # ordered choices of k different drinks: n (n - 1) ... (n - k + 1), for k from 2
    total, ways = 0, n
    for k in range(2, n + 1):
        ways *= n - k + 1
        total += ways
    print(total)


main()
