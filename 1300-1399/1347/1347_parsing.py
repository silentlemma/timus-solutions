import re
import sys

FRIEND = re.compile(rb"<friend>(.*?)</friend>", re.S)
TAG = re.compile(rb"<[^>]*>")


def main():
    lines = sys.stdin.buffer.read().split(b"\n")
    n = int(lines[0])
    pos, blogs = 1, []
    for _ in range(n):
        while not lines[pos].strip():
            pos += 1
        name = lines[pos].strip()
        start = pos + 1
        pos = start
        while b"</blog>" not in lines[pos]:
            pos += 1
        text = b"\n".join(lines[start : pos + 1])
        pos += 1
        # the name inside a friend tag, without other tags or spaces
        friends = {TAG.sub(b"", m).strip() for m in FRIEND.findall(text)}
        friends.discard(name)
        friends.discard(b"")
        blogs.append((name, friends))
    out = []
    for name, friends in blogs:
        readers = {other for other, theirs in blogs if other != name and name in theirs}
        if out:
            out.append(b"")
        out.append(name)
        for number, group in enumerate((friends, readers, friends & readers), 1):
            out.append(b"%d: " % number + b", ".join(sorted(group)))
    sys.stdout.buffer.write(b"\n".join(out) + b"\n")


main()
