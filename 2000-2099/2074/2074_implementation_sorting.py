import sys


def main():
    path = []  # names of the current topic and its ancestors
    topics = {}  # problem -> descriptions of its topics
    current = ""
    for line in sys.stdin.read().split("\n"):
        words = line.split()
        if not words:
            continue
        if words[0].endswith("."):
            # a heading "1.2. name": its depth is the number of dots
            depth = words[0].count(".")
            del path[depth - 1:]
            path.append(" ".join(words[1:]))
            current = ".".join(path)
        else:
            for w in words:
                topics.setdefault(int(w), set()).add(current)
    groups = {}
    for problem, own in topics.items():
        groups.setdefault(", ".join(sorted(own)), []).append(problem)
    lines = sorted(", ".join(map(str, sorted(ps))) + " : " + key for key, ps in groups.items())
    print("\n".join(lines))


main()
