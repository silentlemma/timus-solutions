#include <cstdio>

const long long DAY = 1440, HOUR = 60;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    long long now = 0;
    for (int i = 1; i < n; i++) {
        int q;
        long long delay, flight;
        if (scanf("%d", &q) != 1 || scanf("%lld %lld", &delay, &flight) != 2)
            return 0;
        long long best = -1;
        for (int j = 0; j < q; j++) {
            int hours, minutes;
            if (scanf("%d:%d", &hours, &minutes) != 2)
                return 0;
            long long leave = hours * HOUR + minutes + delay;
            if (leave < now)  // the same flight on a later day
                leave += (now - leave + DAY - 1) / DAY * DAY;
            if (best < 0 || leave < best)
                best = leave;
        }
        now = best + flight;
    }
    printf("%lld\n", now);
}
