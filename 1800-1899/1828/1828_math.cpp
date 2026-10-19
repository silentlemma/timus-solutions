#include <cstdio>

int main() {
    long long n;
    if (scanf("%lld", &n) != 1) return 0;
    // least squares line through the points (i, a_i), i = 0 .. n - 1:
    // the normal equations give the step and then the first term
    long long sumX = n * (n - 1) / 2, sumXX = 0, sumA = 0, sumXA = 0;
    for (long long i = 0; i < n; i++) {
        long long v;
        scanf("%lld", &v);
        sumXX += i * i;
        sumA += v;
        sumXA += i * v;
    }
    double step = double(n * sumXA - sumX * sumA) / double(n * sumXX - sumX * sumX);
    double first = (sumA - step * sumX) / n;
    printf("%.9f %.9f\n", first, step);
    return 0;
}
