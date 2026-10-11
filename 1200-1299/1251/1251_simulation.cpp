#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <vector>

const int FORGET = 1001; // a grave untouched for 1000 days can go on the next day
const int NOTICE = 101;  // and only when no neighbour was visited in the last 100

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int cells = n * m;
    // the client in each grave (0 if free), the last burial or visit of that
    // client, the last visit next door and the day the grave may be freed
    std::vector<int> owner(cells, 0), touched(cells, 0), nearVisit(cells, -NOTICE),
        release(cells, 0);
    std::vector<int> graveOf; // grave of each client, -1 if none
    std::priority_queue<int, std::vector<int>, std::greater<int>> free, pending;
    for (int g = 0; g < cells; g++)
        free.push(g);
    // a pending release is day * cells + grave
    auto schedule = [&](int g) {
        release[g] = std::max(touched[g] + FORGET, nearVisit[g] + NOTICE);
        pending.push(release[g] * cells + g);
    };
    int cremated = 0, day;
    char kind[2];
    while (scanf("%d %1s", &day, kind) == 2) {
        // graves free at the start of the day, before its events
        while (!pending.empty() && pending.top() / cells <= day) {
            int top = pending.top(), g = top % cells;
            pending.pop();
            if (owner[g] && release[g] == top / cells) {
                graveOf[owner[g] - 1] = -1;
                owner[g] = 0;
                free.push(g);
            }
        }
        if (kind[0] == 'd') {
            graveOf.push_back(-1);
            if (free.empty()) {
                cremated++;
                continue;
            }
            int g = free.top();
            free.pop();
            owner[g] = graveOf.size();
            graveOf.back() = g;
            touched[g] = day;
            schedule(g);
            continue;
        }
        int client;
        scanf("%d", &client);
        int g = graveOf[client - 1];
        if (g < 0)
            continue;
        touched[g] = day;
        schedule(g);
        int r = g / m, c = g % m;
        for (int nr = r - 1; nr <= r + 1; nr++)
            for (int nc = c - 1; nc <= c + 1; nc++)
                if ((nr != r || nc != c) && nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    int k = nr * m + nc;
                    nearVisit[k] = day;
                    if (owner[k])
                        schedule(k);
                }
    }
    printf("%d\n", cremated);
}
