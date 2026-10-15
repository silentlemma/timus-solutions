#include <algorithm>
#include <cstdio>
#include <vector>

const int WIN = 3;
const char *SIGNS[] = {"<", "<=", ">=", ">"};

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> left(n);
    for (int &x : left) scanf("%d", &x);
    std::vector<std::vector<int>> got(n, std::vector<int>(n, 0));
    std::vector<int> active(n);
    for (int i = 0; i < n; i++) active[i] = i;
    bool ok = true;
    // the weakest team plays all its games now: it keeps its own points
    // and hands the rest out, three a game, to the strongest teams first
    while (ok && active.size() > 1) {
        std::sort(active.begin(), active.end(), [&](int a, int b) {
            return left[a] != left[b] ? left[a] < left[b] : a < b;
        });
        int weak = active[0];
        int give = WIN * ((int)active.size() - 1) - left[weak];
        if (give < 0) break;
        for (size_t k = active.size() - 1; k >= 1; k--) {
            int t = active[k], share = std::min(WIN, give);
            give -= share;
            left[t] -= share;
            got[t][weak] = share;
            got[weak][t] = WIN - share;
            if (left[t] < 0) ok = false;
        }
        left[weak] = 0;
        if (give) ok = false;
        active.erase(active.begin());
    }
    for (int x : left) {
        if (x) ok = false;
    }
    if (!ok) {
        printf("INCORRECT\n");
        return 0;
    }
    printf("CORRECT\n");
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) printf("%d %s %d\n", i + 1, SIGNS[got[i][j]], j + 1);
    }
}
