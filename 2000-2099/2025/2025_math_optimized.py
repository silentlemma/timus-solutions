from sys import stdin

read = stdin.buffer.readline
for _ in range(int(read())):
    count, groups = map(int, read().split())
    small, extra = divmod(count, groups)
    same_group = groups * small * (small - 1) // 2 + extra * small
    print(count * (count - 1) // 2 - same_group)
