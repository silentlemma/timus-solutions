import sys

PEG_SUM = 3


def solve(state):
    source = answer = 0
    for disk in range(len(state) - 1, -1, -1):
        target = ord(state[disk]) - ord("A")
        if target != source:
            answer += 1 << disk
            source = PEG_SUM - source - target
    return answer


def main():
    tokens = sys.stdin.read().split()
    print(solve(tokens[1]))


if __name__ == "__main__":
    main()
