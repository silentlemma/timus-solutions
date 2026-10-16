#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    // joining i and j whenever i + j > n gives student i a degree of i up to
    // the middle and i - 1 after it, so only one degree is shared, by two
    std::vector<std::pair<int, int>> pairs;
    for (int i = 1; i <= n; i++)
        for (int j = i + 1; j <= n; j++)
            if (i + j > n) pairs.push_back({i, j});
    printf("%d\n", (int)pairs.size());
    for (auto [i, j] : pairs) printf("%d %d\n", i, j);
    return 0;
}
