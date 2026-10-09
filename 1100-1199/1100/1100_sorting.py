import sys
from array import array

MOST = 100
# teams written at once, so that the text in memory stays small
CHUNK = 4096


def main():
    data = sys.stdin.buffer
    n = int(data.readline())
    # bubble sort never swaps equal scores, so teams with the same score keep
    # their input order: a counting sort by score does the same
    buckets = [array("i") for _ in range(MOST + 1)]
    for _ in range(n):
        team, solved = data.readline().split()
        buckets[int(solved)].append(int(team))
    out = sys.stdout
    for solved in range(MOST, -1, -1):
        tail = " %d\n" % solved
        bucket = buckets[solved]
        for start in range(0, len(bucket), CHUNK):
            out.write(tail.join(map(str, bucket[start : start + CHUNK])) + tail)


main()
