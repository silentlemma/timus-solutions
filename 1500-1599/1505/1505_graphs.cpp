#include <cstdio>
#include <functional>
#include <iostream>
#include <iterator>
#include <queue>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
const ll INF = 1LL << 62;

int main() {
    string data((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    size_t pos = 0;
    auto number = [&]() {
        while (data[pos] < '0' || data[pos] > '9')
            pos++;
        ll v = 0;
        while (pos < data.size() && data[pos] >= '0' && data[pos] <= '9')
            v = v * 10 + (data[pos++] - '0');
        return v;
    };
    int n = number();
    vector<int> origin, target;
    vector<ll> cap, flow, cost;
    vector<vector<int>> out(n + 1), into(n + 1);
    vector<ll> balance(n + 1, 0); // outflow minus inflow
    // each pipe ends with a comma or a dot, each station with a dot
    for (int i = 1; i <= n; pos++) {
        char ch = data[pos];
        if (ch >= '0' && ch <= '9') {
            int a = number(), e = target.size();
            ll b = number(), c = number(), d = number();
            out[i].push_back(e);
            into[a].push_back(e);
            origin.push_back(i);
            target.push_back(a);
            cap.push_back(b);
            flow.push_back(c);
            cost.push_back(d);
            balance[i] += c;
            balance[a] -= c;
            pos--;
        } else if (ch == '.')
            i++;
    }

    // one more unit from any station with a well to station n through the
    // residual network: a pipe with spare room is free, a full one costs d,
    // and pushing back existing flow is free
    vector<ll> dist(n + 1, INF);
    vector<int> cameBy(n + 1, -1), step(n + 1, 0);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> heap;
    for (int i = 1; i < n; i++)
        if (balance[i] > 0) {
            dist[i] = 0;
            heap.push({0, i});
        }
    while (!heap.empty()) {
        auto [du, u] = heap.top();
        heap.pop();
        if (du > dist[u])
            continue;
        for (int e : out[u]) {
            ll nd = du + (flow[e] == cap[e] ? cost[e] : 0);
            int v = target[e];
            if (nd < dist[v]) {
                dist[v] = nd, cameBy[v] = e, step[v] = 1;
                heap.push({nd, v});
            }
        }
        for (int e : into[u]) {
            int v = origin[e];
            if (flow[e] > 0 && du < dist[v]) {
                dist[v] = du, cameBy[v] = e, step[v] = -1;
                heap.push({du, v});
            }
        }
    }
    if (dist[n] == INF) {
        puts("Impossible");
        return 0;
    }
    for (int v = n; cameBy[v] >= 0;) {
        int e = cameBy[v];
        flow[e] += step[v];
        v = step[v] == 1 ? origin[e] : target[e];
    }
    string res = to_string(dist[n]) + "\n";
    for (int i = 1; i <= n; i++) {
        for (size_t k = 0; k < out[i].size(); k++) {
            int e = out[i][k];
            if (k > 0)
                res += ", ";
            res += to_string(target[e]) + " " + to_string(flow[e]);
        }
        res += ".\n";
    }
    fputs(res.c_str(), stdout);
}
