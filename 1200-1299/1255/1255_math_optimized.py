from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
# with r = N mod K, an s x s corner square is left over, s = min(r, K - r)
r = n % k
s = min(r, k - r)
stdout.write(str((n * n - s * s) // k if n >= k else 0))
