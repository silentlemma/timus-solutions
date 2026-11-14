import sys


SEPARATORS = bytes.maketrans(b"(),:=", b"     ")


def main():
    lines = iter(sys.stdin.buffer)
    functions = {}
    for _ in range(int(next(lines))):
        tokens = next(lines).translate(SEPARATORS).split()
        functions[tuple(tokens[:-1])] = tokens[-1]

    variables = {}
    inferred = []
    for number in range(1, int(next(lines)) + 1):
        declared, name, function, *arguments = next(lines).translate(SEPARATORS).split()
        if name in variables:
            error = "Double declaration"
        else:
            try:
                signature = (function, *map(variables.__getitem__, arguments))
            except KeyError:
                error = "Unknown variable"
            else:
                result = functions.get(signature)
                if result is None:
                    error = "No such function"
                elif declared != b"auto" and declared != result:
                    error = "Invalid initialization"
                else:
                    variables[name] = result
                    if declared == b"auto":
                        inferred.append(b"%s : %s\n" % (name, result))
                    continue
        print(f"Error on line {number}: {error}")
        return
    sys.stdout.buffer.write(b"".join(inferred))


main()
