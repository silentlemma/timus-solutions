#include <algorithm>
#include <cstdio>
#include <vector>

// where the cheapest way to an office comes from
enum From { START, BELOW, LEFT, RIGHT };

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 1;
    std::vector<std::vector<long long>> fee(m, std::vector<long long>(n)), best = fee;
    for (auto &row : fee)
        for (long long &f : row)
            if (scanf("%lld", &f) != 1)
                return 1;
    std::vector<std::vector<From>> from(m, std::vector<From>(n, START));
    for (int i = 0; i < m; i++) {
        // from below first, then improve along the floor in both directions
        for (int j = 0; j < n; j++) {
            best[i][j] = fee[i][j] + (i > 0 ? best[i - 1][j] : 0);
            from[i][j] = i > 0 ? BELOW : START;
        }
        for (int j = 1; j < n; j++)
            if (best[i][j - 1] + fee[i][j] < best[i][j])
                best[i][j] = best[i][j - 1] + fee[i][j], from[i][j] = LEFT;
        for (int j = n - 2; j >= 0; j--)
            if (best[i][j + 1] + fee[i][j] < best[i][j])
                best[i][j] = best[i][j + 1] + fee[i][j], from[i][j] = RIGHT;
    }
    int i = m - 1, j = std::min_element(best[i].begin(), best[i].end()) - best[i].begin();
    std::vector<int> rooms;
    while (true) {
        rooms.push_back(j + 1);
        if (from[i][j] == START)
            break;
        if (from[i][j] == BELOW)
            i--;
        else
            j += from[i][j] == LEFT ? -1 : 1;
    }
    for (size_t k = rooms.size(); k-- > 0;)
        printf("%d%c", rooms[k], k > 0 ? ' ' : '\n');
}
