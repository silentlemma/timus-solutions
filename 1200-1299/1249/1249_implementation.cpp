#include <cstdio>
#include <vector>

const int THREE = 3;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    // every dark region is a rectangle exactly when no 2 x 2 window holds
    // three dark cells, so two rows are enough, and the image never fits in
    // 4 MB anyway
    std::vector<int> prev(m), cur(m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int c = getchar();
            while (c != '0' && c != '1')
                c = getchar();
            cur[j] = c - '0';
            if (i > 0 && j > 0 && prev[j - 1] + prev[j] + cur[j - 1] + cur[j] == THREE) {
                puts("No");
                return 0;
            }
        }
        prev.swap(cur);
    }
    puts("Yes");
}
