import sys

MOD = 1000000007


def solve(n, a, b):
    ends_one = [0] * (b + 1)
    ends_two = [0] * (a + 1)
    ends_one[0] = ends_two[0] = 1
    window_one = window_two = 1
    last_one = last_two = 0
    for length in range(1, n + 1):
        last_one, last_two = window_one, window_two
        expired_two = ends_two[(length - a) % (a + 1)] if length >= a else 0
        expired_one = ends_one[(length - b) % (b + 1)] if length >= b else 0
        window_one = (window_one + last_two - expired_two) % MOD
        window_two = (window_two + last_one - expired_one) % MOD
        ends_one[length % (b + 1)] = last_one
        ends_two[length % (a + 1)] = last_two
    return (last_one + last_two) % MOD


if __name__ == "__main__":
    print(solve(*map(int, sys.stdin.buffer.read().split())))
