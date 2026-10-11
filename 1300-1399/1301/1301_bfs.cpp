#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>

enum Side { TOP, BOTTOM, NORTH, SOUTH, EAST, WEST, SIDES };
enum Move { GO_EAST, GO_WEST, GO_NORTH, GO_SOUTH, MOVES };
const int SIZE = 12;
const int WORD = 16;
const int DX[MOVES] = {1, -1, 0, 0};
const int DY[MOVES] = {0, 0, 1, -1};

// a roll moves every face to a new side; only the side that holds the
// starting top face matters, so each roll (east, west, north, south)
// maps every side to the side it lands on
const int ROLL[MOVES][SIDES] = {
    {EAST, WEST, NORTH, SOUTH, BOTTOM, TOP},
    {WEST, EAST, NORTH, SOUTH, TOP, BOTTOM},
    {NORTH, SOUTH, BOTTOM, TOP, EAST, WEST},
    {SOUTH, NORTH, TOP, BOTTOM, EAST, WEST},
};

bool blocked[SIZE][SIZE][MOVES];
int dist[SIZE][SIZE][SIDES];

int main() {
    int width = 0, height = 0, a = 0, b = 0, c = 0, d = 0;
    if (scanf("%d %d %d %d %d %d", &width, &height, &a, &b, &c, &d) < 1)
        return 0;
    char word[WORD];
    char kind = 0;
    while (scanf("%15s", word) == 1) {
        if (word[0] == 'v' || word[0] == 'h') {
            kind = word[0];
            continue;
        }
        int n = atoi(word), m = 0;
        if (scanf("%d", &m) != 1)
            break;
        // a v wall stands between (n, m) and (n + 1, m), an h wall between
        // (n, m) and (n, m + 1), and each blocks the move both ways
        if (kind == 'v') {
            blocked[n][m][GO_EAST] = blocked[n + 1][m][GO_WEST] = true;
        } else {
            blocked[n][m][GO_NORTH] = blocked[n][m + 1][GO_SOUTH] = true;
        }
    }
    memset(dist, -1, sizeof dist);
    std::queue<int> queue;
    dist[a][b][TOP] = 0;
    queue.push((a * SIZE + b) * SIDES + TOP);
    while (!queue.empty()) {
        int state = queue.front();
        queue.pop();
        int side = state % SIDES, x = state / SIDES / SIZE, y = state / SIDES % SIZE;
        if (x == c && y == d && side == TOP) {
            printf("%d\n", dist[x][y][side]);
            return 0;
        }
        for (int k = 0; k < MOVES; k++) {
            int nx = x + DX[k], ny = y + DY[k], ns = ROLL[k][side];
            if (nx < 1 || nx > width || ny < 1 || ny > height || blocked[x][y][k])
                continue;
            if (dist[nx][ny][ns] >= 0)
                continue;
            dist[nx][ny][ns] = dist[x][y][side] + 1;
            queue.push((nx * SIZE + ny) * SIDES + ns);
        }
    }
    puts("No solution");
    return 0;
}
