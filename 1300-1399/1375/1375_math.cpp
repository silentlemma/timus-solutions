#include <cstdio>

using U = unsigned long long;
const U FOUR = 4;

U power(U value, U exponent, U modulus) {
    U result = 1;
    while (exponent) {
        if (exponent & 1)
            result = result * value % modulus;
        value = value * value % modulus;
        exponent /= 2;
    }
    return result;
}

void answer(U x, U y) { printf("%llu %llu\n", x, y); }

int main() {
    U key = 0, p = 0;
    if (scanf("%llu %llu", &key, &p) != 2)
        return 0;
    if (p == 2 || key == 0) {
        answer(key, 0);
        return 0;
    }
    if (p % FOUR == 1) {
        U z = 2;
        while (power(z, (p - 1) / 2, p) != p - 1)
            ++z;
        U imaginary = power(z, (p - 1) / FOUR, p);
        U odd = key % 2 ? key : key + p;
        answer(((odd + 1) / 2) % p, ((odd - 1) / 2) * imaginary % p);
        return 0;
    }
    for (U x = 0; x <= p / 2; ++x) {
        U residue = (key + p - x * x % p) % p;
        U y = power(residue, (p + 1) / FOUR, p);
        if (y * y % p == residue) {
            answer(x, y);
            return 0;
        }
    }
    puts("NO SOLUTION");
}
