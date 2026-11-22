import sys

MOD = 1000000007


def solve(n, a, b):
    size_one, size_two = b + 1, a + 1
    ends_one, ends_two = [0] * size_one, [0] * size_two
    ends_one[0] = ends_two[0] = 1
    window_one = window_two = 1
    last_one = last_two = pos_one = pos_two = 0
    for length in range(1, n + 1):
        pos_one += 1
        if pos_one == size_one:
            pos_one = 0
        pos_two += 1
        if pos_two == size_two:
            pos_two = 0
        old_one, old_two = pos_one + 1, pos_two + 1
        if old_one == size_one:
            old_one = 0
        if old_two == size_two:
            old_two = 0
        last_one, last_two = window_one, window_two
        expired_two = ends_two[old_two] if length >= a else 0
        expired_one = ends_one[old_one] if length >= b else 0
        window_one += last_two - expired_two
        window_two += last_one - expired_one
        # Each result is between -MOD and 2*MOD: a single correction replaces division.
        if window_one < 0:
            window_one += MOD
        elif window_one >= MOD:
            window_one -= MOD
        if window_two < 0:
            window_two += MOD
        elif window_two >= MOD:
            window_two -= MOD
        ends_one[pos_one] = last_one
        ends_two[pos_two] = last_two
    return (last_one + last_two) % MOD


print(solve(*map(int, sys.stdin.buffer.read().split())))
