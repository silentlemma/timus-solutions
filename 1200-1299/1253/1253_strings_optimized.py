import sys

LIMIT = 1_000_000
CACHE_LIMIT = 4096
ACTIVE = -1
UNVISITED = -2
ZERO = ord("0")


def expand(templates, write):
    pieces = [[]]
    for text in templates:
        literal, *references = text.split(b"*")
        parts = [literal] if literal else []
        for reference in references:
            parts.append(reference[0] - ZERO)
            tail = reference[1:]
            if tail:
                parts.append(tail)
        pieces.append(parts)

    lengths = [UNVISITED] * len(pieces)
    cache = [None] * len(pieces)

    def measure(index):
        known = lengths[index]
        if known == ACTIVE:
            return LIMIT + 1
        if known != UNVISITED:
            return known
        lengths[index] = ACTIVE
        length = 0
        for part in pieces[index]:
            length += len(part) if isinstance(part, bytes) else measure(part)
            if length > LIMIT:
                lengths[index] = LIMIT + 1
                return LIMIT + 1
        lengths[index] = length
        if length <= CACHE_LIMIT:
            cache[index] = b"".join(
                part if isinstance(part, bytes) else cache[part] for part in pieces[index]
            )
        return length

    if measure(1) > LIMIT:
        write(b"#\n")
        return

    def emit(index):
        cached = cache[index]
        if cached is not None:
            if cached:
                write(cached)
            return
        for part in pieces[index]:
            if isinstance(part, bytes):
                write(part)
            else:
                emit(part)

    emit(1)
    write(b"\n")


def main():
    input_stream = sys.stdin.buffer
    count = int(input_stream.readline())
    blocks = input_stream.read().replace(b"\r", b"").split(b"#", count)
    templates = [blocks[0], *(block.removeprefix(b"\n") for block in blocks[1:count])]
    expand(templates, sys.stdout.buffer.write)


if __name__ == "__main__":
    main()
