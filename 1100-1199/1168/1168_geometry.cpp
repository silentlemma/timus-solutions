#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

// R is a real number; all other lengths are integers, so a squared distance
// is an integer and only the integer part of R*R matters
const double EPS = 1e-6;
// above every altitude a station allows: 32000 plus 100000
const long long SKY = 1000000;

long long isqrt(long long v) {
    long long s = std::sqrt((double)v);
    while (s * s > v) {
        s--;
    }
    while ((s + 1) * (s + 1) <= v) {
        s++;
    }
    return s;
}

int main() {
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);
    std::vector<long long> h(m * n);
    for (auto &x : h) {
        scanf("%lld", &x);
    }
    std::vector<int> si(k), sj(k);
    std::vector<long long> z(k), reach(k);
    std::vector<bool> taken(m * n, false);
    for (int t = 0; t < k; t++) {
        double r;
        scanf("%d %d %lf", &si[t], &sj[t], &r);
        si[t]--;
        sj[t]--;
        z[t] = h[si[t] * n + sj[t]];
        reach[t] = (long long)(r * r + EPS);
        taken[si[t] * n + sj[t]] = true;
    }
    long long total = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (taken[i * n + j]) {
                continue;
            }
            // the receiver at altitude a hears a station at height z when
            // (a - z)^2 <= R^2 - (horizontal distance)^2
            long long low = h[i * n + j], high = SKY;
            for (int t = 0; t < k && low <= high; t++) {
                long long di = i - si[t], dj = j - sj[t];
                long long rest = reach[t] - di * di - dj * dj;
                if (rest < 0) {
                    high = -1;
                    break;
                }
                long long s = isqrt(rest);
                low = std::max(low, z[t] - s);
                high = std::min(high, z[t] + s);
            }
            if (low <= high) {
                total += high - low + 1;
            }
        }
    }
    printf("%lld\n", total);
}
