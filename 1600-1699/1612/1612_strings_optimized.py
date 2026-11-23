from os import _exit as _finish_process
import sys as _finish_sys
import sys


def main():
    table = bytes(value if ord("a") <= value <= ord("z") else ord(" ") for value in range(256))
    words = sys.stdin.buffer.read().translate(table).split()
    trams, trolleys = words.count(b"tram"), words.count(b"trolleybus")
    if trams > trolleys:
        print("Tram driver")
    elif trolleys > trams:
        print("Trolleybus driver")
    else:
        print("Bus driver")


main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
