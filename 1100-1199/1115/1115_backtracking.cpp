#include <algorithm>
#include <bitset>
#include <cstdio>
#include <functional>
#include <vector>

// no row is longer than all the ships together: 99 * 100
const int MAX_SUM = 10000;
typedef std::bitset<MAX_SUM> Sums;

int n, m;
std::vector<int> ships, rows, order, owner;

bool fill(int pos);

bool pick(int pos, const std::vector<int> &free, const std::vector<Sums> &reach, int k, int need) {
    if (need == 0)
        return fill(pos + 1);
    if (!reach[k][need])
        return false;
    int last = -1;
    for (int j = k; j < (int)free.size(); j++) {
        int length = ships[free[j]];
        // equal ships are interchangeable: try each length once per place
        if (length == last || length > need || !reach[j + 1][need - length])
            continue;
        last = length;
        owner[free[j]] = order[pos];
        if (pick(pos, free, reach, j + 1, need - length))
            return true;
        owner[free[j]] = -1;
    }
    return false;
}

bool fill(int pos) {
    std::vector<int> free;
    for (int i = 0; i < n; i++)
        if (owner[i] < 0)
            free.push_back(i);
    if (pos == m - 1) {
        // the last row takes every ship that is left
        int sum = 0;
        for (int i : free)
            sum += ships[i];
        if (sum != rows[order[pos]])
            return false;
        for (int i : free)
            owner[i] = order[pos];
        return true;
    }
    // reach[k]: the sums that the free ships from k on can make
    std::vector<Sums> reach(free.size() + 1);
    reach[free.size()][0] = true;
    for (int k = (int)free.size() - 1; k >= 0; k--)
        reach[k] = reach[k + 1] | reach[k + 1] << ships[free[k]];
    return pick(pos, free, reach, 0, rows[order[pos]]);
}

int main() {
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    ships.resize(n);
    rows.resize(m);
    for (auto &s : ships)
        scanf("%d", &s);
    for (auto &r : rows)
        scanf("%d", &r);
    std::sort(ships.begin(), ships.end(), std::greater<int>());
    // the shortest rows first: they have the fewest ways to be filled
    for (int r = 0; r < m; r++)
        order.push_back(r);
    std::sort(order.begin(), order.end(), [](int a, int b) { return rows[a] < rows[b]; });
    owner.assign(n, -1);
    fill(0);
    for (int r = 0; r < m; r++) {
        std::vector<int> row;
        for (int i = 0; i < n; i++)
            if (owner[i] == r)
                row.push_back(ships[i]);
        printf("%d\n", (int)row.size());
        for (size_t i = 0; i < row.size(); i++)
            printf(i + 1 < row.size() ? "%d " : "%d\n", row[i]);
    }
}
