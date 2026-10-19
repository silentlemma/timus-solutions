import sys


OPERATION_LIMIT = 1000000
SIZE_LIMIT = 500


def check(input_text, output_text):
    data = list(map(int, input_text.split()))
    if not data or not 1 <= data[0] <= SIZE_LIMIT:
        return False, "invalid input size"
    size = data[0]
    values = data[1:]
    if sorted(values) != list(range(1, size + 1)):
        return False, "invalid input permutation"
    words = output_text.split()
    if not words or words[0] == "Impossible":
        return False, "every input permutation is sortable"
    count = int(words[0])
    if not 0 <= count <= OPERATION_LIMIT or len(words) != count + 1:
        return False, "operation count mismatch or limit exceeded"
    positions = [0] * (size + 1)
    for index, value in enumerate(values):
        positions[value] = index
    for word in words[1:]:
        value = int(word)
        if not 1 <= value <= size:
            return False, "operation argument outside range"
        start = positions[value]
        target = (start + value) % size
        other = values[target]
        values[start], values[target] = other, value
        positions[value] = target
        positions[other] = start
    if values != list(range(1, size + 1)):
        return False, "result is not sorted"
    return True, "valid sorting sequence"


def main():
    try:
        with open(sys.argv[1], encoding="utf-8") as stream:
            input_text = stream.read()
        with open(sys.argv[3], encoding="utf-8") as stream:
            output_text = stream.read()
        okay, message = check(input_text, output_text)
    except (OSError, ValueError, IndexError) as error:
        okay, message = False, str(error)
    print(message)
    return 0 if okay else 1


if __name__ == "__main__":
    sys.exit(main())
