n, p = map(int, input().split())
# the route is the capital, then the other n - 1 = m cities twice each with
# no city twice in a row, then the capital; such words over m pairs obey
# a(m) = m (2m - 1) a(m - 1) + m (m - 1) a(m - 2), with no division
before, current = 1 % p, 0
for m in range(2, n):
    before, current = current, (m * (2 * m - 1) * current + m * (m - 1) * before) % p
print(current % p)
