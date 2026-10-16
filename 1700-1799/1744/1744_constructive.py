n = int(input())
# every day uses three pairs and every pair may meet three times, so at
# most n (n - 1) / 2 days; the triples i, i + d, i + 2d modulo n give
# each pair three meetings, twice as neighbours and once two steps apart
days = ["%d %d %d" % (i + 1, (i + d) % n + 1, (i + 2 * d) % n + 1)
        for d in range(1, (n - 1) // 2 + 1) for i in range(n)]
print(len(days))
print("\n".join(days))
