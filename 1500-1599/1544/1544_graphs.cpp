#include <algorithm>
#include <cstdio>
#include <queue>
#include <set>
#include <vector>
using namespace std;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    vector<char> protocol(n);
    for (char &p : protocol)
        if (scanf(" %c", &p) != 1)
            return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        adj[a - 1].push_back(b - 1);
        adj[b - 1].push_back(a - 1);
    }
    // glue neighbours with the same protocol into regions
    vector<int> region(n, -1);
    int regions = 0;
    for (int s = 0; s < n; s++)
        if (region[s] < 0) {
            region[s] = regions;
            vector<int> stack = {s};
            while (!stack.empty()) {
                int v = stack.back();
                stack.pop_back();
                for (int u : adj[v])
                    if (region[u] < 0 && protocol[u] == protocol[v]) {
                        region[u] = regions;
                        stack.push_back(u);
                    }
            }
            regions++;
        }
    vector<set<int>> near(regions);
    for (int v = 0; v < n; v++)
        for (int u : adj[v])
            if (region[u] != region[v])
                near[region[v]].insert(region[u]);
    // switching a region merges it with all its neighbours, so switching the
    // same region again and again takes its eccentricity in steps, and no
    // plan does better than the radius of the region graph
    int best = regions, centre = 0;
    for (int start = 0; start < regions; start++) {
        vector<int> dist(regions, -1);
        dist[start] = 0;
        queue<int> q;
        q.push(start);
        while (!q.empty()) {
            int r = q.front();
            q.pop();
            for (int x : near[r])
                if (dist[x] < 0) {
                    dist[x] = dist[r] + 1;
                    q.push(x);
                }
        }
        int far = *max_element(dist.begin(), dist.end());
        if (far < best) {
            best = far;
            centre = start;
        }
    }
    int computer = find(region.begin(), region.end(), centre) - region.begin();
    char current = protocol[computer];
    printf("%d\n", best);
    for (int i = 0; i < best; i++) {
        current = current == 'J' ? 'E' : 'J';
        printf("%d %c\n", computer + 1, current);
    }
}
