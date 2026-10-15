import sys

FAILED = "I HAVE FAILED!!!"


def prefix_function(t):
    p = [0] * len(t)
    k = 0
    for i in range(1, len(t)):
        while k and t[i] != t[k]:
            k = p[k - 1]
        if t[i] == t[k]:
            k += 1
        p[i] = k
    return p


def find(s, start, t, p):
    # the first occurrence of t in s at or after start, or -1
    k = 0
    for i in range(start, len(s)):
        while k and s[i] != t[k]:
            k = p[k - 1]
        if s[i] == t[k]:
            k += 1
            if k == len(t):
                return i - k + 1
    return -1


def main():
    lines = sys.stdin.read().split("\n")
    source = lines[0].rstrip("\r")
    target = lines[1].rstrip("\r").split(" ")
    out = list(source)
    keep = [False] * len(source)
    j = 0
    p = prefix_function(target[0])
    offset = 0
    # each wanted word goes to its earliest place in the current word,
    # at least one erased letter after the previous one there; if it does
    # not fit, the next word of the source is tried
    for word in source.split(" "):
        pos = 0
        while j < len(target) and len(word) - pos >= len(target[j]):
            at = find(word, pos, target[j], p)
            if at < 0:
                break
            for i in range(at, at + len(target[j])):
                keep[offset + i] = True
            pos = at + len(target[j]) + 1
            j += 1
            if j < len(target):
                p = prefix_function(target[j])
        offset += len(word) + 1
    if j < len(target):
        print(FAILED)
        return
    for i, c in enumerate(source):
        if c != " " and not keep[i]:
            out[i] = "_"
    print("".join(out))


main()
