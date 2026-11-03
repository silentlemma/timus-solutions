import sys
from array import array


class Automaton:
    def __init__(self, text):
        self.length = array("i", [0])
        self.link = array("i", [-1])
        self.head = array("i", [-1])
        self.target = array("i")
        self.following = array("i")
        self.letter = bytearray()
        last = 0
        for ch in text:
            current = len(self.length)
            self.length.append(self.length[last] + 1)
            self.link.append(0)
            self.head.append(-1)
            state = last
            while state >= 0 and self.find(state, ch) < 0:
                self.add(state, ch, current)
                state = self.link[state]
            if state >= 0:
                target = self.target[self.find(state, ch)]
                if self.length[state] + 1 == self.length[target]:
                    self.link[current] = target
                else:
                    clone = len(self.length)
                    self.length.append(self.length[state] + 1)
                    self.link.append(self.link[target])
                    self.head.append(-1)
                    # A clone needs independent edges because redirects may
                    # later change either state's transition destinations.
                    edge = self.head[target]
                    while edge >= 0:
                        self.add(clone, self.letter[edge], self.target[edge])
                        edge = self.following[edge]
                    while state >= 0:
                        edge = self.find(state, ch)
                        if edge < 0 or self.target[edge] != target:
                            break
                        self.target[edge] = clone
                        state = self.link[state]
                    self.link[target] = self.link[current] = clone
            last = current

    def find(self, state, ch):
        # Sparse transitions use linear scans of at most the 26 letters.
        edge = self.head[state]
        while edge >= 0 and self.letter[edge] != ch:
            edge = self.following[edge]
        return edge

    def add(self, state, ch, target):
        self.target.append(target)
        self.following.append(self.head[state])
        self.letter.append(ch)
        self.head[state] = len(self.target) - 1


def main():
    data = sys.stdin.buffer.read().split()
    first, second = data[1], data[2]
    a = Automaton(first)
    state, run, best, end = 0, 0, 0, 0
    for i, ch in enumerate(second):
        edge = a.find(state, ch)
        while state and edge < 0:
            state = a.link[state]
            run = a.length[state]
            edge = a.find(state, ch)
        if edge >= 0:
            state = a.target[edge]
            run += 1
        else:
            run = 0
        if run > best:
            best, end = run, i + 1
    print(second[end - best : end].decode())


main()
