#include <cstdio>
#include <vector>

// the 15000th prime is 163841
const int LIMIT = 163842;

int main() {
    std::vector<bool> composite(LIMIT, false);
    std::vector<int> primes;
    for (int p = 2; p < LIMIT; p++) {
        if (composite[p])
            continue;
        primes.push_back(p);
        for (long long q = (long long)p * p; q < LIMIT; q += p)
            composite[q] = true;
    }
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    while (k-- > 0) {
        int n;
        scanf("%d", &n);
        printf("%d\n", primes[n - 1]);
    }
}
