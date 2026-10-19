import sys

MODULUS = 1000000007


def distinct_parts(rules, width):
    limit = width - 1
    prefixes = [None] * len(rules)
    suffixes = [None] * len(rules)
    parts = set()

    def visit(vertex):
        if prefixes[vertex] is not None:
            return
        if rules[vertex] is None:
            symbol = bytes([vertex + 1])
            prefixes[vertex] = symbol
            suffixes[vertex] = symbol
            return
        prefix = b""
        suffix = b""
        for child in rules[vertex]:
            visit(child)
            span = suffix + prefixes[child]
            for start in range(len(span) - width + 1):
                parts.add(span[start : start + width])
            prefix = (prefix + prefixes[child])[:limit]
            suffix = (suffix + suffixes[child])[-limit:]
        prefixes[vertex] = prefix
        suffixes[vertex] = suffix

    for vertex in range(len(rules)):
        visit(vertex)
    return len(parts) % MODULUS


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count, width = next(tokens), next(tokens)
    rules = []
    for _ in range(count):
        length = next(tokens)
        rules.append(
            None if length == -1 else [next(tokens) - 1 for _ in range(length)]
        )
    print(distinct_parts(rules, width))


if __name__ == "__main__":
    main()
