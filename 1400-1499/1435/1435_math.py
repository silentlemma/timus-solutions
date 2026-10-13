import sys

NINE = 9
BASE = 10


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    records = data[1 : 1 + n]
    diff = int(data[1 + n]) - sum(map(int, records))
    if diff == 0:
        print("Input has no error.")
        return
    # swapping digits a (at 10^(i+1)) and b (at 10^i) adds 9 * (b - a) * 10^i
    if diff % NINE == 0:
        step, place = diff // NINE, 0
        while step % BASE == 0:
            step //= BASE
            place += 1
        if abs(step) < BASE:
            for number, rec in enumerate(records, 1):
                digits = rec.decode()
                hi = len(digits) - 2 - place  # index of the digit at 10^(i+1)
                if hi < 0 or int(digits[hi + 1]) - int(digits[hi]) != step:
                    continue
                if hi == 0 and digits[1] == "0":
                    continue  # the swap would make a leading zero
                fixed = digits[:hi] + digits[hi + 1] + digits[hi] + digits[hi + 2 :]
                print("Error in record #%d. Correct number is: %s." % (number, fixed))
                return
    print("Unrecoverable error.")


main()
