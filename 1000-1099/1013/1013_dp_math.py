from sys import stdin, stdout

n, base, modulus = map(int, stdin.read().split())
c = (base - 1) % modulus
# Represent a*X+b modulo X^2-c*X-c; start with X^0.
a, b = 0, 1
bit = 1 << (n.bit_length() - 1)
while bit:
    shared = (a * a % modulus) * c
    a, b = (shared + 2 * a * b) % modulus, (shared + b * b) % modulus
    if n & bit:
        shared = a * c % modulus
        a, b = (shared + b) % modulus, shared
    bit >>= 1
stdout.write(str((a * c + b) % modulus))
