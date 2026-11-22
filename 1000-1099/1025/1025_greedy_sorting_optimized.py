from os import _exit, write


def main():
    values = map(int, open(0, "rb", buffering=0).read().split())
    group_count = next(values)
    groups = sorted(values)
    needed = group_count // 2 + 1
    # All group sizes are odd, so sum((s+1)//2)=(sum(s)+needed)//2.
    answer = (sum(groups[:needed]) + needed) // 2
    write(1, (str(answer) + "\n").encode())
    _exit(0)


main()
