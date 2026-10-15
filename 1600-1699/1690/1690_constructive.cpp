#include <algorithm>
#include <cstdio>
#include <vector>

const int CLASSES = 4;               // houses by the parities of x and y
const int CANDIDATES_PER_PLACE = 5;  // 5n names for n places

int main() {
    int n;
    scanf("%d", &n);
    std::vector<int> groups[CLASSES];
    for (int i = 1; i <= CANDIDATES_PER_PLACE * n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        groups[2 * (x & 1) + (y & 1)].push_back(i);
    }
    // two houses with the same parities differ by even dx and dy, so the
    // middle of their segment is a lattice point; 5n houses in 4 classes
    // leave one class with at least n of them, so the army always exists
    const std::vector<int>& best = *std::max_element(
        groups, groups + CLASSES, [](const std::vector<int>& a, const std::vector<int>& b) {
            return a.size() < b.size();
        });
    printf("OK\n");
    for (int i = 0; i < n; i++) {
        printf(i ? " %d" : "%d", best[i]);
    }
    printf("\n");
}
