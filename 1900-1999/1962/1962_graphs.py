import sys


MODULUS = 1000000007


def seating_count(size, requests):
    if size == 2:
        return 1
    neighbors = [[] for _ in range(size)]
    for person, target in enumerate(requests):
        if target not in neighbors[person]:
            neighbors[person].append(target)
            neighbors[target].append(person)
            if len(neighbors[person]) > 2 or len(neighbors[target]) > 2:
                return 0
    visited = [False] * size
    components = paths = 0
    for start in range(size):
        if visited[start]:
            continue
        stack = [start]
        visited[start] = True
        vertices = degrees = 0
        while stack:
            person = stack.pop()
            vertices += 1
            degrees += len(neighbors[person])
            for target in neighbors[person]:
                if not visited[target]:
                    visited[target] = True
                    stack.append(target)
        if degrees == 2 * vertices:
            return 2 if vertices == size else 0
        components += 1
        paths += vertices > 1
    answer = pow(2, paths, MODULUS)
    for factor in range(2, components):
        answer = answer * factor % MODULUS
    return answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    size, count = data[:2]
    requests = [value - 1 for value in data[2 : count + 2]]
    print(seating_count(size, requests))


if __name__ == "__main__":
    main()
