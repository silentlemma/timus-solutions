#include <cstdio>

long long solve(long long count, long long groups) {
    long long small = count / groups;
    long long larger = count % groups;
    long long squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1);
    return (count * count - squares) / 2;
}

// scanf and printf instead of iostream, which needs less memory
int main() {
    int tests;
    if (std::scanf("%d", &tests) != 1)
        return 0;
    while (tests--) {
        long long count, groups;
        std::scanf("%lld %lld", &count, &groups);
        std::printf("%lld\n", solve(count, groups));
    }
    return 0;
}
