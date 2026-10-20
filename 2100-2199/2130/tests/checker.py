"""Check each prefix independently, accepting any witness in the allowed range."""

import math
import sys

LIMIT = 10**12
ARGUMENT_COUNT = 3


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source, encoding="utf-8").read().split()))
    count = data[0]
    words = open(output, encoding="utf-8").read().split()
    if len(words) != count:
        raise Bad("expected %d answers" % count)
    if any(word != "-1" and not (word.isascii() and word.isdigit()) for word in words):
        raise Bad("expected integer answers")
    answers = list(map(int, words))
    multiple = 1
    possible = True
    negative = []
    seen_negative = set()
    checked = {}
    for index, answer in enumerate(answers):
        start = 2 * index + 1
        divisor, positive = data[start : start + 2]
        if possible:
            if positive:
                old_multiple = multiple
                multiple = multiple // math.gcd(multiple, divisor) * divisor
                if multiple > LIMIT:
                    possible = False
                elif multiple != old_multiple:
                    possible = all(multiple % value for value in negative)
            elif multiple % divisor == 0:
                possible = False
            elif divisor not in seen_negative:
                seen_negative.add(divisor)
                negative.append(divisor)
        if not possible:
            if answer != -1:
                raise Bad("answer %d: this prefix is contradictory" % (index + 1))
            continue
        if not 1 <= answer <= LIMIT:
            raise Bad("answer %d: a witness between 1 and the limit exists" % (index + 1))
        if answer % multiple:
            raise Bad("answer %d: an affirmative answer is violated" % (index + 1))
        first_unchecked = checked.get(answer, 0)
        if any(answer % value == 0 for value in negative[first_unchecked:]):
            raise Bad("answer %d: a negative answer is violated" % (index + 1))
        checked[answer] = len(negative)


def main():
    try:
        if len(sys.argv) != ARGUMENT_COUNT + 1:
            raise Bad("expected input, expected output, and actual output paths")
        check(*sys.argv[1:])
    except (Bad, OSError, ValueError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
