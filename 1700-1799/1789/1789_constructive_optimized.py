from sys import stdin, stdout

FIRST = 2
n = int(stdin.read())
if n == FIRST:
    stdout.write("2\n1 1\n")
else:
    # Two parity-catching sweeps, streamed instead of retaining both lists.
    stdout.write(str(2 * (n - FIRST)) + "\n")
    for label in range(FIRST, n):
        stdout.write(str(label) + " ")
    for label in range(n - 1, FIRST - 1, -1):
        stdout.write(str(label) + " ")
    stdout.write("\n")
