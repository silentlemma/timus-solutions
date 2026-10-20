import sys
from array import array
from math import isqrt

SMALL_LIMIT = 100
WORD_BITS = 30
QUERY_FIELDS = 3


def main():
    data = array("I", map(int, sys.stdin.buffer.read().split()))
    n, count = data[:2]
    largest = max(data)
    smallest = array("H", [0]) * (largest + 1)
    prime_bits = array("I", [0]) * (SMALL_LIMIT + 1)
    bit = 1
    for prime in range(2, isqrt(largest) + 1):
        if smallest[prime]:
            continue
        if prime <= SMALL_LIMIT:
            prime_bits[prime] = bit
            bit *= 2
        for multiple in range(prime * prime, largest + 1, prime):
            if not smallest[multiple]:
                smallest[multiple] = prime
    for prime in range(2, min(SMALL_LIMIT, largest) + 1):
        if not smallest[prime] and not prime_bits[prime]:
            prime_bits[prime] = bit
            bit *= 2
    repeat_bit = bit
    # Three distinct primes above 100 already have a product exceeding the value limit.
    # The smaller primes and the repetition flag fit in a native integer on PyPy.
    factor_masks = array("I", [0]) * (largest + 1)
    factor_first = array("I", [0]) * (largest + 1)
    factor_second = array("I", [0]) * (largest + 1)
    for value in range(2, largest + 1):
        prime = smallest[value]
        if not prime:
            if value <= SMALL_LIMIT:
                factor_masks[value] = prime_bits[value]
            else:
                factor_first[value] = value
        else:
            remaining = value // prime
            if prime <= SMALL_LIMIT:
                factor_masks[value] = factor_masks[remaining] | prime_bits[prime]
                factor_first[value] = factor_first[remaining]
                factor_second[value] = factor_second[remaining]
            else:
                factor_first[value] = prime
                other = factor_first[remaining]
                if other != prime:
                    factor_second[value] = other
    del smallest, prime_bits
    event_shift = ((n + count) * 2).bit_length()
    position_shift = event_shift + n.bit_length()
    event_mask = (1 << event_shift) - 1
    position_mask = (1 << n.bit_length()) - 1
    # Sorting packed prime, position, and event fields assigns all occurrence ranks offline.
    records = []
    for event in range(n + count):
        if event < n:
            position = event
            value = data[event + 2]
        else:
            index = n + 2 + (event - n) * QUERY_FIELDS
            if data[index] == 1:
                continue
            position = data[index + 1] - 1
            value = data[index + 2]
        first = factor_first[value]
        second = factor_second[value]
        if first:
            records.append((first << position_shift) | (position << event_shift) | event * 2)
        if second:
            records.append((second << position_shift) | (position << event_shift) | (event * 2 + 1))
    del factor_first, factor_second
    records.sort()
    ranks = array("I", [0]) * ((n + count) * 2)
    positions = array("i", [-1])
    primes = array("I", [0])
    previous = array("I", [0])
    following = array("I", [0])
    present = bytearray(1)
    last_key = -1
    rank = 0
    for record in records:
        event = record & event_mask
        key = record >> event_shift
        if key != last_key:
            rank += 1
            positions.append(key & position_mask)
            primes.append(record >> position_shift)
            previous.append(0)
            following.append(0)
            present.append(0)
            last_key = key
        ranks[event] = rank
        if event < n * 2:
            present[rank] = 1
    del records
    # A word in each upper level marks nonempty words in the level below.
    levels = []
    length = rank + 1
    while True:
        length = (length + WORD_BITS - 1) // WORD_BITS
        levels.append(array("I", [0]) * length)
        if length == 1:
            break
    words = levels[0]
    predecessor = array("i", [-1]) * (rank + 1)
    last = 0
    for node in range(1, rank + 1):
        if present[node]:
            previous[node] = last
            if primes[last] == primes[node]:
                predecessor[node] = positions[last]
            following[last] = node
            last = node
            words[node // WORD_BITS] |= 1 << (node % WORD_BITS)
    del present
    for level in range(1, len(levels)):
        lower = levels[level - 1]
        upper = levels[level]
        for block, word in enumerate(lower):
            if word:
                upper[block // WORD_BITS] |= 1 << (block % WORD_BITS)

    def remove(node):
        node_id = node
        before = previous[node]
        after = following[node]
        following[before] = after
        if after:
            previous[after] = before
        level = 0
        while True:
            block, offset = divmod(node, WORD_BITS)
            layer = levels[level]
            layer[block] ^= 1 << offset
            if layer[block] or level + 1 == len(levels):
                break
            node = block
            level += 1
        if after and primes[after] == primes[node_id]:
            predecessor[after] = positions[before] if primes[before] == primes[node_id] else -1
            return after
        return 0

    def insert(node):
        cursor = node
        level = 0
        while True:
            block, offset = divmod(cursor, WORD_BITS)
            word = levels[level][block] & ((1 << offset) - 1)
            if word:
                before = block * WORD_BITS + word.bit_length() - 1
                while level:
                    level -= 1
                    before = before * WORD_BITS + levels[level][before].bit_length() - 1
                break
            level += 1
            if level == len(levels):
                before = 0
                break
            cursor = block
        after = following[before]
        predecessor[node] = positions[before] if primes[before] == primes[node] else -1
        previous[node] = before
        following[node] = after
        following[before] = node
        if after:
            previous[after] = node
        cursor = node
        for layer in levels:
            block, offset = divmod(cursor, WORD_BITS)
            word = layer[block]
            layer[block] = word | (1 << offset)
            if word:
                break
            cursor = block
        if after and primes[after] == primes[node]:
            predecessor[after] = positions[node]
            return after
        return 0

    # Each segment stores small-prime occurrences and the largest large-prime predecessor.
    size = 1
    while size < n:
        size *= 2
    masks = array("I", [0]) * (size * 2)
    maximum = array("i", [-1]) * (size * 2)
    current_first = ranks[:n * 2:2]
    current_second = ranks[1:n * 2:2]
    for position in range(n):
        masks[size + position] = factor_masks[data[position + 2]]
        best = max(predecessor[current_first[position]], predecessor[current_second[position]])
        maximum[size + position] = best
    for node in range(size - 1, 0, -1):
        left = node * 2
        left_mask = masks[left]
        right_mask = masks[left + 1]
        mask = left_mask | right_mask
        if left_mask & right_mask:
            mask |= repeat_bit
        masks[node] = mask
        maximum[node] = max(maximum[left], maximum[left + 1])

    def refresh_previous(position):
        first = predecessor[current_first[position]]
        second = predecessor[current_second[position]]
        best = first if first > second else second
        node = size + position
        if maximum[node] == best:
            return
        maximum[node] = best
        node //= 2
        while node:
            left = maximum[node * 2]
            right = maximum[node * 2 + 1]
            best = left if left > right else right
            if maximum[node] == best:
                break
            maximum[node] = best
            node //= 2

    def refresh_masks(position, mask):
        node = size + position
        if masks[node] == mask:
            return
        masks[node] = mask
        node //= 2
        while node:
            left = node * 2
            left_mask = masks[left]
            right_mask = masks[left + 1]
            mask = left_mask | right_mask
            if left_mask & right_mask:
                mask |= repeat_bit
            if masks[node] == mask:
                break
            masks[node] = mask
            node //= 2

    answers = []
    for query in range(count):
        index = n + 2 + query * QUERY_FIELDS
        kind = data[index]
        first = data[index + 1]
        second = data[index + 2]
        first -= 1
        if kind == 2:
            rank_index = (n + query) * 2
            new_first = ranks[rank_index]
            new_second = ranks[rank_index + 1]
            old_first = current_first[first]
            old_second = current_second[first]
            affected = []
            for old in (old_first, old_second):
                if old and old != new_first and old != new_second:
                    after = remove(old)
                    if after:
                        affected.append(positions[after])
            for new in (new_first, new_second):
                if new and new != old_first and new != old_second:
                    after = insert(new)
                    if after:
                        affected.append(positions[after])
            current_first[first] = new_first
            current_second[first] = new_second
            for position in affected:
                refresh_previous(position)
            refresh_previous(first)
            refresh_masks(first, factor_masks[second])
            continue
        # Visit segments in order, then descend to the earliest valid second position.
        second -= 1
        left = first + size
        right = second + size + 1
        prefix = repeat_bit
        tail = []
        candidate = 0
        while left < right:
            if left & 1:
                if masks[left] & prefix or maximum[left] >= first:
                    candidate = left
                    break
                prefix |= masks[left]
                left += 1
            if right & 1:
                right -= 1
                tail.append(right)
            left //= 2
            right //= 2
        if not candidate:
            for node in reversed(tail):
                if masks[node] & prefix or maximum[node] >= first:
                    candidate = node
                    break
                prefix |= masks[node]
        if not candidate:
            answers.append("-1")
            continue
        while candidate < size:
            candidate *= 2
            if not (masks[candidate] & prefix or maximum[candidate] >= first):
                prefix |= masks[candidate]
                candidate += 1
        position = candidate - size
        partner = maximum[candidate]
        target = masks[candidate]
        # Finish by choosing the last earlier position sharing a small prime.
        if target and partner < position - 1:
            left = first + size
            right = position + size
            head = []
            candidate = 0
            while left < right:
                if right & 1:
                    right -= 1
                    if masks[right] & target:
                        candidate = right
                        break
                if left & 1:
                    head.append(left)
                    left += 1
                left //= 2
                right //= 2
            if not candidate:
                for node in reversed(head):
                    if masks[node] & target:
                        candidate = node
                        break
            if candidate:
                while candidate < size:
                    candidate = candidate * 2 + 1
                    if not masks[candidate] & target:
                        candidate -= 1
                partner = max(partner, candidate - size)
        answers.append(f"{partner + 1} {position + 1}")
    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
