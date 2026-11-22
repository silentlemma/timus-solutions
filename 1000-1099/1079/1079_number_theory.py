import sys

MAX_BITS = 17
FIBONACCI = [0, 1]
for _ in range(MAX_BITS):
    FIBONACCI.append(FIBONACCI[-1] + FIBONACCI[-2])


def maximum(n):
    a, b, answer = 0, 1, 0
    for remaining in range(n.bit_length() - 1, -1, -1):
        if (n >> remaining) & 1:
            # Fibonacci weights maximize the unrestricted zero branch from its
            # adjacent Stern values; the final-bit case contributes only a.
            bound = (
                a
                if remaining == 0
                else FIBONACCI[remaining + 1] * (a + b) + FIBONACCI[remaining] * a
            )
            if bound > answer:
                answer = bound
            a += b
        else:
            b += a
    return max(answer, a)


def main():
    answers = []
    for n in map(int, sys.stdin.buffer.read().split()):
        if n == 0:
            break
        answers.append(str(maximum(n)))
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
