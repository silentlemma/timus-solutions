import sys

MAX_FACTOR = 100
LOW_FPS = 10
HIGH_FPS = 60
# 2**11 * 320 * 200 * 10 exceeds the maximum hardware power.
EXACT_OPTIONS = 10


def product_of(counts, present):
    product = 1
    while present:
        bit = present & -present
        factor = bit.bit_length() - 1
        product *= factor ** counts[factor]
        present ^= bit
    return product


def classify(active, product, area, power):
    if active > EXACT_OPTIONS or LOW_FPS * area * product > power:
        return b"Slideshow\n"
    if HIGH_FPS * area * product <= power:
        return b"Perfect\n"
    return b"So-so\n"


def main():
    read = sys.stdin.buffer.readline
    write = sys.stdout.buffer.write
    options = {}
    counts = [0] * (MAX_FACTOR + 1)
    active = int(read())
    for _ in range(active):
        name, text = read().split()
        factor = int(text)
        options[name] = factor
        counts[factor] += 1
    present = sum(1 << factor for factor, count in enumerate(counts) if count)
    product = product_of(counts, present) if active <= EXACT_OPTIONS else 1
    width, height, power = map(int, read().split())
    area = width * height
    write(classify(active, product, area, power))
    for _ in range(int(read())):
        command, argument = read().split(None, 1)
        if command == b"Resolution":
            width, height = map(int, argument.split())
            area = width * height
        else:
            factor = options[argument.rstrip()]
            bit = 1 << factor
            if command == b"On":
                active += 1
                counts[factor] += 1
                present |= bit
                if active <= EXACT_OPTIONS:
                    product *= factor
            else:
                active -= 1
                counts[factor] -= 1
                if counts[factor] == 0:
                    present ^= bit
                if active == EXACT_OPTIONS:
                    product = product_of(counts, present)
                elif active < EXACT_OPTIONS:
                    product //= factor
        write(classify(active, product, area, power))


if __name__ == "__main__":
    main()
