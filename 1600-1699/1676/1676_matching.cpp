#include <cstdio>
#include <string>
#include <vector>

const int BUFFER = 2048;

int n, m;
std::vector<std::string> beats;  // beats[i][j] == '1' when fighter j beats monster i
std::vector<int> owner, match;
std::vector<char> seen;

// Kuhn's augmenting search from monster u
bool augment(int u) {
    for (int j = 0; j < m; j++) {
        if (beats[u][j] == '1' && !seen[j]) {
            seen[j] = 1;
            if (owner[j] < 0 || augment(owner[j])) {
                owner[j] = u;
                match[u] = j;
                return true;
            }
        }
    }
    return false;
}

int main() {
    scanf("%d %d", &n, &m);
    beats.assign(n, "");
    std::string cells;
    static char buf[BUFFER];
    while ((int)cells.size() < n * m && scanf("%2047s", buf) == 1) {
        cells += buf;
    }
    for (int i = 0; i < n; i++) {
        beats[i] = cells.substr(i * m, m);
    }
    owner.assign(m, -1);
    match.assign(n, -1);
    for (int i = 0; i < n; i++) {
        seen.assign(m, 0);
        if (!augment(i)) {
            // some monster cannot be beaten in any assignment
            std::string row(m, '1'), out;
            for (int k = 0; k < n; k++) {
                out += row + "\n";
            }
            printf("%s", out.c_str());
            return 0;
        }
    }
    // i may take fighter j if j is free or its own, or if j's monster k moves on:
    // with k -> k2 when k can take k2's fighter, k reaches i (closing a cycle)
    // or reaches a monster (k included) that some free fighter beats
    std::vector<std::vector<int>> next(n);
    std::vector<char> loose(n, 0);
    for (int k = 0; k < n; k++) {
        for (int j = 0; j < m; j++) {
            if (beats[k][j] == '1') {
                if (owner[j] < 0) {
                    loose[k] = 1;
                } else if (owner[j] != k) {
                    next[k].push_back(owner[j]);
                }
            }
        }
    }
    std::vector<std::vector<char>> reach(n, std::vector<char>(n, 0));
    std::vector<char> helped(n, 0);
    for (int k = 0; k < n; k++) {
        std::vector<int> queue = {k};
        for (size_t h = 0; h < queue.size(); h++) {
            for (int k2 : next[queue[h]]) {
                if (!reach[k][k2]) {
                    reach[k][k2] = 1;
                    queue.push_back(k2);
                }
            }
        }
        helped[k] = loose[k];
        for (int x = 0; x < n; x++) {
            helped[k] |= reach[k][x] && loose[x];
        }
    }
    std::string out;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool ok = beats[i][j] == '1' &&
                      (owner[j] < 0 || match[i] == j || helped[owner[j]] || reach[owner[j]][i]);
            out += ok ? '0' : '1';
        }
        out += '\n';
    }
    printf("%s", out.c_str());
}
