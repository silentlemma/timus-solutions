from array import array

INPUT_BLOCK_SIZE = 8192
ASCII_SPACE = ord(" ")
ASCII_ZERO = ord("0")


def integers():
    source = open(0, "rb")
    value = 0
    started = False
    for block in iter(lambda: source.read(INPUT_BLOCK_SIZE), b""):
        for byte in block:
            if byte > ASCII_SPACE:
                value = value * 10 + byte - ASCII_ZERO
                started = True
            elif started:
                yield value
                value = 0
                started = False
    if started:
        yield value


values = integers()
n = next(values)
votes = array("I", [0]) * n
for student in range(n):
    start = student - next(values) + 1
    if start < 0:
        start += n
    votes[start] += 1
print(max(range(n), key=votes.__getitem__) + 1)
