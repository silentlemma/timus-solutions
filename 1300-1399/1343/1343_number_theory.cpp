#include <cstdio>
#include <iostream>
#include <string>

typedef unsigned long long u64;

const int DIGITS = 12;
const u64 BASES[] = {2, 3, 5, 7, 11, 13}; // enough for every number below 3 * 10^12

u64 mulmod(u64 a, u64 b, u64 n) { return (unsigned __int128)a * b % n; }

u64 powmod(u64 a, u64 e, u64 n) {
    u64 r = 1;
    for (a %= n; e > 0; e >>= 1, a = mulmod(a, a, n)) {
        if (e & 1)
            r = mulmod(r, a, n);
    }
    return r;
}

// Miller-Rabin with fixed bases, exact for all 12-digit numbers
bool isPrime(u64 n) {
    if (n < 2)
        return false;
    for (u64 p : BASES) {
        if (n % p == 0)
            return n == p;
    }
    u64 d = n - 1;
    int s = 0;
    for (; d % 2 == 0; d /= 2)
        s++;
    for (u64 a : BASES) {
        u64 x = powmod(a, d, n);
        bool witness = x != 1 && x != n - 1;
        for (int i = 1; i < s && witness; i++) {
            x = mulmod(x, x, n);
            witness = x != n - 1;
        }
        if (witness)
            return false;
    }
    return true;
}

int main() {
    int count = 0;
    std::cin >> count;
    std::string digits, word;
    while (std::cin >> word)
        digits += word; // the digits, together or apart
    std::string prefix = digits.substr(0, count);
    u64 scale = 1;
    for (int i = count; i < DIGITS; i++)
        scale *= 10;
    u64 base = (prefix.empty() ? 0 : std::stoull(prefix)) * scale, number = base;
    if (count < DIGITS) {
        while (!isPrime(number))
            number++;
    }
    printf("%0*llu\n", DIGITS, number);
    return 0;
}
