def main():
    n = int(input())
    # Euler's totient: the turns 2*pi*m/n with gcd(m, n) = 1
    phi, rest, p = n, n, 2
    while p * p <= rest:
        if rest % p == 0:
            while rest % p == 0:
                rest //= p
            phi -= phi // p
        p += 1
    if rest > 1:
        phi -= phi // rest
    print(phi // 2)


main()
