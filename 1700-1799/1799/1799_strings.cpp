#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

const int ALPHABET = 26;

// suffix automaton; first[v] is the end of the first occurrence of v
struct Automaton {
    std::vector<std::array<int, ALPHABET>> next;
    std::vector<int> link, len, first;
    int last = 0;
    std::vector<int> prefix;  // the state of each prefix

    explicit Automaton(const std::string &s) {
        add(-1, 0, 0);
        for (int i = 0; i < (int)s.size(); i++) {
            extend(s[i] - 'a', i);
            prefix.push_back(last);
        }
    }

    int add(int parent, int length, int end) {
        std::array<int, ALPHABET> none;
        none.fill(-1);
        next.push_back(none);
        link.push_back(parent);
        len.push_back(length);
        first.push_back(end);
        return (int)len.size() - 1;
    }

    void extend(int c, int end) {
        int cur = add(0, len[last] + 1, end), p = last;
        while (p != -1 && next[p][c] == -1) {
            next[p][c] = cur;
            p = link[p];
        }
        if (p != -1) {
            int q = next[p][c];
            if (len[p] + 1 == len[q]) {
                link[cur] = q;
            } else {
                int clone = add(link[q], len[p] + 1, first[q]);
                next[clone] = next[q];
                while (p != -1 && next[p][c] == q) {
                    next[p][c] = clone;
                    p = link[p];
                }
                link[q] = link[cur] = clone;
            }
        }
        last = cur;
    }
};

// range add and range sum over positions 0 .. size - 1
struct Fenwick {
    std::vector<long long> plain, scaled;
    explicit Fenwick(int size) : plain(size + 1), scaled(size + 1) {}
    void point(std::vector<long long> &tree, int at, long long value) {
        for (at++; at < (int)tree.size(); at += at & -at) tree[at] += value;
    }
    long long prefix(int count) {  // sum over positions below count
        long long a = 0, b = 0;
        for (int at = count; at > 0; at -= at & -at) {
            a += plain[at];
            b += scaled[at];
        }
        return a * count - b;
    }
    void add(int from, int to, long long value) {  // positions from .. to - 1
        if (from >= to) return;
        point(plain, from, value);
        point(plain, to, -value);
        point(scaled, from, value * from);
        point(scaled, to, -value * to);
    }
};

long long swagness(const std::string &s) {
    int n = s.size();
    Automaton sam(s);
    int states = sam.len.size();
    std::vector<int> order(states);
    for (int v = 0; v < states; v++) order[v] = v;
    std::sort(order.begin(), order.end(), [&](int a, int b) { return sam.len[a] < sam.len[b]; });

    // a state with exactly one way out is squeezed into the edge through it
    std::vector<int> only(states, -1), target(states), extra(states, 0);
    std::vector<char> keep(states);
    for (int v = 0; v < states; v++) {
        int ways = 0;
        for (int c = 0; c < ALPHABET; c++) {
            if (sam.next[v][c] != -1) {
                ways++;
                only[v] = sam.next[v][c];
            }
        }
        keep[v] = v == 0 || ways != 1;
    }
    for (int k = states - 1; k >= 0; k--) {
        int v = order[k];
        if (keep[v]) {
            target[v] = v;
        } else {
            target[v] = target[only[v]];
            extra[v] = 1 + extra[only[v]];
        }
    }
    // the compressed edges and, for each, its label s[from .. to]
    struct Edge {
        int source, dest, from, to;
        long long distinct;
    };
    std::vector<Edge> edges;
    for (int u = 0; u < states; u++) {
        if (!keep[u]) continue;
        for (int c = 0; c < ALPHABET; c++) {
            int t = sam.next[u][c];
            if (t == -1) continue;
            int dest = target[t], to = sam.first[dest];
            edges.push_back({u, dest, to - extra[t], to, 0});
        }
    }

    // the suffix link tree in Euler order
    std::vector<std::vector<int>> children(states);
    for (int v = 1; v < states; v++) children[sam.link[v]].push_back(v);
    std::vector<int> tin(states), tout(states);
    {
        int timer = 0;
        std::vector<std::pair<int, size_t>> stack = {{0, 0}};
        tin[0] = timer++;
        while (!stack.empty()) {
            auto &[v, at] = stack.back();
            if (at == children[v].size()) {
                tout[v] = timer;
                stack.pop_back();
                continue;
            }
            int child = children[v][at++];
            tin[child] = timer++;
            stack.push_back({child, 0});
        }
    }
    // the latest end seen in a subtree, as a segment tree of maxima
    int size = 1;
    while (size < states) size *= 2;
    std::vector<int> latest(2 * size, 0);
    auto query = [&](int lo, int hi) {
        int best = 0;
        for (lo += size, hi += size; lo < hi; lo /= 2, hi /= 2) {
            if (lo & 1) best = std::max(best, latest[lo++]);
            if (hi & 1) best = std::max(best, latest[--hi]);
        }
        return best;
    };
    auto update = [&](int at, int value) {
        for (latest[at += size] = value; at > 1; at /= 2) {
            latest[at / 2] = std::max(latest[at], latest[at ^ 1]);
        }
    };

    std::vector<std::vector<int>> byEnd(n + 1);
    for (int e = 0; e < (int)edges.size(); e++) byEnd[edges[e].to + 1].push_back(e);
    // count[p]: distinct substrings of s[0 .. end) whose last occurrence
    // starts at p; the states on one suffix link path that share their
    // last end form chains, and top[end] is the state just above a chain
    Fenwick count(n);
    std::vector<char> seen(states, 0);
    seen[0] = 1;
    std::vector<int> top(n + 1, 0);
    for (int end = 1; end <= n; end++) {
        int v = sam.prefix[end - 1];
        count.add(end - sam.len[v], end, 1);
        int u = v;
        while (!seen[u]) {
            seen[u] = 1;
            u = sam.link[u];
        }
        while (u != 0) {
            int was = query(tin[u], tout[u]);
            int above = top[was];
            count.add(was - sam.len[u], was - sam.len[above], -1);
            top[was] = u;
            u = above;
        }
        update(tin[v], end);
        top[end] = 0;
        for (int e : byEnd[end]) {
            edges[e].distinct = count.prefix(end) - count.prefix(edges[e].from);
        }
    }

    // each compressed edge stands for as many tree edges as there are
    // paths from the root to its source
    std::vector<long long> paths(states, 0);
    paths[0] = 1;
    std::vector<std::vector<int>> out(states);
    for (int e = 0; e < (int)edges.size(); e++) out[edges[e].source].push_back(e);
    long long total = 0;
    for (int v : order) {
        if (!keep[v] || paths[v] == 0) continue;
        for (int e : out[v]) {
            total += paths[v] * edges[e].distinct;
            paths[edges[e].dest] += paths[v];
        }
    }
    return total;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n)) return 0;
    std::string s;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        std::cout << swagness(s) << "\n";
    }
    return 0;
}
