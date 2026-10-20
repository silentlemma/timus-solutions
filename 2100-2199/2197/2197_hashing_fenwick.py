import sys
from array import array
from bisect import bisect_right
from math import gcd

MOD = 1000000007
OTHER_MOD = 1000000009
BASE = 911382323
WORD_BITS = 32
CACHE_LIMIT = 1024


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    n, m, q = int(next(tokens)), int(next(tokens)), int(next(tokens))
    strings = [next(tokens)]
    strings.extend(next(tokens) for _ in range(m))
    power = array('I', [1])
    other_power = array('I', [1])
    a = b = 1
    for _ in range(n):
        a = a * BASE % MOD
        b = b * BASE % OTHER_MOD
        power.append(a)
        other_power.append(b)
    first = array('I', [0])
    second = array('I', [0])
    counts = array('i', [0])
    starts = array('i')
    lengths = array('i')
    a = b = count = 0
    # Every source starts with the same powers; a copy only needs one shift.
    for text in strings:
        starts.append(len(first) - 1)
        lengths.append(len(text))
        if len(text) > n:
            continue
        for index, char in enumerate(text):
            a = (a + char * power[index]) % MOD
            b = (b + char * other_power[index]) % OTHER_MOD
            first.append(a)
            second.append(b)
            count += char
            counts.append(count)
    del strings

    following = array('i', [n]) * (n + 1)
    sources = array('i', [0]) * (n + 1)
    shifts = array('i', [0]) * (n + 1)
    values = array('I', [0]) * (n + 1)
    other_values = array('I', [0]) * (n + 1)
    boundaries = []
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            if divisor < n:
                boundaries.append(divisor)
            partner = n // divisor
            if partner != divisor and partner < n:
                boundaries.append(partner)
        divisor += 1
    boundaries.sort()
    size = len(boundaries)
    buckets = array('i', (bisect_right(boundaries, position) + 1 for position in range(n)))
    indices = {length: index + 1 for index, length in enumerate(boundaries)}
    fenwick = array('q', [0]) * (size + 1)
    other_fenwick = array('q', [0]) * (size + 1)
    whole, other_whole = first[n], second[n]
    total = counts[n]
    values[0], other_values[0] = whole, other_whole
    index = 1
    while index <= size:
        fenwick[index], other_fenwick[index] = whole, other_whole
        index *= 2

    low = array('I', [0]) * (n // WORD_BITS + 1)
    middle = array('I', [0]) * (len(low) // WORD_BITS + 1)
    high = array('I', [0]) * (len(middle) // WORD_BITS + 1)
    low[0] = middle[0] = high[0] = 1
    top = 1

    def insert(position):
        nonlocal top
        block, bit = divmod(position, WORD_BITS)
        previous = low[block]
        low[block] |= 1 << bit
        if previous:
            return
        group, bit = divmod(block, WORD_BITS)
        previous = middle[group]
        middle[group] |= 1 << bit
        if previous:
            return
        block, bit = divmod(group, WORD_BITS)
        previous = high[block]
        high[block] |= 1 << bit
        if previous:
            return
        top |= 1 << block

    def erase(position):
        nonlocal top
        block, bit = divmod(position, WORD_BITS)
        low[block] &= ~(1 << bit)
        if not low[block]:
            group, bit = divmod(block, WORD_BITS)
            middle[group] &= ~(1 << bit)
            if not middle[group]:
                block, bit = divmod(group, WORD_BITS)
                high[block] &= ~(1 << bit)
                if not high[block]:
                    top &= ~(1 << block)

    def predecessor(position):
        block, bit = divmod(position, WORD_BITS)
        bits = low[block] & ((1 << (bit + 1)) - 1)
        if not bits:
            group, bit = divmod(block, WORD_BITS)
            bits = middle[group] & ((1 << bit) - 1)
            if not bits:
                upper, bit = divmod(group, WORD_BITS)
                bits = high[upper] & ((1 << bit) - 1)
                if not bits:
                    upper = (top & ((1 << upper) - 1)).bit_length() - 1
                    bits = high[upper]
                group = upper * WORD_BITS + bits.bit_length() - 1
                bits = middle[group]
            block = group * WORD_BITS + bits.bit_length() - 1
            bits = low[block]
        return block * WORD_BITS + bits.bit_length() - 1

    def set_value(position, a, b):
        delta = a - values[position]
        other_delta = b - other_values[position]
        values[position], other_values[position] = a, b
        index = buckets[position]
        while index <= size:
            fenwick[index] += delta
            other_fenwick[index] += other_delta
            index += index & -index

    def replace(begin, end, source):
        nonlocal whole, other_whole, total
        position = predecessor(begin)
        shift = shifts[position]
        old_source = sources[position]
        stop = following[position]
        if end <= stop and source == old_source + begin - position:
            return False
        a = (first[source + end - begin] - first[source]) * power[begin] % MOD
        b = (second[source + end - begin] - second[source]) * other_power[begin] % OTHER_MOD
        if end <= stop:
            left = old_source + begin - position
            right = left + end - begin
            old_a = (first[right] - first[left]) * power[shift] % MOD
            old_b = (second[right] - second[left]) * other_power[shift] % OTHER_MOD
            if a == old_a and b == old_b:
                return False
        removed_a = removed_b = 0
        kept_a = kept_b = 0
        delta_count = counts[source + end - begin] - counts[source]
        # Each erased fragment is visited once; only the two ends can survive.
        while position < end:
            stop = following[position]
            old_source = sources[position]
            shift = shifts[position]
            removed_a += values[position]
            removed_b += other_values[position]
            delta_count -= counts[old_source + stop - position] - counts[old_source]
            if position < begin:
                right = old_source + begin - position
                left_a = (first[right] - first[old_source]) * power[shift] % MOD
                left_b = (second[right] - second[old_source]) * other_power[shift] % OTHER_MOD
                kept_a += left_a
                kept_b += left_b
                delta_count += counts[right] - counts[old_source]
                following[position] = begin
                set_value(position, left_a, left_b)
            elif position != begin:
                set_value(position, 0, 0)
                erase(position)
            if end < stop:
                left = old_source + end - position
                right = old_source + stop - position
                right_a = (first[right] - first[left]) * power[shift] % MOD
                right_b = (second[right] - second[left]) * other_power[shift] % OTHER_MOD
                kept_a += right_a
                kept_b += right_b
                delta_count += counts[right] - counts[left]
                sources[end], shifts[end], following[end] = left, shift, stop
                set_value(end, right_a, right_b)
                insert(end)
            position = stop
        whole = (whole + a + kept_a - removed_a) % MOD
        other_whole = (other_whole + b + kept_b - removed_b) % OTHER_MOD
        total += delta_count
        sources[begin], shifts[begin], following[begin] = source, begin, end
        set_value(begin, a, b)
        insert(begin)
        return True

    def prefix(length):
        position = predecessor(length - 1)
        a = b = 0
        index = indices[length]
        while index:
            a += fenwick[index]
            b += other_fenwick[index]
            index -= index & -index
        stop = following[position]
        if stop != length:
            source = sources[position]
            left, right = source + length - position, source + stop - position
            shift = shifts[position]
            a -= (first[right] - first[left]) * power[shift] % MOD
            b -= (second[right] - second[left]) * other_power[shift] % OTHER_MOD
        return a % MOD, b % OTHER_MOD

    primes = []
    remaining = n
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            primes.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        primes.append(remaining)
    repeated, other_repeated = power[n] - 1, other_power[n] - 1
    cache = {}
    longest = str(n * n)

    def answer():
        repetitions = gcd(n, total)
        if repetitions == 1:
            return longest
        key = whole * OTHER_MOD + other_whole
        if key in cache:
            return cache[key]
        period = n
        for prime in primes:
            while period % prime == 0:
                candidate = period // prime
                # Repeating a prefix repeats its character sum as well.
                if repetitions % (n // candidate):
                    break
                a, b = prefix(candidate)
                if whole * (power[candidate] - 1) % MOD != a * repeated % MOD:
                    break
                if other_whole * (other_power[candidate] - 1) % OTHER_MOD != (
                    b * other_repeated % OTHER_MOD
                ):
                    break
                period = candidate
        result = str(n * period)
        if len(cache) == CACHE_LIMIT:
            cache.clear()
        cache[key] = result
        return result

    result = [answer()]
    for _ in range(q):
        begin, index = int(next(tokens)) - 1, int(next(tokens))
        end = begin + lengths[index]
        if replace(begin, end, starts[index]):
            result.append(answer())
        else:
            result.append(result[-1])
    sys.stdout.write('\n'.join(result) + '\n')


if __name__ == '__main__':
    main()
