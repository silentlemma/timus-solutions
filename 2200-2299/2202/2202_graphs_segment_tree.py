import sys

UNSEEN = -1


class SegmentTree:
    def __init__(self, mate):
        self.absent = len(mate)
        self.size = 1
        while self.size < self.absent:
            self.size *= 2
        self.low = [self.absent] * (2 * self.size)
        self.high = [UNSEEN] * (2 * self.size)
        self.low[self.size : self.size + self.absent] = mate
        self.high[self.size : self.size + self.absent] = mate
        low, high = self.low, self.high
        for node in range(self.size - 1, 0, -1):
            child = 2 * node
            a, b = low[child], low[child + 1]
            low[node] = a if a < b else b
            a, b = high[child], high[child + 1]
            high[node] = a if a > b else b

    def erase(self, position):
        node = self.size + position
        low, high = self.low, self.high
        low[node] = self.absent
        high[node] = UNSEEN
        node //= 2
        while node:
            child = 2 * node
            a, b = low[child], low[child + 1]
            new_low = a if a < b else b
            a, b = high[child], high[child + 1]
            new_high = a if a > b else b
            if low[node] == new_low and high[node] == new_high:
                break
            low[node], high[node] = new_low, new_high
            node //= 2

    def crossing(self, left, right):
        first = self.size + left + 1
        last = self.size + right
        low, high = self.low, self.high
        while first < last:
            if first & 1:
                if low[first] < left:
                    return low[first]
                if high[first] > right:
                    return high[first]
                first += 1
            if last & 1:
                last -= 1
                if low[last] < left:
                    return low[last]
                if high[last] > right:
                    return high[last]
            first //= 2
            last //= 2
        return UNSEEN


def region(x, y, width, height):
    if x < 0 or x > width or y < 0 or y > height:
        return UNSEEN
    return int(0 < x < width and 0 < y < height)


def perimeter(x, y, width, height):
    if y == 0:
        return x
    if x == width:
        return width + y
    if y == height:
        return 2 * width + height - x
    return 2 * (width + height) - y


def main():
    read = sys.stdin.buffer.readline
    n, width, height = map(int, read().split())
    events = []
    count = 0
    for _ in range(n):
        x, y, u, v = map(int, read().split())
        first = region(x, y, width, height)
        second = region(u, v, width, height)
        if first * second == UNSEEN:
            print("NO")
            return
        if first == 0 and second == 0:
            events.append((perimeter(x, y, width, height), count))
            events.append((perimeter(u, v, width, height), count))
            count += 1

    events.sort()
    left, right = [UNSEEN] * count, [0] * count
    owner = [pair for _, pair in events]
    for position, pair in enumerate(owner):
        if left[pair] == UNSEEN:
            left[pair] = position
        else:
            right[pair] = position
    del events
    mate = [0] * len(owner)
    for pair in range(count):
        mate[left[pair]] = right[pair]
        mate[right[pair]] = left[pair]

    tree = SegmentTree(mate)
    color = [UNSEEN] * count
    for root in range(count):
        if color[root] != UNSEEN:
            continue
        color[root] = 0
        tree.erase(left[root])
        tree.erase(right[root])
        queue = [root]
        # Find a spanning forest without listing every crossing.
        for pair in queue:
            while True:
                witness = tree.crossing(left[pair], right[pair])
                if witness == UNSEEN:
                    break
                other = owner[witness]
                color[other] = color[pair] ^ 1
                tree.erase(left[other])
                tree.erase(right[other])
                queue.append(other)

    # Each side must have a properly nested boundary matching.
    stacks = [[], []]
    for position, pair in enumerate(owner):
        stack = stacks[color[pair]]
        if position == left[pair]:
            stack.append(pair)
        elif not stack or stack.pop() != pair:
            print("NO")
            return
    print("YES")


main()
