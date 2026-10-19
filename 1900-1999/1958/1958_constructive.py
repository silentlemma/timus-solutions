import sys


OUTPUT_BLOCK = 4096


def sort_operations(permutation):
    values = permutation[:]
    size = len(values)
    operations = []

    def flush():
        while values[-1] != size:
            value = values[-1]
            values[-1], values[value - 1] = values[value - 1], value
            operations.append(value)

    flush()
    unfixed = size - 1
    while unfixed > 0:
        while unfixed > 0 and values[unfixed - 1] == unfixed:
            unfixed -= 1
        if unfixed == 0:
            break
        start = values.index(1)
        for position in range(start, size - 1):
            values[position], values[position + 1] = values[position + 1], 1
            operations.append(1)
        flush()
    return operations


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    size = data[0]
    operations = sort_operations(data[1 : size + 1])
    write = sys.stdout.write
    write(str(len(operations)) + "\n")
    for begin in range(0, len(operations), OUTPUT_BLOCK):
        write("\n".join(map(str, operations[begin : begin + OUTPUT_BLOCK])) + "\n")


if __name__ == "__main__":
    main()
