def main():
    n = int(input())
    # the cheapest round trip, as a cycle through n: one side of n goes
    # 2, n - 2, 4, n - 4, ..., the other 1, n - 1, 3, n - 3, ...; step k
    # takes the pair k, k + 1 for odd k and n - k, n - k + 1 for even k
    used = [False] * (n + 1)
    used[n] = True
    one_side = []
    other_side = []
    k = 1
    while True:
        pair = (k + 1, k) if k % 2 == 1 else (n - k, n - k + 1)
        if pair[0] < 1 or used[pair[0]] or used[pair[1]]:
            break
        one_side.append(pair[0])
        other_side.append(pair[1])
        used[pair[0]] = used[pair[1]] = True
        k += 1
    # at most one city is left, where the two sides meet
    middle = [v for v in range(1, n) if not used[v]]
    cycle = [n] + one_side + middle + other_side[::-1]
    # the dearest: odd numbers up, then even numbers down, so that every
    # city is next to the two closest in size
    dear = list(range(1, n + 1, 2)) + list(range(n - n % 2, 1, -2))
    print(" ".join(map(str, cycle[-1:] + cycle[:-1])))
    print(" ".join(map(str, dear)))


main()
