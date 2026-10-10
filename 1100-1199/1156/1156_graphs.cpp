#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    int total = 2 * n;
    std::vector<std::vector<int>> near(total + 1);
    for (int k = 0; k < m; k++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        near[a].push_back(b);
        near[b].push_back(a);
    }
    // similar problems must go to different rounds: colour every component of
    // the conflict graph in two colours, or give up on an odd cycle
    std::vector<int> colour(total + 1, -1);
    std::vector<std::vector<int>> comps;
    for (int start = 1; start <= total; start++) {
        if (colour[start] >= 0)
            continue;
        colour[start] = 0;
        std::vector<int> members = {start}, stack = {start};
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            for (int w : near[v]) {
                if (colour[w] < 0) {
                    colour[w] = 1 - colour[v];
                    members.push_back(w);
                    stack.push_back(w);
                } else if (colour[w] == colour[v]) {
                    puts("IMPOSSIBLE");
                    return 0;
                }
            }
        }
        comps.push_back(members);
    }
    // each component sends one of its colours to the first round; reach[k][s]
    // tells whether the first k components can give it s problems
    int c = comps.size();
    std::vector<std::vector<int>> sizes(c, std::vector<int>(2, 0));
    for (int k = 0; k < c; k++)
        for (int v : comps[k])
            sizes[k][colour[v]]++;
    std::vector<std::vector<bool>> reach(c + 1, std::vector<bool>(n + 1, false));
    reach[0][0] = true;
    for (int k = 0; k < c; k++)
        for (int s = 0; s <= n; s++)
            if (reach[k][s])
                for (int side = 0; side < 2; side++)
                    if (s + sizes[k][side] <= n)
                        reach[k + 1][s + sizes[k][side]] = true;
    if (!reach[c][n]) {
        puts("IMPOSSIBLE");
        return 0;
    }
    std::vector<bool> first(total + 1, false);
    for (int k = c - 1, s = n; k >= 0; k--) {
        int side = s >= sizes[k][0] && reach[k][s - sizes[k][0]] ? 0 : 1;
        for (int v : comps[k])
            if (colour[v] == side)
                first[v] = true;
        s -= sizes[k][side];
    }
    for (int round = 0; round < 2; round++) {
        bool space = false;
        for (int v = 1; v <= total; v++)
            if (first[v] == (round == 0)) {
                printf(space ? " %d" : "%d", v);
                space = true;
            }
        puts("");
    }
}
