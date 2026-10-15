#include <cstdio>

const long long SHARES = 3;  // a bill is split three ways

int main() {
    long long n, total = 0;
    int m;
    scanf("%lld %d", &n, &m);
    for (int i = 1; i <= m; i++) {
        long long bill;
        scanf("%lld", &bill);
        total += bill;
        // Vanya's share total / 3 exceeds n exactly when total > 3n
        if (total > SHARES * n) {
            printf("Free after %d times.\n", i);
            return 0;
        }
    }
    printf("Team.GOV!\n");
}
