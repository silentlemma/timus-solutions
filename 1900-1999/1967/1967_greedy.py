import sys


DECIMAL_BASE = 10


def optimal_lengths(bits):
    powers = []
    value = 1
    end = len(bits)
    lengths = []
    while end:
        index = 0
        while True:
            if index == len(powers):
                value *= DECIMAL_BASE
                powers.append(bin(value)[2:])
            threshold = powers[index]
            length = len(threshold)
            if length >= end:
                lengths.append(end)
                lengths.reverse()
                return lengths
            start = end - length
            if bits[start] == '1' and bits[start:end] < threshold:
                lengths.append(length)
                end = start
                break
            index += 1
    lengths.reverse()
    return lengths


def main():
    maximum = int(sys.stdin.buffer.read())
    bits = ''.join(bin(value)[2:] for value in range(1, maximum + 1))
    lengths = optimal_lengths(bits)
    print(len(lengths))
    print(*lengths)


if __name__ == '__main__':
    main()
