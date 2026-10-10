#include <cstdio>
#include <vector>

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<int> count(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int x;
        if (scanf("%d", &x) != 1)
            return 0;
        count[x]++;
    }
    // card k shows k - 1 and k, so the number x fits cards x and x + 1; going
    // up from the smallest number, card x is useless to anything later, so
    // it is taken first
    std::vector<bool> used(n + 2, false);
    bool ok = true;
    for (int x = 0; x <= n && ok; x++) {
        for (int card = x; card <= x + 1 && count[x] > 0; card++)
            if (card >= 1 && card <= n && !used[card]) {
                used[card] = true;
                count[x]--;
            }
        ok = count[x] == 0;
    }
    puts(ok ? "YES" : "NO");
}
