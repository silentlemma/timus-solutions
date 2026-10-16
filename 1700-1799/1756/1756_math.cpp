#include <cstdio>

int main() {
    long long m, d1, d2;
    if (scanf("%lld %lld %lld", &m, &d1, &d2) < 1) return 0;
    // the work is m * d1 digger-days; spreading it as evenly as possible
    // over d2 days needs the fewest diggers, the rounded-up average
    long long work = m * d1, low = work / d2, extra = work % d2;
    for (long long day = 0; day < d2; day++) {
        printf(day ? " %lld" : "%lld", day < d2 - extra ? low : low + 1);
    }
    printf("\n");
    return 0;
}
