from sys import stdin

KEYS = (b"abc", b"def", b"ghi", b"jkl", b"mno", b"pqr", b"stu", b"vwx", b"yz", b".,!", b" ")
text = stdin.buffer.readline()
print(sum(text.count(letter) * presses for key in KEYS for presses, letter in enumerate(key, 1)))
