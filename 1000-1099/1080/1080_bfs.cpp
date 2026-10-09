#include <cstdio>
#include <queue>
#include <string>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> adj(n + 1);
    for (int i = 1; i <= n; i++) {
        int v;
        while (scanf("%d", &v) == 1 && v != 0) {
            adj[i].push_back(v);
            adj[v].push_back(i);
        }
    }
    // the map is connected, so the colour of the first country decides all
    std::vector<int> color(n + 1, -1);
    color[1] = 0;
    std::queue<int> queue;
    queue.push(1);
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop();
        for (int v : adj[u]) {
            if (color[v] < 0) {
                color[v] = 1 - color[u];
                queue.push(v);
            } else if (color[v] == color[u]) {
                puts("-1");
                return 0;
            }
        }
    }
    std::string out;
    for (int i = 1; i <= n; i++)
        out += char('0' + color[i]);
    puts(out.c_str());
}
