from sys import stdin

read = stdin.buffer.readline
n = int(read())
names = {read().rstrip(b"\r\n") for _ in range(n)}
print(n - len(names))
