import sys
from math import gcd


BLOCK_SIZE = 2048
BLOCK_GROWTH = 4
GROWTH_THRESHOLD = 1000
MINIMUM_MERGE = 3
MAXIMUM_GROWTH_BLOCKS = 100000
MINIMUM_PREFIX = 28
MAXIMUM_SUFFIX = 32
BYTE_BITS = 8
BYTE_MASK = (1 << BYTE_BITS) - 1


def count_with_prefix(weights, target, prefix):
    matrices = []
    for byte in range(1 << BYTE_BITS):
        first, second, third, fourth = 1, 0, 0, 1
        for shift in range(BYTE_BITS - 1, -1, -1):
            if byte >> shift & 1:
                first, second = first + third, second + fourth
            else:
                third, fourth = first + third, second + fourth
        matrices.append((first, second, third, fourth))

    sums = []
    total = 0
    for weight in weights:
        total += weight
        sums.append(total)
    unit = weights[0]
    limit = 1 << prefix
    first_shift = prefix // BYTE_BITS * BYTE_BITS

    # A doubled prefix has the hyperbinary counts given by Stern's sequence.
    def prefix_count(residual):
        if residual % unit:
            return 0
        value = limit - residual // unit
        if value & (value - 1) == 0:
            return 1
        shift = first_shift
        _, low, _, high = matrices[value >> shift]
        shift -= BYTE_BITS
        while shift >= 0:
            first, second, third, fourth = matrices[value >> shift & BYTE_MASK]
            low, high = first * low + second * high, third * low + fourth * high
            shift -= BYTE_BITS
        return low

    def visit(index, residual):
        while index >= prefix:
            if residual == 0:
                return 1
            bound = sums[index - 1]
            other = abs(residual - weights[index])
            first = residual <= bound
            second = other <= bound
            index -= 1
            if first and second:
                return visit(index, residual) + visit(index, other)
            if second:
                residual = other
            elif not first:
                return 0
        return prefix_count(residual)

    return visit(len(weights) - 1, abs(target - total))


def count_ways(weights, target):
    total = sum(weights)
    if target > 2 * total:
        return 0
    if target == 0 or target == 2 * total:
        return 1

    divisor = 0
    for weight in weights:
        divisor = gcd(divisor, weight)
    if target % divisor:
        return 0
    weights = [weight // divisor for weight in weights]
    target //= divisor
    total //= divisor

    prefix = 1
    while prefix < len(weights) and weights[prefix] == 2 * weights[prefix - 1]:
        prefix += 1
    if prefix >= MINIMUM_PREFIX and len(weights) - prefix <= MAXIMUM_SUFFIX:
        return count_with_prefix(weights, target, prefix)

    block = BLOCK_SIZE
    index, offset = divmod(target, block)
    states = {index: (1 << offset,)}
    growth_allowed = True

    for weight in reversed(weights):
        total -= weight
        last, tail = divmod(2 * total, block)
        following = {}
        get = following.get

        # A tuple stores binary bit planes of the counts in one block.
        def add(index, value):
            old = get(index)
            if old is None:
                following[index] = value
                return
            if len(old) == 1 and len(value) == 1:
                before = old[0]
                after = value[0]
                carry = before & after
                following[index] = (before ^ after, carry) if carry else (before | after,)
                return
            result = list(old)
            if len(result) < len(value):
                result.extend([0] * (len(value) - len(result)))
            for plane, carry in enumerate(value):
                while carry:
                    if plane == len(result):
                        result.append(carry)
                        break
                    before = result[plane]
                    result[plane] = before ^ carry
                    carry &= before
                    plane += 1
            following[index] = tuple(result)

        shifts = []
        for digit in (1, 2):
            whole, offset = divmod(digit * weight, block)
            shifts.append((whole, offset, (1 << offset) - 1, block - offset))

        # Release old blocks as their three possible transitions are processed.
        while states:
            index, planes = states.popitem()
            if index <= last:
                add(index, planes)
            for whole, offset, low_mask, high_shift in shifts:
                destination = index - whole
                if offset:
                    if 0 <= destination <= last:
                        if len(planes) == 1:
                            value = planes[0] >> offset
                            if value:
                                add(destination, (value,))
                        else:
                            value = tuple(plane >> offset for plane in planes)
                            while value and not value[-1]:
                                value = value[:-1]
                            if value:
                                add(destination, value)
                    destination -= 1
                    if 0 <= destination <= last:
                        if len(planes) == 1:
                            value = (planes[0] & low_mask) << high_shift
                            if value:
                                add(destination, (value,))
                        else:
                            value = tuple((plane & low_mask) << high_shift for plane in planes)
                            while value and not value[-1]:
                                value = value[:-1]
                            if value:
                                add(destination, value)
                elif 0 <= destination <= last:
                    add(destination, planes)

        if last in following:
            mask = (1 << (tail + 1)) - 1
            value = tuple(plane & mask for plane in following[last])
            while value and not value[-1]:
                value = value[:-1]
            if value:
                following[last] = value
            else:
                del following[last]
        states = following
        if not states:
            return 0

        if len(states) > MAXIMUM_GROWTH_BLOCKS:
            growth_allowed = False
        if growth_allowed and block == BLOCK_SIZE and len(states) > GROWTH_THRESHOLD:
            groups = {index // BLOCK_GROWTH for index in states}
            if len(groups) * MINIMUM_MERGE < len(states):
                following = {}
                get = following.get
                while states:
                    index, planes = states.popitem()
                    destination, offset = divmod(index, BLOCK_GROWTH)
                    shift = offset * block
                    old = get(destination)
                    if old is None:
                        following[destination] = tuple(plane << shift for plane in planes)
                    else:
                        result = list(old)
                        if len(result) < len(planes):
                            result.extend([0] * (len(planes) - len(result)))
                        for plane, value in enumerate(planes):
                            result[plane] |= value << shift
                        following[destination] = tuple(result)
                states = following
                block *= BLOCK_GROWTH

    return sum((plane & 1) << index for index, plane in enumerate(states.get(0, ())))


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    count, target = data[:2]
    print(count_ways(data[2 : count + 2], target))


if __name__ == "__main__":
    main()
