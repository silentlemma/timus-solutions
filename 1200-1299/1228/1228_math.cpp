#include <cstdio>
#include <vector>

int main() {
    int n;
    long long s;
    scanf("%d %lld", &n, &s);
    // each factor is the next one times the size of the next dimension, and
    // the first one times the size of the first dimension is the whole array
    std::vector<long long> sizes(n + 1);
    sizes[0] = s;
    for (int i = 1; i <= n; i++) {
        scanf("%lld", &sizes[i]);
    }
    for (int i = 0; i < n; i++) {
        printf("%lld%c", sizes[i] / sizes[i + 1] - 1, i + 1 < n ? ' ' : '\n');
    }
}
