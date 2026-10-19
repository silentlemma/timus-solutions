#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const char* KEYS[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
const int SLOWEST = 4;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int presses['z' + 1] = {0};
    for (const char* key : KEYS)
        for (int k = 0; key[k]; k++) presses[(unsigned char)key[k]] = k + 1;
    int n;
    cin >> n;
    vector<string> words(n);
    for (string& w : words) cin >> w;
    // state offset[x] + d: name x is current and its first d letters are
    // typed; node_of[state] is the trie node of the typed letters
    vector<int> offset(n + 1, 0);
    for (int x = 0; x < n; x++) offset[x + 1] = offset[x] + words[x].size() + 1;
    int states = offset[n];
    vector<int> node_of(states), owner(states);
    vector<int> low = {0}, high = {n - 1};  // the names below a node form a range
    vector<vector<pair<int, int>>> children(1);  // (state, letter cost)
    vector<int> path = {0};
    for (int x = 0; x < n; x++) {
        const string& w = words[x];
        size_t same = 0;
        if (x > 0) {
            const string& p = words[x - 1];
            while (same < w.size() && same < p.size() && w[same] == p[same]) same++;
        }
        path.resize(same + 1);
        for (size_t d = same + 1; d <= w.size(); d++) {
            int v = low.size();
            low.push_back(x);
            high.push_back(x);
            children.emplace_back();
            children[path.back()].push_back({offset[x] + (int)d, presses[(unsigned char)w[d - 1]]});
            path.push_back(v);
        }
        for (size_t d = 0; d <= w.size(); d++) {
            node_of[offset[x] + d] = path[d];
            owner[offset[x] + d] = x;
            high[path[d]] = x;
        }
    }
    int hubs = low.size();
    const int INF = 1 << 30;
    vector<int> dist(states + hubs, INF);
    // every move costs at most SLOWEST, so SLOWEST + 1 buckets in a circle
    vector<vector<int>> buckets(SLOWEST + 1);
    dist[0] = 0;
    buckets[0].push_back(0);
    long long pending = 1;
    vector<pair<int, int>> moves;
    for (int now = 0; pending; now++) {
        vector<int>& bucket = buckets[now % (SLOWEST + 1)];
        while (!bucket.empty()) {
            int s = bucket.back();
            bucket.pop_back();
            pending--;
            if (dist[s] != now) continue;
            moves.clear();
            if (s >= states) {
                moves = children[s - states];
            } else {
                int x = owner[s], d = s - offset[x], v = node_of[s];
                int nxt = x < high[v] ? x + 1 : low[v];
                int prv = x > low[v] ? x - 1 : high[v];
                moves.push_back({offset[nxt] + d, 1});
                moves.push_back({offset[prv] + d, 1});
                moves.push_back({states + v, 0});
                if (d) moves.push_back({s - 1, 1});
            }
            for (auto [t, cost] : moves) {
                if (now + cost < dist[t]) {
                    dist[t] = now + cost;
                    buckets[(now + cost) % (SLOWEST + 1)].push_back(t);
                    pending++;
                }
            }
        }
    }
    string out;
    for (int x = 0; x < n; x++) {
        int best = *min_element(dist.begin() + offset[x], dist.begin() + offset[x + 1]);
        out += to_string(best);
        out += x + 1 < n ? ' ' : '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
