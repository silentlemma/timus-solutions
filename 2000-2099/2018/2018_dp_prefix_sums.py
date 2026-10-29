MOD = 10**9 + 7

n, a, b = map(int, input().split())
# one[i], two[i]: sequences of length i that end with a run of ones or twos,
# the empty sequence counts once on both sides, so one[0] = two[0] = 1
one = [1] + [0] * n
two = [1] + [0] * n
sum_one = [1] + [0] * n
sum_two = [1] + [0] * n
for i in range(1, n + 1):
    # the last run of ones has length 1..a and follows a sequence ending in twos
    one[i] = (sum_two[i - 1] - (sum_two[i - a - 1] if i - a - 1 >= 0 else 0)) % MOD
    two[i] = (sum_one[i - 1] - (sum_one[i - b - 1] if i - b - 1 >= 0 else 0)) % MOD
    sum_one[i] = (sum_one[i - 1] + one[i]) % MOD
    sum_two[i] = (sum_two[i - 1] + two[i]) % MOD
print((one[n] + two[n]) % MOD)
