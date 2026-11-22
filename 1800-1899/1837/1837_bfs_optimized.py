import sys

CHAMPION = b"Isenbaev"


def main():
    source = sys.stdin.buffer
    teams = int(source.readline())
    mates = {}
    tokens = (word for line in source for word in line.split())
    for _ in range(teams):
        a, b, c = next(tokens), next(tokens), next(tokens)
        mates.setdefault(a, set()).update((b, c))
        mates.setdefault(b, set()).update((a, c))
        mates.setdefault(c, set()).update((a, b))
    distance = {}
    if CHAMPION in mates:
        distance[CHAMPION] = 0
        queue = [CHAMPION]
        for name in queue:
            next_distance = distance[name] + 1
            for mate in mates[name]:
                if mate not in distance:
                    distance[mate] = next_distance
                    queue.append(mate)
    output = []
    for name in sorted(mates):
        value = distance.get(name)
        text = b"undefined" if value is None else str(value).encode()
        output.append(name + b" " + text)
    sys.stdout.buffer.write(b"\n".join(output) + b"\n")


main()
