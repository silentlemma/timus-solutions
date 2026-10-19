"""Generate from seed and mode: 1 valid random, 2 duplicate, 3 unknown
argument, 4 missing overload, 5 wrong initialization, 6 maximal valid,
7 maximal invalid. Modes 6 and 7 include ten arguments and long names."""

import random
import sys

TYPES = ("int", "real", "string")
MAX_COUNT = 100
MAX_ARGUMENTS = 10
MAX_NAME = 20
SMALL_COUNT = 25
FIRST_RANDOM_LINE = 3
NAME_DIGITS = 3
ALPHABET = 26
VALID_MODE = 1
DUPLICATE_MODE = 2
UNKNOWN_MODE = 3
MISSING_MODE = 4
INITIALIZATION_MODE = 5
MAX_VALID_MODE = 6
MAX_INVALID_MODE = 7


def identifier(index, prefix, long_names):
    letters = []
    for _ in range(NAME_DIGITS):
        letters.append(chr(ord("a") + index % ALPHABET))
        index //= ALPHABET
    result = prefix + "".join(reversed(letters))
    return result.ljust(MAX_NAME, "x") if long_names else result


def generate(seed, mode):
    rng = random.Random(seed)
    maximal = mode in (MAX_VALID_MODE, MAX_INVALID_MODE)
    count = MAX_COUNT if maximal else rng.randint(FIRST_RANDOM_LINE + 1, SMALL_COUNT)
    definitions = [("ReadInt", (), "int"), ("ReadReal", (), "real")]
    definitions.append(("ReadString", (), "string"))
    signatures = {(name, arguments) for name, arguments, _ in definitions}
    while len(definitions) < count:
        index = rng.randrange(count)
        name = identifier(index, rng.choice(("F", "f")), maximal)
        arity = MAX_ARGUMENTS if maximal else rng.randint(0, MAX_ARGUMENTS)
        arguments = tuple(rng.choice(TYPES) for _ in range(arity))
        if (name, arguments) in signatures:
            continue
        signatures.add((name, arguments))
        definitions.append((name, arguments, rng.choice(TYPES)))
    variables = {value_type: [] for value_type in TYPES}
    program = []
    for index, (function, _, result) in enumerate(definitions[:FIRST_RANDOM_LINE]):
        variable = identifier(index, "v", maximal)
        program.append(("auto", variable, function, ()))
        variables[result].append(variable)
    while len(program) < count:
        function, types, result = rng.choice(definitions)
        arguments = tuple(rng.choice(variables[value_type]) for value_type in types)
        variable = identifier(len(program), "v", maximal)
        declared = rng.choice(("auto", result))
        program.append((declared, variable, function, arguments))
        variables[result].append(variable)
    if mode != VALID_MODE and mode != MAX_VALID_MODE:
        error_mode = (
            rng.randint(DUPLICATE_MODE, INITIALIZATION_MODE) if maximal else mode
        )
        at = rng.randrange(FIRST_RANDOM_LINE, count)
        declared, variable, function, arguments = program[at]
        if error_mode == DUPLICATE_MODE:
            variable = program[rng.randrange(at)][1]
            function, arguments = "Absent", ("unknown",)
        elif error_mode == UNKNOWN_MODE:
            function, arguments = "Absent", ("unknown",)
        elif error_mode == MISSING_MODE:
            function, arguments = "Absent", (program[0][1],)
        else:
            result = next(value for name, _, value in definitions if name == "ReadInt")
            function, arguments = "ReadInt", ()
            declared = rng.choice([value for value in TYPES if value != result])
        program[at] = (declared, variable, function, arguments)
    return definitions, program


def render(definitions, program):
    lines = [str(len(definitions))]
    lines.extend(
        f"{name}({', '.join(arguments)}) : {result}"
        for name, arguments, result in definitions
    )
    lines.append(str(len(program)))
    lines.extend(
        f"{declared} {variable} = {function}({', '.join(arguments)})"
        for declared, variable, function, arguments in program
    )
    return "\n".join(lines) + "\n"


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode not in range(VALID_MODE, MAX_INVALID_MODE + 1):
        raise ValueError("mode must be from 1 to 7")
    sys.stdout.write(render(*generate(seed, mode)))


if __name__ == "__main__":
    main()
