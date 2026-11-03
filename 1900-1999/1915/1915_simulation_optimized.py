OUTPUT_BLOCK = 8192

reader = open(0, "rb", closefd=False)
operations = [int(reader.readline()) for _ in range(int(reader.readline()))]
remaining = operations.count(-1)
capacity = remaining
coins = [0] * capacity
bottom = 0
size = 0
block = []
writer = open(1, "wb", closefd=False)
for operation in operations:
    if remaining == 0:
        break
    if operation > 0:
        if size == remaining:
            bottom += 1
            if bottom == capacity:
                bottom = 0
            size -= 1
        index = bottom + size
        if index >= capacity:
            index -= capacity
        coins[index] = operation
        size += 1
    elif operation == -1:
        remaining -= 1
        size -= 1
        index = bottom + size
        if index >= capacity:
            index -= capacity
        block.append(str(coins[index]))
        if len(block) == OUTPUT_BLOCK:
            writer.write(("\n".join(block) + "\n").encode("ascii"))
            block.clear()
    else:
        extra = min(size, remaining - size)
        if extra:
            # Prepend only the suffix that future removals could expose.
            new_bottom = bottom - extra
            if new_bottom < 0:
                new_bottom += capacity
            source = bottom + size - extra
            if source >= capacity:
                source -= capacity
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
if block:
    writer.write(("\n".join(block) + "\n").encode("ascii"))
writer.flush()
