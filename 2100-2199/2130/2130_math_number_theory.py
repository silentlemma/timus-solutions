import sys
from math import gcd

LIMIT = 1_000_000_000_000


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(data)
    multiple = 1
    forbidden = []
    possible = True
    answers = []
    for _ in range(count):
        divisor = next(data)
        positive = next(data)
        if possible:
            if positive:
                updated = multiple * (divisor // gcd(multiple, divisor))
                if updated > LIMIT:
                    possible = False
                elif updated != multiple:
                    multiple = updated
                    # A strict LCM increase at least doubles the candidate.
                    for value in forbidden:
                        if multiple % value == 0:
                            possible = False
                            break
            elif multiple % divisor == 0:
                possible = False
            else:
                forbidden.append(divisor)
        answers.append(str(multiple) if possible else "-1")
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
