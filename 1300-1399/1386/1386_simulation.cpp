#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int COMMANDS = 4;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int cells = n * m;
    // go[k][c]: the cell reached from cell c by command k, cells numbered by rows
    vector<vector<int>> go(COMMANDS, vector<int>(cells));
    for (int k = 0; k < COMMANDS; k++)
        for (int c = 0; c < cells; c++) {
            int row, col;
            scanf("%d %d", &row, &col);
            go[k][c] = (row - 1) * m + (col - 1);
        }
    int s;
    scanf("%d", &s);
    // the distinct cells the player may stand on, and when each was last added
    vector<int> cur(cells), next, mark(cells, -1);
    for (int c = 0; c < cells; c++)
        cur[c] = c;
    for (int step = 0; step < s; step++) {
        int k;
        scanf("%d", &k);
        const vector<int> &to = go[k - 1];
        next.clear();
        for (int c : cur)
            if (mark[to[c]] != step) {
                mark[to[c]] = step;
                next.push_back(to[c]);
            }
        swap(cur, next);
    }
    sort(cur.begin(), cur.end());
    printf("%d\n", (int)cur.size());
    for (int c : cur)
        printf("%d %d\n", c / m + 1, c % m + 1);
}
