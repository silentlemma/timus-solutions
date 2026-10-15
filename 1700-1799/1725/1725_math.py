# everyone on the far side of Vasya can be made to trip except the two
# seats at the far end, who always come in from their own end
SAFE = 2

n, k = map(int, input().split())
print(max(0, max(k - 1, n - k) - SAFE))
