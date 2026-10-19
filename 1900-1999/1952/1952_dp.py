from array import array
from fractions import Fraction
from functools import lru_cache
import math
import sys
from collections import namedtuple

STORM = "Storm"
BREATH = "Breath"
TAIL = "Tail"
AURA_FIELDS = 3
ERROR_MARGIN = 4
ROOT_CACHE_SIZE = 4096
SIGN_CACHE_SIZE = 2048
INITIAL_ROOT_DIGITS = 16
BOUND_ROOT_DIGITS = 32
MISSING_PARENT = 255


Spell = namedtuple("Spell", "kind power duration places")


@lru_cache(maxsize=ROOT_CACHE_SIZE)
def split_square(value):
    outside = inside = 1
    divisor = 2
    while divisor * divisor <= value:
        count = 0
        while value % divisor == 0:
            value //= divisor
            count += 1
        outside *= divisor ** (count // 2)
        if count & 1:
            inside *= divisor
        divisor += 1
    return outside, inside * value


@lru_cache(maxsize=ROOT_CACHE_SIZE)
def root_bounds(radicand, digits):
    denominator = 10**digits
    lower = math.isqrt(radicand * denominator * denominator)
    return Fraction(lower, denominator), Fraction(lower + 1, denominator)


@lru_cache(maxsize=SIGN_CACHE_SIZE)
def exact_sign(terms):
    if not terms:
        return 0
    if len(terms) == 1 and terms[0][0] == 1:
        return (terms[0][1] > 0) - (terms[0][1] < 0)
    digits = INITIAL_ROOT_DIGITS
    while True:
        lower = upper = Fraction(0)
        for radicand, coefficient in terms:
            if radicand == 1:
                lower += coefficient
                upper += coefficient
                continue
            left, right = root_bounds(radicand, digits)
            if coefficient < 0:
                left, right = right, left
            lower += coefficient * left
            upper += coefficient * right
        if lower > 0:
            return 1
        if upper < 0:
            return -1
        digits *= 2


class Surd:
    __slots__ = ("terms",)

    def __init__(self, value=0):
        if isinstance(value, Surd):
            self.terms = value.terms
        else:
            value = Fraction(value)
            self.terms = ((1, value),) if value else ()

    @classmethod
    def from_terms(cls, coefficients):
        result = cls.__new__(cls)
        result.terms = tuple(
            sorted((key, value) for key, value in coefficients.items() if value)
        )
        return result

    def __add__(self, other):
        other = Surd(other)
        result = dict(self.terms)
        for key, value in other.terms:
            result[key] = result.get(key, 0) + value
        return self.from_terms(result)

    __radd__ = __add__

    def __neg__(self):
        return self.from_terms({key: -value for key, value in self.terms})

    def __sub__(self, other):
        return self + -Surd(other)

    def __rsub__(self, other):
        return Surd(other) + -self

    def __mul__(self, other):
        other = Surd(other)
        result = {}
        for first, a in self.terms:
            for second, b in other.terms:
                common = math.gcd(first, second)
                key = (first // common) * (second // common)
                result[key] = result.get(key, 0) + a * b * common
        return self.from_terms(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1 / Fraction(other))

    def __eq__(self, other):
        return self.terms == Surd(other).terms

    def __lt__(self, other):
        return exact_sign((self - other).terms) < 0

    def __le__(self, other):
        return exact_sign((self - other).terms) <= 0

    def __gt__(self, other):
        return exact_sign((self - other).terms) > 0

    def __ge__(self, other):
        return exact_sign((self - other).terms) >= 0

    def float_bounds(self):
        lower = upper = Fraction(0)
        for key, coefficient in self.terms:
            if key == 1:
                lower += coefficient
                upper += coefficient
                continue
            left, right = root_bounds(key, BOUND_ROOT_DIGITS)
            if coefficient < 0:
                left, right = right, left
            lower += coefficient * left
            upper += coefficient * right
        low, high = float(lower), float(upper)
        if Fraction.from_float(low) > lower:
            low = math.nextafter(low, -math.inf)
        if Fraction.from_float(high) < upper:
            high = math.nextafter(high, math.inf)
        return low, high


def root(value):
    if not value:
        return Surd(0)
    outside, inside = split_square(value)
    return Surd.from_terms({inside: Fraction(outside)})


NEGATIVE = -math.inf
POSITIVE = math.inf


def add(first, second):
    return math.nextafter(first[0] + second[0], NEGATIVE), math.nextafter(
        first[1] + second[1], POSITIVE
    )


def subtract(first, second):
    return math.nextafter(first[0] - second[1], NEGATIVE), math.nextafter(
        first[1] - second[0], POSITIVE
    )


def times(first, second):
    return (math.nextafter(first[0] * second[0], NEGATIVE),
            math.nextafter(first[1] * second[1], POSITIVE))


def divide(first, denominator):
    assert denominator > 0
    return math.nextafter(first[0] / denominator, NEGATIVE), math.nextafter(
        first[1] / denominator, POSITIVE
    )


def minimum(first, second):
    return min(first[0], second[0]), min(first[1], second[1])


def maximum(first, second):
    return max(first[0], second[0]), max(first[1], second[1])


def nonnegative(value):
    return maximum((0.0, 0.0), value)


def travel_bounds(first, second, speed):
    squared = (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
    if not squared:
        return 0.0, 0.0
    approximate = math.sqrt(squared) / speed
    lower = math.nextafter(approximate, NEGATIVE)
    upper = math.nextafter(approximate, POSITIVE)
    while Fraction.from_float(lower) ** 2 * speed * speed > squared:
        lower = math.nextafter(lower, NEGATIVE)
    while Fraction.from_float(upper) ** 2 * speed * speed < squared:
        upper = math.nextafter(upper, POSITIVE)
    return lower, upper


def aura_deficit(start, cap, rise, fall, travel, duration):
    cap_interval = float(cap), float(cap)
    falling = nonnegative(minimum(travel, divide(start, fall)))
    after = nonnegative(subtract(start, times((float(fall), float(fall)), travel)))
    casting = nonnegative(subtract(duration, travel))
    rising = nonnegative(
        minimum(casting, divide(nonnegative(subtract(cap_interval, after)), rise))
    )
    final = minimum(
        cap_interval, add(after, times((float(rise), float(rise)), casting))
    )
    run = divide(
        times(
            add(
                nonnegative(subtract(cap_interval, start)),
                nonnegative(subtract(cap_interval, after)),
            ),
            falling,
        ),
        2,
    )
    run = add(run, times(cap_interval, nonnegative(subtract(travel, falling))))
    cast = divide(
        times(
            add(
                nonnegative(subtract(cap_interval, after)),
                nonnegative(subtract(cap_interval, final)),
            ),
            rising,
        ),
        2,
    )
    return final, nonnegative(add(run, cast))


def restricted_optimum(weights):
    size = len(weights)
    limit = 1 << size
    count = limit * limit
    lower = array("d", [math.inf]) * count
    upper = array("d", [math.inf]) * count
    parent = bytearray([MISSING_PARENT]) * count
    lower[0] = upper[0] = 0.0
    bounds = [[[v.float_bounds() for v in row] for row in w] for w in weights]
    masks, available = layout(size)

    def path(index):
        result = []
        while index:
            a, b = divmod(parent[index], size)
            result.append((a, b))
            left, right = divmod(index, limit)
            index = (left ^ (1 << a)) * limit + (right ^ (1 << b))
        return tuple(reversed(result))

    for person in range(size):
        paths = {}
        for left in masks[person]:
            for right in masks[person]:
                index = left * limit + right
                if math.isinf(lower[index]):
                    continue
                for next_left, a in available[left]:
                    for next_right, b in available[right]:
                        target = next_left * limit + next_right
                        lo, hi = bounds[person][a][b]
                        lo = math.nextafter(lower[index] + lo, -math.inf)
                        hi = math.nextafter(upper[index] + hi, math.inf)
                        choose = math.isinf(lower[target]) or hi < lower[target]
                        if not choose and lo < upper[target]:
                            if index not in paths:
                                paths[index] = path(index)
                            candidate = paths[index] + ((a, b),)
                            difference = Surd(0)
                            for actor, (new, old) in enumerate(zip(candidate, path(target))):
                                if new != old:
                                    difference += (weights[actor][new[0]][new[1]]
                                                   - weights[actor][old[0]][old[1]])
                            choose = exact_sign(difference.terms) < 0
                        if choose:
                            lower[target], upper[target] = lo, hi
                            parent[target] = a * size + b
    return sum(weights[i][a][b] for i, (a, b) in enumerate(path(count - 1)))


def matching(cost, bound=False):
    people, places = len(cost), len(cost[0])
    u, v = [0] * (people + 1), [0] * (places + 1)
    owner, parent = [0] * (places + 1), [0] * (places + 1)
    for person in range(1, people + 1):
        owner[0] = person
        best, used = [None] * (places + 1), [False] * (places + 1)
        place = 0
        while True:
            used[place] = True
            actor = owner[place]
            delta, target = None, 0
            for other in range(1, places + 1):
                if used[other]:
                    continue
                value = cost[actor - 1][other - 1] - u[actor] - v[other]
                if best[other] is None or value < best[other]:
                    best[other], parent[other] = value, place
                if delta is None or best[other] < delta:
                    delta, target = best[other], other
            for other in range(places + 1):
                if used[other]:
                    u[owner[other]] += delta
                    v[other] -= delta
                else:
                    best[other] -= delta
            place = target
            if not owner[place]:
                break
        while place:
            previous = parent[place]
            owner[place] = owner[previous]
            place = previous
    assignment = [0] * people
    for place in range(1, places + 1):
        if owner[place]:
            assignment[owner[place] - 1] = place - 1
    value = sum(row[j] for row, j in zip(cost, assignment))
    if bound:
        value = 0.0
        for row in cost:
            term = min(math.nextafter(c - min(0.0, v[j + 1]), -math.inf)
                       for j, c in enumerate(row))
            value = math.nextafter(value + term, -math.inf)
        for term in v[1:]:
            value = math.nextafter(value + min(0.0, term), -math.inf)
    return value, assignment


def relaxation(weights, pairs, first=None, second=None):
    size = len(weights[0])
    first = list(range(size)) if first is None else first
    second = list(range(size)) if second is None else second
    projected = [[min(tensor[a][b] for b in second) if pairs else tensor[a][0]
                  for a in first] for tensor in weights]
    lower, order = matching(projected, bound=True)
    left = [first[a] for a in order]
    right = [0] * len(weights)
    if pairs:
        other = [[min(tensor[a][b] for a in first) for b in second]
                 for tensor in weights]
        lower = max(lower, matching(other, bound=True)[0])
        for _ in range(size):
            matrix = [[tensor[a][b] for b in second]
                      for tensor, a in zip(weights, left)]
            value, order = matching(matrix)
            right = [second[b] for b in order]
            matrix = [[tensor[a][b] for a in first]
                      for tensor, b in zip(weights, right)]
            improved, order = matching(matrix)
            if improved >= value:
                break
            left = [first[a] for a in order]
    upper = sum(tensor[a][b] for tensor, a, b in zip(weights, left, right))
    return lower, upper, left, right


@lru_cache(maxsize=None)
def layout(size):
    limit = 1 << size
    masks = [[] for _ in range(size + 1)]
    options = []
    for mask in range(limit):
        masks[mask.bit_count()].append(mask)
        options.append([(mask | (1 << j), j) for j in range(size) if not mask >> j & 1])
    return masks, options


def role_dp(weights, size, pairs, cutoff=math.inf):
    limit = 1 << size
    masks, options = layout(size)
    values = array('d', [math.inf]) * (limit * limit if pairs else limit)
    values[0] = 0.0
    suffix = [0.0] * (len(weights) + 1)
    for person in range(len(weights) - 1, -1, -1):
        suffix[person] = suffix[person + 1] + min(map(min, weights[person]))
    projections = []
    if not math.isinf(cutoff):
        for transpose in range(2 if pairs else 1):
            bound = [0.0] * limit
            for person in range(len(weights) - 1, -1, -1):
                tensor = weights[person]
                row = [min(tensor[a][b] for a in range(size)) for b in range(size)] if (
                    transpose) else [min(row) for row in tensor]
                for mask in masks[person]:
                    bound[mask] = min(row[j] + bound[target] for target, j in options[mask])
            projections.append(bound)
    # One-layer completion DPs discard unaffordable two-layer states.
    for person, tensor in enumerate(weights):
        ceiling = cutoff - suffix[person + 1]
        for left in masks[person]:
            base = left * limit
            for right in masks[person] if pairs else (0,):
                current = values[base + right if pairs else left]
                if current >= ceiling:
                    continue
                if projections and current + max(
                        projections[0][left], projections[-1][right if pairs else left]
                ) >= cutoff:
                    continue
                for target_left, a in options[left]:
                    row = tensor[a]
                    target_base = target_left * limit
                    for target_right, b in options[right] if pairs else ((0, 0),):
                        value = current + row[b]
                        target = target_base + target_right if pairs else target_left
                        if value < ceiling and value < values[target]:
                            values[target] = value
    return values


def exact_optimum(weights, pairs):
    if not pairs:
        return matching([[row[0] for row in tensor] for tensor in weights])[0]
    if all(tensor == weights[0] for tensor in weights):
        return matching(weights[0])[0]
    symbolic = [[[Surd(value) for value in row] for row in tensor] for tensor in weights]
    return restricted_optimum(symbolic)


def exact_distance(first, second, speed):
    squared = (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
    length = math.isqrt(squared)
    return Fraction(length, speed) if length * length == squared else root(squared) / speed


def exact_deficit(start, cap, rise, fall, travel, duration):
    after = max(Fraction(0), start - fall * travel)
    final = min(Fraction(cap), after + rise * (duration - travel))
    running = (start * start - after * after) / (2 * fall)
    before, after_cast = cap - after, cap - final
    missing = (before * before - after_cast * after_cast) / (2 * rise)
    return final, cap * travel - running + missing


class Block:
    def __init__(self, attackers, healers, health, speed, start, breaths, storm, initial):
        self.args = attackers, healers, health, speed, start, breaths, storm, initial
        self.breaths = breaths
        self.pairs = len(breaths) == 2
        self.size = len(attackers) + len(healers)
        self.total = sum(aura[0] for aura in attackers) * sum(
            spell.duration for spell in breaths + [storm])
        self.exact_data = None
        self.best_exact = None
        self.candidates = None
        self.witness = None
        self.hweights, self.aweights, self.budget, self.herror, self.aerror = self.build(False)
        self.bounds = None

    def build(self, exact):
        attackers, healers, health, speed, start, breaths, storm, initial = self.args
        travel = exact_distance if exact else travel_bounds
        first = breaths[0] if breaths else storm
        outgoing = [travel(start, place, speed) for place in first.places]
        returning = [travel(place, storm.places[0], speed)
                     for place in breaths[-1].places] if breaths else []
        between = [[travel(a, b, speed) for b in breaths[1].places]
                   for a in first.places] if self.pairs else []
        latest = max(returning if breaths else outgoing)
        if not exact:
            latest = max(t[0] for t in returning or outgoing), max(
                t[1] for t in returning or outgoing)
        cap_sum = sum(aura[0] for aura in healers)
        fixed = sum((spell.power - cap_sum) * spell.duration for spell in breaths)
        gap = storm.power - cap_sum
        budget = health - fixed - gap * latest if exact else subtract(
            (float(health - fixed),) * 2, times((float(gap),) * 2, latest))
        groups, errors = [], []
        cache = {}
        for healing, auras in ((True, healers), (False, attackers)):
            weights, error, magnitude = [], 0.0, 0.0
            for cap, rise, fall in auras:
                scale = math.gcd(cap, math.gcd(rise, fall)) if exact else 1
                cap, rise, fall = cap // scale, rise // scale, fall // scale
                key = healing, cap, rise, fall
                if key in cache:
                    tensor, uncertainty, largest = cache[key]
                else:
                    tensor, uncertainty, largest = [], 0.0, 0.0
                    power = cap if healing or not initial else 0
                    power = Fraction(power) if exact else (float(power),) * 2
                    metric = exact_deficit if exact else aura_deficit
                    for a, run in enumerate(outgoing):
                        duration = latest if healing and not breaths else first.duration
                        duration = duration if exact or isinstance(duration, tuple) else (
                            float(duration),) * 2
                        state, value = metric(power, cap, rise, fall, run, duration)
                        row = []
                        for b in range(len(returning)) if self.pairs else (a,):
                            end, cost = state, value
                            if self.pairs:
                                duration = breaths[1].duration
                                duration = duration if exact else (float(duration),) * 2
                                end, middle = metric(end, cap, rise, fall,
                                                     between[a][b], duration)
                                cost = cost + middle if exact else add(cost, middle)
                            if breaths:
                                duration = latest if healing else storm.duration
                                duration = duration if exact or isinstance(duration, tuple) else (
                                    float(duration),) * 2
                                _, final = metric(end, cap, rise, fall, returning[b], duration)
                                cost = cost + final if exact else add(cost, final)
                            if exact:
                                row.append(cost)
                            else:
                                center = (cost[0] + cost[1]) / 2
                                uncertainty = max(uncertainty, center - cost[0], cost[1] - center)
                                largest = max(largest, abs(center))
                                row.append(center)
                        tensor.append(row)
                    cache[key] = tensor, uncertainty, largest
                weights.append([[v * scale for v in row] for row in tensor]
                               if scale != 1 else tensor)
                error = math.nextafter(error + uncertainty, math.inf)
                magnitude += largest
            groups.append(weights)
            errors.append(math.nextafter(error + 2 * len(auras) * math.ulp(magnitude), math.inf))
        if exact:
            return groups[0], groups[1], budget
        approximate = (budget[0] + budget[1]) / 2
        errors[0] += max(approximate - budget[0], budget[1] - approximate)
        return groups[0], groups[1], approximate, errors[0], errors[1]

    def data(self):
        if self.exact_data is None:
            self.exact_data = self.build(True)
        return self.exact_data

    def feasible(self, left, right):
        weights, _, budget = self.data()
        if not self.breaths:
            return sum(tensor[0][0] for tensor in weights) < budget
        selected = [[[tensor[a][b] for b in right] for a in left] for tensor in weights]
        return exact_optimum(selected, self.pairs) < budget

    def fast(self):
        if not self.breaths:
            cost = sum(tensor[0][0] for tensor in self.hweights)
            if cost - self.herror >= self.budget:
                return False
            if cost + self.herror >= self.budget and not self.feasible([0], [0]):
                return False
            damage = self.total - sum(tensor[0][0] for tensor in self.aweights)
            self.bounds = (math.nextafter(damage - self.aerror, -math.inf),
                           math.nextafter(damage + self.aerror, math.inf))
            return True
        lower, upper, left, right = relaxation(self.hweights, self.pairs)
        if lower - self.herror >= self.budget:
            return False
        if upper + self.herror >= self.budget:
            if lower + self.herror >= self.budget:
                weights, _, budget = self.data()
                projected = [[min(row) for row in tensor] for tensor in weights]
                if matching(projected)[0] >= budget:
                    return False
            return self.tighten()
        free_left = [a for a in range(self.size) if a not in left]
        free_right = [b for b in range(self.size) if b not in right]
        _, witness, aleft, aright = relaxation(
            self.aweights, self.pairs, free_left, free_right)
        self.witness = left, right, aleft, aright
        lower = relaxation(self.aweights, self.pairs)[0]
        self.bounds = (math.nextafter(self.total - witness - self.aerror, -math.inf),
                       math.nextafter(self.total - lower + self.aerror, math.inf))
        return True

    def tighten(self):
        if self.best_exact is not None:
            return True
        if self.witness is not None and self.bounds[1] - self.bounds[0] <= (
                ERROR_MARGIN * self.aerror + 2 * math.ulp(self.total)):
            hw, aw, budget = self.data()
            left, right, aleft, aright = self.witness
            loss = sum(w[a][b] for w, a, b in zip(hw, left, right))
            cost = sum(w[a][b] for w, a, b in zip(aw, aleft, aright))
            lower = matching([[min(row) for row in w] for w in aw])[0]
            if loss < budget and cost == lower:
                self.best_exact = self.total - cost
                self.bounds = Surd(self.best_exact).float_bounds()
                return True
        if self.candidates is not None:
            return True
        limit = 1 << self.size
        full = limit - 1
        pairs = self.pairs
        healers = len(self.hweights)
        masks = layout(self.size)[0][healers]
        survival = role_dp(self.hweights, self.size, pairs,
                           math.nextafter(self.budget + self.herror, math.inf))
        viable = []
        for a in masks:
            for b in masks if pairs else (0,):
                value = survival[a * limit + b if pairs else a]
                if value - self.herror >= self.budget:
                    continue
                if value + self.herror >= self.budget:
                    left = [j for j in range(self.size) if a >> j & 1]
                    right = [j for j in range(self.size) if b >> j & 1] if pairs else [0]
                    if not self.feasible(left, right):
                        continue
                viable.append((full ^ a, full ^ b if pairs else 0))
        if not viable:
            return False
        del survival
        a, b = viable[0]
        first = [j for j in range(self.size) if a >> j & 1]
        second = [j for j in range(self.size) if b >> j & 1] if pairs else [0]
        ceiling = relaxation(self.aweights, pairs, first, second)[1]
        cutoff = math.nextafter(ceiling + ERROR_MARGIN * self.aerror, math.inf)
        if len(viable) == 1:
            weights = [[[w[x][y] for y in second] for x in first] for w in self.aweights]
            best = role_dp(weights, len(first), pairs, cutoff)[-1]
            self.candidates = viable
        else:
            damage = role_dp(self.aweights, self.size, pairs, cutoff)
            best = min(damage[a * limit + b if pairs else a] for a, b in viable)
            self.candidates = [(a, b) for a, b in viable if
                               damage[a * limit + b if pairs else a] <= best + 2 * self.aerror]
        self.bounds = (math.nextafter(self.total - best - self.aerror, -math.inf),
                       math.nextafter(self.total - best + self.aerror, math.inf))
        return True

    def exact(self):
        if self.best_exact is not None:
            return self.best_exact
        _, weights, _ = self.data()
        if not self.breaths:
            self.best_exact = self.total - sum(tensor[0][0] for tensor in weights)
            return self.best_exact
        self.tighten()
        if self.best_exact is not None:
            return self.best_exact
        best = None
        projected = [[min(row) for row in tensor] for tensor in weights]
        global_lower = matching(projected)[0]
        seen = set()
        for a, b in self.candidates:
            left = [j for j in range(self.size) if a >> j & 1]
            right = [j for j in range(self.size) if b >> j & 1] if self.pairs else [0]
            selected = [[[tensor[x][y] for y in right] for x in left] for tensor in weights]
            key = tuple(tuple(tuple(Surd(v).terms for v in row) for row in tensor)
                        for tensor in selected)
            if key in seen:
                continue
            seen.add(key)
            value = exact_optimum(selected, self.pairs)
            if value == global_lower:
                best = value
                break
            if best is None or value < best:
                best = value
        self.best_exact = self.total - best
        return self.best_exact


def solve(attackers, healers, health, speed, dragon, spells):
    start, initial, breaths, blocks = (0, 0), True, [], []
    cache = {}
    for index, spell in enumerate(spells, 1):
        if spell.kind == TAIL:
            break
        if spell.kind == BREATH:
            breaths.append(spell)
            continue
        key = start, initial, tuple((s.power, s.duration, tuple(s.places))
                                   for s in breaths + [spell])
        if key not in cache:
            block = Block(attackers, healers, health, speed, start, breaths, spell, initial)
            if not block.fast():
                return None
            cache[key] = block
        blocks.append(cache[key])
        lower, upper = 0.0, 0.0
        for block in blocks:
            lower, upper = add((lower, upper), block.bounds)
        if lower >= dragon:
            return index
        if upper >= dragon:
            for block in dict.fromkeys(blocks):
                if block.breaths:
                    block.tighten()
            lower, upper = 0.0, 0.0
            for block in blocks:
                lower, upper = add((lower, upper), block.bounds)
            if lower >= dragon:
                return index
            if upper >= dragon and sum(block.exact() for block in blocks) >= dragon:
                return index
        start, initial, breaths = spell.places[0], False, []
    return None


def parse_input(text):
    words = iter(text.split())
    attackers_count, healers_count, count = (
        int(next(words)) for _ in range(AURA_FIELDS)
    )
    health, speed, dragon = (int(next(words)) for _ in range(AURA_FIELDS))
    attackers = [
        tuple(int(next(words)) for _ in range(AURA_FIELDS))
        for _ in range(attackers_count)
    ]
    healers = [
        tuple(int(next(words)) for _ in range(AURA_FIELDS))
        for _ in range(healers_count)
    ]
    spells = []
    for _ in range(count):
        kind = next(words)
        if kind == TAIL:
            spells.append(Spell(kind, 0, 0, []))
            continue
        power, duration = int(next(words)), int(next(words))
        places = 1 if kind == STORM else attackers_count + healers_count
        points = [(int(next(words)), int(next(words))) for _ in range(places)]
        spells.append(Spell(kind, power, duration, points))
    return attackers, healers, health, speed, dragon, spells


def main():
    result = solve(*parse_input(sys.stdin.read()))
    message = "You are not prepared" if result is None else "No useful loot again\n" + str(result)
    sys.stdout.write(message + "\n")



if __name__ == "__main__":
    main()
