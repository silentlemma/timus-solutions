#include <algorithm>
#include <cstdio>
#include <vector>

const int END = 1000000000, TOKENS_PER_REPAINT = 3;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 1;
    std::vector<int> a(n), b(n);
    std::vector<char> colour(n);
    std::vector<int> xs = {0, END};
    for (int i = 0; i < n; i++) {
        if (scanf("%d %d %c", &a[i], &b[i], &colour[i]) != TOKENS_PER_REPAINT)
            return 1;
        xs.push_back(a[i]);
        xs.push_back(b[i]);
    }
    std::sort(xs.begin(), xs.end());
    xs.erase(std::unique(xs.begin(), xs.end()), xs.end());
    auto index = [&](int x) { return std::lower_bound(xs.begin(), xs.end(), x) - xs.begin(); };

    // piece i is [xs[i], xs[i + 1]); repaint the pieces of every segment
    std::vector<char> piece(xs.size() - 1, 'w');
    for (int i = 0; i < n; i++)
        std::fill(piece.begin() + index(a[i]), piece.begin() + index(b[i]), colour[i]);

    // the longest run of white pieces; a strict comparison keeps the leftmost
    int bestX = 0, bestY = 0;
    for (size_t i = 0, j; i < piece.size(); i = j) {
        for (j = i; j < piece.size() && piece[j] == piece[i]; j++) {
        }
        if (piece[i] == 'w' && xs[j] - xs[i] > bestY - bestX)
            bestX = xs[i], bestY = xs[j];
    }
    printf("%d %d\n", bestX, bestY);
}
