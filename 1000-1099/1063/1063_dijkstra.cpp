#include <array>
#include <cstdio>
#include <functional>
#include <map>
#include <queue>
#include <tuple>
#include <vector>

const int FACES = 6, MASKS = 1 << FACES;

// the faces split into connected groups, the faces that have dominoes and
// the faces of odd degree
struct State {
    std::array<int, FACES> group;
    int active, odd;
};

// relabels the groups in order of first appearance and packs the state
long long normalize(State &s) {
    std::array<int, FACES> name;
    name.fill(-1);
    int next = 0;
    long long code = 0;
    for (int v = 0; v < FACES; v++) {
        if (name[s.group[v]] < 0)
            name[s.group[v]] = next++;
        code = code * FACES + name[s.group[v]];
    }
    for (int v = 0; v < FACES; v++)
        s.group[v] = name[s.group[v]];
    return (code * MASKS + s.active) * MASKS + s.odd;
}

void join(State &s, int a, int b) {
    int ga = s.group[a], gb = s.group[b];
    for (int &g : s.group)
        if (g == gb)
            g = ga;
    s.active |= 1 << a | 1 << b;
    s.odd ^= 1 << a ^ 1 << b;
}

bool done(const State &s) {
    int group = -1;
    for (int v = 0; v < FACES; v++)
        if (s.active >> v & 1) {
            if (group >= 0 && s.group[v] != group)
                return false;
            group = s.group[v];
        }
    return __builtin_popcount(s.odd) <= 2;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    State start;
    for (int v = 0; v < FACES; v++)
        start.group[v] = v;
    start.active = start.odd = 0;
    for (int k = 0; k < n; k++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        join(start, a - 1, b - 1);
    }
    // Dijkstra over the states: adding the domino (a, b) costs a + b, joins
    // the groups of a and b and flips the parity of both faces
    std::map<long long, int> dist;
    std::map<long long, State> state;
    std::map<long long, std::tuple<long long, int, int>> parent;
    long long key = normalize(start);
    dist[key] = 0;
    state[key] = start;
    typedef std::pair<int, long long> item;
    std::priority_queue<item, std::vector<item>, std::greater<item>> heap;
    heap.push({0, key});
    while (!heap.empty()) {
        auto [d, k] = heap.top();
        heap.pop();
        if (d > dist[k])
            continue;
        if (done(state[k])) {
            key = k;
            break;
        }
        for (int a = 0; a < FACES; a++)
            for (int b = a + 1; b < FACES; b++) {
                State next = state[k];
                join(next, a, b);
                long long nk = normalize(next);
                int cost = d + (a + 1) + (b + 1);
                auto it = dist.find(nk);
                if (it == dist.end() || cost < it->second) {
                    dist[nk] = cost;
                    state[nk] = next;
                    parent[nk] = {k, a + 1, b + 1};
                    heap.push({cost, nk});
                }
            }
    }
    std::vector<std::pair<int, int>> added;
    for (long long k = key; parent.count(k); k = std::get<0>(parent[k]))
        added.push_back({std::get<1>(parent[k]), std::get<2>(parent[k])});
    printf("%d\n%d\n", dist[key], (int)added.size());
    for (auto [a, b] : added)
        printf("%d %d\n", a, b);
}
