"""Compare palindrome frequencies with a compact shared palindromic tree."""

from array import array
from io import BytesIO
import re
import sys

OUTPUT_BATCH = 4096
BYTE_VALUES = 256
SHORT_PALINDROME = re.compile(rb"(.)\1|(.).\2")


def compare_periodic(a, b):
    """Count each alternating palindrome family by its decreasing frequencies."""
    na, nb = len(a), len(b)
    if a.count(a[:1]) == na and b.count(b[:1]) == nb:
        if a[0] != b[0]:
            return na, 0, nb
        if na > nb:
            return na, 0, 0
        if na < nb:
            return 0, 0, nb
        return 0, na, 0
    if na < 2 or nb < 2 or a[0] == a[1] or b[0] == b[1]:
        return None
    if a[2:] != a[:-2] or b[2:] != b[:-2]:
        return None
    x = y = z = 0
    if a[:2] == b[:2] or a[:2] == b[1::-1]:
        for letter in a[:2]:
            ca = (na + 1 - (a[0] != letter)) // 2
            cb = (nb + 1 - (b[0] != letter)) // 2
            if ca > cb:
                x += ca
            elif ca < cb:
                z += cb
            else:
                y += ca
    else:
        x, z = na - 2, nb - 2
        for letter in set(a[:2] + b[:2]):
            ca = (na + 1 - (a[0] != letter)) // 2 if letter in a[:2] else 0
            cb = (nb + 1 - (b[0] != letter)) // 2 if letter in b[:2] else 0
            if ca > cb:
                x += 1
            elif ca < cb:
                z += 1
            else:
                y += 1
    return x, y, z


class Tree:
    def __init__(self):
        self.span = array("i", [0, 1])
        self.link = array("i", [0, 0])
        self.first = array("i", [0, 0])
        self.next = array("i", [0, 0])
        self.label = bytearray(2)
        self.count = array("i", [0, 0])

    def solve(self, a, b):
        answer = compare_periodic(a, b)
        if answer is not None:
            return answer
        if not SHORT_PALINDROME.search(a) and not SHORT_PALINDROME.search(b):
            x = y = z = 0
            for letter in set(a + b):
                character = bytes([letter])
                ca, cb = a.count(character), b.count(character)
                if ca > cb:
                    x += 1
                elif ca < cb:
                    z += 1
                else:
                    y += 1
            return x, y, z
        equal = a == b
        if equal:
            b = b""
        n = len(a) + len(b) + 2
        missing = n - len(self.span)
        if missing > 0:
            zero = array("i", [0]) * missing
            for storage in (self.span, self.link, self.first, self.next, self.count):
                storage.extend(zero)
            self.label.extend(b"\0" * missing)
        span, link = self.span, self.link
        first, next_node, label = self.first, self.next, self.label
        count = self.count
        count[0] = count[1] = 0
        roots = array("i", [0]) * (2 * BYTE_VALUES)
        nodes = 2
        for word, increment in ((a, 1), (b, -1)):
            data = b"\0" + word
            last = 1
            for end in range(1, len(data)):
                letter = data[end]
                node = last
                while data[end - span[node]] != letter:
                    node = link[node]
                if node < 2:
                    found = roots[node * BYTE_VALUES + letter]
                else:
                    found = first[node]
                    while found and label[found] != letter:
                        found = next_node[found]
                if not found:
                    found = nodes
                    nodes += 1
                    size = span[node] + 2
                    suffix = 1
                    if size != 2:
                        candidate = link[node]
                        while data[end - span[candidate]] != letter:
                            candidate = link[candidate]
                        if candidate < 2:
                            suffix = roots[candidate * BYTE_VALUES + letter]
                        else:
                            suffix = first[candidate]
                            while label[suffix] != letter:
                                suffix = next_node[suffix]
                    span[found] = size
                    link[found] = suffix
                    first[found] = 0
                    if node < 2:
                        roots[node * BYTE_VALUES + letter] = found
                    else:
                        next_node[found] = first[node]
                        label[found] = letter
                        first[node] = found
                    count[found] = 0
                last = found
                count[found] += increment
        if equal:
            return 0, nodes - 2, 0
        x = y = z = 0
        for node in range(nodes - 1, 1, -1):
            diff = count[node]
            count[link[node]] += diff
            if diff > 0:
                x += 1
            elif diff == 0:
                y += 1
            else:
                z += 1
        return x, y, z


def main():
    stream = BytesIO(sys.stdin.buffer.read())
    total = int(stream.readline())
    tree = Tree()
    previous_a = previous_b = None
    previous_answer = None
    output = []
    for index in range(1, total + 1):
        a = stream.readline().rstrip(b"\r\n")
        b = stream.readline().rstrip(b"\r\n")
        if len(a) == len(b) == 1:
            tail = b": 0 1 0\n" if a == b else b": 1 0 1\n"
            output.append(b"Case #" + str(index).encode() + tail)
        else:
            if a == previous_a and b == previous_b:
                x, y, z = previous_answer
            elif a == previous_b and b == previous_a:
                z, y, x = previous_answer
            else:
                x, y, z = tree.solve(a, b)
            previous_a, previous_b = a, b
            previous_answer = x, y, z
            output.append(f"Case #{index}: {x} {y} {z}\n".encode())
        if len(output) == OUTPUT_BATCH:
            sys.stdout.buffer.write(b"".join(output))
            output.clear()
    sys.stdout.buffer.write(b"".join(output))


if __name__ == "__main__":
    main()
