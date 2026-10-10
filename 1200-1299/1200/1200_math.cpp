#include <algorithm>
#include <cmath>
#include <cstdio>

int main() {
    const long long CENTS = 100, PEAK = 2 * CENTS;
    double fa, fb;
    long long k;
    scanf("%lf %lf %lld", &fa, &fb, &k);
    long long a = std::llround(fa * CENTS), b = std::llround(fb * CENTS);
    // everything is in kopecks: x horns earn a * x - 100 * x^2
    long long best = -1, bestX = 0, bestY = 0, yPeak = std::max(b, 0LL) / PEAK;
    for (long long x = 0; x <= k; x++) {
        long long room = k - x, gainX = a * x - CENTS * x * x;
        // the hoof profit is concave in y, so the best y is next to its peak
        for (long long y : {std::min(yPeak, room), std::min(yPeak + 1, room)}) {
            long long total = gainX + b * y - CENTS * y * y;
            if (total > best) {
                best = total, bestX = x, bestY = y;
            }
        }
    }
    printf("%lld.%02lld\n%lld %lld\n", best / CENTS, best % CENTS, bestX, bestY);
}
