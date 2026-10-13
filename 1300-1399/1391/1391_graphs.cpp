#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const int LONGEST = 16;    // the longest cycle counted: no snake of length 18 gets out
const int SHORTEST = 4;    // the shortest cycle on a grid
const int LAST_SNAKE = 17; // snakes of lengths 2 .. 17 are answered
const int DIRECTIONS = 4;

int h, w, root, limit;
vector<vector<int>> nearCells;
vector<int> dist, rnk, best;
vector<bool> onPath, needed;

void walk(int v, int steps) {
    for (int u : nearCells[v]) {
        if (u == root) {
            if (steps + 1 >= SHORTEST && needed[steps + 1]) {
                best[steps + 1] = dist[root];
                needed[steps + 1] = false;
            }
        } else if (!onPath[u] && rnk[u] > rnk[root] &&
                   steps + 1 + abs(u / w - root / w) + abs(u % w - root % w) <= limit) {
            onPath[u] = true;
            walk(u, steps + 1);
            onPath[u] = false;
        }
    }
}

int main() {
    int r0, c0;
    scanf("%d %d %d %d", &h, &w, &r0, &c0);
    int start = (r0 - 1) * w + c0 - 1;
    vector<char> free(h * w);
    for (int v = 0; v < h * w; v++) {
        char cell;
        scanf(" %c", &cell);
        free[v] = cell == '.';
    }
    free[start] = true;
    nearCells.assign(h * w, {});
    const int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    for (int v = 0; v < h * w; v++)
        for (int k = 0; k < DIRECTIONS; k++) {
            int nr = v / w + dr[k], nc = v % w + dc[k];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && free[nr * w + nc])
                nearCells[v].push_back(nr * w + nc);
        }
    // distances from the entrance
    dist.assign(h * w, -1);
    dist[start] = 0;
    vector<int> order = {start};
    for (size_t i = 0; i < order.size(); i++)
        for (int u : nearCells[order[i]])
            if (dist[u] < 0) {
                dist[u] = dist[order[i]] + 1;
                order.push_back(u);
            }
    // rank: breadth-first position; a cycle is found from its first cell in this order
    rnk.assign(h * w, (int)order.size());
    for (size_t i = 0; i < order.size(); i++)
        rnk[order[i]] = (int)i;
    best.assign(LONGEST + 1, -1);
    needed.assign(LONGEST + 1, false);
    for (int c = SHORTEST; c <= LONGEST; c += 2)
        needed[c] = true;
    onPath.assign(h * w, false);
    for (int v : order) {
        limit = 0;
        for (int c = SHORTEST; c <= LONGEST; c++)
            if (needed[c])
                limit = c;
        if (limit == 0)
            break;
        root = v;
        onPath[v] = true;
        walk(v, 0);
        onPath[v] = false;
    }
    for (int length = 2; length <= LAST_SNAKE; length++) {
        int answer = -1;
        for (int c = length; c <= LONGEST; c++)
            if (best[c] >= 0 && (answer < 0 || 2 * best[c] + c < answer))
                answer = 2 * best[c] + c;
        printf("%d\n", answer);
    }
}
