#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

// a raise must be a whole number of percent of this base
const int PERCENT = 100;

int main() {
    int n, s;
    if (scanf("%d %d", &n, &s) != 2)
        return 0;
    if (s > n) {
        puts("0");
        return 0;
    }
    // jobs[a] is the longest run of jobs from salary s ending at salary a, and
    // a raise from a is a whole percent exactly when it is a multiple of
    // a / gcd(a, 100)
    std::vector<int> jobs(n + 1, 0);
    jobs[s] = 1;
    int best = 1;
    for (int a = s; a <= n; a++) {
        if (!jobs[a])
            continue;
        best = std::max(best, jobs[a]);
        int step = a / std::gcd(a, PERCENT);
        for (int b = a + step; b <= n; b += step)
            jobs[b] = std::max(jobs[b], jobs[a] + 1);
    }
    printf("%d\n", best);
}
