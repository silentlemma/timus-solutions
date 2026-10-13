#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> routes(n), onStop(m + 1);
    for (int r = 0; r < n; r++) {
        int k;
        scanf("%d", &k);
        routes[r].resize(k);
        for (int &st : routes[r]) {
            scanf("%d", &st);
            onStop[st].push_back(r);
        }
    }
    int a, b;
    scanf("%d %d", &a, &b);
    // one ride along a route reaches any of its stops, both ways; layers of rides
    vector<int> rides(m + 1, -1), cameBy(m + 1, -1), boarded(n, -1), queue = {a};
    rides[a] = 0;
    for (size_t head = 0; head < queue.size() && rides[b] < 0; head++) {
        int st = queue[head];
        for (int r : onStop[st]) {
            if (boarded[r] >= 0)
                continue;
            boarded[r] = st; // the stop where the route was first taken
            for (int next : routes[r])
                if (rides[next] < 0) {
                    rides[next] = rides[st] + 1;
                    cameBy[next] = r;
                    queue.push_back(next);
                }
        }
    }
    if (rides[b] < 0) {
        printf("-1\n");
        return 0;
    }
    vector<int> path = {b};
    while (path.back() != a)
        path.push_back(boarded[cameBy[path.back()]]);
    reverse(path.begin(), path.end());
    printf("%d\n", rides[b]);
    for (size_t i = 0; i < path.size(); i++)
        printf("%d%c", path[i], i + 1 < path.size() ? ' ' : '\n');
}
