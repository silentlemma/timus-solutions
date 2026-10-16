#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

const long long INF = 1LL << 62;

struct Update {
    int to;
    long long size;
    char kind;  // 'P'irated, 'C'racked or 'L'icensed
};

int main() {
    std::ios::sync_with_stdio(false);
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<Update>> updates(n + 1);
    for (int i = 0; i < m; i++) {
        int x, y;
        long long d;
        std::string kind;
        std::cin >> x >> y >> d >> kind;
        updates[x].push_back({y, d, kind[0]});
    }
    // updates only go up, so the versions can be taken in order; the
    // client is either still licensed (0) or already pirated (1)
    std::vector<std::array<long long, 2>> best(n + 1, {INF, INF});
    best[1][0] = 0;
    for (int v = 1; v <= n; v++) {
        for (const Update &u : updates[v]) {
            for (int state = 0; state < 2; state++) {
                if (best[v][state] == INF) continue;
                long long cost = best[v][state] + u.size;
                long long &target = u.kind == 'P' ? best[u.to][1] : best[u.to][state];
                if (u.kind != 'L' || state == 0) target = std::min(target, cost);
            }
        }
    }
    long long answer = std::min(best[n][0], best[n][1]);
    if (answer == INF) {
        std::cout << "Offline\n";
    } else {
        std::cout << "Online\n" << answer << "\n";
    }
}
