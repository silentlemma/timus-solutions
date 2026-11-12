#include <algorithm>
#include <array>
#include <cstdio>
#include <utility>

constexpr int MAX_SLEEPERS = 100;

int main() {
    int n;
    scanf("%d", &n);
    std::array<std::pair<int, int>, MAX_SLEEPERS> sleepers{};
    std::array<int, MAX_SLEEPERS> tails{};
    for (int i = 0; i < n; ++i)
        scanf("%d %d", &sleepers[i].first, &sleepers[i].second);
    std::sort(sleepers.begin(), sleepers.begin() + n);
    int kept = 0;
    for (int i = 0; i < n; ++i) {
        // tails[k] is the least possible last endpoint of a length-(k+1) subsequence.
        auto at = std::lower_bound(tails.begin(), tails.begin() + kept, sleepers[i].second);
        if (at == tails.begin() + kept)
            ++kept;
        *at = sleepers[i].second;
    }
    printf("%d\n", n - kept);
}
