#include <cstdio>
#include <numeric>
#include <vector>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> teeth(n + 1);
    std::vector<std::vector<int>> adj(n + 1);
    for (int i = 1; i <= n; i++) {
        if (scanf("%d", &teeth[i]) != 1)
            return 0;
        int j = 0;
        while (scanf("%d", &j) == 1 && j != 0) {
            // a link may be listed at one end only, so store it both ways
            adj[i].push_back(j);
            adj[j].push_back(i);
        }
    }
    int root = 0, speed = 0;
    if (scanf("%d %d", &root, &speed) != 2)
        return 0;
    // meshed gears share the speed of their rims, speed * teeth, and turn
    // opposite ways; so gear j turns at +-speed * teeth[root] / teeth[j]
    int rim = speed * teeth[root];
    std::vector<int> sign(n + 1, 0), queue = {root};
    sign[root] = 1;
    for (size_t head = 0; head < queue.size(); head++) {
        int u = queue[head];
        for (int v : adj[u]) {
            if (sign[v] == 0) {
                sign[v] = -sign[u];
                queue.push_back(v);
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        if (sign[i] == 0) {
            puts("0/1");
        } else {
            int g = std::gcd(rim, teeth[i]);
            printf("%d/%d\n", sign[i] * rim / g, teeth[i] / g);
        }
    }
    return 0;
}
