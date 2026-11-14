from sys import stdin, stdout


MAX_LENGTH = 140
PREFIX_LENGTH = len(b"RT @: ")


def reached(names, ids, audiences, length):
    # The first bucket processing a user gives their shortest possible tweet.
    # Decode followers only if that user can send a message.
    buckets = [0] * (MAX_LENGTH + 1)
    buckets[length] = 1
    sent = 0
    knows = 1
    all_users = (1 << len(names)) - 1
    for length in range(length, MAX_LENGTH + 1):
        waiting = buckets[length] & ~sent
        while waiting:
            sender = waiting & -waiting
            waiting ^= sender
            sent |= sender
            index = sender.bit_length() - 1
            followers = audiences[index].split()
            audience = sum(map(ids.__getitem__, set(followers)))
            knows |= audience
            if knows == all_users:
                return knows
            longer = length + PREFIX_LENGTH + len(names[index])
            if longer <= MAX_LENGTH:
                buckets[longer] |= audience
    return knows


def solve(stream):
    count = int(stream.readline())
    names = []
    audiences = []
    for _ in range(count):
        description = stream.readline().split(None, 2)
        names.append(description[0])
        audiences.append(description[2] if len(description) > 2 else b"")
    length = len(stream.readline().removesuffix(b"\n").removesuffix(b"\r"))
    ids = {name: 1 << index for index, name in enumerate(names)}
    knows = reached(names, ids, audiences, length)
    answer = [str(knows.bit_count()).encode()]
    answer.extend(name for name, mask in ids.items() if knows & mask)
    return b"\n".join(answer) + b"\n"


if __name__ == "__main__":
    stdout.buffer.write(solve(stdin.buffer))
