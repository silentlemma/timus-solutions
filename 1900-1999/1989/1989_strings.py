import sys


def main():
    read = sys.stdin.buffer.readline
    word = bytearray(read().strip())
    size = len(word)
    reverse = bytearray(word[::-1])
    reverse_view = memoryview(reverse)
    answers = []
    for _ in range(int(read())):
        operation, left, right = read().split()
        if operation == b"change":
            position = int(left) - 1
            value = right[0]
            word[position] = value
            reverse[size - 1 - position] = value
        else:
            first = int(left) - 1
            end = int(right)
            half = (end - first) // 2
            reflected = reverse_view[size - end : size - end + half]
            answers.append(b"Yes\n" if word.startswith(reflected, first, first + half) else b"No\n")
    sys.stdout.buffer.write(b"".join(answers))


if __name__ == "__main__":
    main()
