import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # votes[k]: how many students get their wish if student k starts
    votes = [0] * (n + 1)
    for i, want in enumerate(map(int, data[1:n + 1]), start=1):
        # student i speaks want-th when student i - want + 1 starts
        votes[(i - want) % n + 1] += 1
    print(max(range(1, n + 1), key=votes.__getitem__))


main()
