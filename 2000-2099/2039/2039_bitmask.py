"""Count striped squares with bitmasks, run endpoints, and packed size intervals."""

from array import array
from bisect import bisect_left, insort
from itertools import chain
import re
import sys

SMALL_TYPE_LIMIT = 16
SUBBLOCK_K_LIMIT = 8
BAND_MINIMUM = 8
HEADER_FIELDS = 3
LANE_BYTES = 2
LANE_BITS = 16
LANE_BASE = 1 << LANE_BITS
LONG_FIRST = 32
SINGLE_BASE = 3
INFINITE = 1024
PACKED_RANK_LIMIT = 64
SHORT_RANGE_LIMIT = 8
DIRECT_SIZE_LIMIT = 16
RUN_SCAN_LIMIT = 16
ENDPOINT_CHANGE_LIMIT = 8
ENDPOINT_REFRESH_DIVISOR = 2
MAX_SIDE = 1000
COORDINATES = "".join(map(chr, range(MAX_SIDE + 2)))
BYTE_BASE = 1 << (LANE_BITS // LANE_BYTES)
BYTE_MASK = BYTE_BASE - 1
RANK_SELECTORS = [
    bytes(BYTE_MASK if value == page else 0 for value in range(BYTE_BASE))
    for page in range(MAX_SIDE // BYTE_BASE + 1)
]


def greater_count(masks, k, valid_mask):
    planes = []
    for value in masks:
        bit = 0
        while value:
            if bit == len(planes):
                planes.append(value)
                break
            carry = value & planes[bit]
            planes[bit] ^= value
            value = carry
            bit += 1
    if len(planes) < k.bit_length():
        return 0
    equal = valid_mask
    greater = 0
    for bit in range(len(planes) - 1, -1, -1):
        if k >> bit & 1:
            equal &= planes[bit]
        else:
            greater |= equal & planes[bit]
            equal &= ~planes[bit]
    return greater & valid_mask


def excessive_blocks(black, n, m, k):
    size = 2 * k + 1
    if k > SUBBLOCK_K_LIMIT or size > min(n, m):
        return None
    valid_mask = (1 << (m - size + 1)) - 1
    horizontal = [erosion(row, size) for row in black]
    rows = []
    for r in range(n - size + 1):
        vertical = black[r]
        for bits in black[r + 1 : r + size]:
            vertical &= bits
        bad = greater_count(horizontal[r : r + size], k, valid_mask)
        bad |= greater_count((vertical >> c for c in range(size)), k, valid_mask)
        rows.append(valid_mask ^ bad)
    return size, square_table(rows, n - size + 1, m - size + 1)


def square_table(rows, n, m):
    table = [rows]
    power = 1
    while power * 2 <= min(n, m):
        old = table[-1]
        combined = [old[r] & old[r + power] for r in range(n - power * 2 + 1)]
        new = [bits & (bits >> power) for bits in combined]
        if not any(new):
            break
        table.append(new)
        power *= 2
    return table


def square_bits(table, size, r):
    level = size.bit_length() - 1
    if level >= len(table):
        return 0
    power = 1 << level
    bits = table[level][r] & table[level][r + size - power]
    return bits & (bits >> (size - power))


def mixed_limit(grid, k, with_columns=False):
    n, m = len(grid), len(grid[0])
    limit = min(n, m)
    if k >= limit:
        return (limit, None, None) if with_columns else limit
    mask = (1 << m) - 1
    black = [int(row[::-1], 2) for row in grid]
    white = [mask ^ row for row in black]
    good = []
    pair_mask = (1 << (m - 1)) - 1
    for a, b in zip(white, white[1:]):
        ar, br = a >> 1, b >> 1
        diagonal = (a & br & ~ar & ~b) | (ar & b & ~a & ~br)
        three = (a & ar & (b ^ br)) | (b & br & (a ^ ar))
        good.append(pair_mask & ~(diagonal | three))
    good_table = square_table(good, n - 1, m - 1)
    black_table = square_table(black, n, m)
    white_table = square_table(white, n, m)
    extra = excessive_blocks(black, n, m, k)
    starts_mask = (1 << (m - k)) - 1
    no_black = [starts_mask ^ square_bits(black_table, k + 1, r) for r in range(n - k)]
    no_black_table = square_table(no_black, n - k, m - k)

    def columns(size, r):
        allowed = square_bits(good_table, size - 1, r) & ((1 << (m - size + 1)) - 1)
        if not allowed:
            return 0
        allowed &= square_bits(no_black_table, size - k, r)
        if not allowed:
            return 0
        if extra is not None and size >= extra[0]:
            allowed &= square_bits(extra[1], size - extra[0] + 1, r)
            if not allowed:
                return 0
        return allowed & ~square_bits(white_table, size, r)

    def possible(size):
        return any(columns(size, r) for r in range(n - size + 1))

    lo, hi = k, limit + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if possible(mid):
            lo = mid
        else:
            hi = mid
    return (lo, columns, extra) if with_columns else lo


def erosion(bits, size):
    length = 1
    while bits and 2 * length <= size:
        bits &= bits >> length
        length *= 2
    if length < size:
        bits &= bits >> (size - length)
    return bits


def combine_counts(left, right):
    result = []
    carry = 0
    for bit in range(max(len(left), len(right))):
        a = left[bit] if bit < len(left) else 0
        b = right[bit] if bit < len(right) else 0
        result.append(a ^ b ^ carry)
        carry = (a & b) | ((a ^ b) & carry)
    if carry:
        result.append(carry)
    return result


def parallel_counts(bits, size, stride):
    # Each plane stores one binary digit for every window simultaneously.
    result = []
    block = [bits]
    offset = 0
    while size:
        if size & 1:
            result = combine_counts(result, [value >> offset for value in block])
            offset += stride
        size >>= 1
        if size:
            block = combine_counts(block, [value >> stride for value in block])
            stride *= 2
    return result


def equal_count(planes, target, candidates):
    if target >= 1 << len(planes):
        return 0
    for bit, values in enumerate(planes):
        candidates &= values if target >> bit & 1 else ~values
    return candidates


def expand(bits, size, stride):
    length = 1
    while 2 * length <= size:
        bits |= bits >> (length * stride)
        length *= 2
    if length < size:
        bits |= bits >> ((size - length) * stride)
    return bits


def shrink(bits, size, stride):
    length = 1
    while bits and 2 * length <= size:
        bits &= bits >> (length * stride)
        length *= 2
    if length < size:
        bits &= bits >> ((size - length) * stride)
    return bits


def board_bits(grid):
    return int("".join(row[::-1] for row in reversed(grid)), 2)


def count_parallel(grid, k, first_size, limit, extra):
    n, m = len(grid), len(grid[0])
    original = board_bits(grid)
    row_mask = (1 << m) - 1
    row_ones = ((1 << (n * m)) - 1) // row_mask
    extra_bits = 0
    if extra is not None:
        base, rows = extra
        extra_bits = int("".join(format(row, f"0{m}b") for row in reversed(rows)), 2)
    answer = 0
    for size in range(first_size, limit + 1):
        start_cols = ((1 << (m - size + 1)) - 1) * row_ones
        full_rows = shrink(original, size, 1) & start_cols
        if not full_rows:
            break
        first = ((full_rows & -full_rows).bit_length() - 1) // m
        last = (full_rows.bit_length() - 1) // m
        first = max(0, first - size + 1)
        last = min(n, last + size)
        height = last - first
        if height < size:
            continue
        mask = (1 << (height * m)) - 1
        bits = (original >> (first * m)) & mask
        full_rows = (full_rows >> (first * m)) & mask
        starts = start_cols & ((1 << ((height - size + 1) * m)) - 1)
        if size == k:
            answer += (shrink(full_rows, size, m) & starts).bit_count()
            continue
        if extra is not None and size >= base:
            cropped = (extra_bits >> (first * m)) & mask
            width = size - base + 1
            starts &= shrink(shrink(cropped, width, 1), width, m)
        if not starts:
            continue
        full_columns = shrink(bits, size, m)
        starts &= expand(full_rows, size, m) & expand(full_columns, size, 1)
        if not starts:
            continue
        candidates = equal_count(parallel_counts(full_rows, size, m), k, starts)
        if not candidates:
            continue
        candidates &= equal_count(parallel_counts(full_columns, size, 1), k, starts)
        if not candidates:
            continue
        # The full columns exhaust the black cells of every other allowed row.
        good_rows = full_rows | equal_count(parallel_counts(bits, size, 1), k, mask)
        answer += (candidates & shrink(good_rows, size, m)).bit_count()
    return answer


def length_counts(line, k, limit):
    # Each consecutive group contributes a trapezoid of window lengths.
    # Its second differences need only four endpoint updates.
    positions = [-1] + [i for i, value in enumerate(line) if value == "1"] + [len(line)]
    differences = [0] * (len(line) + 2 + 1)
    for index in range(1, len(positions) - k):
        first, last = positions[index], positions[index + k - 1]
        width = last - first + 1
        before = first - positions[index - 1]
        after = positions[index + k] - last
        differences[width] += 1
        differences[width + before] -= 1
        differences[width + after] -= 1
        differences[width + before + after] += 1
    counts = [0] * (limit + 1)
    slope = value = 0
    for size in range(1, min(limit, len(line)) + 1):
        slope += differences[size]
        value += slope
        counts[size] = value
    return counts


def count_regular(grid, pattern, k):
    n, m = len(grid), len(grid[0])
    full = "1" * m
    rows = "".join("1" if row == full else "0" for row in grid)
    full_rows = sum(max(0, len(run) - k + 1) for run in rows.split("0"))
    full_cols = sum(max(0, len(run) - k + 1) for run in pattern.split("0"))
    answer = full_rows * (m - k + 1) + full_cols * (n - k + 1) - full_rows * full_cols
    limit = min(n, m)
    row_counts = length_counts(rows, k, limit)
    col_counts = length_counts(pattern, k, limit)
    return answer + sum(row_counts[size] * col_counts[size] for size in range(k + 1, limit + 1))


def separate_components(grid, patterns):
    # A striped square connects all its rows and columns through black cells.
    remaining = [int(row[::-1], 2) for row in patterns if "1" in row]
    components = []
    while remaining:
        columns = remaining.pop()
        previous = -1
        while previous != columns:
            previous = columns
            keep = []
            for row in remaining:
                if row & columns:
                    columns |= row
                else:
                    keep.append(row)
            remaining = keep
        components.append(columns)
    if len(components) < 2:
        return None
    rows = [int(row[::-1], 2) for row in grid]
    rectangles = []
    for columns in components:
        left = (columns & -columns).bit_length() - 1
        right = columns.bit_length()
        if (columns >> left) & ((columns >> left) + 1):
            return None
        indices = [r for r, row in enumerate(rows) if row & columns]
        top, bottom = indices[0], indices[-1] + 1
        if bottom - top != len(indices):
            return None
        rectangles.append([row[left:right] for row in grid[top:bottom]])
    return rectangles


def local_shapes(black, n, m, k):
    # White cells form the product of their occupied rows and columns.
    # Overlapping base windows share a white cell after black blocks are excluded.
    # Consequently these local certificates extend to every larger square.
    base = k + 2
    if base > min(n, m):
        return []
    full = [erosion(row, base) for row in black]
    blocks = []
    for r in range(n - k):
        value = black[r]
        for row in black[r + 1 : r + k + 1]:
            value &= row
        blocks.append(erosion(value, k + 1))
    pairs = {}
    for r in range(n):
        for q in range(r + 1, min(n, r + base)):
            pairs[r, q] = full[r] | full[q] | erosion(~(black[r] ^ black[q]), base)
    mask = (1 << (m - base + 1)) - 1
    good = []
    for r in range(n - base + 1):
        invalid = blocks[r] | blocks[r + 1]
        allowed = mask & ~(invalid | (invalid >> 1))
        for a in range(r, r + base):
            for b in range(a + 1, r + base):
                allowed &= pairs[a, b]
        good.append(allowed)
    return square_table(good, n - base + 1, m - base + 1)


def packed_minimum(a, b, highs):
    flags = (((a | highs) - b) & highs) >> (LANE_BITS - 1)
    return a ^ ((a ^ b) & (flags * (LANE_BASE - 1)))


def packed_flags(bits, width):
    value = bin(bits)[2:].zfill(width)[::-1].encode("utf-16le")
    return int.from_bytes(value.translate(bytes.maketrans(b"01", b"\0\1")), "little")


def unpack_flags(value, width):
    digits = value.to_bytes(width * LANE_BYTES, "little")[::LANE_BYTES]
    return int(digits.translate(bytes.maketrans(b"\0\1", b"01"))[::-1], 2)


def distances(noise, width, cache):
    if noise not in cache:
        row = bin(noise)[2:].zfill(width)[::-1].replace("1", "\0")
        row = re.sub("0+", lambda match: COORDINATES[len(match[0]):0:-1], row)
        cache[noise] = int.from_bytes(row.encode("utf-16le"), "little")
    return cache[noise]


def shape_bounds(allowed, m, k):
    # A row of square-DP values is bounded by the next row and its right zero.
    # Packed minima evaluate all columns together without a per-cell recurrence.
    width = m - k - 1
    ones = ((1 << (width * LANE_BITS)) - 1) // (LANE_BASE - 1)
    highs = ones << (LANE_BITS - 1)
    mask = (1 << width) - 1
    dp = 0
    result = [0] * len(allowed)
    cache = {}
    for r in range(len(allowed) - 1, -1, -1):
        distance = distances(mask ^ allowed[r], width, cache)
        dp = packed_minimum(packed_minimum(dp, dp >> LANE_BITS, highs) + ones, distance, highs)
        result[r] = dp + (k + 1) * ones
    return result


def endpoints(line, k):
    # A whole run advances through consecutive ranks, so array slices suffice.
    length = len(line)
    if line.count("01") > RUN_SCAN_LIMIT:
        positions = "".join(COORDINATES[a:b] for a, b in (
            match.span() for match in re.finditer("1+", line)
        ))
        ones = ((1 << (length * LANE_BITS)) - 1) // (LANE_BASE - 1)
        digits = line.encode("utf-16le").translate(bytes.maketrans(b"01", b"\0\1"))
        value = int.from_bytes(digits, "little")
        ranks = len(positions) * ones - value - value // (LANE_BASE - 1)
        ranks = ranks.to_bytes(length * LANE_BYTES, "little")
        rank_low, rank_high = ranks[::LANE_BYTES], ranks[1::LANE_BYTES]
        result = []
        for offset in (k - 1, k):
            table = (positions[offset:] + chr(length) * (k + 1)).encode("utf-16le")
            lower, upper = table[::LANE_BYTES], table[1::LANE_BYTES]
            low_bytes = high_bytes = 0
            for page in range(len(positions) // BYTE_BASE + 1):
                selected = int.from_bytes(rank_high.translate(RANK_SELECTORS[page]), "little")
                if not selected:
                    continue
                start, end = page * BYTE_BASE, (page + 1) * BYTE_BASE
                lo = lower[start:end].ljust(BYTE_BASE, bytes([length % BYTE_BASE]))
                hi = upper[start:end].ljust(BYTE_BASE, bytes([length // BYTE_BASE]))
                low_bytes |= int.from_bytes(rank_low.translate(lo), "little") & selected
                high_bytes |= int.from_bytes(rank_low.translate(hi), "little") & selected
            packed = bytearray(length * LANE_BYTES)
            packed[::LANE_BYTES] = low_bytes.to_bytes(length, "little")
            packed[1::LANE_BYTES] = high_bytes.to_bytes(length, "little")
            values = array("H")
            values.frombytes(packed)
            result.append(values)
        return tuple(result)
    runs = [match.span() for match in re.finditer("1+", line)]
    positions = array("H", chain.from_iterable(range(a, b) for a, b in runs))
    positions.extend(array("H", [length]) * (k + 1))
    low, high = array("H"), array("H")
    before = rank = 0
    for a, b in runs:
        gap = a - before
        low.extend(array("H", [positions[rank + k - 1]]) * gap)
        high.extend(array("H", [positions[rank + k]]) * gap)
        count = b - a
        low.extend(positions[rank + k - 1:rank + k - 1 + count])
        high.extend(positions[rank + k:rank + k + count])
        rank += count
        before = b
    low.extend(array("H", [length]) * (length - before))
    high.extend(array("H", [length]) * (length - before))
    return low, high


def update_endpoints(bits, previous, k, width):
    # Sliding intersections often change only a few columns.
    # A changed black cell affects only the preceding k+1 successor ranks.
    old, positions, low, high = previous
    changed = bits ^ old
    if changed.bit_count() > ENDPOINT_CHANGE_LIMIT:
        return None
    if positions is None:
        line = bin(old)[2:].zfill(width)[::-1]
        positions = [i for i, value in enumerate(line) if value == "1"]
    intervals = []
    while changed:
        bit = changed & -changed
        changed -= bit
        c = bit.bit_length() - 1
        rank = bisect_left(positions, c)
        left = positions[rank - k - 1] + 1 if rank > k else 0
        intervals.append((left, c + 1))
        if bits & bit:
            insort(positions, c)
        else:
            positions.pop(rank)
    intervals.sort()
    merged = []
    for left, right in intervals:
        if merged and left <= merged[-1][1]:
            merged[-1] = merged[-1][0], max(right, merged[-1][1])
        else:
            merged.append((left, right))
    if sum(b - a for a, b in merged) * ENDPOINT_REFRESH_DIVISOR > width:
        return None
    padded = positions + [width] * (k + 1)
    for left, right in merged:
        rank = bisect_left(positions, left)
        for c in range(left, right):
            while padded[rank] < c:
                rank += 1
            low[c] = padded[rank + k - 1]
            high[c] = padded[rank + k]
    return bits, positions, low, high


def certified_shapes(black, n, m, k):
    # Equal nonempty white row counts certify the Cartesian product of white cells.
    # Two occupied rows and columns make adjacent base windows share a white cell.
    base = k + 2
    width = m - base + 1
    if width <= 0 or n < base:
        return []
    ones = ((1 << (m * LANE_BITS)) - 1) // (LANE_BASE - 1)
    highs = ones << (LANE_BITS - 1)
    mask = (1 << m) - 1
    valid = (1 << width) - 1
    counts = []
    white_windows = []
    prepared = {}
    for row in black:
        if row in prepared:
            count, windows = prepared[row]
            counts.append(count)
            white_windows.append(windows)
            continue
        value = packed_flags(mask ^ row, m)
        prefix = value + value // (LANE_BASE - 1)
        value = prefix - (prefix >> (base * LANE_BITS))
        zeros = (~((value | highs) - ones) & highs) >> (LANE_BITS - 1)
        counts.append(value | zeros * INFINITE)
        white_windows.append(valid ^ (erosion(row, base) & valid))
        prepared[row] = counts[-1], white_windows[-1]
    prefix = [0] * n
    suffix = [0] * n
    prefix_or = [0] * n
    suffix_or = [0] * n
    prefix_one = [0] * n
    suffix_one = [0] * n
    prefix_two = [0] * n
    suffix_two = [0] * n
    for r in range(n):
        value = white_windows[r]
        white = mask ^ black[r]
        if r % base == 0:
            prefix[r] = counts[r]
            prefix_or[r] = white
            prefix_one[r] = value
        else:
            prefix[r] = packed_minimum(prefix[r - 1], counts[r], highs)
            prefix_or[r] = prefix_or[r - 1] | white
            prefix_two[r] = prefix_two[r - 1] | (prefix_one[r - 1] & value)
            prefix_one[r] = prefix_one[r - 1] | value
    for r in range(n - 1, -1, -1):
        value = white_windows[r]
        white = mask ^ black[r]
        if r == n - 1 or (r + 1) % base == 0:
            suffix[r] = counts[r]
            suffix_or[r] = white
            suffix_one[r] = value
        else:
            suffix[r] = packed_minimum(suffix[r + 1], counts[r], highs)
            suffix_or[r] = suffix_or[r + 1] | white
            suffix_two[r] = suffix_two[r + 1] | (suffix_one[r + 1] & value)
            suffix_one[r] = suffix_one[r + 1] | value
    cache = {}
    result = []
    for r in range(n - base + 1):
        end = r + base - 1
        union = prefix_or[end] | suffix_or[r]
        if union not in cache:
            value = packed_flags(union, m)
            value += value // (LANE_BASE - 1)
            cache[union] = value - (value >> (base * LANE_BITS))
        total = cache[union]
        minimum = packed_minimum(prefix[end], suffix[r], highs)
        different = minimum ^ total
        equal = ~((different | highs) - ones) & highs
        two_cols = ((total | highs) - 2 * ones) & highs
        two_rows = prefix_two[end]
        if r % base:
            two_rows |= suffix_two[r] | (prefix_one[end] & suffix_one[r])
        allowed = unpack_flags((equal & two_cols) >> (LANE_BITS - 1), m) & valid & two_rows
        result.append(allowed)
    return result


def packed_transpose(data, height):
    # Byte strides transpose compact endpoints without per-cell Python integers.
    low = data[::LANE_BYTES]
    high = data[1::LANE_BYTES]
    byte_bits = LANE_BITS // LANE_BYTES
    for r in range(height):
        a = int.from_bytes(low[r::height].decode("latin1").encode("utf-16le"), "little")
        b = int.from_bytes(high[r::height].decode("latin1").encode("utf-16le"), "little")
        yield a | (b << byte_bits)


def single_white(zero, one, size, stride, mask):
    # Disjoint blocks retain whether they contain zero or at most one white cell.
    result_zero = result_one = mask
    offset = 0
    while size:
        if size & 1:
            a, b = zero >> offset, one >> offset
            result_one = (result_one & a) | (result_zero & b)
            result_zero &= a
            offset += stride
        size >>= 1
        if size:
            one = (one & (zero >> stride)) | (zero & (one >> stride))
            zero &= zero >> stride
            stride *= 2
    return result_zero, result_one


def count_small(grid, k):
    # A square of side k is black; side k+1 requires exactly one white cell.
    n, m = len(grid), len(grid[0])
    original = board_bits(grid)
    row_mask = (1 << m) - 1
    row_ones = ((1 << (n * m)) - 1) // row_mask
    starts = ((1 << (m - k + 1)) - 1) * row_ones
    starts &= (1 << ((n - k + 1) * m)) - 1
    answer = (shrink(shrink(original, k, 1), k, m) & starts).bit_count()
    size = k + 1
    if size > min(n, m):
        return answer
    mask = (1 << (n * m)) - 1
    zero, one = single_white(original, mask, size, 1, mask)
    zero, one = single_white(zero, one, size, m, mask)
    starts = ((1 << (m - size + 1)) - 1) * row_ones
    starts &= (1 << ((n - size + 1) * m)) - 1
    return answer + (one & ~zero & starts).bit_count()


def count_offline(grid, k):
    # Among the first k+1 rows, at least one is not a stripe.
    # Their intersection therefore gives exactly the full columns of a valid square.
    # The transposed intersection gives its full rows and their endpoint intervals.
    n, m = (len(grid), len(grid[0]))
    base = k + 2
    width = m - k - 1
    answer = count_small(grid, k)
    if base > min(n, m):
        return answer
    black = [int(row[::-1], 2) for row in grid]
    extra = excessive_blocks(black, n, m, k)
    if extra is not None:
        upper = extra[0] - 1 if not any(extra[1][0]) else extra[0] + (1 << len(extra[1])) - 2
        if upper - k <= SHORT_RANGE_LIMIT:
            return answer + count_parallel(grid, k, base, min(n, m, upper), None)
    if k <= SUBBLOCK_K_LIMIT:
        allowed = local_shapes(black, n, m, k)[0]
    else:
        allowed = certified_shapes(black, n, m, k)
    if not any(allowed):
        return answer
    active_columns = 0
    for bits in allowed:
        active_columns |= bits
    certificate = square_table(allowed, n - base + 1, width)
    if len(certificate) <= 2:
        return answer + count_parallel(grid, k, base, min(n, m, k + (1 << len(certificate))), None)
    bounds = shape_bounds(allowed, m, k)
    mask = (1 << width) - 1
    packed_rows = None
    if k <= PACKED_RANK_LIMIT:
        rank_ones = ((1 << (width * LANE_BITS)) - 1) // (LANE_BASE - 1)
        full_selection = rank_ones * (LANE_BASE - 1)
        ranks = [n * rank_ones] * (k + 1)
        packed_rows = []
        seen = 0
        selections = {}
        for r in range(n - 1, -1, -1):
            bits = erosion(black[r], k + 1) & active_columns
            if bits not in selections:
                selections[bits] = packed_flags(bits, width) * (LANE_BASE - 1)
            selection = selections[bits]
            if selection:
                seen = min(k, seen + 1)
                if selection == full_selection:
                    ranks[1:] = ranks[:-1]
                    ranks[0] = r * rank_ones
                else:
                    for j in range(seen, 0, -1):
                        ranks[j] ^= (ranks[j] ^ ranks[j - 1]) & selection
                    ranks[0] ^= (ranks[0] ^ r * rank_ones) & selection
            packed_rows.append((ranks[k - 1] + (1 - r) * rank_ones, ranks[k] - r * rank_ones))
        packed_rows.reverse()
        lows = highs_list = [None] * n
    else:
        horizontal = [format(erosion(row, k + 1) & mask, f'0{width}b')[::-1] for row in black]
        columns = [''.join(col) for col in zip(*horizontal)]
        cache = {}
        lows = []
        highs_list = []
        empty = array("H", [n]) * n
        for c, line in enumerate(columns):
            if not (active_columns >> c & 1):
                lows.append(empty)
                highs_list.append(empty)
                continue
            if line not in cache:
                cache[line] = endpoints(line, k)
            lo, hi = cache[line]
            lows.append(lo)
            highs_list.append(hi)
        lower_bytes = b"".join(values.tobytes() for values in lows)
        upper_bytes = b"".join(values.tobytes() for values in highs_list)
        lows = packed_transpose(lower_bytes, n)
        highs_list = packed_transpose(upper_bytes, n)
    size = k + 1
    prefix = [0] * n
    suffix = [0] * n
    for r in range(n):
        prefix[r] = black[r] if r % size == 0 else prefix[r - 1] & black[r]
    for r in range(n - 1, -1, -1):
        suffix[r] = black[r] if r == n - 1 or (r + 1) % size == 0 else suffix[r + 1] & black[r]
    ones = ((1 << (width * LANE_BITS)) - 1) // (LANE_BASE - 1)
    highs = ones << (LANE_BITS - 1)
    evenmask = sum((LANE_BASE - 1) << (LANE_BITS * c) for c in range(0, width, 2))
    coords = int.from_bytes(array('H', range(width)).tobytes(), 'little')
    cache = {}
    previous = None
    for r, (b, rowlo, rowhi) in enumerate(zip(bounds, lows, highs_list)):
        if not allowed[r]:
            continue
        colmask = suffix[r] & prefix[r + k]
        if colmask not in cache:
            updated = update_endpoints(colmask, previous, k, m) if previous else None
            if updated is None:
                line = bin(colmask)[2:].zfill(m)[::-1]
                lo, hi = endpoints(line, k)
                previous = colmask, None, lo, hi
            else:
                previous = updated
                _, _, lo, hi = previous
            lo = int.from_bytes(lo[:width].tobytes(), 'little') - coords + ones
            hi = int.from_bytes(hi[:width].tobytes(), 'little') - coords
            cache[colmask] = (lo, hi)
        lo, hi = cache[colmask]
        if packed_rows is not None:
            rl, rh = packed_rows[r]
        else:
            rl = rowlo + (1 - r) * ones
            rh = rowhi - r * ones
        low = lo ^ rl ^ packed_minimum(lo, rl, highs)
        first = base * ones
        low = low ^ first ^ packed_minimum(low, first, highs)
        high = packed_minimum(packed_minimum(hi, rh, highs), b, highs)
        diff = (high | highs) + ones - low
        ok = ((diff & highs) >> (LANE_BITS - 1)) * (LANE_BASE - 1)
        values = diff & ok & ~highs
        total = (values & evenmask) + ((values >> LANE_BITS) & evenmask)
        answer += total % ((1 << (2 * LANE_BITS)) - 1)
    return answer


def single_shapes(grid):
    n, m = len(grid), len(grid[0])
    black = [int(row[::-1], 2) for row in grid]
    base = SINGLE_BASE
    full = [erosion(row, base) for row in black]
    adjacent = [
        full[r] | full[r + 1] | erosion(~(black[r] ^ black[r + 1]), base) for r in range(n - 1)
    ]
    blocks = [erosion(a & b, 2) for a, b in zip(black, black[1:])]
    mask = (1 << (m - base + 1)) - 1
    good = []
    for r in range(n - base + 1):
        invalid = blocks[r] | blocks[r + 1]
        allowed = mask & ~(invalid | (invalid >> 1))
        allowed &= adjacent[r] & adjacent[r + 1]
        allowed &= full[r] | full[r + 2] | erosion(~(black[r] ^ black[r + 2]), base)
        good.append(allowed)
    return black, square_table(good, n - base + 1, m - base + 1)


def single_candidates(black, table, n, m, size):
    horizontal = [erosion(row, size) for row in black]
    prefix = [0] * n
    suffix = [0] * n
    prefix_two = [0] * n
    suffix_two = [0] * n
    prefix_and = [0] * n
    suffix_and = [0] * n
    for r in range(n):
        if r % size == 0:
            prefix[r] = horizontal[r]
            prefix_and[r] = black[r]
        else:
            prefix_two[r] = prefix_two[r - 1] | (prefix[r - 1] & horizontal[r])
            prefix[r] = prefix[r - 1] | horizontal[r]
            prefix_and[r] = prefix_and[r - 1] & black[r]
    for r in range(n - 1, -1, -1):
        if r == n - 1 or (r + 1) % size == 0:
            suffix[r] = horizontal[r]
            suffix_and[r] = black[r]
        else:
            suffix_two[r] = suffix_two[r + 1] | (suffix[r + 1] & horizontal[r])
            suffix[r] = suffix[r + 1] | horizontal[r]
            suffix_and[r] = suffix_and[r + 1] & black[r]
    cache = {}
    starts = []
    valid_mask = (1 << (m - size + 1)) - 1
    for r in range(n - size + 1):
        end = r + size - 1
        if r % size == 0:
            two = prefix_two[end]
        else:
            two = prefix_two[end] | suffix_two[r] | (prefix[end] & suffix[r])
        rows = (suffix[r] | prefix[end]) & ~two & valid_mask
        if not rows:
            starts.append(0)
            continue
        if size > 2:
            rows &= square_bits(table, size - 2, r)
            if not rows:
                starts.append(0)
                continue
        vertical = suffix_and[r] & prefix_and[end]
        if vertical not in cache:
            cache[vertical] = equal_count(parallel_counts(vertical, size, 1), 1, valid_mask)
        starts.append(rows & cache[vertical])
    return starts


def count_single_bands(grid, bound, prepared=None):
    # Every larger one-stripe square contains a smaller square with the same crossing.
    # Separate candidate groups have disjoint expanded crops, so counts do not overlap.
    n, m = len(grid), len(grid[0])
    answer = sum(row.count("1") for row in grid)
    if bound < 2:
        return answer
    black, table = prepared if prepared is not None else single_shapes(grid)
    first = 2
    while first <= bound:
        last = min(bound, first * 2 - 1)
        starts = single_candidates(black, table, n, m, first)
        selected = [r for r, bits in enumerate(starts) if bits]
        if not selected:
            break
        groups = []
        top = previous = selected[0]
        columns = starts[top]
        for r in selected[1:]:
            if r - previous >= 2 * last - first:
                groups.append((top, previous, columns))
                top = r
                columns = 0
            columns |= starts[r]
            previous = r
        groups.append((top, previous, columns))
        for top, bottom, columns in groups:
            left = (columns & -columns).bit_length() - 1
            right = columns.bit_length() - 1
            margin = last - first
            top = max(0, top - margin)
            bottom = min(n, bottom + last)
            left = max(0, left - margin)
            right = min(m, right + last)
            cropped = [row[left:right] for row in grid[top:bottom]]
            width = right - left
            full = "1" * width
            patterns = set(cropped)
            patterns.discard(full)
            if len(patterns) <= 1:
                pattern = patterns.pop() if patterns else full
                rows = "".join("1" if row == full else "0" for row in cropped)
                row_counts = length_counts(rows, 1, last)
                col_counts = length_counts(pattern, 1, last)
                answer += sum(row_counts[s] * col_counts[s] for s in range(first, last + 1))
            else:
                answer += count_parallel(cropped, 1, first, last, None)
        first = last + 1
    return answer


def count_anchor(grid, ar, ac, first, last):
    # A one-stripe square has a unique crossing, which prevents duplicate counting.
    # Removing its row and column leaves an empty square inside the black run bounds.
    n, m = len(grid), len(grid[0])
    col = "".join(row[ac] for row in grid)
    left = grid[ar].rfind("0", 0, ac) + 1
    right = grid[ar].find("0", ac)
    if right < 0:
        right = m
    top = col.rfind("0", 0, ar) + 1
    bottom = col.find("0", ar)
    if bottom < 0:
        bottom = n
    top = max(top, ar - last + 1)
    bottom = min(bottom, ar + last)
    left = max(left, ac - last + 1)
    right = min(right, ac + last)
    if min(bottom - top, right - left) < first:
        return 0
    width = right - left
    pc = ac - left
    ones = ((1 << (width * LANE_BITS)) - 1) // (LANE_BASE - 1)
    highs = ones << (LANE_BITS - 1)
    evenmask = sum((LANE_BASE - 1) << (LANE_BITS * c) for c in range(0, width, 2))
    columns = int.from_bytes(
        array("H", list(range(pc + 1, 0, -1)) + [0] * (width - pc - 1)).tobytes(), "little"
    )
    selected = (1 << ((pc + 1) * LANE_BITS)) - 1
    limit = last * ones
    dp = answer = 0
    cache = {}
    for r in range(bottom - 1, top - 1, -1):
        row = grid[r][left:right] if r != ar else "0" * width
        row = row[:pc] + "0" + row[pc + 1 :]
        if row not in cache:
            packed = bytearray(
                row.encode()
                .replace(b"1", b"\0" * LANE_BYTES)
                .replace(b"0", b"\1" + b"\0" * (LANE_BYTES - 1))
            )
            for match in re.finditer("00+", row):
                start, end = match.span()
                packed[start * LANE_BYTES : end * LANE_BYTES] = array(
                    "H", range(end - start, 0, -1)
                ).tobytes()
            cache[row] = int.from_bytes(packed, "little")
        dp = packed_minimum(packed_minimum(dp, dp >> LANE_BITS, highs) + ones, cache[row], highs)
        if r > ar:
            continue
        need = max(first, ar - r + 1)
        required = need * ones
        low = columns ^ required ^ packed_minimum(columns, required, highs)
        high = packed_minimum(dp, limit, highs)
        diff = (high | highs) + ones - low
        ok = ((diff & highs) >> (LANE_BITS - 1)) * (LANE_BASE - 1)
        values = diff & ok & ~highs & selected
        total = (values & evenmask) + ((values >> LANE_BITS) & evenmask)
        count = total % ((1 << (2 * LANE_BITS)) - 1)
        answer += count
        if not count and ar - r + 1 >= first:
            break
    return answer


def count_single(grid, bound):
    n, m = len(grid), len(grid[0])
    black, table = single_shapes(grid)
    answer = count_single_bands(grid, min(bound, LONG_FIRST - 1), (black, table))
    if bound < LONG_FIRST:
        return answer
    starts = single_candidates(black, table, n, m, LONG_FIRST)
    anchors = set()
    cols = {}
    for r, bits in enumerate(starts):
        if not bits:
            continue
        vertical = black[r]
        for row in black[r + 1 : r + LONG_FIRST]:
            vertical &= row
        spread = bits
        length = 1
        while 2 * length <= LONG_FIRST:
            spread |= spread << length
            length *= 2
        if length < LONG_FIRST:
            spread |= spread << (LONG_FIRST - length)
        active = vertical & spread
        while active:
            bit = active & -active
            active -= bit
            c = bit.bit_length() - 1
            low = max(0, c - LONG_FIRST + 1)
            possible = bits & (((1 << (c + 1)) - 1) ^ ((1 << low) - 1))
            start = (possible & -possible).bit_length() - 1
            q = start + (start == c)
            if q not in cols:
                cols[q] = int("".join(row[q] for row in grid)[::-1], 2)
            row = r + ((cols[q] >> r) & ((1 << LONG_FIRST) - 1)).bit_length() - 1
            anchors.add((row, c))
    for r, c in anchors:
        answer += count_anchor(grid, r, c, LONG_FIRST, bound)
    return answer


def count_nested(grid, k):
    # In a mixed square, equal shortest rows precede exactly k longer rows.
    # Their number cannot exceed the gap to the next distinct prefix length.
    m = len(grid[0])
    lengths = []
    for row in grid:
        length = row.find("0")
        if length < 0:
            length = m
        elif "1" in row[length:]:
            return None
        lengths.append(length)
    if all(a >= b for a, b in zip(lengths, lengths[1:])):
        lengths.reverse()
    elif any(a > b for a, b in zip(lengths, lengths[1:])):
        return None
    n = len(lengths)
    answer = sum(max(0, value - k + 1) for value in lengths[:n - k + 1])
    start = 0
    while start < n:
        end = start + 1
        value = lengths[start]
        while end < n and lengths[end] == value:
            end += 1
        if value >= k and end + k <= n:
            answer += min(end - start, lengths[end] - value, m - value)
        start = end
    return answer


def solve(grid, k):
    n, m = len(grid), len(grid[0])
    if k > min(n, m):
        return 0
    if all("0" not in row for row in grid):
        return (n - k + 1) * (m - k + 1)
    nonempty = [r for r, row in enumerate(grid) if "1" in row]
    if not nonempty:
        return 0
    grid = grid[nonempty[0] : nonempty[-1] + 1]
    left = min(row.find("1") for row in grid if "1" in row)
    right = max(row.rfind("1") for row in grid) + 1
    if left or right < m:
        grid = [row[left:right] for row in grid]
    n, m = len(grid), len(grid[0])
    if k > min(n, m):
        return 0
    patterns = set(grid)
    patterns.discard("1" * m)
    if not patterns:
        return (n - k + 1) * (m - k + 1)
    if len(patterns) == 1:
        return count_regular(grid, patterns.pop(), k)
    if len(patterns) <= SMALL_TYPE_LIMIT and "1" * m not in grid:
        components = separate_components(grid, patterns)
        if components is not None:
            return sum(solve(component, k) for component in components)
    nested = count_nested(grid, k)
    if nested is None:
        nested = count_nested([row[::-1] for row in grid], k)
    if nested is not None:
        return nested
    black = [int(row, 2) for row in grid]
    pair_mask = (1 << (m - 1)) - 1
    horizontal = sum(((row ^ (row >> 1)) & pair_mask).bit_count() for row in black)
    vertical = sum((a ^ b).bit_count() for a, b in zip(black, black[1:]))
    # Fewer pattern changes reduce both run extraction and packed certificate work.
    if 2 * (vertical + m * (k + 2)) < horizontal + n * (k + 2):
        return solve(["".join(column) for column in zip(*grid)], k)
    bound, _, extra = mixed_limit(grid, k, True)
    if k > 1 and bound - k > DIRECT_SIZE_LIMIT:
        return count_offline(grid, k)
    if k == 1 and bound >= BAND_MINIMUM:
        return count_single(grid, bound)
    if bound < BAND_MINIMUM or bound == k:
        local_extra = (extra[0], extra[1][0]) if extra is not None else None
        return count_parallel(grid, k, k, bound, local_extra)
    whole = board_bits(grid)
    row_mask = (1 << m) - 1
    row_ones = ((1 << (m * n)) - 1) // row_mask
    first_size = k
    answer = 0
    while first_size <= bound:
        last_size = min(bound, first_size * 2 - 1)
        full = shrink(whole, first_size, 1)
        full &= ((1 << (m - first_size + 1)) - 1) * row_ones
        if not full:
            break
        first = ((full & -full).bit_length() - 1) // m
        last = (full.bit_length() - 1) // m
        top, bottom = max(0, first - last_size + 1), min(n, last + last_size)
        columns = expand(shrink(whole, first_size, m), n, m) & row_mask
        if not columns:
            break
        first = (columns & -columns).bit_length() - 1
        last = columns.bit_length() - 1
        left, right = max(0, first - last_size + 1), min(m, last + last_size)
        if min(bottom - top, right - left) < last_size:
            last_size = min(last_size, bottom - top, right - left)
        if last_size < first_size:
            break
        cropped = [row[left:right] for row in grid[top:bottom]]
        local_extra = None
        if extra is not None:
            crop_mask = (1 << (right - left)) - 1
            rows = [(row >> left) & crop_mask for row in extra[1][0][top:bottom]]
            local_extra = extra[0], rows
        answer += count_parallel(cropped, k, first_size, last_size, local_extra)
        first_size = last_size + 1
    return answer


def main():
    data = sys.stdin.buffer.read().split()
    n, m, k = map(int, data[:HEADER_FIELDS])
    grid = [row.decode("ascii") for row in data[HEADER_FIELDS : HEADER_FIELDS + n]]
    print(solve(grid, k))


if __name__ == "__main__":
    main()
