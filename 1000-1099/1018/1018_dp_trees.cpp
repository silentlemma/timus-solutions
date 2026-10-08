#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

const long long NONE = -1;
const int TOKENS_PER_BRANCH = 3;
std::vector<std::vector<std::pair<int, int>>> adj;
int q;

// best[k]: the most apples on k branches kept in the subtree of v, all of
// them connected to v (NONE if the subtree has fewer than k branches)
std::vector<long long> solve(int v, int parent) {
    std::vector<long long> best = {0};
    for (auto [child, apples] : adj[v]) {
        if (child == parent)
            continue;
        std::vector<long long> sub = solve(child, v);
        // taking j >= 1 branches on the child's side: its edge and j - 1 below
        int size = std::min<int>(q, best.size() - 1 + sub.size());
        std::vector<long long> merged(size + 1, NONE);
        for (size_t i = 0; i < best.size(); i++)
            for (size_t j = 0; j <= sub.size() && i + j <= (size_t)size; j++) {
                long long gain = j == 0 ? 0 : apples + sub[j - 1];
                if (best[i] != NONE && (j == 0 || sub[j - 1] != NONE))
                    merged[i + j] = std::max(merged[i + j], best[i] + gain);
            }
        best = merged;
    }
    return best;
}

int main() {
    int n;
    if (scanf("%d %d", &n, &q) != 2)
        return 1;
    adj.assign(n + 1, {});
    for (int i = 1; i < n; i++) {
        int a, b, apples;
        if (scanf("%d %d %d", &a, &b, &apples) != TOKENS_PER_BRANCH)
            return 1;
        adj[a].push_back({b, apples});
        adj[b].push_back({a, apples});
    }
    printf("%lld\n", solve(1, 0)[q]);
}
