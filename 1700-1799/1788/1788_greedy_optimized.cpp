#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

// stdio avoids the iostream runtime for at most 100 values in each group.
int main() {
    int n, m;
    if (std::scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<int> girls(n), boys(m);
    for (int &g : girls)
        std::scanf("%d", &g);
    for (int &b : boys)
        std::scanf("%d", &b);
    // with k pairs the k most sensitive girls stay dry, and the k most
    // sensitive boys walk with them
    std::sort(girls.begin(), girls.end());
    std::sort(boys.begin(), boys.end());
    long long best = -1;
    for (int k = 0; k <= std::min(n, m); k++) {
        long long wet = std::accumulate(girls.begin(), girls.end() - k, 0LL);
        long long alone = std::accumulate(boys.begin(), boys.end() - k, 0LL);
        long long total = wet + alone * k;
        if (best < 0 || total < best)
            best = total;
    }
    std::printf("%lld\n", best);
    return 0;
}
