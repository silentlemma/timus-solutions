#include <algorithm>
#include <cstdio>
#include <deque>
#include <map>
#include <string>
#include <utility>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> rows(n);
    for (auto &row : rows) {
        int k;
        scanf("%d", &k);
        row.resize(k);
        for (auto &v : row) {
            scanf("%d", &v);
            v--;
        }
    }
    // pair the k-th mention of v in room u with the k-th mention of u in room
    // v; a door to the room itself is mentioned twice in its own row
    struct End {
        int room, pos;
    };
    std::vector<std::pair<End, End>> ends;
    std::map<std::pair<int, int>, std::deque<int>> waiting;
    for (int u = 0; u < n; u++)
        for (int i = 0; i < (int)rows[u].size(); i++) {
            int v = rows[u][i];
            auto &queue = waiting[{std::min(u, v), std::max(u, v)}];
            if (!queue.empty()) {
                ends[queue.front()].second = {u, i};
                queue.pop_front();
            } else {
                queue.push_back(ends.size());
                ends.push_back({{u, i}, {-1, -1}});
            }
        }
    // a dummy room joined to every room of odd degree makes all degrees even
    int dummy = n, edges = ends.size();
    std::vector<std::vector<std::pair<int, int>>> adj(n + 1);
    for (int e = 0; e < edges; e++) {
        int u = ends[e].first.room, v = ends[e].second.room;
        adj[u].push_back({v, e});
        adj[v].push_back({u, e});
    }
    for (int u = 0; u < n; u++)
        if (adj[u].size() % 2) {
            adj[u].push_back({dummy, edges});
            adj[dummy].push_back({u, edges});
            edges++;
        }
    // walk Euler circuits and orient each door along the walk
    std::vector<bool> used(edges, false);
    std::vector<int> tail(edges), ptr(n + 1, 0);
    for (int start = 0; start <= n; start++) {
        std::vector<int> stack = {start};
        while (!stack.empty()) {
            int u = stack.back();
            while (ptr[u] < (int)adj[u].size() && used[adj[u][ptr[u]].second])
                ptr[u]++;
            if (ptr[u] == (int)adj[u].size()) {
                stack.pop_back();
                continue;
            }
            auto [v, e] = adj[u][ptr[u]];
            used[e] = true;
            tail[e] = u;
            stack.push_back(v);
        }
    }
    std::vector<std::string> colours(n);
    for (int u = 0; u < n; u++)
        colours[u].assign(rows[u].size(), ' ');
    for (int e = 0; e < (int)ends.size(); e++) {
        auto [a, b] = ends[e];
        // green on the side the walk leaves from, orange where it enters
        bool out_a = tail[e] == a.room;
        colours[a.room][a.pos] = out_a ? 'G' : 'Y';
        colours[b.room][b.pos] = out_a ? 'Y' : 'G';
    }
    std::string out;
    for (int u = 0; u < n; u++) {
        for (size_t i = 0; i < colours[u].size(); i++)
            out += std::string(i ? " " : "") + colours[u][i];
        out += "\n";
    }
    fputs(out.c_str(), stdout);
}
