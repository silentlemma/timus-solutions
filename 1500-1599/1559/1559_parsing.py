import sys
from collections import namedtuple

# what is known about a set of words: is it non-empty, does it hold the empty
# word, does it hold a non-empty word, is it infinite
Words = namedtuple("Words", "any empty_word long_word infinite")
NOTHING = Words(False, False, False, False)
EMPTY_WORD = Words(True, True, False, False)
LETTER = Words(True, False, True, False)


def union(x, y):
    return Words(*(a or b for a, b in zip(x, y)))


def concat(x, y):
    if not (x.any and y.any):
        return NOTHING
    return Words(
        True, x.empty_word and y.empty_word, x.long_word or y.long_word, x.infinite or y.infinite
    )


def star(x):
    # repeating a non-empty word gives ever longer words
    return Words(True, True, x.long_word, x.long_word)


class Frame:
    """One level of brackets: the union so far, the concatenation so far and
    the last symbol, which a star may still apply to."""

    def __init__(self):
        self.all, self.cat, self.last = NOTHING, EMPTY_WORD, None

    def close(self):
        return union(self.all, self.cat if self.last is None else concat(self.cat, self.last))

    def push(self, symbol):
        if self.last is not None:
            self.cat = concat(self.cat, self.last)
        self.last = symbol


def main():
    frames = [Frame()]
    for c in sys.stdin.read():
        frame = frames[-1]
        if c == "(":
            frames.append(Frame())
        elif c == ")":
            frames.pop()
            frames[-1].push(frame.close())
        elif c == "|":
            frame.all, frame.cat, frame.last = frame.close(), EMPTY_WORD, None
        elif c == "*":
            frame.last = star(frame.last)
        elif c == "0":
            frame.push(NOTHING)
        elif "a" <= c <= "z":
            frame.push(LETTER)
    print("N" if frames[0].close().infinite else "F")


main()
