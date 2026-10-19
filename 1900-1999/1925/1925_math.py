import sys


def required_input(current, pairs):
    answer = current - 2
    for displayed, entered in pairs:
        answer += displayed - entered - 2
    return answer


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count, current = next(tokens), next(tokens)
    pairs = ((next(tokens), next(tokens)) for _ in range(count))
    answer = required_input(current, pairs)
    print(answer if answer >= 0 else "Big Bang!")


if __name__ == "__main__":
    main()
