#include <cstdio>
#include <cstdlib>

int main() {
    int n;
    long long prev, cur;
    if (scanf("%d %lld", &n, &prev) != 2)
        return 1;
    // the slope of a chord is the mean of the slopes of the steps under it, so
    // the steepest valid chord joins two neighbours; take the first steepest
    long long best = -1;
    int a = 1;
    for (int x = 2; x <= n; x++) {
        if (scanf("%lld", &cur) != 1)
            return 1;
        if (std::llabs(cur - prev) > best) {
            best = std::llabs(cur - prev);
            a = x - 1;
        }
        prev = cur;
    }
    printf("%d %d\n", a, a + 1);
}
