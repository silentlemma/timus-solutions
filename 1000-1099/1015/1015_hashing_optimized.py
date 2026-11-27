import os
from array import array
import sys
from itertools import permutations

OUTPUT_CHUNK_LINES = 1024
INPUT_BUFFER_BYTES = 4096

FACES = 6
FACE_BITS = 3
SPACE_BYTE = ord(" ")
# quarter turns around the vertical and the left-right axes: the new face at
# position i is the old face at position TURNS[t][i]
TURNS = ((3, 5, 2, 1, 4, 0), (0, 1, 5, 2, 3, 4))


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > SPACE_BYTE else b""
        yield from parts
    if pending:
        yield pending


def rotations():
    seen, todo = {tuple(range(FACES))}, [tuple(range(FACES))]
    while todo:
        p = todo.pop()
        for turn in TURNS:
            r = tuple(p[i] for i in turn)
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return seen


def packed(faces):
    result = 0
    for face in faces:
        result = (result << FACE_BITS) | face
    return result


def main():
    rots = rotations()
    # all 720 dice, each mapped to the smallest of its rotations
    key = {}
    for die in permutations(range(1, FACES + 1)):
        key[packed(die)] = min(packed(die[i] for i in rotation) for rotation in rots)
    values = map(int, words())
    count = next(values)
    groups = {}
    for index in range(1, count + 1):
        value = 0
        for _ in range(FACES):
            value = (value << FACE_BITS) | next(values)
        canonical = key[value]
        group = groups.get(canonical)
        if group is None:
            group = array("I")
            groups[canonical] = group
        group.append(index)
    # dicts keep the order of first appearance
    write = sys.stdout.write
    write(str(len(groups)) + "\n")
    for group in groups.values():
        separator = ""
        for start in range(0, len(group), OUTPUT_CHUNK_LINES):
            write(separator + " ".join(map(str, group[start : start + OUTPUT_CHUNK_LINES])))
            separator = " "
        write("\n")


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
