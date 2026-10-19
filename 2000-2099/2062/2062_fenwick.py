"""Track radiation with range-add Fenwick sums over exact divisor pairs."""

from array import array
from math import isqrt
import sys

OUTPUT_BATCH = 1024


def divisors_csr(size):
    offsets = array("I", [0]) * (size + 2)
    for divisor in range(1, isqrt(size) + 1):
        for multiple in range(divisor * divisor, size + 1, divisor):
            offsets[multiple + 1] += 1
    for index in range(1, size + 2):
        offsets[index] += offsets[index - 1]
    values = array("H", [0]) * offsets[-1]
    cursor = array("I", offsets)
    for divisor in range(1, isqrt(size) + 1):
        for multiple in range(divisor * divisor, size + 1, divisor):
            at = cursor[multiple]
            values[at] = divisor
            cursor[multiple] = at + 1
    return offsets, values


class Charges:
    def __init__(self, initial):
        self.size = len(initial) - 1
        self.initial = initial
        self.offsets, self.divisors = divisors_csr(self.size)
        self.tree = array("q", [0]) * (self.size + 1)

    def irradiate(self, left, right, power):
        size, tree = self.size, self.tree
        while left <= size:
            tree[left] += power
            left += left & -left
        right += 1
        while right <= size:
            tree[right] -= power
            right += right & -right

    def measure(self, index):
        total = self.initial[index]
        offsets, divisors, tree = self.offsets, self.divisors, self.tree
        for at in range(offsets[index], offsets[index + 1]):
            divisor = divisors[at]
            partner = index // divisor
            while divisor:
                total += tree[divisor]
                divisor &= divisor - 1
            if partner != divisors[at]:
                while partner:
                    total += tree[partner]
                    partner &= partner - 1
        return total


def main():
    read = sys.stdin.buffer.readline
    size = int(read())
    initial = array("q", [0])
    initial.extend(map(int, read().split()))
    assert len(initial) == size + 1
    charges = Charges(initial)
    count = int(read())
    output = []
    write = sys.stdout.write
    for _ in range(count):
        query = iter(map(int, read().split()))
        if next(query) == 1:
            output.append(str(charges.measure(next(query))))
            if len(output) == OUTPUT_BATCH:
                write("\n".join(output) + "\n")
                output.clear()
        else:
            charges.irradiate(next(query), next(query), next(query))
    if output:
        write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
