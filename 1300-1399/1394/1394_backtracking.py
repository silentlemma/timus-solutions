import random
import sys
import time

SLICE = 0.02  # seconds for the first round of every search
GROWTH = 1.6  # every round gives each search this much more time
ASSIGNMENT_TIME = 0.05  # seconds for the scaled problem of one residue assignment
FILL_CAP = 8000  # the most fillings of all rows but the longest for FillSearch
FILL_SHARE = 3  # FillSearch gets this many slices a round
FIRST_TRIES = 0.05  # seconds of random tries before any other search
FILL_SEED = 12345  # seeds of the random tries and of the shuffled row orders
SHUFFLE_SEED = 54321


class Timeout(Exception):
    pass


def subset_sums(lengths, counts, mask):
    """Bitset of the sums made of the given lengths, each at most its count."""
    reach = 1
    for length, count in zip(lengths, counts):
        # binary splitting of the count keeps the shifts few
        step = 1
        while count > 0:
            take = step if step < count else count
            reach |= reach << (length * take)
            count -= take
            step <<= 1
        reach &= mask
    return reach


def counts_add_up(by, total, gaps):
    """Every gap needs some number of ships, and the numbers must add up to total.

    by[c] is the bitset of the sums of exactly c of the remaining ships."""
    sums = 1
    for g in gaps:
        bit = 1 << g
        allowed = 0
        for c in range(1, len(by)):
            if by[c] & bit:
                allowed |= 1 << c
        if not allowed:
            return False
        nxt = 0
        while allowed:
            low = allowed & -allowed
            nxt |= sums << (low.bit_length() - 1)
            allowed ^= low
        sums = nxt
    return sums >> total & 1 == 1


class RowSearch:
    """Rows one at a time; a row takes a vector of counts of the distinct lengths."""

    def __init__(self, ships, rows, order, with_counts):
        self.lengths = sorted(set(ships), reverse=True)
        index = {x: i for i, x in enumerate(self.lengths)}
        self.counts = [0] * len(self.lengths)
        for s in ships:
            self.counts[index[s]] += 1
        self.rows = rows
        self.order = order[:-1]
        self.last = order[-1]  # the last row takes whatever is left
        self.mask = (1 << (max(rows) + 1)) - 1
        self.with_counts = with_counts
        self.failed = set()  # states proved hopeless, kept across slices

    def feasible(self, cnt, remaining):
        lengths, mask = self.lengths, self.mask
        reach = subset_sums(lengths, cnt, mask)
        for r in remaining:
            if not reach >> self.rows[r] & 1:
                return False
        if not self.with_counts:
            return True
        total = sum(cnt)
        by = [0] * (total + 1)
        by[0] = 1
        have = 0
        for i, length in enumerate(lengths):
            for _ in range(cnt[i]):
                have += 1
                for c in range(have, 0, -1):
                    by[c] |= (by[c - 1] << length) & mask
        return counts_add_up(by, total, [self.rows[r] for r in remaining])

    def run(self, deadline):
        self.deadline = deadline
        self.steps = 0
        self.chosen = [None] * len(self.rows)
        if not self.fill(0, list(self.counts)):
            return None
        out = []
        for use in self.chosen:
            group = []
            for i, t in enumerate(use):
                group += [self.lengths[i]] * t
            out.append(group)
        return out

    def fill(self, pos, cnt):
        if pos == len(self.order):
            self.chosen[self.last] = tuple(cnt)
            return True
        key = (tuple(cnt), pos)
        if key in self.failed:
            return False
        lengths, mask = self.lengths, self.mask
        k = len(lengths)
        r = self.order[pos]
        target = self.rows[r]
        # suffix[i]: the sums made of the lengths i.. that are left
        suffix = [0] * (k + 1)
        suffix[k] = 1
        for i in range(k - 1, -1, -1):
            reach = suffix[i + 1]
            length, c = lengths[i], cnt[i]
            step = 1
            while c > 0:
                take = step if step < c else c
                reach |= reach << (length * take)
                c -= take
                step <<= 1
            suffix[i] = reach & mask
        if not suffix[0] >> target & 1:
            self.failed.add(key)
            return False
        use = [0] * k
        rest_rows = self.order[pos + 1:] + [self.last]

        def pick(i, left):
            self.steps += 1
            if self.steps & 255 == 0 and time.time() > self.deadline:
                raise Timeout
            if left == 0:
                rest = [cnt[j] - use[j] for j in range(k)]
                if self.feasible(rest, rest_rows):
                    self.chosen[r] = tuple(use)
                    if self.fill(pos + 1, rest):
                        return True
                return False
            if i == k:
                return False
            length = lengths[i]
            for t in range(min(cnt[i], left // length), -1, -1):
                rem = left - t * length
                if suffix[i + 1] >> rem & 1:
                    use[i] = t
                    if pick(i + 1, rem):
                        return True
            use[i] = 0
            return False

        if pick(0, target):
            return True
        self.failed.add(key)
        return False


class ShipSearch:
    """Ships one at a time into rows, the rarest lengths first."""

    def __init__(self, ships, rows):
        count = {}
        for s in ships:
            count[s] = count.get(s, 0) + 1
        self.order = order = sorted(ships, key=lambda s: (count[s], -s))
        self.rows = rows
        n = len(order)
        mask = (1 << (max(rows) + 1)) - 1
        # reach[i]: the sums of subsets of order[i:]
        self.reach = reach = [0] * (n + 1)
        reach[n] = 1
        for i in range(n - 1, -1, -1):
            reach[i] = (reach[i + 1] | (reach[i + 1] << order[i])) & mask
        # exact[i][c]: the sums of exactly c ships of order[i:]
        self.exact = exact = [None] * (n + 1)
        exact[n] = [1]
        for i in range(n - 1, -1, -1):
            nxt = exact[i + 1]
            cur = [0] * (n - i + 1)
            cur[0] = 1
            s = order[i]
            for c in range(1, n - i + 1):
                v = nxt[c] if c < len(nxt) else 0
                cur[c] = (v | (nxt[c - 1] << s)) & mask
            exact[i] = cur
        self.failed = set()

    def run(self, deadline):
        self.deadline = deadline
        self.steps = 0
        n, m = len(self.order), len(self.rows)
        self.rem = list(self.rows)
        self.where = [0] * n
        if not self.place(0, 0):
            return None
        out = [[] for _ in range(m)]
        for i in range(n):
            out[self.where[i]].append(self.order[i])
        return out

    def place(self, i, low_row):
        order, rem = self.order, self.rem
        n, m = len(order), len(rem)
        if i == n:
            return True
        self.steps += 1
        if self.steps & 255 == 0 and time.time() > self.deadline:
            raise Timeout
        key = (i, tuple(sorted(rem)))
        if key in self.failed:
            return False
        s = order[i]
        after = self.reach[i + 1]
        forced = -1
        for r in range(m):
            g = rem[r]
            if g and not after >> g & 1:
                # this row cannot be completed without the current ship
                if forced >= 0 or g < s:
                    self.failed.add(key)
                    return False
                forced = r
        # equal ships go to rows in order, and rows with equal gaps are tried once
        start = low_row if i > 0 and order[i - 1] == s else 0
        tried = set()
        for r in ([forced] if forced >= 0 else range(start, m)):
            g = rem[r]
            if r < start or g < s or g in tried:
                continue
            tried.add(g)
            if not after >> (g - s) & 1:
                continue
            rem[r] = g - s
            self.where[i] = r
            gaps = [x for x in rem if x]
            if counts_add_up(self.exact[i + 1], n - i - 1, gaps) and self.place(i + 1, r):
                return True
            rem[r] = g
        self.failed.add(key)
        return False


class RandomFill:
    """Random tries: the ships in a random order, the rows in a random order
    with the longest last; a row takes every ship that still lets it be
    completed by the later ones, and the longest row takes the rest."""

    def __init__(self, ships, rows):
        self.ships, self.rows = ships, rows
        self.rng = random.Random(FILL_SEED)
        m = len(rows)
        self.last = max(range(m), key=lambda r: rows[r])
        self.others = [r for r in range(m) if r != self.last]

    def run(self, deadline):
        rng, rows = self.rng, self.rows
        tries = 0
        while True:
            tries += 1
            if tries & 15 == 0 and time.time() > deadline:
                raise Timeout
            left = list(self.ships)
            rng.shuffle(left)
            order = list(self.others)
            rng.shuffle(order)
            out = [None] * len(rows)
            for r in order:
                target = rows[r]
                mask = (1 << (target + 1)) - 1
                n = len(left)
                suffix = [0] * (n + 1)
                reach = suffix[n] = 1
                for i in range(n - 1, -1, -1):
                    reach = (reach | reach << left[i]) & mask
                    suffix[i] = reach
                if not reach >> target & 1:
                    break
                need = target
                group, rest = [], []
                for i in range(n):
                    s = left[i]
                    if s <= need and suffix[i + 1] >> (need - s) & 1:
                        group.append(s)
                        need -= s
                    else:
                        rest.append(s)
                out[r] = group
                left = rest
            else:
                out[self.last] = left
                return out


class FillSearch:
    """Every row but the longest takes one of its fillings (a count for every
    distinct length), the row with the fewest fillings that still fit first;
    the longest row takes the rest. Only for fleets with few fillings."""

    def __init__(self, ships, rows):
        self.lengths = sorted(set(ships), reverse=True)
        index = {x: i for i, x in enumerate(self.lengths)}
        self.counts = [0] * len(self.lengths)
        for s in ships:
            self.counts[index[s]] += 1
        self.rows = rows
        m = len(rows)
        self.last = max(range(m), key=lambda r: rows[r])
        self.others = [r for r in range(m) if r != self.last]
        self.fills = {}
        total = 0
        for r in self.others:
            got = self.fillings(rows[r], FILL_CAP - total)
            if got is None:
                self.fills = None
                return
            # fillings with fewer ships first
            got.sort(key=sum)
            self.fills[r] = got
            total += len(got)
        # over[r][i][t]: the fillings of row r with more than t ships of length i
        self.over = {}
        for r in self.others:
            table = []
            for i in range(len(self.lengths)):
                # the bits as a string, the last filling first
                column = [f[i] for f in reversed(self.fills[r])]
                top = max(column)
                masks = [int("".join("1" if c > t else "0" for c in column), 2)
                         for t in range(top)]
                table.append(masks + [0] * (self.counts[i] + 1 - top))
            self.over[r] = table
        # failures do not depend on the order of the fillings
        self.failed = set()

    def fillings(self, target, cap):
        lengths, counts = self.lengths, self.counts
        k = len(lengths)
        mask = (1 << (target + 1)) - 1
        suffix = [0] * (k + 1)
        suffix[k] = 1
        for i in range(k - 1, -1, -1):
            reach = suffix[i + 1]
            step = 1
            c = counts[i]
            while c > 0:
                take = step if step < c else c
                reach |= reach << (lengths[i] * take)
                c -= take
                step <<= 1
            suffix[i] = reach & mask
        out = []
        use = [0] * k

        def go(i, left):
            if left == 0:
                out.append(tuple(use))
                return len(out) <= cap
            if i == k:
                return True
            for t in range(min(counts[i], left // lengths[i]), -1, -1):
                rem = left - t * lengths[i]
                if suffix[i + 1] >> rem & 1:
                    use[i] = t
                    if not go(i + 1, rem):
                        return False
            use[i] = 0
            return True

        return out if go(0, target) else None

    def run(self, deadline):
        self.deadline = deadline
        self.steps = 0
        self.chosen = {}
        rem = list(self.counts)
        doms = {}
        for r in self.others:
            dom = (1 << len(self.fills[r])) - 1
            for i in range(len(rem)):
                dom &= ~self.over[r][i][rem[i]]
            doms[r] = dom
        if not self.place(rem, doms):
            return None
        out = [None] * len(self.rows)
        left = list(self.counts)
        for r in self.others:
            group = []
            for i, t in enumerate(self.fills[r][self.chosen[r]]):
                group += [self.lengths[i]] * t
                left[i] -= t
            out[r] = group
        out[self.last] = [x for i, x in enumerate(self.lengths) for _ in range(left[i])]
        return out

    def place(self, rem, doms):
        if not doms:
            return True
        self.steps += 1
        if self.steps & 63 == 0 and time.time() > self.deadline:
            raise Timeout
        key = (tuple(rem), tuple(sorted(doms)))
        if key in self.failed:
            return False
        best, size = -1, 1 << 30
        for r, dom in doms.items():
            c = dom.bit_count()
            if c < size:
                best, size = r, c
        dom = doms[best]
        fills = self.fills[best]
        while dom:
            low = dom & -dom
            j = low.bit_length() - 1
            dom ^= low
            f = fills[j]
            used = [i for i in range(len(f)) if f[i]]
            for i in used:
                rem[i] -= f[i]
            # every other row keeps only the fillings that still fit
            new = {}
            for r, d in doms.items():
                if r == best:
                    continue
                over = self.over[r]
                for i in used:
                    d &= ~over[i][rem[i]]
                if not d:
                    break
                new[r] = d
            else:
                self.chosen[best] = j
                if self.place(rem, new):
                    return True
            for i in used:
                rem[i] += f[i]
        self.failed.add(key)
        return False


class ResidueSearch:
    """Most ships are multiples of k: the others go first, so that every row's
    remaining length becomes a multiple of k, and the multiples then fill the
    rows as a problem scaled down by k."""

    def __init__(self, ships, rows, k):
        self.k = k
        self.rows = rows
        self.odd = sorted((s for s in ships if s % k), reverse=True)
        self.even = [s // k for s in ships if s % k == 0]
        self.total_even = sum(self.even)
        self.assignments = self.spread()
        self.sub = None

    def spread(self):
        """Every way to give the non-multiples to rows with all residues right.

        Rows take multisets of the non-multiples one row at a time, the
        smallest multisets first, so that one special ship per row comes
        out early."""
        k, rows = self.k, self.rows
        m = len(rows)
        values = sorted(set(self.odd), reverse=True)
        left = [self.odd.count(v) for v in values]
        d = len(values)
        # the multiples of k can make these sums (in units of k)
        even_reach = subset_sums(*self.grouped(self.even), (1 << (max(rows) // k + 1)) - 1)
        full = (1 << k) - 1
        # rows that need a non-multiple first, the shortest first
        order = sorted(range(m), key=lambda r: (rows[r] % k == 0, rows[r]))
        need_rows = [0] * (m + 1)
        for p in range(m - 1, -1, -1):
            need_rows[p] = need_rows[p + 1] + (rows[order[p]] % k != 0)
        use = [[0] * d for _ in range(m)]

        def residues(cnt):
            reach = 1
            for v, c in zip(values, cnt):
                r = v % k
                for _ in range(min(c, k)):
                    reach |= ((reach << r) | (reach >> (k - r))) & full
            return reach

        def fits(g, total):
            return total <= g and (g - total) % k == 0 and even_reach >> ((g - total) // k) & 1

        def pick(i, size, total, cur):
            # multisets of exactly size ships from values[i:], sum so far total
            if size == 0:
                yield total
                return
            if i == d:
                return
            v = values[i]
            for t in range(min(left[i], size), -1, -1):
                if total + t * v > g_now[0]:
                    continue
                cur[i] = t
                yield from pick(i + 1, size - t, total + t * v, cur)
            cur[i] = 0

        g_now = [0]

        def go(p, ships_left):
            r = order[p]
            g = rows[r]
            cur = use[r]
            if p == m - 1:
                # the last row takes every remaining non-multiple
                total = sum(v * c for v, c in zip(values, left))
                if fits(g, total):
                    cur[:] = left
                    yield self.unpack(values, use)
                return
            for size in range(0, ships_left - need_rows[p + 1] + 1):
                g_now[0] = g
                for total in pick(0, size, 0, cur):
                    if not fits(g, total):
                        continue
                    for i in range(d):
                        left[i] -= cur[i]
                    rest = residues(left)
                    if all(rest >> (rows[order[q]] % k) & 1 for q in range(p + 1, m)):
                        saved = list(cur)
                        yield from go(p + 1, ships_left - size)
                        cur[:] = saved
                    for i in range(d):
                        left[i] += cur[i]
                    g_now[0] = g
            for i in range(d):
                cur[i] = 0

        return go(0, len(self.odd))

    @staticmethod
    def grouped(ships):
        lengths = sorted(set(ships))
        return lengths, [ships.count(x) for x in lengths]

    def unpack(self, values, use):
        """The row of every non-multiple, in the order of self.odd."""
        slots = {}
        for r, cnt in enumerate(use):
            for v, c in zip(values, cnt):
                slots.setdefault(v, []).extend([r] * c)
        return [slots[s].pop() for s in self.odd]

    def run(self, deadline):
        while True:
            if self.sub is None:
                where = next(self.assignments, None)
                if where is None:
                    return None
                gaps = list(self.rows)
                for s, r in zip(self.odd, where):
                    gaps[r] -= s
                # rows filled by their non-multiples alone take no other ship
                keep = [r for r in range(len(gaps)) if gaps[r]]
                if not keep:
                    if not self.even:
                        self.where = where
                        return self.merge(keep, [])
                    continue
                part = [gaps[r] // self.k for r in keep]
                order = sorted(range(len(part)), key=lambda r: part[r])
                self.sub = (where, keep, [RandomFill(self.even, part),
                                          RowSearch(self.even, part, order, False)])
                self.spent = 0.0
            where, keep, searches = self.sub
            for search in searches:
                begin = time.time()
                try:
                    got = search.run(min(deadline, begin + SLICE))
                except Timeout:
                    self.spent += time.time() - begin
                    continue
                if got is not None:
                    self.where = where
                    return self.merge(keep, got)
                # the scaled problem has no solution: try the next assignment
                self.spent = float("inf")
                break
            if self.spent > ASSIGNMENT_TIME:
                self.sub = None
            if time.time() > deadline:
                raise Timeout

    def merge(self, keep, sub):
        out = [[] for _ in self.rows]
        for r, group in zip(keep, sub):
            out[r] = [s * self.k for s in group]
        for s, r in zip(self.odd, self.where):
            out[r].append(s)
        return out


def residue_moduli(ships, rows):
    """Moduli that divide most ships, the best first."""
    found = []
    n, m = len(ships), len(rows)
    for k in range(2, 51):
        rest = sum(1 for s in ships if s % k)
        if 0 < rest <= max(2 * m, n // 3) and rest < n:
            found.append(((n - rest) * k, k))
    found.sort(reverse=True)
    return [k for _, k in found[:2]]


def solve(ships, rows):
    m = len(rows)
    ascending = sorted(range(m), key=lambda r: rows[r])
    rng = random.Random(SHUFFLE_SEED)
    # random tries alone settle most fleets before the other searches are even built
    first = RandomFill(ships, rows)
    try:
        return first.run(time.time() + FIRST_TRIES)
    except Timeout:
        pass
    searches = [first,
                RowSearch(ships, rows, ascending, False),
                RowSearch(ships, rows, ascending[-2::-1] + ascending[-1:], True),
                ShipSearch(ships, rows)]
    searches += [ResidueSearch(ships, rows, k) for k in residue_moduli(ships, rows)]
    fill = FillSearch(ships, rows)
    if fill.fills is not None:
        searches.insert(0, fill)
    budget = SLICE
    while True:
        for search in searches:
            share = FILL_SHARE if search is fill else 1
            try:
                plan = search.run(time.time() + budget * share)
            except Timeout:
                continue
            if plan is not None:
                return plan
        # a shuffled row order joins every round; the longest row still comes last
        shuffled = ascending[:-1]
        rng.shuffle(shuffled)
        searches.append(RowSearch(ships, rows, shuffled + ascending[-1:], False))
        budget *= GROWTH


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    ships = [int(x) for x in data[2:2 + n]]
    rows = [int(x) for x in data[2 + n:2 + n + m]]
    lines = []
    for group in solve(ships, rows):
        lines.append(str(len(group)))
        lines.append(" ".join(map(str, group)))
    sys.stdout.write("\n".join(lines) + "\n")


main()
