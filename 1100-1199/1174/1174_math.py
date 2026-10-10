def main():
    n = int(input())
    perm = list(map(int, input().split()))
    where = [0] * (n + 1)
    for i, v in enumerate(perm):
        where[v] = i
    # rank of the order of 1..k among themselves: element k sweeps once
    # across the order of 1..k-1, to the left in even sweeps and to the
    # right in odd ones, and that order's rank counts the sweeps before
    rank = 0
    for k in range(2, n + 1):
        smaller_left = sum(1 for v in range(1, k) if where[v] < where[k])
        step = smaller_left if rank % 2 else k - 1 - smaller_left
        rank = rank * k + step
    print(rank + 1)


main()
