#include <iostream>

long long solve(long long count, long long groups) {
    long long small = count / groups;
    long long larger = count % groups;
    long long squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1);
    return (count * count - squares) / 2;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int tests;
    if (!(std::cin >> tests))
        return 0;
    while (tests--) {
        long long count, groups;
        std::cin >> count >> groups;
        std::cout << solve(count, groups) << '\n';
    }
    return 0;
}
