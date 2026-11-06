from array import array
from sys import stdin, stdout

read = stdin.buffer
size = int(read.readline())
first = array("H", [0]) * size
first[0] = 1
values = array("H")
remainder = 0
for line in read:
    for token in line.split():
        value = int(token)
        values.append(value)
        remainder = (remainder + value) % size
        start = first[remainder]
        if start:
            answer = values[start - 1 :]
            stdout.write(f"{len(answer)}\n")
            stdout.write("\n".join(map(str, answer)) + "\n")
            raise SystemExit
        first[remainder] = len(values) + 1
