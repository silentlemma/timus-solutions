#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>

using namespace std;

const int SIDES = 4;
const int DX[SIDES] = {1, -1, 0, 0}, DY[SIDES] = {0, 0, 1, -1};

int n, m, limit, kx, ky, ex, ey; // the knight, then the demon

bool inside(int x, int y) { return x >= 1 && x <= n && y >= 1 && y <= m && !(x == ex && y == ey); }

int main() {
    scanf("%d %d %d %d %d %d %d", &n, &m, &limit, &kx, &ky, &ex, &ey);
    // the fewest steps from the knight to every cell, around the demon
    vector<vector<int>> dist(n + 1, vector<int>(m + 1, -1));
    queue<pair<int, int>> q;
    dist[kx][ky] = 0;
    q.push({kx, ky});
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        for (int d = 0; d < SIDES; d++) {
            int nx = x + DX[d], ny = y + DY[d];
            if (inside(nx, ny) && dist[nx][ny] < 0) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    // the strike comes from a cell next to the demon after a straight run of
    // k steps; its start must be reachable with the steps that are left
    int best = 0;
    for (int a = 0; a < SIDES; a++) {
        int ax = ex + DX[a], ay = ey + DY[a];
        if (!inside(ax, ay))
            continue;
        for (int d = 0; d < SIDES; d++)
            for (int k = 0;; k++) {
                int sx = ax - k * DX[d], sy = ay - k * DY[d];
                if (!inside(sx, sy))
                    break;
                if (dist[sx][sy] >= 0 && dist[sx][sy] + k <= limit)
                    best = max(best, k + 1);
            }
    }
    printf("%d\n", best);
}
