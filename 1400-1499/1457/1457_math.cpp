#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        long long p;
        scanf("%lld", &p);
        sum += p;
    }
    // the mean of squared distances is smallest at the arithmetic mean
    printf("%.6f\n", (double)sum / n);
}
