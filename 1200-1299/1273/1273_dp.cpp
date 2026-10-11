#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int k;
    scanf("%d", &k);
    std::vector<std::pair<int, int>> sleepers(k);
    for (auto &s : sleepers)
        scanf("%d %d", &s.first, &s.second);
    std::sort(sleepers.begin(), sleepers.end());
    // two sleepers cross when their ends come in opposite orders, so the
    // kept ones form an increasing run of right ends
    std::vector<int> longest(k, 1);
    int best = 0;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < i; j++)
            if (sleepers[j].second < sleepers[i].second)
                longest[i] = std::max(longest[i], longest[j] + 1);
        best = std::max(best, longest[i]);
    }
    printf("%d\n", k - best);
}
