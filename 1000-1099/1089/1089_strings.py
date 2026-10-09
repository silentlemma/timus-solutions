import re
import sys


def main():
    lines = sys.stdin.read().split("\n")
    stop = next(i for i, line in enumerate(lines) if line.strip() == "#")
    known = {w.strip() for w in lines[:stop] if w.strip()}
    by_length = {}
    for w in known:
        by_length.setdefault(len(w), []).append(w)
    errors = 0

    def fix(match):
        nonlocal errors
        word = match.group(0)
        if word in known:
            return word
        # only a single wrong letter is corrected, never a missing or extra one
        for d in by_length.get(len(word), []):
            if sum(a != b for a, b in zip(d, word)) == 1:
                errors += 1
                return d
        return word

    text = "\n".join(line.rstrip("\r") for line in lines[stop + 1 :])
    if not text.endswith("\n"):
        text += "\n"
    sys.stdout.write(re.sub("[a-z]+", fix, text) + str(errors) + "\n")


main()
