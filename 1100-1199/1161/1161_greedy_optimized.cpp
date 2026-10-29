#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>

const int MAX_CREATURES = 100;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // at most 100 weights: a fixed array needs no heap allocation
    int weights[MAX_CREATURES];
    for (int i = 0; i < n; ++i)
        if (scanf("%d", &weights[i]) != 1)
            return 0;
    std::sort(weights, weights + n, std::greater<int>());
    // each collision takes a square root of the product, so the heaviest
    // stripies should meet first and be rooted the most times
    double total = weights[0];
    for (int k = 1; k < n; k++)
        total = 2 * std::sqrt(total * weights[k]);
    printf("%.2f\n", total);
}
