from array import array
from os import urandom
from sys import stdin, stdout


MOD_ONE = 1_000_000_007
MOD_TWO = 1_000_000_009
MIN_BASE = 257
BASE_MARGIN = 512
FIELDS = 4
ALPHABET_SIZE = 256
OUTPUT_BATCH = 8192
SEED_WORD_BYTES = 4
SEED_BYTES = 2 * SEED_WORD_BYTES
REVERSE_TWO = 3
SMALL_QUERY = 3
DECIMAL = 10
SPACE = ord(" ")
ZERO = ord("0")
NINE = ord("9")
CHANGE = ord("c")


def main():
    read = stdin.buffer.readline
    word = bytearray(read().strip())
    size = len(word)
    query_count = int(read())
    commands = stdin.buffer.read()
    cursor = 0
    seed = urandom(SEED_BYTES)
    base_one = int.from_bytes(seed[:SEED_WORD_BYTES], "little") % (MOD_ONE - BASE_MARGIN) + MIN_BASE
    base_two = int.from_bytes(seed[SEED_WORD_BYTES:], "little") % (MOD_TWO - BASE_MARGIN) + MIN_BASE
    powers_one = array("I", [1]) * size
    powers_two = array("I", [1]) * size
    for i in range(1, size):
        powers_one[i] = powers_one[i - 1] * base_one % MOD_ONE
        powers_two[i] = powers_two[i - 1] * base_two % MOD_TWO

    # Each node stores forward/reverse sums for two independently based fields.
    tree = array("I", [0]) * (FIELDS * (size + 1))
    counts = [0] * ALPHABET_SIZE
    for i, value in enumerate(word):
        at = (i + 1) * FIELDS
        tree[at] = value * powers_one[i] % MOD_ONE
        tree[at + 1] = value * powers_one[size - 1 - i] % MOD_ONE
        tree[at + 2] = value * powers_two[i] % MOD_TWO
        tree[at + REVERSE_TWO] = value * powers_two[size - 1 - i] % MOD_TWO
        counts[value] += 1
    for i in range(1, size + 1):
        parent = i + (i & -i)
        if parent <= size:
            at, target = i * FIELDS, parent * FIELDS
            tree[target] = (tree[target] + tree[at]) % MOD_ONE
            tree[target + 1] = (tree[target + 1] + tree[at + 1]) % MOD_ONE
            tree[target + 2] = (tree[target + 2] + tree[at + 2]) % MOD_TWO
            tree[target + REVERSE_TWO] = (
                tree[target + REVERSE_TWO] + tree[at + REVERSE_TWO]
            ) % MOD_TWO
    types = sum(count > 0 for count in counts)

    # PyPy can trace this byte parser without allocating split tokens.
    def number():
        nonlocal cursor
        while commands[cursor] <= SPACE:
            cursor += 1
        value = 0
        while cursor < len(commands) and ZERO <= commands[cursor] <= NINE:
            value = value * DECIMAL + commands[cursor] - ZERO
            cursor += 1
        return value

    def prefix(index):
        forward_one = reverse_one = forward_two = reverse_two = 0
        while index:
            at = index * FIELDS
            forward_one += tree[at]
            reverse_one += tree[at + 1]
            forward_two += tree[at + 2]
            reverse_two += tree[at + REVERSE_TWO]
            index &= index - 1
        return forward_one, reverse_one, forward_two, reverse_two

    output = []
    append = output.append
    write = stdout.buffer.write
    for _ in range(query_count):
        while commands[cursor] <= SPACE:
            cursor += 1
        operation = commands[cursor]
        while commands[cursor] > SPACE:
            cursor += 1
        first = number() - 1
        if operation == CHANGE:
            while commands[cursor] <= SPACE:
                cursor += 1
            value = commands[cursor]
            cursor += 1
            old = word[first]
            if old == value:
                continue
            word[first] = value
            counts[old] -= 1
            if counts[old] == 0:
                types -= 1
            if counts[value] == 0:
                types += 1
            counts[value] += 1
            difference = value - old
            delta_one = difference * powers_one[first]
            delta_reverse_one = difference * powers_one[size - 1 - first]
            delta_two = difference * powers_two[first]
            delta_reverse_two = difference * powers_two[size - 1 - first]
            index = first + 1
            while index <= size:
                at = index * FIELDS
                tree[at] = (tree[at] + delta_one) % MOD_ONE
                tree[at + 1] = (tree[at + 1] + delta_reverse_one) % MOD_ONE
                tree[at + 2] = (tree[at + 2] + delta_two) % MOD_TWO
                tree[at + REVERSE_TWO] = (tree[at + REVERSE_TWO] + delta_reverse_two) % MOD_TWO
                index += index & -index
            continue

        end = number()
        if types == 1:
            palindrome = True
        else:
            if end - first <= SMALL_QUERY:
                palindrome = word[first] == word[end - 1]
            else:
                a, b, c, d = prefix(end)
                e, f, g, h = prefix(first)
                # Shift both polynomial intervals to the same exponent range.
                palindrome = (a - e) * powers_one[size - end] % MOD_ONE == (b - f) * powers_one[
                    first
                ] % MOD_ONE and (c - g) * powers_two[size - end] % MOD_TWO == (d - h) * powers_two[
                    first
                ] % MOD_TWO
        append(b"Yes" if palindrome else b"No")
        if len(output) == OUTPUT_BATCH:
            write(b"\n".join(output) + b"\n")
            output.clear()
    if output:
        write(b"\n".join(output) + b"\n")


main()
