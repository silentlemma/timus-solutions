n, m = map(int, input().split())
# with first boxes 1..n and second boxes spaced n apart above them, every
# sum a + b names its pair, so no two gifts can weigh the same
print(" ".join(str(i) for i in range(1, n + 1)))
print(" ".join(str((j + 1) * n + 1) for j in range(m)))
