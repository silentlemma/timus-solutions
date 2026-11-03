import sys
from array import array

CUT = 1 << 31


def main():
    word = sys.stdin.buffer.readline().strip()
    text = sys.stdin.buffer.readline().strip()
    size = len(word)
    prefix = array("I", [0]) * size
    for i in range(1, size):
        k = prefix[i - 1]
        while k and word[k] != word[i]:
            k = prefix[k - 1]
        if word[k] == word[i]:
            k += 1
        prefix[i] = k
    matched = array("I", [0]) * (len(text) + 1)
    k = 0
    for end, ch in enumerate(text, 1):
        while k and (k == size or word[k] != ch):
            k = prefix[k - 1]
        if word[k] == ch:
            k += 1
        matched[end] = k
    end = len(text)
    while end:
        length = matched[end]
        if not length:
            print("Yes")
            return
        # All lengths fit 17 bits; the high bit marks output cuts in place.
        matched[end] |= CUT
        end -= length
    output = bytearray(b"No\n")
    begin = 0
    for end in range(1, len(text) + 1):
        if matched[end] & CUT:
            if begin:
                output.extend(b" ")
            output.extend(text[begin:end])
            begin = end
    output.append(10)
    sys.stdout.buffer.write(output)


main()
