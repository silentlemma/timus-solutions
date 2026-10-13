#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> ends(2 * m);
    vector<int> degree(n + 1, 0);
    for (int &v : ends) {
        scanf("%d", &v);
        degree[v]++;
    }
    // vertex 0 is a helper joined to every room with an odd number of tunnels
    for (int v = 1; v <= n; v++)
        if (degree[v] % 2) {
            ends.push_back(0);
            ends.push_back(v);
        }
    int edges = ends.size() / 2;
    vector<vector<int>> adj(n + 1);
    for (int e = 0; e < edges; e++) {
        adj[ends[2 * e]].push_back(e);
        adj[ends[2 * e + 1]].push_back(e);
    }
    // an Euler circuit, found without recursion
    vector<bool> used(edges, false);
    vector<size_t> pos(n + 1, 0);
    vector<int> stack = {adj[0].empty() ? 1 : 0}, circuit;
    while (!stack.empty()) {
        int v = stack.back();
        while (pos[v] < adj[v].size() && used[adj[v][pos[v]]])
            pos[v]++;
        if (pos[v] == adj[v].size()) {
            circuit.push_back(v);
            stack.pop_back();
            continue;
        }
        int e = adj[v][pos[v]];
        used[e] = true;
        stack.push_back(ends[2 * e] + ends[2 * e + 1] - v);
    }
    // the helper edges cut the circuit into trails of real tunnels
    vector<string> trails;
    string current;
    for (int v : circuit) {
        if (v == 0) {
            if (!current.empty())
                trails.push_back(current);
            current.clear();
        } else {
            current += (current.empty() ? "" : " ") + to_string(v);
        }
    }
    if (!current.empty())
        trails.push_back(current);
    printf("%d\n", (int)trails.size());
    for (auto &t : trails)
        printf("%s\n", t.c_str());
}
