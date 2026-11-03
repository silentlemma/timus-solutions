PERCENT = 100


def main():
    n, start = map(int, input().split())
    if start > n:
        print(0)
        return
    jobs = [0] * (n + 1)
    jobs[start] = answer = 1
    for salary in range(start, n + 1):
        here = jobs[salary]
        if not here:
            continue
        if here > answer:
            answer = here
        # Try each possible integer percentage; its raise must be whole rubles.
        limit = PERCENT * (n - salary) // salary
        for percentage in range(1, limit + 1):
            raise_amount = salary * percentage
            if raise_amount % PERCENT == 0:
                following = salary + raise_amount // PERCENT
                if jobs[following] <= here:
                    jobs[following] = here + 1
    print(answer)


main()
