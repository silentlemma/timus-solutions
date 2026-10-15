#include <cmath>
#include <cstdio>

int main() {
    long long a1, b1, a2, b2;
    if (scanf("%lld %lld", &a1, &b1) != 2 || scanf("%lld %lld", &a2, &b2) != 2)
        return 0;
    // the largest singular value of [[a1, b1], [a2, b2]] without cancellation:
    // both sums of squares are exact integers
    long long p = (a1 + b2) * (a1 + b2) + (b1 - a2) * (b1 - a2);
    long long q = (a1 - b2) * (a1 - b2) + (b1 + a2) * (b1 + a2);
    printf("%.10f\n", (std::sqrt((double)p) + std::sqrt((double)q)) / 2);
}
