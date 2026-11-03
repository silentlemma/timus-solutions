from sys import stdin, stdout

FACES = 4


def equivalent(a, b):
    if sorted(a) != sorted(b):
        return False
    if len(set(a)) < FACES:
        return True
    permutation = [a.index(letter) for letter in b]
    inversions = sum(
        permutation[i] > permutation[j] for i in range(FACES) for j in range(i + 1, FACES)
    )
    return inversions % 2 == 0


a = stdin.readline().strip()
b = stdin.readline().strip()
stdout.write(str("equal" if equivalent(a, b) else "different"))
