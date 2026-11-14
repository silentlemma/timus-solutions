from array import array
import sys


def states(text):
    state = array("I", [0]) * (len(text) + 1)
    current = 0
    case_bit = ord("a") ^ ord("A")
    for position, letter in enumerate(text, 1):
        # An opener's parent is the state immediately before that opener.
        if letter >= ord("a") and current and text[current - 1] == letter ^ case_bit:
            current = state[current - 1]
        else:
            current = position
        state[position] = current
    return state


def main():
    source = sys.stdin.buffer
    state = states(source.readline().strip())
    count = int(source.readline())
    answers = bytearray(count + 1)
    tokens = (token for line in source for token in line.split())
    for index in range(count):
        left, right = int(next(tokens)), int(next(tokens))
        answers[index] = ord("0") + (state[left - 1] == state[right])
    answers[count] = ord("\n")
    sys.stdout.buffer.write(answers)


if __name__ == "__main__":
    main()
