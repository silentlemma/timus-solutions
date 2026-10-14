#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int NEED = 2; // a run needs two generating intervals inside it to be split

// g[l][r]: columns l .. r-1 must be a union of chosen intervals inside them.
// Going right, an interval that two smaller chosen ones already cover is
// dropped, and those it leaned on move right: the smallest such family.
void smallestFamily(vector<vector<char>> &g, int width) {
    for (int right = 1; right <= width; right++) {
        while (true) {
            vector<int> count(width + 1, 0);
            int covered = 0, rest = 0; // chosen inside [t, u), those starting before t
            int u = right, t = right - 1;
            bool redundant = true;
            while (u > t) {
                covered -= count[u];
                for (int left = 0; left < u; left++) {
                    if (!g[left][u])
                        continue;
                    count[left]++;
                    if (left >= t)
                        covered++;
                    else
                        rest++;
                }
                if (covered + rest < NEED) {
                    redundant = false;
                    break;
                }
                while (covered < NEED) {
                    t--;
                    covered += count[t];
                    rest -= count[t];
                }
                u--;
            }
            if (!redundant)
                break;
            int w = u;
            while (!g[w][right])
                w++;
            g[w][right] = 0;
            for (int end = right - 1; w > u; end--) {
                int x = u;
                while (x < w && !g[x][end])
                    x++;
                if (x == w)
                    continue;
                g[x][end] = 0;
                g[w][end] = 1;
                w = x;
            }
        }
    }
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    // the black pixels of a column form one run from top to bottom
    vector<int> top(m, n), bottom(m, -1);
    vector<vector<char>> g(m + 1, vector<char>(m + 1, 0));
    vector<char> line(m + 1);
    for (int row = 0; row < n; row++) {
        string format = "%" + to_string(m) + "s";
        scanf(format.c_str(), line.data());
        for (int col = 0; col < m;) {
            if (line[col] == '0') {
                col++;
                continue;
            }
            int left = col;
            while (col < m && line[col] == '1') {
                top[col] = min(top[col], row);
                bottom[col] = max(bottom[col], row);
                col++;
            }
            g[left][col] = 1;
        }
    }
    smallestFamily(g, m);
    // a chosen interval of columns spans every row where all of them are black
    vector<string> rects;
    for (int lo = 0; lo < m; lo++)
        for (int hi = lo + 1; hi <= m; hi++) {
            if (!g[lo][hi])
                continue;
            int first = 0, last = n - 1;
            for (int c = lo; c < hi; c++) {
                first = max(first, top[c]);
                last = min(last, bottom[c]);
            }
            rects.push_back(to_string(first + 1) + " " + to_string(lo + 1) + " " +
                            to_string(last + 1) + " " + to_string(hi));
        }
    printf("%d\n", (int)rects.size());
    for (const string &r : rects)
        printf("%s\n", r.c_str());
}
