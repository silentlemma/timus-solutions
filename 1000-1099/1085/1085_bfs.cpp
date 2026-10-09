#include <cstdio>
#include <queue>
#include <vector>

const int TICKET = 4;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<std::vector<int>> routes(m), routes_at(n + 1);
    for (int r = 0; r < m; r++) {
        int size;
        scanf("%d", &size);
        routes[r].resize(size);
        for (int &s : routes[r]) {
            scanf("%d", &s);
            routes_at[s].push_back(r);
        }
    }
    int k;
    scanf("%d", &k);
    std::vector<long long> total(n + 1, 0);
    std::vector<bool> ok(n + 1, true);
    for (int f = 0; f < k; f++) {
        int money, start, card;
        scanf("%d %d %d", &money, &start, &card);
        // fewest rides from the start to every stop; a ride covers a whole route
        std::vector<int> rides(n + 1, -1);
        std::vector<bool> used(m, false);
        rides[start] = 0;
        std::queue<int> queue;
        queue.push(start);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (int r : routes_at[u]) {
                if (used[r])
                    continue;
                used[r] = true;
                for (int v : routes[r])
                    if (rides[v] < 0) {
                        rides[v] = rides[u] + 1;
                        queue.push(v);
                    }
            }
        }
        for (int t = 1; t <= n; t++) {
            int cost = card ? 0 : TICKET * rides[t];
            if (rides[t] < 0 || cost > money)
                ok[t] = false;
            else
                total[t] += cost;
        }
    }
    int stop = 0;
    for (int t = 1; t <= n; t++)
        if (ok[t] && (stop == 0 || total[t] < total[stop]))
            stop = t;
    if (stop == 0)
        puts("0");
    else
        printf("%d %lld\n", stop, total[stop]);
}
