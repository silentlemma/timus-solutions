#include <cstdio>
#include <utility>
#include <vector>

const int MAX_N = 10000;

// the number of comparisons after which the search over n elements reaches
// index target, when every other element sends it towards the target
int steps(int n, int target) {
    int p = 0, q = n - 1;
    for (int count = 1; p <= q; count++) {
        int i = (p + q) / 2;
        if (i == target)
            return count;
        if (target < i)
            q = i - 1;
        else
            p = i + 1;
    }
    return 0;
}

int main() {
    int target, l;
    if (scanf("%d %d", &target, &l) != 2)
        return 0;
    // any array whose elements before the target are smaller and after it are
    // larger leads the search there, so only n decides the number of steps
    std::vector<std::pair<int, int>> runs;
    for (int n = target + 1; n <= MAX_N; n++) {
        if (steps(n, target) != l)
            continue;
        if (!runs.empty() && runs.back().second == n - 1)
            runs.back().second = n;
        else
            runs.push_back({n, n});
    }
    printf("%d\n", (int)runs.size());
    for (auto [a, b] : runs)
        printf("%d %d\n", a, b);
}
