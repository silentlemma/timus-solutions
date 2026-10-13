#include <cstdio>
#include <vector>

int main() {
    long long k = 0, p = 0;
    if (scanf("%lld %lld", &k, &p) != 2)
        return 0;
    // root[v]: some y with y^2 = v (mod p), or -1 when v is not a square
    std::vector<int> root(p, -1);
    for (long long y = 0; y < p; y++) {
        long long v = y * y % p;
        if (root[v] < 0)
            root[v] = (int)y;
    }
    // half the values are squares, so some x soon leaves a square k - x^2
    for (long long x = 0; x < p; x++) {
        long long y = root[((k - x * x) % p + p) % p];
        if (y >= 0) {
            printf("%lld %lld\n", x, y);
            return 0;
        }
    }
    puts("NO SOLUTION");
    return 0;
}
