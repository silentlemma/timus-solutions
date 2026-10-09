#include <cstdio>
#include <map>

const int COUNT = 10, BASE = 10;

int main() {
    // the exponents of the primes in the product of all the numbers
    std::map<int, int> exponent;
    for (int i = 0; i < COUNT; i++) {
        int x;
        if (scanf("%d", &x) != 1)
            return 0;
        for (int p = 2; p * p <= x; p++)
            for (; x % p == 0; x /= p)
                exponent[p]++;
        if (x > 1)
            exponent[x]++;
    }
    // a divisor picks each prime from 0 to its exponent times
    int last = 1;
    for (auto [p, e] : exponent)
        last = last * (e + 1) % BASE;
    printf("%d\n", last);
}
