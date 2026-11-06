# Contests played by players 0 to 13, counted from the story.
ANSWERS = (
    b"5\n",
    b"21\n",
    b"12\n",
    b"2\n",
    b"1\n",
    b"4\n",
    b"6\n",
    b"1\n",
    b"4\n",
    b"4\n",
    b"1\n",
    b"0\n",
    b"1\n",
    b"1\n",
)

with open(0, "rb", buffering=0, closefd=False) as stdin:
    player = int(stdin.read())
with open(1, "wb", buffering=0, closefd=False) as stdout:
    stdout.write(ANSWERS[player])
