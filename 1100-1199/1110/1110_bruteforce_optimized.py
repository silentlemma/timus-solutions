import os
from sys import stdin, stdout


def main():
    exponent, modulus, remainder = map(int, stdin.buffer.read().split())
    roots = [str(value) for value in range(modulus) if pow(value, exponent, modulus) == remainder]
    stdout.write(" ".join(roots) if roots else "-1")
    stdout.flush()


main()
os._exit(0)
