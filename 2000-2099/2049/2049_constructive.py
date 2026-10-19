"""Build legal transfers by reversing splits and equal-volume exchanges."""

from array import array
import sys

SPLIT_DIVISOR = 4
OUTPUT_CHUNK = 4096


class State:
    __slots__ = (
        "volumes",
        "previous",
        "following",
        "groups",
        "value_previous",
        "value_following",
        "odd_head",
        "even_head",
        "even_count",
        "from_ids",
        "to_ids",
    )

    def __init__(self, size, target):
        self.volumes = array("I", [0]) * (size + 1)
        self.previous = array("I", [0]) * (size + 1)
        self.following = array("I", [0]) * (size + 1)
        self.groups = array("I", [0]) * (size + 1)
        self.value_previous = array("I", [0]) * (size + 1)
        self.value_following = array("I", [0]) * (size + 1)
        self.odd_head = self.even_head = self.even_count = 0
        self.from_ids, self.to_ids = array("I"), array("I")
        self.volumes[1] = target
        self.attach(1)
        if size != target:
            self.volumes[2] = size - target
            self.attach(2)

    def attach(self, index):
        value = self.volumes[index]
        if value % 2:
            head = self.groups[value]
            if head == 0:
                self.value_previous[value] = 0
                self.value_following[value] = self.odd_head
                if self.odd_head:
                    self.value_previous[self.odd_head] = value
                self.odd_head = value
            self.groups[value] = index
        else:
            head = self.even_head
            self.even_head = index
            self.even_count += 1
        self.previous[index] = 0
        self.following[index] = head
        if head:
            self.previous[head] = index

    def detach(self, index):
        value = self.volumes[index]
        if value == 0:
            return
        before, after = self.previous[index], self.following[index]
        if before:
            self.following[before] = after
        elif value % 2:
            self.groups[value] = after
        else:
            self.even_head = after
        if after:
            self.previous[after] = before
        if value % 2:
            if self.groups[value] == 0:
                before, after = self.value_previous[value], self.value_following[value]
                if before:
                    self.value_following[before] = after
                else:
                    self.odd_head = after
                if after:
                    self.value_previous[after] = before
        else:
            self.even_count -= 1

    def undo(self, donor, receiver):
        self.detach(donor)
        self.detach(receiver)
        half = self.volumes[receiver] // 2
        self.volumes[receiver] = half
        self.volumes[donor] += half
        self.attach(donor)
        self.attach(receiver)
        self.from_ids.append(donor)
        self.to_ids.append(receiver)


def solve(n, k):
    power = k & (k - 1) == 0
    size = k if power else k + 1 + (k & 1)
    if size > n:
        return None
    state = State(size, k)
    empty = array("I", (i for i in range(1, size + 1) if not state.volumes[i]))
    while state.even_count:
        receiver = state.even_head
        if state.even_count > 1 or state.volumes[receiver] % SPLIT_DIVISOR == 0:
            state.undo(empty.pop(), receiver)
            continue
        value = state.odd_head
        if value == state.volumes[receiver] // 2:
            value = state.value_following[value]
        if value == 0:
            state.undo(empty.pop(), receiver)
            continue
        donor = state.groups[value]
        while state.volumes[receiver] % SPLIT_DIVISOR:
            state.undo(donor, receiver)
            receiver, donor = donor, receiver
    return state.from_ids, state.to_ids


def write_answer(answer):
    if answer is None:
        print(-1)
        return
    from_ids, to_ids = answer
    print(len(from_ids))
    output = []
    for i in range(len(from_ids) - 1, -1, -1):
        output.append(f"{from_ids[i]} {to_ids[i]}")
        if len(output) == OUTPUT_CHUNK:
            sys.stdout.write("\n".join(output) + "\n")
            output.clear()
    if output:
        sys.stdout.write("\n".join(output) + "\n")


def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    write_answer(solve(n, k))


if __name__ == "__main__":
    main()
