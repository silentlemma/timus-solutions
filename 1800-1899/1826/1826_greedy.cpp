#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

const int TRIO = 3;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> times(n);
    for (auto &t : times) scanf("%d", &t);
    std::sort(times.begin(), times.end());
    long long total = 0;
    // move the two slowest across each round, in whichever of two ways is
    // cheaper: the fastest escorts each of them, or the two fastest cross,
    // one comes back, the two slowest cross together and the other returns
    while ((int)times.size() > TRIO) {
        int a = times[0], b = times[1], y = times[times.size() - 2], z = times.back();
        total += std::min(2 * a + y + z, a + 2 * b + z);
        times.resize(times.size() - 2);
    }
    if ((int)times.size() == TRIO) {
        total += std::accumulate(times.begin(), times.end(), 0);
    } else {
        total += times.back();
    }
    printf("%lld\n", total);
    return 0;
}
