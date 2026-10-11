import sys

SPACE = 0x20


def main():
    s1, s2 = sys.stdin.read().split()
    short, long = bytes.fromhex(s1), bytes.fromhex(s2)
    # the long message is a space followed by the short one, so its first
    # byte gives the first key byte, and byte i+1 of the long message hides
    # the same clear byte as byte i of the short one
    key = [long[0] ^ SPACE]
    for e, f in zip(short, long[1:]):
        key.append(f ^ e ^ key[-1])
    print(bytes(key).hex().upper())


main()
