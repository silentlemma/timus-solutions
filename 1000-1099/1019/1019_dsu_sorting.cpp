#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

const int END = 1000000000, TOKENS_PER_REPAINT = 3;

std::vector<int> nextFree;

// the first piece at or after i that no later repainting has covered yet
int find(int i) {
    while (nextFree[i] != i)
        i = nextFree[i] = nextFree[nextFree[i]];
    return i;
}

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

    // the colour of a piece is set by the last repainting covering it: go
    // backwards and paint only pieces that are still free, skipping the rest
    int pieces = xs.size() - 1;
    std::vector<char> piece(pieces, 'w');
    nextFree.resize(pieces + 1);
    std::iota(nextFree.begin(), nextFree.end(), 0);
    for (int i = n - 1; i >= 0; i--)
        for (int p = find(index(a[i])); p < index(b[i]); p = find(p)) {
            piece[p] = colour[i];
            nextFree[p] = p + 1;
        }

    // the longest run of white pieces; a strict comparison keeps the leftmost
    int bestX = 0, bestY = 0;
    for (int i = 0, j; i < pieces; i = j) {
        for (j = i; j < pieces && piece[j] == piece[i]; j++) {
        }
        if (piece[i] == 'w' && xs[j] - xs[i] > bestY - bestX)
            bestX = xs[i], bestY = xs[j];
    }
    printf("%d %d\n", bestX, bestY);
}
