import sys

# every occurrence of a spell starts with an occurrence of its first
# letter, so a most frequent single letter is a strongest spell
word = sys.stdin.buffer.read().strip()
letters = range(ord("a"), ord("z") + 1)
print(chr(max(letters, key=word.count)))
