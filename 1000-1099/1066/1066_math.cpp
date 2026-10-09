#include <algorithm>
#include <cstdio>

int main() {
    int n;
    double a;
    if (scanf("%d %lf", &n, &a) != 2)
        return 0;
    // with the second height x, lamp i hangs at a + (i-1)(x - a) + (i-1)(i-2)
    // and the last height grows with x, so x is the smallest value keeping every
    // lamp at height 0 or above
    double x = 0;
    for (int k = 1; k < n; k++)
        x = std::max(x, a - a / k - (k - 1));
    printf("%.2f\n", a + (n - 1) * (x - a) + (double)(n - 1) * (n - 2));
}
