import sys


def build_path(start, finish, free):
    answer = []

    def visit(first, last, dimensions):
        if dimensions & (dimensions - 1) == 0:
            answer.append(first)
            if last != first:
                answer.append(last)
            return
        difference = first ^ last
        split = difference & -difference
        remaining = dimensions ^ split
        bridge = remaining & -remaining
        if first ^ bridge ^ split == last and remaining != bridge:
            choices = remaining ^ bridge
            bridge = choices & -choices
        middle = first ^ bridge
        visit(first, middle, remaining)
        visit(middle ^ split, last, remaining)

    visit(start, finish, free)
    return answer


def configuration(mask):
    enabled = []
    while mask:
        bit = mask & -mask
        enabled.append(str(bit.bit_length()))
        mask ^= bit
    return str(len(enabled)) + (' ' + ' '.join(enabled) if enabled else '')


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    dimensions = next(tokens)
    start = sum(1 << (next(tokens) - 1) for _ in range(next(tokens)))
    finish = sum(1 << (next(tokens) - 1) for _ in range(next(tokens)))
    path = build_path(start, finish, (1 << dimensions) - 1)
    sys.stdout.write(str(len(path)) + '\n' + '\n'.join(map(configuration, path)) + '\n')


if __name__ == '__main__':
    main()
