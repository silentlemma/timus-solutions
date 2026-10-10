#include <cstdio>
#include <cstdlib>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::vector<bool>> knows(n, std::vector<bool>(n, false));
    for (int i = 0; i < n; i++) {
        for (int j; scanf("%d", &j) == 1 && j != 0;) {
            knows[i][j - 1] = true;
        }
    }
    // two people who do not both know each other must be in different
    // teams, so these pairs must form a bipartite graph; each component
    // gives two sides, and one side of each goes to the first team
    std::vector<int> side(n, -1);
    std::vector<std::vector<int>> parts[2];
    for (int s = 0; s < n; s++) {
        if (side[s] >= 0) {
            continue;
        }
        side[s] = 0;
        std::vector<int> groups[2], queue = {s};
        for (size_t h = 0; h < queue.size(); h++) {
            int v = queue[h];
            groups[side[v]].push_back(v);
            for (int u = 0; u < n; u++) {
                if (u != v && !(knows[v][u] && knows[u][v])) {
                    if (side[u] < 0) {
                        side[u] = 1 - side[v];
                        queue.push_back(u);
                    } else if (side[u] == side[v]) {
                        printf("No solution\n");
                        return 0;
                    }
                }
            }
        }
        parts[0].push_back(groups[0]);
        parts[1].push_back(groups[1]);
    }
    int count = parts[0].size();
    // reach[k][size]: which side of part k-1 gives the first team that
    // size, or -1 when it cannot be reached
    std::vector<std::vector<int>> reach(count + 1, std::vector<int>(n + 1, -1));
    reach[0][0] = 0;
    for (int k = 0; k < count; k++) {
        for (int size = 0; size <= n; size++) {
            if (reach[k][size] < 0) {
                continue;
            }
            for (int pick = 0; pick < 2; pick++) {
                int next = size + parts[pick][k].size();
                if (reach[k + 1][next] < 0) {
                    reach[k + 1][next] = pick;
                }
            }
        }
    }
    int size = -1;
    for (int s = 0; s <= n; s++) {
        if (reach[count][s] >= 0 && (size < 0 || abs(2 * s - n) < abs(2 * size - n))) {
            size = s;
        }
    }
    std::vector<int> team[2];
    for (int k = count - 1; k >= 0; k--) {
        int pick = reach[k + 1][size];
        for (int t = 0; t < 2; t++) {
            for (int v : parts[pick ^ t][k]) {
                team[t].push_back(v);
            }
        }
        size -= parts[pick][k].size();
    }
    for (auto &t : team) {
        printf("%d", (int)t.size());
        for (int v : t) {
            printf(" %d", v + 1);
        }
        printf("\n");
    }
}
