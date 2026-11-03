import sys
from array import array

MAX_WORD_LENGTH = 50
KEYPAD = b"22233344115566070778889990"
ALPHABET = 10


def solve(phone, count, stream):
    n = len(phone)
    edges = array("i", [0]) * ((n * min(n, MAX_WORD_LENGTH) + 1) * ALPHABET)
    words = [None]
    # A dictionary trie can grow with the whole input. Only phone substrings
    # can be used, so build their bounded trie first and discard other words.
    for start in range(n):
        node = 0
        for end in range(start, min(n, start + MAX_WORD_LENGTH)):
            slot = node * ALPHABET + phone[end] - ord("0")
            if edges[slot] == 0:
                edges[slot] = len(words)
                words.append(None)
            node = edges[slot]
    for _ in range(count):
        word = stream.readline().strip()
        node = 0
        for letter in word:
            node = edges[node * ALPHABET + KEYPAD[letter - ord("a")] - ord("0")]
            if node == 0:
                break
        if node and words[node] is None:
            words[node] = word

    best = [n + 1] * (n + 1)
    how = [0] * (n + 1)
    best[0] = 0
    for start in range(n):
        if best[start] > n:
            continue
        node = 0
        for end in range(start, min(n, start + MAX_WORD_LENGTH)):
            node = edges[node * ALPHABET + phone[end] - ord("0")]
            if words[node] is not None and best[start] + 1 < best[end + 1]:
                best[end + 1] = best[start] + 1
                how[end + 1] = node
    if best[n] > n:
        return "No solution."
    answer = []
    position = n
    while position:
        word = words[how[position]]
        answer.append(word.decode())
        position -= len(word)
    return " ".join(reversed(answer))


def main():
    stream = sys.stdin.buffer
    for line in stream:
        phone = line.strip()
        if phone == b"-1":
            break
        print(solve(phone, int(stream.readline()), stream))


main()
