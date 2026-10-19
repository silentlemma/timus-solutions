import random
import string
import sys


MAX_STRUCTURES = 240
MAX_DESCRIPTION_LINES = 1000
MAX_HEX_LENGTH = 10000
MAX_OUTPUT_BYTES = 30000
MAX_NAME_LENGTH = 10
INTEGER_BYTES = 4
BYTE_BITS = 8
INTEGER_BITS = INTEGER_BYTES * BYTE_BITS
UINT_MAX = (1 << INTEGER_BITS) - 1
SIGN_BIT = 1 << (INTEGER_BITS - 1)
BYTE_PATTERN = 0x01020304
MAX_SMALL_STRUCTURES = 40
MAX_SMALL_FIELDS = 6
MAX_SMALL_LEAVES = 64
MAX_SMALL_RECORDS = 20
MAX_SMALL_STRING = 24
MAX_INTEGER_RECORDS = 16
MAX_STRING_SAMPLE = 1024
STRING_RECORDS = 4
MIXED_RECORDS = 18
OUTPUT_DEPTH = 32
ARGUMENT_COUNT = 3
MAX_INTEGER_FIELDS = MAX_DESCRIPTION_LINES - 1
MAX_TINY_RECORDS = MAX_HEX_LENGTH // (2 * 2 * INTEGER_BYTES)
ALPHABET = string.ascii_lowercase
EDGE_INTEGERS = (0, 1, SIGN_BIT - 1, SIGN_BIT, UINT_MAX, BYTE_PATTERN)


def structure_name(index, long_name=False):
    result = ""
    if long_name:
        for _ in range(MAX_NAME_LENGTH):
            index, digit = divmod(index, len(ALPHABET))
            result = ALPHABET[digit] + result
        return result
    while True:
        index, digit = divmod(index, len(ALPHABET))
        result = ALPHABET[digit] + result
        if not index:
            break
        index -= 1
    return result


class Case:
    def __init__(self, fields, long_names=False):
        self.fields = fields
        self.names = [structure_name(i, long_names) for i in range(len(fields))]
        assert len(set(self.names)) == len(self.names)
        self.payload = bytearray()
        self.output = ""

    def add(self, index, values):
        payload = bytearray((index + 1).to_bytes(INTEGER_BYTES, "big"))
        lines = []

        def visit(current, content, depth):
            assert len(content) == len(self.fields[current])
            lines.append(" " * depth + self.names[current])
            for field, value in zip(self.fields[current], content):
                prefix = " " * (depth + 1)
                if field == "int":
                    payload.extend(value.to_bytes(INTEGER_BYTES, "big"))
                    lines.append(prefix + "int " + str(value))
                elif field == "string":
                    raw = value.encode("ascii")
                    assert all(letter in ALPHABET for letter in value)
                    payload.extend(len(raw).to_bytes(INTEGER_BYTES, "big"))
                    payload.extend(raw)
                    lines.append(prefix + "string " + value)
                else:
                    visit(field, value, depth + 1)

        visit(index, values, 0)
        output = "\n".join(lines) + "\n"
        if len(self.payload) + len(payload) > MAX_HEX_LENGTH // 2:
            return False
        if len(self.output) + len(output) > MAX_OUTPUT_BYTES:
            return False
        self.payload.extend(payload)
        self.output += output
        return True

    def render(self):
        description = []
        assert 1 <= len(self.fields) <= MAX_STRUCTURES
        for index, fields in enumerate(self.fields):
            assert fields
            description.append("struct " + self.names[index])
            for field in fields:
                if isinstance(field, int):
                    assert 0 <= field < index
                    field = self.names[field]
                description.append(" " + field)
        assert 2 * len(self.fields) <= len(description) <= MAX_DESCRIPTION_LINES
        assert self.payload
        assert len(self.payload) * 2 <= MAX_HEX_LENGTH
        assert len(self.output) <= MAX_OUTPUT_BYTES
        header = f"{len(self.fields)} {len(description)}\n"
        data = self.payload.hex().upper()
        return header + "\n".join(description) + "\n" + data + "\n", self.output


def random_values(fields, index, rng, string_limit=MAX_SMALL_STRING):
    values = []
    for field in fields[index]:
        if field == "int":
            value = rng.choice(EDGE_INTEGERS) if rng.randrange(2) else rng.getrandbits(INTEGER_BITS)
        elif field == "string":
            length = rng.randrange(string_limit + 1)
            value = "".join(rng.choice(ALPHABET) for _ in range(length))
        else:
            value = random_values(fields, field, rng, string_limit)
        values.append(value)
    return values


def small_case(rng):
    fields = []
    leaves = []
    count = rng.randint(1, MAX_SMALL_STRUCTURES)
    for index in range(count):
        current = []
        total = 0
        for _ in range(rng.randint(1, MAX_SMALL_FIELDS)):
            field = rng.choice(("int", "string"))
            cost = 1
            if index and rng.randrange(2):
                candidate = rng.randrange(index)
                if total + leaves[candidate] <= MAX_SMALL_LEAVES:
                    field, cost = candidate, leaves[candidate]
            if total + cost <= MAX_SMALL_LEAVES:
                current.append(field)
                total += cost
        fields.append(current)
        leaves.append(total)
    case = Case(fields, long_names=bool(rng.randrange(2)))
    for _ in range(MAX_SMALL_RECORDS):
        index = rng.randrange(count)
        case.add(index, random_values(fields, index, rng))
    if not case.payload:
        assert case.add(0, random_values(fields, 0, rng))
    return case


def integer_case(rng):
    fields = [["int"] * (len(EDGE_INTEGERS) + 1)]
    case = Case(fields)
    for _ in range(MAX_INTEGER_RECORDS):
        values = list(EDGE_INTEGERS) + [rng.getrandbits(INTEGER_BITS)]
        rng.shuffle(values)
        assert case.add(0, values)
    return case


def string_case(rng):
    fields = [["string", "int", "string", "string", "int", "string"]]
    case = Case(fields)
    for _ in range(STRING_RECORDS):
        length = rng.randint(MAX_STRING_SAMPLE // 2, MAX_STRING_SAMPLE)
        text = "".join(rng.choice(ALPHABET) for _ in range(length))
        values = ["", rng.choice(EDGE_INTEGERS), "a", ALPHABET, UINT_MAX, text]
        case.add(0, values)
    return case


def mixed_case(rng):
    fields = [["int", "string"], [0, 0, "int"], ["string", 1, 0, 1, "string"]]
    fields.append([2, 1, 2])
    case = Case(fields)
    for _ in range(MIXED_RECORDS):
        index = rng.randrange(len(fields))
        case.add(index, random_values(fields, index, rng))
    return case


def schema_limit_case(rng):
    fields = [["int"] for _ in range(MAX_STRUCTURES)]
    remaining = MAX_DESCRIPTION_LINES - 2 * MAX_STRUCTURES
    for index in range(remaining):
        field = "string" if index % 2 else "int"
        fields[index % MAX_STRUCTURES].append(field)
    case = Case(fields, long_names=True)
    for index in reversed(range(MAX_STRUCTURES)):
        assert case.add(index, random_values(fields, index, rng, string_limit=2))
    return case


def depth_case(rng):
    fields = [["int"]] + [[index - 1] for index in range(1, MAX_STRUCTURES)]
    case = Case(fields)
    values = random_values(fields, MAX_STRUCTURES - 1, rng)
    assert case.add(MAX_STRUCTURES - 1, values)
    return case


def hex_limit_case(rng):
    length = MAX_HEX_LENGTH // 2 - 2 * INTEGER_BYTES
    value = "".join(rng.choice(ALPHABET) for _ in range(length))
    case = Case([["string"]])
    assert case.add(0, [value])
    assert len(case.payload) * 2 == MAX_HEX_LENGTH
    return case


def output_limit_case(rng):
    fields = [["int"]] + [[index - 1] for index in range(1, OUTPUT_DEPTH)]
    case = Case(fields)
    while case.add(OUTPUT_DEPTH - 1, random_values(fields, OUTPUT_DEPTH - 1, rng)):
        pass
    while case.add(0, [0]):
        pass
    return case


def wide_case(rng):
    fields = [["int"] * MAX_INTEGER_FIELDS]
    case = Case(fields)
    assert case.add(0, random_values(fields, 0, rng))
    return case


def root_limit_case(rng):
    fields = [["int"]]
    case = Case(fields)
    for _ in range(MAX_TINY_RECORDS):
        assert case.add(0, random_values(fields, 0, rng))
    assert len(case.payload) * 2 == MAX_HEX_LENGTH
    return case


MODES = {
    "1": small_case,
    "2": integer_case,
    "3": string_case,
    "4": mixed_case,
    "5": schema_limit_case,
    "6": depth_case,
    "7": hex_limit_case,
    "8": output_limit_case,
    "9": wide_case,
    "10": root_limit_case,
}


def make_case(mode, seed):
    return MODES[str(mode)](random.Random(seed)).render()


def main():
    if len(sys.argv) != ARGUMENT_COUNT or sys.argv[1] not in MODES:
        raise SystemExit("usage: python gen.py MODE SEED; MODE is 1 through 10")
    data, _ = make_case(sys.argv[1], int(sys.argv[2]))
    sys.stdout.buffer.write(data.encode("ascii"))


if __name__ == "__main__":
    main()
