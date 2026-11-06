#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int LIMIT = 3162;
constexpr int PERSISTENT = 3;
static bool composite[LIMIT + 1];
static unsigned char occurrences[LIMIT + 1];

int main() {
    int size;
    if (std::scanf("%d", &size) != 1)
        return 0;
    std::vector<int> primes, large;
    large.reserve(size);
    for (int p = 2; p <= LIMIT; ++p) {
        if (composite[p])
            continue;
        primes.push_back(p);
        for (int j = p * p; j <= LIMIT; j += p)
            composite[j] = true;
    }
    int best = 0;
    const auto count_small = [&](int p) {
        best = std::max(best, static_cast<int>(++occurrences[p]));
        return best == PERSISTENT;
    };
    for (int i = 0; i < size; ++i) {
        int value;
        std::scanf("%d", &value);
        for (int prime : primes) {
            if (prime * prime > value)
                break;
            if (value % prime == 0) {
                if (count_small(prime)) {
                    std::puts("infinity");
                    return 0;
                }
                do {
                    value /= prime;
                } while (value % prime == 0);
            }
        }
        if (value > LIMIT) {
            // A value up to 10^7 can have only one prime factor above LIMIT.
            large.push_back(value);
        } else if (value > 1 && count_small(value)) {
            std::puts("infinity");
            return 0;
        }
    }
    std::sort(large.begin(), large.end());
    int previous = 0, count = 0;
    for (int prime : large) {
        count = prime == previous ? count + 1 : 1;
        previous = prime;
        best = std::max(best, count);
        if (best == PERSISTENT) {
            std::puts("infinity");
            return 0;
        }
    }
    std::printf("%d\n", best);
}
