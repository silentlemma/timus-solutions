import sys


def main():
    size, budget, drum = sys.stdin.buffer.read().split()
    size, budget = int(size), int(budget)
    pattern = bytearray(size // 2)
    for period in range(1, len(pattern) + 1):
        if size % period:
            continue
        changes = 0
        copies = size // period
        for residue in range(period):
            part = drum[residue::period]
            if part[0] == part[-1] and part.count(part[0]) == copies:
                letter, kept = part[0], copies
            else:
                count = part.count
                letter = max(set(part), key=count)
                kept = count(letter)
            changes += copies - kept
            if changes > budget:
                break
            pattern[residue] = letter
        else:
            output = sys.stdout.buffer
            output.write(str(period).encode() + b"\n")
            output.write(pattern[:period] * copies + b"\n")
            return
    sys.stdout.buffer.write(str(size).encode() + b"\n" + drum + b"\n")


if __name__ == "__main__":
    main()
