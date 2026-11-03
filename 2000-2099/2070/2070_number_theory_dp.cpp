#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const int FOURTH_ROOT_LIMIT = 1000, FIRST_HIGHER_EXPONENT = 4;

int floor_sqrt(long long value) {
    int root = std::sqrt(static_cast<double>(value));
    while (1LL * (root + 1) * (root + 1) <= value)
        root++;
    while (1LL * root * root > value)
        root--;
    return root;
}

int prime_count(int n) {
    if (n < 2)
        return 0;
    int root = floor_sqrt(n);
    std::vector<int> small(root + 1), large(root + 1);
    for (int i = 1; i <= root; i++) {
        small[i] = i - 1;
        large[i] = n / i - 1;
    }
    for (int prime = 2; prime <= root; prime++) {
        if (small[prime] == small[prime - 1])
            continue;
        int before = small[prime - 1], square = prime * prime;
        // g(v) counts survivors after smaller primes. Remove multiples
        // whose remaining factor is at least this prime.
        for (int i = 1; i <= std::min(root, n / square); i++) {
            int reduced = n / i / prime;
            int count = reduced <= root ? small[reduced] : large[n / reduced];
            large[i] -= count - before;
        }
        // Descending values preserve the previous-prime layer.
        for (int value = root; value >= square; value--)
            small[value] -= small[value / prime] - before;
    }
    return large[1];
}

int main() {
    long long left, right;
    scanf("%lld %lld", &left, &right);
    long long bad = prime_count(floor_sqrt(right)) - prime_count(floor_sqrt(left - 1));
    bool composite[FOURTH_ROOT_LIMIT + 1] = {};
    composite[0] = composite[1] = true;
    for (int p = 2; p * p <= FOURTH_ROOT_LIMIT; p++)
        if (!composite[p])
            for (int multiple = p * p; multiple <= FOURTH_ROOT_LIMIT; multiple += p)
                composite[multiple] = true;
    // k+1 prime and k>=2 implies even k. Beyond squares p^4<=R,
    // so a sieve only up to the fourth root supplies all remaining bases.
    for (int prime = 2; prime <= FOURTH_ROOT_LIMIT; prime++) {
        if (composite[prime])
            continue;
        long long square = 1LL * prime * prime;
        if (square > right / square)
            break;
        long long power = square * square;
        int exponent = FIRST_HIGHER_EXPONENT;
        while (true) {
            if (power >= left && !composite[exponent + 1])
                bad++;
            if (power > right / square)
                break;
            power *= square;
            exponent += 2;
        }
    }
    printf("%lld\n", right - left + 1 - bad);
}
