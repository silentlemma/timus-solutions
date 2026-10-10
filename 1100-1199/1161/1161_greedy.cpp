#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> weights(n);
    for (int &w : weights)
        if (scanf("%d", &w) != 1)
            return 0;
    std::sort(weights.begin(), weights.end(), std::greater<int>());
    // each collision takes a square root of the product, so the heaviest
    // stripies should meet first and be rooted the most times
    double total = weights[0];
    for (int k = 1; k < n; k++)
        total = 2 * std::sqrt(total * weights[k]);
    printf("%.2f\n", total);
}
