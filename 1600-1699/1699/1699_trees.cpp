#include <cstdio>
#include <string>
#include <utility>
#include <vector>

const int LOG = 17;  // 2^17 > 100000 cells

int main() {
    int h, w;
    scanf("%d %d", &h, &w);
    int cells = h * w;
    std::vector<bool> open(cells);
    std::vector<char> row(w + 1);
    for (int r = 0; r < h; r++) {
        scanf("%s", row.data());
        for (int c = 0; c < w; c++) {
            open[r * w + c] = row[c] == '#';
        }
    }
    // the open cells form a tree; root it at the first open cell and keep, for
    // every cell, its parent, depth, the direction of the step from the parent
    // (as the index offset) and the number of turns from the root
    int root = 0;
    while (!open[root]) {
        root++;
    }
    std::vector<int> parent(cells, -1), depth(cells, 0), step(cells, 0), turns(cells, 0);
    parent[root] = root;
    std::vector<int> order = {root};
    for (size_t k = 0; k < order.size(); k++) {
        int v = order[k], r = v / w, c = v % w;
        int next[] = {v - w, v + w, v - 1, v + 1};
        bool fits[] = {r > 0, r < h - 1, c > 0, c < w - 1};
        for (int d = 0; d < (int)(sizeof next / sizeof next[0]); d++) {
            int u = next[d];
            if (fits[d] && open[u] && parent[u] < 0) {
                parent[u] = v;
                depth[u] = depth[v] + 1;
                step[u] = u - v;
                turns[u] = turns[v] + (v != root && step[v] != u - v);
                order.push_back(u);
            }
        }
    }
    // closed cells point at themselves, which keeps the jump table in range
    for (int v = 0; v < cells; v++) {
        parent[v] = parent[v] < 0 ? v : parent[v];
    }
    std::vector<std::vector<int>> up(LOG, parent);
    for (int b = 1; b < LOG; b++) {
        for (int v = 0; v < cells; v++) {
            up[b][v] = up[b - 1][up[b - 1][v]];
        }
    }
    int q;
    scanf("%d", &q);
    std::string out;
    while (q--) {
        int r1, c1, r2, c2;
        scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
        int a = (r1 - 1) * w + c1 - 1, b = (r2 - 1) * w + c2 - 1;
        if (depth[a] < depth[b]) {
            std::swap(a, b);
        }
        int answer = 0;
        if (a != b) {
            int a1 = a, b1 = b;
            bool below = false;
            if (depth[a] > depth[b]) {
                // lift a to just below b's depth: if it then hangs from b, b is
                // an ancestor and only the way down from b counts
                for (int k = depth[a] - depth[b] - 1, bit = 0; k; k >>= 1, bit++) {
                    if (k & 1) {
                        a1 = up[bit][a1];
                    }
                }
                below = parent[a1] == b;
                if (!below) {
                    a1 = parent[a1];
                }
            }
            if (below) {
                answer = turns[a] - turns[a1];
            } else {
                for (int bit = LOG - 1; bit >= 0; bit--) {
                    if (up[bit][a1] != up[bit][b1]) {
                        a1 = up[bit][a1];
                        b1 = up[bit][b1];
                    }
                }
                // a1 and b1 are the children of the meeting cell on the two sides,
                // the path turns there unless it goes straight through
                bool straight = step[a1] == -step[b1];
                answer = turns[a] - turns[a1] + turns[b] - turns[b1] + (straight ? 0 : 1);
            }
        }
        out += std::to_string(answer) + "\n";
    }
    fputs(out.c_str(), stdout);
}
