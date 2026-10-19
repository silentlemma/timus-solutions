"""Batch paints and repair bounded palindrome counts near surviving boundaries."""

import sys
from array import array
from bisect import bisect_left, bisect_right
from functools import lru_cache

BYTE_VALUES = 256
INCREMENT = bytes(min(i + 1, BYTE_VALUES - 1) for i in range(BYTE_VALUES))
POPCOUNT_WIDTH = 17
POPCOUNT_MASK = (1 << POPCOUNT_WIDTH) - 1
POPCOUNT = b'\x00'
for unused in range(POPCOUNT_WIDTH):
    POPCOUNT += POPCOUNT.translate(INCREMENT)

BLOCK = 128
SUM_BITS = 23
SUM_MASK = (1 << SUM_BITS) - 1
CACHE_SIZE = 4096
LETTER_FIELD = 3
ASCII_SIZE = 128
BASE_CASES = (1 << 2) - 1
QUERY_CACHE_SIZE = 512
UNIFORM_CACHE_SIZE = 256


@lru_cache(maxsize=UNIFORM_CACHE_SIZE)
def uniform_ends(n, k):
    h = min(n, k)
    return bytes(range(1, h)) + bytes([h]) * (n - h + 1)


def ending_counts(text, k):
    full = (1 << k) - 1
    seen = [0] * ASCII_SIZE
    last = [0] * ASCII_SIZE
    ends = bytearray(len(text))
    palindromes = 0
    for i, c in enumerate(text):
        distance = i - last[c]
        # Bit d records a matching letter d positions before the current one.
        history = ((seen[c] & (full >> distance)) << distance) | 1
        seen[c] = history
        last[c] = i
        # Extending a palindrome adds two letters; lengths one and two are seeds.
        palindromes = ((palindromes << 2) | BASE_CASES) & history
        ends[i] = (POPCOUNT[palindromes & POPCOUNT_MASK]
                   + POPCOUNT[(palindromes >> POPCOUNT_WIDTH) & POPCOUNT_MASK]
                   + POPCOUNT[palindromes >> (2 * POPCOUNT_WIDTH)])
    return bytes(ends)


def native_ending_counts(text, k):
    full = (1 << k) - 1
    seen = [0] * ASCII_SIZE
    last = [0] * ASCII_SIZE
    ends = bytearray(len(text))
    palindromes = 0
    for i, c in enumerate(text):
        distance = i - last[c]
        # Bit d records a matching letter d positions before the current one.
        history = ((seen[c] & (full >> distance)) << distance) | 1
        seen[c] = history
        last[c] = i
        # Extending a palindrome adds two letters; lengths one and two are seeds.
        palindromes = ((palindromes << 2) | BASE_CASES) & history
        ends[i] = palindromes.bit_count()
    return bytes(ends)


if sys.implementation.name != 'pypy':
    ending_counts = native_ending_counts


BOUNDARY_FACTOR = 3
POSITION_BITS = 17
POSITION_MASK = (1 << POSITION_BITS) - 1


def compute_endpoints(text, k):
    n = len(text)
    c = text[:1]
    rest = text.lstrip(c)
    if not rest:
        ends = uniform_ends(n, k)
        return ends[::-1], ends
    if n <= BOUNDARY_FACTOR * k:
        a = n - len(rest)
        tail = rest.lstrip(rest[:1])
        if not tail:
            first = uniform_ends(a, k)
            last = uniform_ends(n - a, k)
            return first[::-1] + last[::-1], first + last
        b = n - len(tail)
        if tail.count(tail[0]) == len(tail):
            first = uniform_ends(a, k)
            middle = uniform_ends(b - a, k)
            last = uniform_ends(n - b, k)
            starts = first[::-1] + middle[::-1] + last[::-1]
            ends = first + middle + last
            if c[0] == tail[0]:
                radius = min(a, n - b, (k - b + a) // 2)
                if radius > 0:
                    starts = (starts[:a - radius]
                              + starts[a - radius:a].translate(INCREMENT) + starts[a:])
                    ends = (ends[:b] + ends[b:b + radius].translate(INCREMENT)
                            + ends[b + radius:])
            return starts, ends
    return ending_counts(text[::-1], k)[::-1], ending_counts(text, k)


endpoint_cache = {}
query_cache = {}


def cached_endpoints(text, k):
    result = endpoint_cache.get(text)
    if result is None:
        result = compute_endpoints(text, k)
        if len(endpoint_cache) >= CACHE_SIZE:
            endpoint_cache.clear()
        endpoint_cache[text] = result
    return result


def run_total(text):
    n = len(text)
    result = work = 0
    a = 0
    while a < n:
        b = a + 1
        while b < n and text[b] == text[a]:
            b += 1
        # A palindrome using different letters is centered at a whole run.
        length = b - a
        result += length * (length + 1) // 2
        d = 0
        while a > d and b + d < n and text[a - d - 1] == text[b + d]:
            d += 1
        result += d
        work += d
        if work > 2 * n:
            return sum(ending_counts(text, n))
        a = b
    return result


def query_total(text, k):
    result = query_cache.get(text)
    if result is None:
        n = len(text)
        if text.count(text[0]) == n:
            result = n * (n + 1) // 2
        else:
            result = run_total(text)
        if len(query_cache) >= QUERY_CACHE_SIZE:
            query_cache.clear()
        query_cache[text] = result
    return result


endpoints = compute_endpoints


class Solver:
    def __init__(self, text, k):
        self.n, self.k = len(text), k
        self.text = bytearray(text)
        self.starts, self.ends = map(bytearray, endpoints(text, k))
        blocks = (self.n + BLOCK - 1) // BLOCK
        self.mark = bytearray(blocks)
        self.size = size = 1 << (blocks - 1).bit_length()
        # Each field holds at most n*k; their sums cannot carry into each other.
        self.height = size.bit_length() - 1
        self.unit = k * BLOCK * ((1 << SUM_BITS) + 1)
        self.lazy = bytearray(2 * size)
        self.total = total = [0] * (2 * size)
        self.fill = bytes([k]) * BLOCK
        self.letters = [bytes([c]) * BLOCK for c in range(ASCII_SIZE)]
        for block in range(blocks):
            a, b = block * BLOCK, (block + 1) * BLOCK
            total[size + block] = sum(self.ends[a:b]) + (sum(self.starts[a:b]) << SUM_BITS)
        for v in range(size - 1, 0, -1):
            total[v] = total[v * 2] + total[v * 2 + 1]

    def push(self, v):
        if self.lazy[v]:
            self.total[v * 2] = self.total[v * 2 + 1] = self.total[v] // 2
            self.lazy[v * 2] = self.lazy[v * 2 + 1] = 1
            self.lazy[v] = 0

    def paint(self, first, last):
        left, right = self.size + first, self.size + last
        a, b = left, right - 1
        for shift in range(self.height, 0, -1):
            self.push(a >> shift)
            if a >> shift != b >> shift:
                self.push(b >> shift)
        width = 1
        total, lazy, unit = self.total, self.lazy, self.unit
        while left < right:
            if left & 1:
                total[left] = unit * width
                lazy[left] = 1
                left += 1
            if right & 1:
                right -= 1
                total[right] = unit * width
                lazy[right] = 1
            left //= 2
            right //= 2
            width *= 2
        a //= 2
        b //= 2
        while a:
            if not lazy[a]:
                total[a] = total[a * 2] + total[a * 2 + 1]
            if b != a and not lazy[b]:
                total[b] = total[b * 2] + total[b * 2 + 1]
            a //= 2
            b //= 2

    def materialize(self, block):
        c = self.mark[block]
        if c:
            # Resolve the sum path before this leaf becomes explicit.
            v, lo, hi = 1, 0, self.size
            while hi - lo > 1:
                self.push(v)
                mid = (lo + hi) // 2
                if block < mid:
                    v, hi = v * 2, mid
                else:
                    v, lo = v * 2 + 1, mid
            a, b = block * BLOCK, min(self.n, (block + 1) * BLOCK)
            length = b - a
            self.text[a:b] = self.letters[c][:length]
            self.starts[a:b] = self.ends[a:b] = self.fill[:length]
            self.mark[block] = 0

    def word(self, left, right):
        for block in range(left // BLOCK, (right - 1) // BLOCK + 1):
            self.materialize(block)
        return bytes(self.text[left:right])

    def refresh(self, first, last):
        total, size = self.total, self.size
        for block in range(first // BLOCK, (last - 1) // BLOCK + 1):
            a, b = block * BLOCK, (block + 1) * BLOCK
            value = sum(self.ends[a:b]) + (sum(self.starts[a:b]) << SUM_BITS)
            v = size + block
            change = value - total[v]
            if change:
                while v:
                    total[v] += change
                    v //= 2

    def assign(self, left, right, c):
        k, n = self.k, self.n
        first_block, last_block = left // BLOCK, (right - 1) // BLOCK
        if first_block == last_block:
            self.materialize(first_block)
            if self.text.count(c, left, right) == right - left:
                return
        lo, hi = (left + BLOCK - 1) // BLOCK, right // BLOCK
        if lo < hi:
            self.paint(lo, hi)
            self.mark[lo:hi] = bytes([c]) * (hi - lo)
        if left % BLOCK:
            self.materialize(first_block)
            end = min(right, (first_block + 1) * BLOCK)
            self.text[left:end] = self.letters[c][:end - left]
            self.starts[left:end] = self.ends[left:end] = self.fill[:end - left]
        if right % BLOCK and (not left % BLOCK or first_block != last_block):
            self.materialize(last_block)
            start = max(left, last_block * BLOCK)
            self.text[start:right] = self.letters[c][:right - start]
            self.starts[start:right] = self.ends[start:right] = self.fill[:right - start]
        first = max(0, left - k + 1)
        last = min(n, right + k - 1)
        if right - left >= 2 * (k - 1):
            end, start = left + k - 1, right - k + 1
            s, e = cached_endpoints(self.word(first, end), k)
            self.starts[first:left] = s[:left - first]
            self.ends[left:end] = e[left - first:]
            s, e = cached_endpoints(self.word(start, last), k)
            self.starts[start:right] = s[:right - start]
            self.ends[right:last] = e[right - start:]
            self.refresh(first, end)
            self.refresh(start, last)
        else:
            s, e = endpoints(self.word(first, last), k)
            self.starts[first:right] = s[:right - first]
            self.ends[left:last] = e[left - first:]
            self.refresh(first, last)

    def prefix(self, pos, starts):
        block = pos // BLOCK
        total, size = self.total, self.size
        if block == size:
            value = total[1]
            return value >> SUM_BITS if starts else value & SUM_MASK
        answer = 0
        v, a, b = 1, 0, size
        while b - a > 1:
            if self.lazy[v]:
                answer = answer >> SUM_BITS if starts else answer & SUM_MASK
                return answer + (pos - a * BLOCK) * self.k
            mid = (a + b) // 2
            if block < mid:
                v, b = v * 2, mid
            else:
                answer += total[v * 2]
                v, a = v * 2 + 1, mid
        answer = answer >> SUM_BITS if starts else answer & SUM_MASK
        if block < len(self.mark) and self.mark[block]:
            return answer + (pos - block * BLOCK) * self.k
        data = self.starts if starts else self.ends
        return answer + sum(data[block * BLOCK:pos])

    def query(self, left, right):
        if left == 0 and right == self.n:
            return self.total[1] & SUM_MASK
        # The endpoint prefixes cancel excluded palindromes for a long interval.
        if right - left >= self.k - 1:
            return self.prefix(right, False) - self.prefix(left, True)
        return query_total(self.word(left, right), self.k)


    def assign_batch(self, paints):
        k, n = self.k, self.n
        # Rebuild each affected neighborhood once, after all writes take effect.
        ending, starting = array('Q'), array('Q')
        for left, right, c in paints:
            word = self.word(left, right)
            letter = bytes([c])
            stripped = word.lstrip(letter)
            if not stripped:
                continue
            left += len(word) - len(stripped)
            right -= len(stripped) - len(stripped.rstrip(letter))
            self.text[left:right] = letter * (right - left)
            ending.append((left << POSITION_BITS) | min(n, right + k - 1))
            starting.append((max(0, left - k + 1) << POSITION_BITS) | right)
        dirty = set()
        for intervals, reverse in ((ending, False), (starting, True)):
            if not intervals:
                continue
            intervals = sorted(intervals)
            merged = []
            a, b = intervals[0] >> POSITION_BITS, intervals[0] & POSITION_MASK
            for interval in intervals[1:]:
                left, right = interval >> POSITION_BITS, interval & POSITION_MASK
                if left <= b + k - 1:
                    b = max(b, right)
                else:
                    merged.append((a, b))
                    a, b = left, right
            merged.append((a, b))
            for a, b in merged:
                if reverse:
                    end = min(n, b + k - 1)
                    counts = ending_counts(self.word(a, end)[::-1], k)[::-1]
                    self.starts[a:b] = counts[:b - a]
                else:
                    start = max(0, a - k + 1)
                    counts = ending_counts(self.word(start, b), k)
                    self.ends[a:b] = counts[a - start:]
                dirty.update(range(a // BLOCK, (b - 1) // BLOCK + 1))
        for block in sorted(dirty):
            self.refresh(block * BLOCK, min(n, (block + 1) * BLOCK))


def prepare(text, lines):
    index = 2
    if not lines[index].startswith(b'1 '):
        return text, index
    word = bytearray(text)
    n = len(word)
    marks = bytearray((n + BLOCK - 1) // BLOCK)
    while lines[index].startswith(b'1 '):
        fields = lines[index].split()
        left, right = int(fields[1]) - 1, int(fields[2])
        c = fields[LETTER_FIELD][0]
        lo, hi = (left + BLOCK - 1) // BLOCK, right // BLOCK
        if lo < hi:
            marks[lo:hi] = bytes([c]) * (hi - lo)
        first, last = left // BLOCK, (right - 1) // BLOCK
        if left % BLOCK:
            start, end = first * BLOCK, min(n, (first + 1) * BLOCK)
            if marks[first]:
                word[start:end] = bytes([marks[first]]) * (end - start)
                marks[first] = 0
            end = min(right, end)
            word[left:end] = bytes([c]) * (end - left)
        if right % BLOCK and (not left % BLOCK or first != last):
            start, end = last * BLOCK, min(n, (last + 1) * BLOCK)
            if marks[last]:
                word[start:end] = bytes([marks[last]]) * (end - start)
                marks[last] = 0
            start = max(left, start)
            word[start:right] = bytes([c]) * (right - start)
        index += 1
    for block, c in enumerate(marks):
        if c:
            start, end = block * BLOCK, min(n, (block + 1) * BLOCK)
            word[start:end] = bytes([c]) * (end - start)
    return bytes(word), index


BATCH_FILTER = 8
BATCH_MERGE = 16
SHORT_PAINT = 100
MERGE_MAX_WIDTH = 1000


def reduce_paints(paints):
    if len(paints) < BATCH_FILTER or max(b - a for a, b, c in paints) <= SHORT_PAINT:
        return paints
    starts, ends, retained = [], [], []
    # No remaining query observes intermediate writes within this batch.
    for left, right, c in reversed(paints):
        index = bisect_right(starts, left) - 1
        if index >= 0 and ends[index] >= right:
            continue
        retained.append((left, right, c))
        # Only long writes enter the union, bounding its number of disjoint parts.
        if right - left <= SHORT_PAINT:
            continue
        lo, hi = bisect_left(starts, left), bisect_right(starts, right)
        if lo > 0 and ends[lo - 1] >= left:
            lo -= 1
            left = starts[lo]
        if hi > lo:
            right = max(right, ends[hi - 1])
        starts[lo:hi] = [left]
        ends[lo:hi] = [right]
    retained.reverse()
    return retained


def main():
    lines = sys.stdin.buffer.read().splitlines()
    del lines[int(lines[1]) + 2:]
    while len(lines) > 2 and lines[-1].startswith(b'1 '):
        lines.pop()
    if len(lines) <= 2:
        return
    text, bound = lines[0].split()
    k = min(int(bound), len(text))
    answers, pending = [], []
    solver = None
    paint_left = paint_right = -1
    known_left = 0
    known_char = text[0] if text.count(text[0]) == len(text) else 0
    known_right = len(text) if known_char else 0
    for line in lines[2:]:
        fields = line.split()
        left, right = int(fields[1]) - 1, int(fields[2])
        if fields[0] == b'1':
            paint_left, paint_right = left, right
            c = fields[LETTER_FIELD][0]
            pending.append((left, right, c))
            if c == known_char and left <= known_right and right >= known_left:
                known_left, known_right = min(left, known_left), max(right, known_right)
            else:
                first = max(0, min(left, known_right) - known_left)
                last = max(0, known_right - max(right, known_left))
                if right - left >= max(first, last):
                    known_left, known_right, known_char = left, right, c
                elif first >= last:
                    known_right = known_left + first
                else:
                    known_left = known_right - last
        # This answer is known before any pending boundary counts are repaired.
        elif (k == 1 or paint_left <= left and right <= paint_right
              or known_left <= left and right <= known_right):
            height = min(k, right - left)
            answers.append(str(height * (right - left) - height * (height - 1) // 2))
        else:
            retained = reduce_paints(pending)
            if solver is None:
                if retained:
                    initial = [lines[0], lines[1]]
                    initial.extend(f'1 {a + 1} {b} {chr(c)}'.encode() for a, b, c in retained)
                    initial.append(line)
                    text, unused = prepare(text, initial)
                solver = Solver(text, k)
            else:
                if (len(retained) >= BATCH_MERGE
                        and max(b - a for a, b, c in retained) <= MERGE_MAX_WIDTH):
                    solver.assign_batch(retained)
                else:
                    for a, b, c in retained:
                        solver.assign(a, b, c)
            pending.clear()
            answers.append(str(solver.query(left, right)))
    if answers:
        sys.stdout.write('\n'.join(answers) + '\n')


if __name__ == '__main__':
    main()
