#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const long long MINUTE = 60;
const long long HOUR = 60 * MINUTE;
const long long CYCLE = 12 * HOUR; // the dial shows the same after 12 hours
const int TWELVE = 12;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<long long> times(n);
    long long total = 0;
    for (auto &t : times) {
        int h, m;
        if (scanf("%d:%d", &h, &m) != 2)
            return 0;
        int s;
        if (scanf(":%d", &s) != 1)
            return 0;
        t = h % TWELVE * HOUR + m * MINUTE + s; // 12 o'clock is 0
        total += t;
    }
    sort(times.begin(), times.end());
    // winding clock i forward to t costs t - time_i, plus a full cycle when
    // the clock shows a later time than t; moving t back to the nearest
    // clock time only helps, so only the clock times are tried
    long long best = 0, bestCost = -1;
    int j = 0; // clocks showing at most t
    for (long long t : times) {
        while (j < n && times[j] <= t)
            j++;
        long long cost = n * t - total + CYCLE * (n - j);
        if (bestCost < 0 || cost < bestCost) {
            best = t;
            bestCost = cost;
        }
    }
    long long h = best / HOUR, rest = best % HOUR;
    printf("%lld:%02lld:%02lld\n", h == 0 ? TWELVE : h, rest / MINUTE, rest % MINUTE);
}
