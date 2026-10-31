import sys


INPUT_BUFFER = 4096


def numbers():
    # carry only an unfinished token across refills, even when a line is huge.
    pending = b""
    for chunk in iter(lambda: sys.stdin.buffer.read(INPUT_BUFFER), b""):
        data = pending + chunk
        tokens = data.split()
        pending = tokens.pop() if data[-1] > ord(" ") else b""
        for token in tokens:
            yield int(token)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    n, champion_value = next(values), next(values)
    champion = best = current_count = best_count = 0
    for index in range(1, n):
        value = next(values)
        current_count += 1
        if current_count > best_count:
            best_count, best = current_count, champion
        if value < champion_value:
            champion_value, champion, current_count = value, index, 1
    print(best + 1)


main()
