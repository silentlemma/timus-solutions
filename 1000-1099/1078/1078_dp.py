import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    ends = list(zip(data[1 : 2 * n + 1 : 2], data[2 : 2 * n + 2 : 2]))
    left = [min(e) for e in ends]
    right = [max(e) for e in ends]
    # a segment inside another is strictly shorter, so by length the inner
    # one always comes first
    order = sorted(range(n), key=lambda i: right[i] - left[i])
    best = [1] * n
    prev = [-1] * n
    for pos, i in enumerate(order):
        for j in order[:pos]:
            if left[i] < left[j] and right[j] < right[i] and best[j] + 1 > best[i]:
                best[i] = best[j] + 1
                prev[i] = j
    end = max(range(n), key=lambda i: best[i])
    chain = []
    while end >= 0:
        chain.append(end + 1)
        end = prev[end]
    print(len(chain))
    print(" ".join(map(str, reversed(chain))))


main()
