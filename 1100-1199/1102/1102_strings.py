import re
import sys

# read backwards the words never start one another, so the reversed line is
# split greedily; the possessive repeat keeps no states to backtrack to
DIALOGUE = re.compile(rb"(?:tuo|tuptuo|notup|ni|tupni|eno)*+")


def main():
    data = sys.stdin.buffer
    n = int(data.readline())
    out = []
    for _ in range(n):
        line = data.readline().rstrip()
        out.append("YES" if DIALOGUE.fullmatch(line[::-1]) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
