#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>

const long long INF = 1LL << 62;

int main() {
    int n, start;
    scanf("%d", &n);
    std::vector<long long> pos(n);
    for (int i = 1; i < n; i++) {
        scanf("%lld", &pos[i]);
        pos[i] += pos[i - 1];
    }
    long long period, firstUp, firstDown;
    scanf("%d %lld %lld %lld", &start, &period, &firstUp, &firstDown);
    start--;
    if (n == 1) {
        printf("0\n");
        return 0;
    }
    // trains run forever: towards N they pass station i at firstUp + pos[i]
    // plus multiples of the period, towards 1 at firstDown + pos[N] - pos[i]
    std::vector<long long> phase[2] = {std::vector<long long>(n), std::vector<long long>(n)};
    for (int i = 0; i < n; i++) {
        phase[0][i] = (firstUp + pos[i]) % period;
        phase[1][i] = (firstDown + pos[n - 1] - pos[i]) % period;
    }
    // the first train in direction d at station j not before time t
    auto next = [&](int d, int j, long long t) {
        return t + ((phase[d][j] - t) % period + period) % period;
    };
    int full = (1 << n) - 1;
    std::vector<long long> arrive((size_t)(full + 1) * n);
    long long best = INF;
    for (int d0 = 0; d0 < 2; d0++) {
        long long t0 = phase[d0][start];
        // arrive[mask * n + j]: earliest time standing at j with mask inspected
        std::fill(arrive.begin(), arrive.end(), INF);
        for (int k = 0; k < n; k++)
            if ((d0 == 0 && k > start) || (d0 == 1 && k < start))
                arrive[(1 << start | 1 << k) * n + k] = t0 + std::llabs(pos[k] - pos[start]);
        for (int mask = 0; mask < full; mask++) {
            if (!(mask >> start & 1))
                continue;
            for (int j = 0; j < n; j++) {
                long long t = arrive[mask * n + j];
                if (t == INF)
                    continue;
                for (int d = 0; d < 2; d++) {
                    long long dep = next(d, j, t + 1);
                    for (int k = 0; k < n; k++) {
                        if ((d == 0 && k <= j) || (d == 1 && k >= j) || (mask >> k & 1))
                            continue;
                        long long &cell = arrive[(mask | 1 << k) * n + k];
                        cell = std::min(cell, dep + std::llabs(pos[k] - pos[j]));
                    }
                }
            }
        }
        // with everything inspected, ride straight back to the start
        for (int j = 0; j < n; j++) {
            long long t = arrive[full * n + j];
            if (t == INF || j == start)
                continue;
            int d = start > j ? 0 : 1;
            best = std::min(best, next(d, j, t + 1) + std::llabs(pos[start] - pos[j]) - t0);
        }
    }
    printf("%lld\n", best);
}
