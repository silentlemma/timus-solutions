from os import _exit, write

# Only the canonical positive powers one and two have witnesses.
token = open(0, "rb", buffering=0).read().strip().lstrip(b"+0")
answer = b"1 2 3\n" if token == b"1" else b"3 4 5\n" if token == b"2" else b"-1\n"
write(1, answer)
_exit(0)
