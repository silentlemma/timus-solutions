from array import array
import sys

OUTPUT_BLOCK = 8192


def popped_coins(operations):
    remaining = operations.count(-1)
    if remaining == 0:
        return
    capacity = remaining
    coins = array("i", [0]) * capacity
    bottom = 0
    size = 0
    for operation in operations:
        if remaining == 0:
            break
        if operation > 0:
            if size == remaining:
                bottom = (bottom + 1) % capacity
                size -= 1
            coins[(bottom + size) % capacity] = operation
            size += 1
        elif operation == -1:
            remaining -= 1
            size -= 1
            yield coins[(bottom + size) % capacity]
        else:
            extra = min(size, remaining - size)
            new_bottom = (bottom - extra) % capacity
            source = (bottom + size - extra) % capacity
            destination = new_bottom
            for _ in range(extra):
                coins[destination] = coins[source]
                source += 1
                destination += 1
                if source == capacity:
                    source = 0
                if destination == capacity:
                    destination = 0
            bottom = new_bottom
            size += extra


def main():
    stream = sys.stdin.buffer
    count = int(stream.readline())
    operations = array("i", (int(stream.readline()) for _ in range(count)))
    block = []
    for coin in popped_coins(operations):
        block.append(str(coin))
        if len(block) == OUTPUT_BLOCK:
            sys.stdout.write("\n".join(block) + "\n")
            block.clear()
    if block:
        sys.stdout.write("\n".join(block) + "\n")


if __name__ == "__main__":
    main()
