import sys


def main():
    data = sys.stdin.read().split()
    n, p, q = int(data[0]), data[1][: int(data[0])], data[2][: int(data[0])]
    # A xor B equals A + B exactly when no position holds two ones. With a
    # equal to p, b follows q up to a 0 that becomes 1, then zeros, and that
    # prefix of q must avoid the ones of p, so it ends before the first clash
    clash = next((i for i in range(n) if p[i] == "1" and q[i] == "1"), n)
    for j in range(clash - 1, -1, -1):
        if p[j] == "0" and q[j] == "0":
            print(p)
            print(q[:j] + "1" + "0" * (n - j - 1))
            return
    # otherwise the next a after p with b all zeros, or start over
    last = p.rfind("0")
    a = p[:last] + "1" + "0" * (n - last - 1) if last >= 0 else "0" * n
    print(a)
    print("0" * n)


main()
