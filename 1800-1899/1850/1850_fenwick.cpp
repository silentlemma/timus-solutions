#include <algorithm>
#include <cstdio>
#include <tuple>
#include <vector>

int main() {
    int n, s, d;
    if (scanf("%d", &n) != 1) return 0;
    scanf("%d %d", &s, &d);
    std::vector<std::pair<int, int>> planets(n);
    for (auto &p : planets) scanf("%d %d", &p.first, &p.second);
    std::sort(planets.begin(), planets.end());
    std::vector<int> dist(n), race(n);
    for (int i = 0; i < n; i++) std::tie(dist[i], race[i]) = planets[i];
    // pieces of planets with gaps of at most d: the tourist moves only
    // inside a piece cut by the range [low, high]
    std::vector<int> piece(n, 0), first = {0};
    for (int i = 1; i < n; i++) {
        if (dist[i] - dist[i - 1] > d) first.push_back(i);
        piece[i] = first.size() - 1;
    }
    first.push_back(n);
    int pieces = first.size() - 1;
    // head[i]: races from the start of i's piece to i; tail[i]: from i to its
    // end; whole[p]: races of piece p
    std::vector<int> head(n), tail(n), whole(pieces), mark(s + 1, -1);
    for (int p = 0; p < pieces; p++) {
        int seen = 0;
        for (int i = first[p]; i < first[p + 1]; i++) {
            if (mark[race[i]] != p) {
                mark[race[i]] = p;
                seen++;
            }
            head[i] = seen;
        }
        whole[p] = seen;
        seen = 0;
        for (int i = first[p + 1] - 1; i >= first[p]; i--) {
            if (mark[race[i]] != -2 - p) {
                mark[race[i]] = -2 - p;
                seen++;
            }
            tail[i] = seen;
        }
    }
    // sparse table of the largest whole piece over ranges of pieces
    std::vector<std::vector<int>> table = {whole};
    for (int step = 1; 2 * step <= pieces; step *= 2) {
        const auto &last = table.back();
        std::vector<int> next(pieces - 2 * step + 1);
        for (size_t i = 0; i < next.size(); i++) next[i] = std::max(last[i], last[i + step]);
        table.push_back(next);
    }
    auto largest = [&](int lo, int hi) {
        // the largest whole piece among pieces lo..hi - 1
        if (lo >= hi) return 0;
        int level = std::__lg(hi - lo);
        return std::max(table[level][lo], table[level][hi - (1 << level)]);
    };
    int m;
    scanf("%d", &m);
    std::vector<int> answer(m, 0);
    std::vector<std::tuple<int, int, int>> inside;  // (right, left, tourist)
    for (int t = 0; t < m; t++) {
        int low, high;
        scanf("%d %d", &low, &high);
        int lo = std::lower_bound(dist.begin(), dist.end(), low) - dist.begin();
        int hi = std::upper_bound(dist.begin(), dist.end(), high) - dist.begin() - 1;
        if (lo > hi) continue;
        if (piece[lo] == piece[hi]) {
            inside.emplace_back(hi, lo, t);
        } else {
            answer[t] = std::max({tail[lo], head[hi], largest(piece[lo] + 1, piece[hi])});
        }
    }
    // distinct races in a range: going right, count each race only at its
    // latest planet, in a Fenwick tree
    std::sort(inside.begin(), inside.end());
    std::vector<int> tree(n + 1, 0), latest(s + 1, -1);
    auto add = [&](int k, int v) {
        for (k++; k <= n; k += k & -k) tree[k] += v;
    };
    auto prefix = [&](int k) {
        int total = 0;
        for (; k > 0; k -= k & -k) total += tree[k];
        return total;
    };
    size_t j = 0;
    for (int i = 0; i < n; i++) {
        if (latest[race[i]] >= 0) add(latest[race[i]], -1);
        latest[race[i]] = i;
        add(i, 1);
        for (; j < inside.size() && std::get<0>(inside[j]) == i; j++) {
            answer[std::get<2>(inside[j])] = prefix(i + 1) - prefix(std::get<1>(inside[j]));
        }
    }
    for (int a : answer) printf("%d\n", a);
    return 0;
}
