"""Rules and a text: a seed and a mode. Words use few letters in mixed case
so that many rules match. Mode 1 writes ordinary lines, mode 2 long runs
of punctuation between words, mode 3 empty lines and no final line
break. Mode 4 writes exactly 100 rules of 40 letters and 450 lines of
250 characters, with random words and competing splits of one suffix."""

import random
import sys

RULES = 100
RULE_LEN = 40
LINES = 450
LINE_LEN = 250
WORD_LEN = 40


def word(rng, top):
    return "".join(rng.choice("abAB") for _ in range(rng.randint(1, top)))


def maximum(rng):
    common = "".join(rng.choice("abAB") for _ in range(WORD_LEN))
    rules = [common[:cut] + "-" + common[cut:] for cut in range(1, WORD_LEN)]
    words = [common]
    while len(rules) < RULES:
        w = "".join(rng.choice("abAB") for _ in range(WORD_LEN))
        cut = rng.randint(1, WORD_LEN - 1)
        rules.append(w[:cut] + "-" + w[cut:])
        words.append(w)
    rng.shuffle(rules)
    print(RULES)
    print("\n".join(rules))
    for _ in range(LINES):
        line = "." * rng.randint(0, WORD_LEN - 1)
        while len(line) < LINE_LEN:
            w = common if rng.random() < 0.5 else rng.choice(words)
            gap = "".join(rng.choice(" ,.-09") for _ in range(rng.randint(1, 6)))
            line += w.swapcase() + gap
        print(line[:LINE_LEN])


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        maximum(rng)
        return
    rules = []
    for _ in range(rng.randint(0, RULES)):
        left = word(rng, rng.randint(1, RULE_LEN // 4))
        right = word(rng, min(rng.randint(1, RULE_LEN // 4), RULE_LEN - len(left)))
        rules.append(left + "-" + right)
    seps = " ,." if mode != 2 else "....... ,"
    lines = []
    for _ in range(rng.randint(1, LINES)):
        if mode == 3 and rng.random() < 0.2:
            lines.append("")
            continue
        line = rng.choice(["", " "])
        while True:
            w = word(rng, rng.choice([4, 12, WORD_LEN]))
            gap = "".join(rng.choice(seps) for _ in range(rng.randint(1, 3 if mode != 2 else 30)))
            if len(line) + len(w) + len(gap) > LINE_LEN:
                break
            line += w + gap
            if rng.random() < 0.1:
                break
        lines.append(line)
    end = "" if mode == 3 else "\n"
    sys.stdout.write("%d\n%s\n%s%s" % (len(rules), "\n".join(rules), "\n".join(lines), end))


if __name__ == "__main__":
    main()
