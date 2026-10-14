#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int n;
    long long r;
    if (scanf("%d %lld", &n, &r) != 2)
        return 0;
    vector<long long> sizes(n);
    for (auto &s : sizes)
        if (scanf("%lld", &s) != 1)
            return 0;
    // coats whose sizes lie within r of each other need different trips, so
    // the largest number of sizes in a window [x, x + r] is a lower bound
    int trips = 0;
    for (int lo = 0, hi = 0; hi < n; hi++) {
        while (sizes[hi] - sizes[lo] > r)
            lo++;
        trips = max(trips, hi - lo + 1);
    }
    // and it is enough: dealing the sorted coats round, the coat after coat i
    // in a trip is coat i + trips, which lies beyond that window
    printf("%d\n", trips);
    for (int t = 0; t < trips; t++) {
        printf("%d", (n - t + trips - 1) / trips);
        for (int coat = t + 1; coat <= n; coat += trips)
            printf(" %d", coat);
        printf("\n");
    }
}
