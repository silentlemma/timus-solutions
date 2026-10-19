import sys


def locate(left, right, queries):
    stack = []
    answers = []
    index = 0
    for point in queries:
        while index < len(left) and left[index] <= point:
            while stack and right[stack[-1]] < left[index]:
                stack.pop()
            stack.append(index)
            index += 1
        while stack and right[stack[-1]] < point:
            stack.pop()
        answers.append(stack[-1] + 1 if stack else -1)
    return answers


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    left, right = [], []
    for _ in range(n):
        left.append(next(tokens))
        right.append(next(tokens))
    m = next(tokens)
    answers = locate(left, right, (next(tokens) for _ in range(m)))
    print("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
