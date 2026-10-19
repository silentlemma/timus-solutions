import sys


WORD_BYTES = 4
INTEGER = -1
STRING = -2


def main():
    source = sys.stdin.buffer
    _, line_count = map(int, source.readline().split())
    names = []
    fields = []
    type_ids = {b"int": INTEGER, b"string": STRING}
    for _ in range(line_count):
        tokens = source.readline().split()
        if tokens[0] == b"struct":
            name = tokens[1]
            type_ids[name] = len(names)
            names.append(name)
            fields.append([])
        else:
            fields[-1].append(type_ids[tokens[0]])

    data = bytes.fromhex(source.readline().decode("ascii"))
    position = 0

    def read_number():
        nonlocal position
        value = int.from_bytes(data[position : position + WORD_BYTES], "big")
        position += WORD_BYTES
        return value

    output = []
    while position < len(data):
        root = read_number() - 1
        output.append(names[root])
        stack = [(root, 0)]
        while stack:
            structure, next_field = stack[-1]
            if next_field == len(fields[structure]):
                stack.pop()
                continue
            field = fields[structure][next_field]
            stack[-1] = (structure, next_field + 1)
            indent = b" " * len(stack)
            if field == INTEGER:
                output.append(indent + b"int " + str(read_number()).encode("ascii"))
            elif field == STRING:
                length = read_number()
                output.append(indent + b"string " + data[position : position + length])
                position += length
            else:
                output.append(indent + names[field])
                stack.append((field, 0))

    sys.stdout.buffer.write(b"\n".join(output) + b"\n")


if __name__ == "__main__":
    main()
