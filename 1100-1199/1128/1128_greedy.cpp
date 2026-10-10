#include <cstdio>
#include <string>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> enemies(n);
    for (auto &list : enemies) {
        int k;
        scanf("%d", &k);
        list.resize(k);
        for (auto &u : list) {
            scanf("%d", &u);
            u--;
        }
    }
    std::vector<int> side(n, 0), work;
    for (int v = 0; v < n; v++)
        work.push_back(v);
    // a child with two or more enemies on its side has at most one on the
    // other, so moving it removes at least one pair of enemies sharing a
    // group; the moves stop after at most as many steps as there are pairs
    while (!work.empty()) {
        int v = work.back();
        work.pop_back();
        int same = 0;
        for (int u : enemies[v])
            same += side[u] == side[v];
        if (same >= 2) {
            side[v] ^= 1;
            work.insert(work.end(), enemies[v].begin(), enemies[v].end());
            work.push_back(v);
        }
    }
    std::vector<int> group, other;
    for (int v = 0; v < n; v++)
        (side[v] == side[0] ? group : other).push_back(v + 1);
    const auto &small = group.size() <= other.size() ? group : other;
    std::string out = std::to_string(small.size()) + "\n";
    for (size_t i = 0; i < small.size(); i++)
        out += (i ? " " : "") + std::to_string(small[i]);
    puts(out.c_str());
}
