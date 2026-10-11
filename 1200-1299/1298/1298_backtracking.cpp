#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

const int MOVES[8][2] = {{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};

int n;
std::vector<std::vector<bool>> seen;
std::vector<std::pair<int, int>> path;

std::vector<std::pair<int, int>> freeSquares(int c, int r) {
    std::vector<std::pair<int, int>> out;
    for (const auto &m : MOVES) {
        int nc = c + m[0], nr = r + m[1];
        if (nc >= 0 && nc < n && nr >= 0 && nr < n && !seen[nc][nr])
            out.push_back({nc, nr});
    }
    return out;
}

bool tour(int c, int r) {
    seen[c][r] = true;
    path.push_back({c, r});
    if ((int)path.size() == n * n)
        return true;
    // Warnsdorff's rule: try first the squares with the fewest onward
    // moves, and the search still backtracks, so it is exact
    std::vector<std::pair<int, std::pair<int, int>>> order;
    for (auto &sq : freeSquares(c, r)) {
        order.push_back({(int)freeSquares(sq.first, sq.second).size(), sq});
    }
    std::stable_sort(order.begin(), order.end(),
                     [](const auto &a, const auto &b) { return a.first < b.first; });
    for (auto &o : order) {
        if (tour(o.second.first, o.second.second))
            return true;
    }
    seen[c][r] = false;
    path.pop_back();
    return false;
}

int main() {
    if (scanf("%d", &n) != 1)
        return 0;
    seen.assign(n, std::vector<bool>(n, false));
    bool found = false;
    for (int c = 0; c < n && !found; c++) {
        for (int r = 0; r < n && !found; r++)
            found = tour(c, r);
    }
    if (!found) {
        puts("IMPOSSIBLE");
        return 0;
    }
    for (auto &sq : path)
        printf("%c%d\n", 'a' + sq.first, sq.second + 1);
    return 0;
}
