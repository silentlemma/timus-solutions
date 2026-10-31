#include <cstdio>

// only adjacent factors are needed, so stream them without a heap allocation.
int main() {
    int n;
    long long previous;
    std::scanf("%d%lld", &n, &previous);
    // each factor is the next one times the size of the next dimension, and
    // the first one times the size of the first dimension is the whole array
    for (int i = 0; i < n; ++i) {
        long long current;
        std::scanf("%lld", &current);
        std::printf("%lld%c", previous / current - 1, i + 1 < n ? ' ' : '\n');
        previous = current;
    }
}
