from os import _exit as _finish_process
import sys as _finish_sys
import sys

MEDALS = (b"gold", b"silver", b"bronze")
PER_MEDAL = 4
PRIZE = 5


def main():
    words = iter(sys.stdin.buffer.read().split())
    medal = {}
    for kind in MEDALS:
        for _ in range(PER_MEDAL):
            medal[next(words)] = kind
    best = winners = 0
    for _ in range(int(next(words))):
        right = 0
        for _ in range(int(next(words))):
            team, _, kind = next(words), next(words), next(words)
            right += medal.get(team) == kind
        if right > best:
            best, winners = right, 1
        elif right == best:
            winners += 1
    print(PRIZE * winners)


main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
