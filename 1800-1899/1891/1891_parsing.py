import re
import sys


def main():
    lines = iter(sys.stdin.read().splitlines())
    functions = {}
    for _ in range(int(next(lines))):
        name, *types = re.findall(r"[A-Za-z]+", next(lines))
        functions[name, tuple(types[:-1])] = types[-1]

    variables, inferred = {}, []
    for number in range(1, int(next(lines)) + 1):
        declared, name, function, *arguments = re.findall(r"[A-Za-z]+", next(lines))
        if name in variables:
            error = "Double declaration"
        elif any(argument not in variables for argument in arguments):
            error = "Unknown variable"
        else:
            parameter_types = tuple(variables[argument] for argument in arguments)
            result = functions.get((function, parameter_types))
            if result is None:
                error = "No such function"
            elif declared != "auto" and declared != result:
                error = "Invalid initialization"
            else:
                variables[name] = result
                if declared == "auto":
                    inferred.append(f"{name} : {result}\n")
                continue
        print(f"Error on line {number}: {error}")
        return
    sys.stdout.write("".join(inferred))


main()
