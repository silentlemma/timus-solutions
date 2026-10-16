#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

struct Word {
    int change, low, size, id;
};

int main() {
    std::ios::sync_with_stdio(false);
    int n;
    std::cin >> n;
    // each word: net change of the depth, lowest depth reached, length
    std::vector<Word> rising, falling;
    int top = 0;
    for (int i = 0; i < n; i++) {
        std::string w;
        std::cin >> w;
        int depth = 0, low = 0;
        for (char c : w) {
            depth += c == '(' ? 1 : -1;
            low = std::min(low, depth);
        }
        top += w.size();
        (depth >= 0 ? rising : falling).push_back({depth, low, (int)w.size(), i + 1});
    }
    // in a best answer the words that open more than they close come first,
    // those that dip least first; the rest go last, those that end highest
    // above their lowest point first
    std::stable_sort(rising.begin(), rising.end(),
                     [](const Word &a, const Word &b) { return a.low > b.low; });
    std::stable_sort(falling.begin(), falling.end(), [](const Word &a, const Word &b) {
        return a.low - a.change < b.low - b.change;
    });
    std::vector<Word> order = rising;
    order.insert(order.end(), falling.begin(), falling.end());
    // best[d]: longest prefix built so far that ends at depth d
    std::vector<int> best(top + 1, -1), next;
    best[0] = 0;
    std::vector<std::vector<char>> taken(order.size(), std::vector<char>(top + 1, 0));
    for (size_t k = 0; k < order.size(); k++) {
        const Word &w = order[k];
        next = best;
        for (int d = 0; d <= top; d++) {
            if (best[d] < 0 || d + w.low < 0) continue;
            int e = d + w.change;
            if (best[d] + w.size > next[e]) {
                next[e] = best[d] + w.size;
                taken[k][e] = 1;
            }
        }
        best.swap(next);
    }
    std::vector<int> used;
    for (int k = order.size() - 1, d = 0; k >= 0; k--) {
        if (taken[k][d]) {
            used.push_back(order[k].id);
            d -= order[k].change;
        }
    }
    std::reverse(used.begin(), used.end());
    printf("%d %d\n", best[0], (int)used.size());
    for (size_t i = 0; i < used.size(); i++) printf(i ? " %d" : "%d", used[i]);
    printf("\n");
}
