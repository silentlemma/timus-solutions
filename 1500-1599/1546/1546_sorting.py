import sys

NUMBER, LETTER = 1, 2  # numbers come before letters


def key(s):
    """Letters and numbers by value first; then, run by run, more leading
    zeros first."""
    main, zeros = [], []
    i = 0
    while i < len(s):
        if not s[i].isdigit():
            main.append((LETTER, s[i]))
            i += 1
            continue
        start = i
        while i < len(s) and s[i] == "0":
            i += 1
        digits = i
        while i < len(s) and s[i].isdigit():
            i += 1
        # equal lengths compare digit by digit, so huge numbers are fine
        main.append((NUMBER, i - digits, s[digits:i]))
        zeros.append(start - digits)
    return main, zeros


def main():
    lines = sys.stdin.read().split()
    lines.sort(key=key)
    sys.stdout.write("".join(s + "\n" for s in lines))


main()
