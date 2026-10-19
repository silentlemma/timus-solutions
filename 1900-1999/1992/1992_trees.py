from array import array
import sys


def main():
    read = sys.stdin.buffer.readline
    count, _ = map(int, read().split())
    size = count + 2
    value = array("i", [0]) * size
    previous = array("i", [0]) * size
    learned = array("i", [0]) * size
    redo = array("i", [0]) * size
    used = 0
    entities = 1
    output = bytearray()
    for _ in range(count):
        parts = read().split()
        command = parts[0]
        entity = int(parts[1])
        if command == b"learn":
            used += 1
            value[used] = int(parts[2])
            previous[used] = learned[entity]
            learned[entity] = used
            redo[entity] = 0
        elif command == b"rollback":
            head = learned[entity]
            used += 1
            value[used] = value[head]
            previous[used] = redo[entity]
            learned[entity] = previous[head]
            redo[entity] = used
        elif command == b"relearn":
            head = redo[entity]
            used += 1
            value[used] = value[head]
            previous[used] = learned[entity]
            redo[entity] = previous[head]
            learned[entity] = used
        elif command == b"clone":
            entities += 1
            learned[entities] = learned[entity]
            redo[entities] = redo[entity]
        else:
            head = learned[entity]
            if head:
                output.extend(str(value[head]).encode())
                output.append(10)
            else:
                output.extend(b"basic\n")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
