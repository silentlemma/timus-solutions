import sys


class Modes:
    def __init__(self, alphabet, capacity):
        self.frequency = [0] * (alphabet + 1)
        self.previous = [0] * (alphabet + 1)
        self.following = [0] * (alphabet + 1)
        self.head = [0] * (capacity + 1)
        self.maximum = 0

    def change(self, value, delta):
        frequency = self.frequency
        previous = self.previous
        following = self.following
        head = self.head
        old = frequency[value]
        if old:
            left, right = previous[value], following[value]
            if left:
                following[left] = right
            else:
                head[old] = right
            if right:
                previous[right] = left
        new = old + delta
        frequency[value] = new
        if new:
            first = head[new]
            previous[value] = 0
            following[value] = first
            if first:
                previous[first] = value
            head[new] = value
        else:
            previous[value] = following[value] = 0
        maximum = max(self.maximum, new)
        while maximum and head[maximum] == 0:
            maximum -= 1
        self.maximum = maximum

    def mode(self):
        return self.head[self.maximum]


def restore(text, pattern):
    text = text[:]
    pattern = pattern[:]
    n, m = len(text), len(pattern)
    gap = n - m
    alphabet = max(max(text), max(pattern))
    if 0 in text:
        counter = Modes(alphabet, m)
        for index in range(n):
            if index < m:
                counter.change(pattern[index], 1)
            if index > gap:
                counter.change(pattern[index - gap - 1], -1)
            if text[index] == 0:
                text[index] = counter.mode()
    elif 0 in pattern:
        width = gap + 1
        counter = Modes(alphabet, width)
        for value in text[:width]:
            counter.change(value, 1)
        for index in range(m):
            if pattern[index] == 0:
                pattern[index] = counter.mode()
            if index + 1 < m:
                counter.change(text[index], -1)
                counter.change(text[index + width], 1)
    return text, pattern


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    text = data[1 : n + 1]
    m = data[n + 1]
    pattern = data[n + 2 : n + 2 + m]
    text, pattern = restore(text, pattern)
    print(*text)
    print(*pattern)


if __name__ == "__main__":
    main()
