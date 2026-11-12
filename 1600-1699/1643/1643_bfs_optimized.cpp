#include <cstdint>
#include <cstdio>

constexpr int MAX_SIDE = 100, MAX_CELLS = MAX_SIDE * MAX_SIDE;
constexpr int LETTERS = 26, SEARCHES = 3;
constexpr uint16_t INF = UINT16_MAX;
int rows, columns, cells;
char grid[MAX_CELLS];
uint16_t heads[LETTERS], nextPortal[MAX_CELLS], distances[SEARCHES][MAX_CELLS];
uint16_t queue[MAX_CELLS];

bool isPortal(char letter) { return letter >= 'A' && letter <= 'Z'; }

void bfs(int run, int start, int forbidden) {
    auto &distance = distances[run];
    for (int cell = 0; cell < cells; ++cell)
        distance[cell] = INF;
    int head = 0, tail = 0;
    auto visit = [&](int cell, uint16_t day) {
        if (distance[cell] != INF)
            return;
        if (isPortal(grid[cell])) {
            // Contract each zero-cost letter group at discovery, so every cell queues once.
            for (int other = heads[grid[cell] - 'A']; other != INF; other = nextPortal[other]) {
                distance[other] = day;
                queue[tail++] = other;
            }
        } else {
            distance[cell] = day;
            queue[tail++] = cell;
        }
    };
    visit(start, 0);
    while (head < tail) {
        int cell = queue[head++], row = cell / columns, column = cell % columns;
        for (int dr = -1; dr <= 1; ++dr)
            for (int dc = -1; dc <= 1; ++dc) {
                int r = row + dr, c = column + dc;
                if ((!dr && !dc) || r < 0 || r >= rows || c < 0 || c >= columns)
                    continue;
                int other = r * columns + c;
                if (grid[other] != '#' && other != forbidden)
                    visit(other, distance[cell] + 1);
            }
    }
}

int main() {
    if (scanf("%d%d", &rows, &columns) != 2)
        return 0;
    cells = rows * columns;
    for (auto &head : heads)
        head = INF;
    int first = 0, second = 0, fortress = 0;
    for (int cell = 0; cell < cells; ++cell) {
        scanf(" %c", &grid[cell]);
        char symbol = grid[cell];
        if (symbol == '$')
            first = cell;
        else if (symbol == '!')
            second = cell;
        else if (symbol == '*')
            fortress = cell;
        else if (isPortal(symbol)) {
            nextPortal[cell] = heads[symbol - 'A'];
            heads[symbol - 'A'] = cell;
        }
    }
    bfs(0, first, fortress);
    bfs(1, second, fortress);
    bfs(SEARCHES - 1, fortress, -1);
    int answer = INF;
    for (int cell = 0; cell < cells; ++cell) {
        int firstDay = distances[0][cell], secondDay = distances[1][cell];
        int afterMeeting = distances[SEARCHES - 1][cell];
        if (cell == fortress || firstDay == INF || secondDay == INF || afterMeeting == INF)
            continue;
        int meet = firstDay > secondDay ? firstDay : secondDay;
        if (meet + afterMeeting < answer)
            answer = meet + afterMeeting;
    }
    if (answer == INF)
        puts("Impossible");
    else
        printf("%d\n", answer);
}
