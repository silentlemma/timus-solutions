import math
import sys
from array import array


TABLE_LIMIT = 65_536


def solve_logarithms(prime, values, queries, data, factors, table_limit):
    group_order = prime - 1
    gcd = math.gcd
    root = 2
    while any(pow(root, group_order // factor, prime) == 1 for factor, _ in factors):
        root += 1

    def make_table(order):
        generator = pow(root, group_order // order, prime)
        value = 1
        table = {}
        for exponent in range(order):
            table[value] = exponent
            value = value * generator % prime
        return table

    # Coprime components can share a table; their logarithms combine by CRT.
    blocks = []
    splits = []
    for factor, factor_power in sorted(factors, key=lambda item: -item[1]):
        if factor_power <= table_limit:
            for index, order in enumerate(blocks):
                if order * factor_power <= table_limit:
                    blocks[index] *= factor_power
                    break
            else:
                blocks.append(factor_power)
        else:
            low_power = 1
            while low_power * low_power < factor_power:
                low_power *= factor
            high_power = factor_power // low_power
            exponent = group_order // factor_power
            coefficient = exponent * pow(exponent, -1, factor_power)
            inverse = pow(root, group_order - exponent, prime)
            # Removing the low digit leaves an element of the complementary subgroup.
            corrections = array("I", [1]) * low_power
            for index in range(1, low_power):
                corrections[index] = corrections[index - 1] * inverse % prime
            splits.append(
                (
                    exponent,
                    low_power,
                    high_power,
                    make_table(low_power),
                    make_table(high_power),
                    corrections,
                    coefficient,
                )
            )
    tables = []
    for order in blocks:
        exponent = group_order // order
        coefficient = exponent * pow(exponent, -1, order)
        tables.append((exponent, make_table(order), coefficient))
    logarithms = {1: 0}

    def logarithm(value):
        cached = logarithms.get(value)
        if cached is not None:
            return cached
        result = 0
        for exponent, table, coefficient in tables:
            result += table[pow(value, exponent, prime)] * coefficient
        for exponent, low_power, high_power, low, high, corrections, coefficient in splits:
            projected = pow(value, exponent, prime)
            digit = low[pow(projected, high_power, prime)]
            remainder = projected * corrections[digit] % prime
            result += (digit + low_power * high[remainder]) * coefficient
        result %= group_order
        logarithms[value] = result
        return result

    # In exponent coordinates, subgroup indices are gcds and updates are additions.
    count = len(values)
    for index, value in enumerate(values):
        values[index] = logarithm(value)
    size = 1
    while size < count:
        size *= 2
    differences = array("I", [0]) * count
    tree = array("I", [group_order]) * (size * 2)
    for index in range(1, count):
        differences[index] = (values[index] - values[index - 1]) % group_order
        tree[size + index] = gcd(differences[index], group_order)
    for node in range(size - 1, 0, -1):
        tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])
    fenwick = array("I", [0]) * (count + 1)

    def change(position, increment):
        if position > 0:
            difference = (differences[position] + increment) % group_order
            differences[position] = difference
            node = size + position
            updated = gcd(difference, group_order)
            while tree[node] != updated:
                tree[node] = updated
                node //= 2
                if node == 0:
                    break
                updated = gcd(tree[node * 2], tree[node * 2 + 1])
        position += 1
        while position <= count:
            fenwick[position] = (fenwick[position] + increment) % group_order
            position += position & -position

    answers = []
    for _ in range(queries):
        kind = next(data)
        left = next(data) - 1
        right = next(data)
        if kind == 1:
            increment = logarithm(next(data))
            if increment:
                change(left, increment)
                if right < count:
                    change(right, group_order - increment)
            continue
        first = size + left + 1
        last = size + right
        index = group_order
        while first < last and index != 1:
            if first & 1:
                index = gcd(index, tree[first])
                first += 1
            if last & 1:
                last -= 1
                index = gcd(index, tree[last])
            first //= 2
            last //= 2
        if index != 1:
            value = values[left]
            position = left + 1
            while position:
                value += fenwick[position]
                position -= position & -position
            index = gcd(index, value)
        answers.append(str(group_order // index))
    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


def main():
    data = iter(array("I", map(int, sys.stdin.buffer.read().split())))
    prime = next(data)
    count = next(data)
    queries = next(data)
    values = array("I", (next(data) for _ in range(count)))
    group_order = prime - 1
    factors = []
    remaining = group_order
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factor_power = 1
            while remaining % divisor == 0:
                remaining //= divisor
                factor_power *= divisor
            factors.append((divisor, factor_power))
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append((remaining, remaining))

    table_limit = min(TABLE_LIMIT, count + queries)
    smooth = True
    for factor, factor_power in factors:
        low_power = 1
        while low_power * low_power < factor_power:
            low_power *= factor
        if factor_power > table_limit and low_power > table_limit:
            smooth = False
            break
    if smooth and prime > 2:
        solve_logarithms(prime, values, queries, data, factors, table_limit)
        return

    indices = {1: group_order}
    if prime > 2:
        indices[group_order] = group_order // 2

    gcd = math.gcd

    def subgroup_index(value, limit):
        cached = indices.get(value)
        if cached is not None:
            return gcd(cached, limit)
        order = group_order
        initial_limit = limit
        for factor, factor_power in factors:
            if limit % factor:
                continue
            removed = gcd(limit, factor_power)
            projected = pow(value, order // removed, prime)
            while projected != 1:
                removed //= factor
                if removed == 1:
                    break
                if factor == 2:
                    projected = projected * projected % prime
                else:
                    projected = pow(projected, factor, prime)
            order //= removed
        result = group_order // order
        if initial_limit == group_order:
            indices[value] = result
        return result

    size = 1
    while size < count:
        size *= 2
    # Each node caches the gcd of its true index with the tested divisor.
    tree = array("I", [group_order]) * (size * 2)
    tested = array("I", [0]) * (size * 2)
    tested[size] = group_order
    tree[size] = group_order
    for index in range(size + count, size * 2):
        tested[index] = group_order
    differences = array("I", [1]) * count
    prefixes = array("I", [1]) * count
    for index in range(1, count):
        prefixes[index] = prefixes[index - 1] * values[index - 1] % prime
    # Recover all adjacent ratios using one inverse of the prefix product.
    inverse = pow(prefixes[-1], prime - 2, prime)
    for index in range(count - 1, 0, -1):
        differences[index] = values[index] * inverse * prefixes[index - 1] % prime
        inverse = inverse * values[index - 1] % prime
    del prefixes
    fenwick = array("I", [1]) * (count + 1)

    def resolve(node, limit):
        previous_limit = tested[node]
        if previous_limit and previous_limit % limit == 0:
            return gcd(tree[node], limit)
        if node >= size:
            known = subgroup_index(differences[node - size], limit)
        else:
            known = resolve(node * 2, limit)
            if known != 1:
                known = resolve(node * 2 + 1, known)
        if previous_limit:
            # Merge compatible projections so later queries retain all tested factors.
            tested[node] = previous_limit // gcd(previous_limit, limit) * limit
            tree[node] = tree[node] // gcd(tree[node], known) * known
        else:
            tested[node] = limit
            tree[node] = known
        return known

    def change(position, multiplier):
        # Only boundaries change in the multiplicative difference array.
        if position > 0:
            differences[position] = differences[position] * multiplier % prime
            node = size + position
            while node:
                tested[node] = 0
                node //= 2
        position += 1
        while position <= count:
            fenwick[position] = fenwick[position] * multiplier % prime
            position += position & -position

    answers = []
    for _ in range(queries):
        kind = next(data)
        left = next(data) - 1
        right = next(data)
        if kind == 1:
            multiplier = next(data)
            if multiplier == 1:
                continue
            change(left, multiplier)
            if right < count:
                change(right, pow(multiplier, prime - 2, prime))
            continue

        first = size + left + 1
        last = size + right
        index = group_order
        while first < last and index != 1:
            if first & 1:
                index = resolve(first, index)
                first += 1
            if last & 1:
                last -= 1
                if index != 1:
                    index = resolve(last, index)
            first //= 2
            last //= 2
        if index == 1:
            answers.append(str(group_order))
            continue

        value = values[left]
        position = left + 1
        while position:
            value = value * fenwick[position] % prime
            position -= position & -position
        answers.append(str(group_order // subgroup_index(value, index)))
    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
