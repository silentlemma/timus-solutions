#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> left(n), right(n);
    for (int i = 0; i < n; i++)
        if (scanf("%d %d", &left[i], &right[i]) == 2 && left[i] > right[i])
            std::swap(left[i], right[i]);
    // a segment inside another is strictly shorter, so by length the inner
    // one always comes first
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(),
              [&](int a, int b) { return right[a] - left[a] < right[b] - left[b]; });
    std::vector<int> best(n, 1), prev(n, -1);
    for (int p = 0; p < n; p++) {
        int i = order[p];
        for (int q = 0; q < p; q++) {
            int j = order[q];
            if (left[i] < left[j] && right[j] < right[i] && best[j] + 1 > best[i])
                best[i] = best[j] + 1, prev[i] = j;
        }
    }
    int end = std::max_element(best.begin(), best.end()) - best.begin();
    std::vector<int> chain;
    for (; end >= 0; end = prev[end])
        chain.push_back(end + 1);
    printf("%d\n", (int)chain.size());
    for (size_t i = chain.size(); i-- > 0;)
        printf("%d%s", chain[i], i ? " " : "\n");
}
