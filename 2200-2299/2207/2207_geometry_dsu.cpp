#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>

using namespace std;
using Int = long long;
constexpr Int INF = 10'000'000'000LL;

struct Dsu {
    vector<int> parent;
    explicit Dsu(int n) : parent(n, -1) {}
    int find(int v) {
        if (parent[v] < 0)
            return v;
        return parent[v] = find(parent[v]);
    }
    bool join(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b)
            return false;
        if (parent[a] > parent[b])
            swap(a, b);
        parent[a] += parent[b];
        parent[b] = a;
        return true;
    }
};

struct Sweep {
    vector<int> order, rank;
    vector<Int> value;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int width, height, n, m;
    cin >> width >> height >> n >> m;
    int count = n + m;
    vector<Int> x(count), y(count), people(count), jobs(count);
    Int total_people = 0, total_jobs = 0;
    for (int i = 0; i < count; ++i) {
        Int amount;
        cin >> x[i] >> y[i] >> amount;
        if (i < n)
            total_people += people[i] = amount;
        else
            total_jobs += jobs[i] = amount;
    }
    Int target = min(total_people, total_jobs);
    vector<Int> ys = y;
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    int span = static_cast<int>(ys.size());
    vector<Sweep> sweeps;
    for (int sx : {1, -1}) {
        for (int sy : {1, -1}) {
            Sweep s;
            s.order.resize(count);
            s.rank.resize(count);
            s.value.resize(count + 1, -INF);
            iota(s.order.begin(), s.order.end(), 0);
            sort(s.order.begin(), s.order.end(), [&](int a, int b) {
                return make_pair(sx * x[a], sy * y[a]) < make_pair(sx * x[b], sy * y[b]);
            });
            for (int i = 0; i < count; ++i) {
                int rank = static_cast<int>(lower_bound(ys.begin(), ys.end(), y[i]) - ys.begin());
                s.rank[i] = sy == 1 ? rank + 1 : span - rank;
                s.value[i] = sx * x[i] + sy * y[i];
            }
            sweeps.push_back(move(s));
        }
    }

    Dsu dsu(count);
    int components = count;
    vector<tuple<Int, int, int>> edges;
    while (components > 1) {
        vector<int> roots(count + 1, -1), from(count, -1), to(count, -1);
        vector<Int> best(count, INF);
        for (int i = 0; i < count; ++i)
            roots[i] = dsu.find(i);
        for (const Sweep &s : sweeps) {
            array<vector<int>, 2> first, second;
            for (int color = 0; color < 2; ++color) {
                first[color].assign(span + 1, count);
                second[color].assign(span + 1, count);
            }
            for (int i : s.order) {
                int color = i >= n, root = roots[i], candidate = count;
                for (int k = s.rank[i]; k > 0; k -= k & -k) {
                    int v = first[1 - color][k];
                    if (roots[v] == root)
                        v = second[1 - color][k];
                    if (s.value[v] > s.value[candidate])
                        candidate = v;
                }
                if (candidate != count && s.value[i] - s.value[candidate] < best[root]) {
                    best[root] = s.value[i] - s.value[candidate];
                    from[root] = i;
                    to[root] = candidate;
                }
                // Two maxima from distinct frozen components suffice for every query.
                for (int k = s.rank[i]; k <= span; k += k & -k) {
                    int v = first[color][k];
                    if (s.value[i] > s.value[v]) {
                        if (roots[v] != root)
                            second[color][k] = v;
                        first[color][k] = i;
                    } else if (roots[v] != root && s.value[i] > s.value[second[color][k]]) {
                        second[color][k] = i;
                    }
                }
            }
        }
        for (int r = 0; r < count; ++r) {
            if (from[r] != -1 && dsu.join(from[r], to[r])) {
                edges.emplace_back(best[r], from[r], to[r]);
                --components;
            }
        }
    }
    sort(edges.begin(), edges.end());
    dsu = Dsu(count);
    Int score = 0;
    for (auto [distance, u, v] : edges) {
        int a = dsu.find(u), b = dsu.find(v);
        score -= min(people[a], jobs[a]) + min(people[b], jobs[b]);
        Int population = people[a] + people[b], capacity = jobs[a] + jobs[b];
        dsu.join(a, b);
        int root = dsu.find(a);
        people[root] = population;
        jobs[root] = capacity;
        score += min(population, capacity);
        if (score == target) {
            cout << target << ' ' << distance << '\n';
            break;
        }
    }
}
