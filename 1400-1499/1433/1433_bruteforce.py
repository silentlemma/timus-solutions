from itertools import permutations

FACES = 4


def even(p):
    inversions = sum(p[i] > p[j] for i in range(FACES) for j in range(i + 1, FACES))
    return inversions % 2 == 0


def main():
    a = input().strip()
    b = input().strip()
    # the rotations of a tetrahedron move its faces by exactly the even permutations
    same = any(
        all(b[i] == a[p[i]] for i in range(FACES)) for p in permutations(range(FACES)) if even(p)
    )
    print("equal" if same else "different")


main()
