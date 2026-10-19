from array import array
from bisect import bisect_left, bisect_right
from io import BytesIO
import sys


EVENT_FIELDS = 3
COORD_BITS = 32
COORD_MASK = (1 << COORD_BITS) - 1
SMALL_CELLS = 256
DEFER_SAVE_THRESHOLD = 2
HALF = 0.5
WORD_BITS = 60


# Reverse assignments identify the first future save for each section.
# Persistent nodes share routes; negative references identify saves and zero discards energy.
# Endpoint densities flow forward only through additions and positive interpolation.
class Routing:
    def __init__(self, coords, kinds, indexes):
        self.size = size = 1 << (len(coords) - 2).bit_length()
        self.height = size.bit_length() - 1
        self.start = start = array("I", [coords[-1]]) * (2 * size)
        self.width = width = array("I", [0]) * (2 * size)
        for i in range(len(coords) - 1):
            start[size + i] = coords[i]
            width[size + i] = coords[i + 1] - coords[i]
        for i in range(size - 1, 0, -1):
            start[i] = start[2 * i]
            width[i] = width[2 * i] + width[2 * i + 1]
        self.left = array("i", [0])
        self.right = array("i", [0])
        self.nodes = array("I", [0])
        versions = array("i", [0]) * (2 * size)
        self.roots = array("i", [0]) * len(kinds)
        self.begin = array("I", [0]) * len(kinds)
        self.end = array("I", [0]) * len(kinds)
        last_enforce = len(kinds) - 1
        while not kinds[last_enforce]:
            last_enforce -= 1
        deferred = len(kinds) - last_enforce > DEFER_SAVE_THRESHOLD
        self.mutable_base = len(kinds) + 1
        owners = heads = links = None
        phase_end = len(kinds)
        for i in range(len(kinds) - 1, -1, -1):
            if deferred and owners is None:
                owners = array("I", [0]) * (2 * size)
                heads = array("I", [0]) * len(kinds)
                links = array("I", [0]) * (2 * size)
            if kinds[i]:
                if deferred:
                    self.serialize(versions, owners, i, phase_end, heads, links)
                self.roots[i] = versions[1]
                previous = i - 1
                while previous >= 0 and not kinds[previous]:
                    previous -= 1
                if previous < 0:
                    break
                deferred = i - previous > DEFER_SAVE_THRESHOLD
                phase_end = i
                continue
            self.begin[i] = len(self.nodes) - 1
            lo, hi = (indexes[2 * i] + size, indexes[2 * i + 1] + size)
            first_level = (lo & -lo).bit_length()
            last_level = (hi & -hi).bit_length()
            for h in range(self.height, 0, -1):
                first, last = (lo >> h, hi - 1 >> h)
                ptr = versions[first]
                if -self.mutable_base < ptr <= 0:
                    versions[first * 2] = versions[first * 2 + 1] = ptr
                if first != last:
                    ptr = versions[last]
                    if -self.mutable_base < ptr <= 0:
                        versions[last * 2] = versions[last * 2 + 1] = ptr
            a, b = (lo, hi)
            label = -i - 1
            while a < b:
                if a & 1:
                    versions[a] = label
                    a += 1
                if b & 1:
                    b -= 1
                    versions[b] = label
                a >>= 1
                b >>= 1
            for h in range(min(first_level, last_level), self.height + 1):
                if h >= first_level:
                    if deferred:
                        self.defer(versions, owners, lo >> h, i)
                    else:
                        self.rebuild(versions, lo >> h)
                if h >= last_level:
                    node = hi - 1 >> h
                    if node != lo >> h or h < first_level:
                        if deferred:
                            self.defer(versions, owners, node, i)
                        else:
                            self.rebuild(versions, node)
            self.end[i] = len(self.nodes) - 1
        del versions, owners, heads, links
        # Versions of the same segment expire at successive intersecting saves.
        # Their energy lifetimes do not overlap, so spatial nodes share density buffers.
        self.low = array("d", [0.0]) * (2 * size)
        self.high = array("d", [0.0]) * (2 * size)
        self.collected = array("d", [0.0]) * len(kinds)

    def defer(self, versions, owners, node, event):
        left, right = (versions[node * 2], versions[node * 2 + 1])
        if left == right and left <= 0:
            versions[node] = left
        else:
            versions[node] = -self.mutable_base - node
            owners[node] = event

    def serialize(self, versions, owners, enforce, phase_end, heads, links):
        # A run of saves needs only its final partition before the preceding reinforcement.
        # Children precede parents within each save's bucket, preserving forward evaluation.
        stack = [1]
        while stack:
            node = stack.pop()
            if versions[node] < -self.mutable_base:
                event = owners[node]
                links[node] = heads[event]
                heads[event] = node
                stack.extend((node * 2, node * 2 + 1))
        for event in range(phase_end - 1, enforce, -1):
            self.begin[event] = len(self.nodes) - 1
            node = heads[event]
            while node:
                versions[node] = len(self.nodes)
                self.nodes.append(node)
                self.left.append(versions[node * 2])
                self.right.append(versions[node * 2 + 1])
                node = links[node]
            heads[event] = 0
            self.end[event] = len(self.nodes) - 1

    def rebuild(self, versions, node):
        left, right = (versions[node * 2], versions[node * 2 + 1])
        if left == right and left <= 0:
            versions[node] = left
        else:
            ptr = versions[node]
            if ptr > 0 and self.left[ptr] == left and (self.right[ptr] == right):
                return
            versions[node] = len(self.nodes)
            self.nodes.append(node)
            self.left.append(left)
            self.right.append(right)

    def add(self, root, begin, end, origin, direction, scale):
        if begin >= end or root == 0:
            return
        stack = [root, 1]
        while stack:
            node = stack.pop()
            ptr = stack.pop()
            if ptr == 0:
                continue
            left = max(begin, self.start[node])
            right = min(end, self.start[node] + self.width[node])
            if ptr < 0:
                weights = (2 * origin + direction * (left + right - 1)) * (right - left)
                self.collected[-ptr - 1] += weights * HALF * scale
            elif left == self.start[node] and right - left == self.width[node]:
                self.low[node] += (origin + direction * left) * scale
                self.high[node] += (origin + direction * (right - 1)) * scale
            else:
                child = node * 2
                middle = self.start[child + 1]
                if begin < middle:
                    stack.extend((self.left[ptr], child))
                if end > middle:
                    stack.extend((self.right[ptr], child + 1))

    def take(self, event):
        for ptr in range(self.end[event], self.begin[event], -1):
            node = self.nodes[ptr]
            first, last = (self.low[node], self.high[node])
            if first == 0.0 and last == 0.0:
                continue
            self.low[node] = self.high[node] = 0.0
            child = node * 2
            a, b = (self.width[child], self.width[child + 1])
            if first == last or self.width[node] == 1:
                midlow = midhigh = first
            else:
                denominator = self.width[node] - 1
                midlow = (first * b + last * (a - 1)) / denominator
                midhigh = (first * (b - 1) + last * a) / denominator
            target = self.left[ptr]
            if target > 0:
                self.low[child] += first
                self.high[child] += midlow
            elif target < 0:
                self.collected[-target - 1] += (first + midlow) * HALF * a
            target = self.right[ptr]
            if target > 0:
                self.low[child + 1] += midhigh
                self.high[child + 1] += last
            elif target < 0:
                self.collected[-target - 1] += (midhigh + last) * HALF * b
        return self.collected[event]


# Small independent spatial components are cheaper to simulate directly.
def direct(n, p, events, kinds, coords, ends, bounds):
    values = array("d", [0.0]) * (len(coords) - 1)
    times = array("I", [0]) * (len(coords) - 1)
    versions = array("I", [0]) * len(ends)
    epoch = 1
    base = 0
    reserve = 0.0
    output = []
    for at, k in enumerate(kinds):
        off = at * EVENT_FIELDS
        t, a, b = (events[off], events[off + 1], events[off + 2])
        if not k and a == 1 and (b == n):
            reserve = n * p * t
            epoch += 1
            base = t
            output.append(str(reserve))
            continue
        left, right = (a - b + 1, a + b) if k else (a, b + 1)
        component = bisect_left(ends, left)
        if versions[component] != epoch:
            versions[component] = epoch
            lo, hi = (bounds[2 * component], bounds[2 * component + 1])
            for i in range(lo, hi):
                times[i] = base
                values[i] = 0.0
        if k:
            scale = reserve / (b * b)
            lo = bisect_right(coords, left) - 1
            hi = bisect_left(coords, right)
            for i in range(lo, hi):
                x, y = (max(left, coords[i]), min(right, coords[i + 1]))
                middle = min(y, a + 1)
                weights = 0
                if x < middle:
                    weights += (2 * (b - a) + x + middle - 1) * (middle - x)
                middle = max(x, a + 1)
                if middle < y:
                    weights += (2 * (b + a) - middle - y + 1) * (y - middle)
                values[i] += weights * HALF * scale
            reserve = 0.0
        else:
            lo, hi = (bisect_left(coords, left), bisect_left(coords, right))
            natural = 0
            collected = 0.0
            for i in range(lo, hi):
                natural += (t - times[i]) * (coords[i + 1] - coords[i])
                collected += values[i]
                times[i] = t
                values[i] = 0.0
            reserve += collected + natural * p
            output.append(str(reserve))
    sys.stdout.write("\n".join(output))


def main():
    read = BytesIO(sys.stdin.buffer.read()).readline
    n, p = map(int, read().split())
    p = float(p)
    q = int(read())
    events = array("I")
    kinds = bytearray()
    coords = [1, n + 1]
    have = False
    spans = []
    widest = widest_width = 0
    for _ in range(q):
        t, k, a, b = read().split()
        t, a, b = (int(t), int(a), int(b))
        if k == b"enforce":
            if not have:
                continue
            kinds.append(1)
            have = False
        else:
            kinds.append(0)
            coords.extend((a, b + 1))
            have = t != 0
        events.extend((t, a, b))
        if k == b"enforce":
            left, right = a - b + 1, a + b - 1
        elif a != 1 or b != n:
            left, right = a, b
        else:
            continue
        span = (left << COORD_BITS) | right
        spans.append(span)
        if right - left >= widest_width:
            widest, widest_width = span, right - left
    del read
    coords = sorted(set(coords))
    if 1 not in kinds:
        growth = Growth(coords)
        reserve = 0.0
        output = []
        for off in range(0, len(events), EVENT_FIELDS):
            t, a, b = (events[off], events[off + 1], events[off + 2])
            x, y = (bisect_left(coords, a), bisect_left(coords, b + 1))
            reserve += growth.take(x, y, t) * p
            output.append(str(reserve))
        sys.stdout.write("\n".join(output))
        return
    ends = []
    bounds = array("I")
    begin = finish = 0
    lo = bisect_right(coords, widest >> COORD_BITS) - 1
    hi = bisect_left(coords, (widest & COORD_MASK) + 1)
    small = hi - lo <= SMALL_CELLS
    for span in sorted(spans) if small else ():
        left, right = (span >> COORD_BITS, span & COORD_MASK)
        if left > finish and finish:
            lo, hi = (bisect_right(coords, begin) - 1, bisect_left(coords, finish + 1))
            bounds.extend((lo, hi))
            ends.append(finish)
            small &= hi - lo <= SMALL_CELLS
            begin, finish = (left, right)
        else:
            if not finish:
                begin = left
            finish = max(finish, right)
    if finish:
        lo, hi = (bisect_right(coords, begin) - 1, bisect_left(coords, finish + 1))
        bounds.extend((lo, hi))
        ends.append(finish)
        small &= hi - lo <= SMALL_CELLS
    if small:
        direct(n, p, events, kinds, coords, ends, bounds)
        return
    del spans, ends, bounds
    lookup = {x: i for i, x in enumerate(coords)}
    if transfers(events, kinds, coords, p, lookup):
        return
    small_saves = True
    full_saves = 0
    indexes = array("I")
    for i, k in enumerate(kinds):
        if k:
            indexes.extend((0, 0))
        else:
            at = EVENT_FIELDS * i
            left, right = lookup[events[at + 1]], lookup[events[at + 2] + 1]
            indexes.extend((left, right))
            full = events[at + 1] == 1 and events[at + 2] == n
            full_saves += full
            if not full:
                small_saves &= right - left <= LOCAL_CELLS
    del lookup
    if small_saves and full_saves * len(coords) <= len(kinds) * LOCAL_CELLS:
        simulate_local(n, p, events, kinds, coords, indexes)
        return
    wall = Routing(coords, kinds, indexes)
    growth = Growth(coords)
    reserve = 0.0
    output = []
    for i, k in enumerate(kinds):
        at = i * EVENT_FIELDS
        t, a, b = (events[at], events[at + 1], events[at + 2])
        if k:
            scale = reserve / (b * b)
            wall.add(wall.roots[i], a - b + 1, a + 1, b - a, 1, scale)
            wall.add(wall.roots[i], a + 1, a + b, b + a, -1, scale)
            reserve = 0.0
        else:
            x, y = (indexes[2 * i], indexes[2 * i + 1])
            natural = growth.take(x, y, t) * p
            reserve += natural + wall.take(i)
            output.append(str(reserve))
    sys.stdout.write("\n".join(output))


# All three levels fit machine integers at the maximum number of save boundaries.
class Bits:
    def __init__(self, count):
        self.words = array("Q", [0]) * ((count + WORD_BITS - 1) // WORD_BITS)
        self.groups = array("Q", [0]) * ((len(self.words) + WORD_BITS - 1) // WORD_BITS)
        self.summary = 0

    def insert(self, node):
        w, b = divmod(node, WORD_BITS)
        old = self.words[w]
        self.words[w] = old | 1 << b
        if not old:
            g, b = divmod(w, WORD_BITS)
            old = self.groups[g]
            self.groups[g] = old | 1 << b
            if not old:
                self.summary |= 1 << g

    def remove(self, node):
        w, b = divmod(node, WORD_BITS)
        self.words[w] &= ~(1 << b)
        if not self.words[w]:
            g, b = divmod(w, WORD_BITS)
            self.groups[g] &= ~(1 << b)
            if not self.groups[g]:
                self.summary &= ~(1 << g)

    def previous(self, node):
        w, b = divmod(node, WORD_BITS)
        selected = self.words[w] & (1 << b + 1) - 1
        if selected:
            return w * WORD_BITS + selected.bit_length() - 1
        g, b = divmod(w, WORD_BITS)
        selected = self.groups[g] & (1 << b) - 1
        if not selected:
            g = (self.summary & (1 << g) - 1).bit_length() - 1
            selected = self.groups[g]
        w = g * WORD_BITS + selected.bit_length() - 1
        return w * WORD_BITS + self.words[w].bit_length() - 1


# Natural growth depends only on the last save time in each interval.
# Overwritten boundaries disappear once, so interval traversal is amortized linear.
class Growth:
    def __init__(self, coords):
        self.coords = coords
        self.times = array("I", [0]) * len(coords)
        self.next = array("I", [0]) * len(coords)
        self.next[0] = len(coords) - 1
        self.bits = Bits(len(coords))
        self.bits.insert(0)
        self.bits.insert(len(coords) - 1)

    def take(self, a, b, t):
        prev = self.bits.previous(a)
        at = prev
        right = self.next[at]
        x = self.coords[a]
        total = 0
        while right < b:
            total += (t - self.times[at]) * (self.coords[right] - x)
            x = self.coords[right]
            at = right
            right = self.next[at]
            self.bits.remove(at)
        total += (t - self.times[at]) * (self.coords[b] - x)
        old = self.times[at]
        if a != prev:
            self.next[prev] = a
            self.bits.insert(a)
        self.times[a] = t
        self.next[a] = b
        if right != b:
            self.times[b] = old
            self.next[b] = right
            self.bits.insert(b)
        return total


TRANSFER_EDGES = 1000000
TRANSFER_SAMPLE = 32
TRANSFER_SPANS = 128


# A reverse interval map sends each reinforcement directly to its first future saves.
# Overwritten intervals also give the natural growth between successive saves.
# A bounded edge budget keeps fragmented maps on the general routing path.
def transfers(events, kinds, coords, p, lookup):
    labels = array("I", [0]) * len(coords)
    links = array("I", [0]) * len(coords)
    links[0] = len(coords) - 1
    bits = Bits(len(coords))
    bits.insert(0)
    bits.insert(len(coords) - 1)
    collected = array("d", [0.0]) * len(kinds)
    begin = array("I", [0]) * len(kinds)
    end = array("I", [0]) * len(kinds)
    targets = array("I")
    weights = array("Q")
    remaining = sum(kinds)
    enforcements = remaining
    processed = largest = 0
    for i in range(len(kinds) - 1, -1, -1):
        off = i * EVENT_FIELDS
        t, a, b = events[off], events[off + 1], events[off + 2]
        if kinds[i]:
            left, right = a - b + 1, a + b
            at = bits.previous(bisect_right(coords, left) - 1)
            nxt = links[at]
            x = left
            begin[i] = len(targets)
            spans = 0
            full = (
                i > 0
                and not kinds[i - 1]
                and events[off - 2] == 1
                and (events[off - 1] + 1 == coords[-1])
            )
            while x < right:
                spans += 1
                if spans > TRANSFER_SPANS and remaining > 2 and not full:
                    return False
                y = min(right, coords[nxt])
                label = labels[at]
                if label:
                    if y <= a + 1:
                        weight = (2 * (b - a) + x + y - 1) * (y - x) // 2
                    elif x > a:
                        weight = (2 * (b + a) - x - y + 1) * (y - x) // 2
                    else:
                        k = a - x + 1
                        weight = (2 * b - k + 1) * k // 2
                        k = y - a - 1
                        weight += (2 * b - k - 1) * k // 2
                    targets.append(label - 1)
                    weights.append(weight)
                    if len(targets) > TRANSFER_EDGES:
                        return False
                x = y
                at = nxt
                nxt = links[at]
            end[i] = len(targets)
            remaining -= 1
            processed += 1
            largest = max(largest, end[i] - begin[i])
            if processed >= TRANSFER_SAMPLE and (
                (len(targets) - largest) * enforcements > TRANSFER_EDGES * processed
            ):
                return False
        else:
            a, z = lookup[a], lookup[b + 1]
            prev = bits.previous(a)
            at = prev
            nxt = links[at]
            x = coords[a]
            while nxt < z:
                label = labels[at]
                if label:
                    collected[label - 1] += (
                        (events[(label - 1) * EVENT_FIELDS] - t) * (coords[nxt] - x) * p
                    )
                x = coords[nxt]
                at = nxt
                nxt = links[at]
                bits.remove(at)
            label = labels[at]
            if label:
                collected[label - 1] += (
                    (events[(label - 1) * EVENT_FIELDS] - t) * (coords[z] - x) * p
                )
            if a != prev:
                links[prev] = a
                bits.insert(a)
            labels[a] = i + 1
            links[a] = z
            if nxt != z:
                labels[z] = label
                links[z] = nxt
                bits.insert(z)
    at = 0
    while links[at]:
        nxt = links[at]
        label = labels[at]
        if label:
            collected[label - 1] += (
                events[(label - 1) * EVENT_FIELDS] * (coords[nxt] - coords[at]) * p
            )
        at = nxt
    reserve = 0.0
    output = []
    for i, k in enumerate(kinds):
        if k:
            b = events[i * EVENT_FIELDS + 2]
            scale = reserve / (b * b)
            for j in range(begin[i], end[i]):
                collected[targets[j]] += weights[j] * scale
            reserve = 0.0
        else:
            reserve += collected[i]
            output.append(str(reserve))
    sys.stdout.write("\n".join(output))
    return True


LOCAL_PYTHON_CELLS = 32
LOCAL_CELLS = 128 if sys.implementation.name == "pypy" else LOCAL_PYTHON_CELLS


# Narrow saves drain short subtrees without maintaining sums or persistent versions.
# A full-wall save uses conservation of energy and clears the numeric buffers.
class LocalWall:
    def __init__(self, coords):
        self.coords = coords
        self.size = size = 1 << (len(coords) - 2).bit_length()
        self.start = start = array("I", [coords[-1]]) * (2 * size)
        self.width = width = array("I", [0]) * (2 * size)
        for i in range(len(coords) - 1):
            start[size + i] = coords[i]
            width[size + i] = coords[i + 1] - coords[i]
        for i in range(size - 1, 0, -1):
            start[i] = start[2 * i]
            width[i] = width[2 * i] + width[2 * i + 1]
        self.low = array("d", [0.0]) * (2 * size)
        self.high = array("d", [0.0]) * (2 * size)

    def deposit(self, node, first, last):
        self.low[node] += first
        self.high[node] += last

    def partial(self, index, left, right, origin, direction, scale):
        if left >= right:
            return
        node = self.size + index
        value = (2 * origin + direction * (left + right - 1)) * (right - left) * HALF * scale
        value /= self.width[node]
        self.deposit(node, value, value)

    def add(self, begin, end, origin, direction, scale):
        if begin >= end:
            return
        lo, hi = bisect_left(self.coords, begin), bisect_right(self.coords, end) - 1
        if lo > hi:
            self.partial(hi, begin, end, origin, direction, scale)
            return
        if self.coords[lo] > begin:
            self.partial(lo - 1, begin, self.coords[lo], origin, direction, scale)
        if self.coords[hi] < end:
            self.partial(hi, self.coords[hi], end, origin, direction, scale)
        left, right = lo + self.size, hi + self.size
        while left < right:
            if left & 1:
                first = origin + direction * self.start[left]
                self.deposit(
                    left, first * scale, (first + direction * (self.width[left] - 1)) * scale
                )
                left += 1
            if right & 1:
                right -= 1
                first = origin + direction * self.start[right]
                self.deposit(
                    right, first * scale, (first + direction * (self.width[right] - 1)) * scale
                )
            left >>= 1
            right >>= 1

    def take(self, begin, end):
        stack = [1]
        result = 0.0
        while stack:
            node = stack.pop()
            if not self.width[node]:
                continue
            child = node * 2
            first, last = self.low[node], self.high[node]
            if begin <= self.start[node] and self.start[node] + self.width[node] <= end:
                result += (first + last) * HALF * self.width[node]
                self.low[node] = self.high[node] = 0.0
                if node < self.size:
                    stack.append(child)
                    stack.append(child + 1)
            else:
                if first or last:
                    a, b = self.width[child], self.width[child + 1]
                    if first == last:
                        midlow = midhigh = first
                    else:
                        w = a + b - 1
                        midlow = (first * b + last * (a - 1)) / w
                        midhigh = (first * (b - 1) + last * a) / w
                    self.deposit(child, first, midlow)
                    self.deposit(child + 1, midhigh, last)
                    self.low[node] = self.high[node] = 0.0
                middle = self.start[child + 1]
                if begin < middle:
                    stack.append(child)
                if end > middle:
                    stack.append(child + 1)
        return result


def simulate_local(n, p, events, kinds, coords, indexes):
    wall = LocalWall(coords)
    times = array("I", [0]) * len(coords)
    reserve = 0.0
    output = []
    for i, k in enumerate(kinds):
        off = i * EVENT_FIELDS
        t, a, b = events[off], events[off + 1], events[off + 2]
        if k:
            scale = reserve / (b * b)
            wall.add(a - b + 1, a + 1, b - a, 1, scale)
            wall.add(a + 1, a + b, b + a, -1, scale)
            reserve = 0.0
        elif a == 1 and b == n:
            reserve = n * p * t
            wall.low = array("d", [0.0]) * (2 * wall.size)
            wall.high = array("d", [0.0]) * (2 * wall.size)
            times = array("I", [t]) * len(coords)
            output.append(str(reserve))
        else:
            lo, hi = indexes[2 * i], indexes[2 * i + 1]
            natural = 0
            for j in range(lo, hi):
                last = times[j]
                natural += (t - last) * (coords[j + 1] - coords[j])
                times[j] = t
            reserve += natural * p + wall.take(a, b + 1)
            output.append(str(reserve))
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
