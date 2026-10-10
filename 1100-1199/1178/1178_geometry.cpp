#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<long long> x(n + 1), y(n + 1);
    for (int i = 1; i <= n; i++) {
        scanf("%lld %lld", &x[i], &y[i]);
    }
    std::vector<int> cities(n);
    std::iota(cities.begin(), cities.end(), 1);
    std::sort(cities.begin(), cities.end(),
              [&](int a, int b) { return x[a] != x[b] ? x[a] < x[b] : y[a] < y[b]; });
    // neighbours in (x, y) order: each road lies in its own strip of x, and
    // two roads can share only the border line, where they end at different
    // cities because no three cities are on one line
    for (int k = 0; k < n; k += 2) {
        printf("%d %d\n", cities[k], cities[k + 1]);
    }
}
