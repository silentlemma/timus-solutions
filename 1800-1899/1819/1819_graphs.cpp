#include <cstdint>
#include <cstdio>
#include <unordered_map>
#include <vector>

// splitmix64 with a fixed seed
const uint64_t SEED = 2010, GAMMA = 0x9e3779b97f4a7c15ULL;
const uint64_t MIX1 = 0xbf58476d1ce4e5b9ULL, MIX2 = 0x94d049bb133111ebULL;
const int SHIFT1 = 30, SHIFT2 = 27, SHIFT3 = 31;
uint64_t state = SEED;

uint64_t nextRandom() {
    uint64_t z = (state += GAMMA);
    z = (z ^ (z >> SHIFT1)) * MIX1;
    z = (z ^ (z >> SHIFT2)) * MIX2;
    return z ^ (z >> SHIFT3);
}

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    // half-edge h runs from ends[h] to ends[h ^ 1], and the half-edges of
    // a vertex are chained through head and nxt
    std::vector<int> ends(2 * k), head(n, -1), nxt(2 * k);
    for (int h = 0; h < 2 * k; h++) {
        scanf("%d", &ends[h]);
        ends[h]--;
        nxt[h] = head[ends[h]];
        head[ends[h]] = h;
    }
    std::vector<int> comp(n, -1), tin(n), parent(n, -1), upEdge(n, -1), order, stack;
    std::vector<int> it = head;
    for (int root = 0; root < n; root++) {
        if (comp[root] >= 0) continue;
        comp[root] = root;
        tin[root] = order.size();
        order.push_back(root);
        stack.push_back(root);
        while (!stack.empty()) {
            int v = stack.back(), h = it[v];
            if (h < 0) {
                stack.pop_back();
                continue;
            }
            it[v] = nxt[h];
            int w = ends[h ^ 1];
            if (comp[w] < 0) {
                comp[w] = root;
                parent[w] = v;
                upEdge[w] = h >> 1;
                tin[w] = order.size();
                order.push_back(w);
                stack.push_back(w);
            }
        }
    }
    // every non-tree edge joins a vertex and its ancestor; mark it with a
    // random value at both ends, so after summing over subtrees the edge
    // above v carries the xor of the non-tree edges passing over it
    std::vector<uint64_t> cover(n, 0);
    std::vector<int> count(n, 0);
    for (int e = 0; e < k; e++) {
        int a = ends[2 * e], b = ends[2 * e + 1];
        if (upEdge[a] == e || upEdge[b] == e) continue;
        if (tin[a] < tin[b]) std::swap(a, b);
        uint64_t r = nextRandom();
        cover[a] ^= r;
        cover[b] ^= r;
        count[a]++;
        count[b]--;
    }
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i], p = parent[v];
        if (p >= 0) {
            cover[p] ^= cover[v];
            count[p] += count[v];
        }
    }
    // a pair of edges is a cut exactly when it is a tree edge covered by
    // nothing but that non-tree edge, or two tree edges covered by the same
    // set; give tree edges values so that a path xors to zero iff it crosses no cut
    std::vector<uint64_t> value(n, 0);
    std::unordered_map<uint64_t, int> first;
    first.reserve(2 * n);
    for (int v : order) {
        if (parent[v] < 0) continue;
        if (count[v] < 2) {
            // a bridge or an edge with one cover: crossing it separates
            value[v] = nextRandom();
            continue;
        }
        // edges with one cover set lie on a chain and cut the tree into
        // pieces closed into a ring; a path inside the ring crosses all of
        // them or none of them, so the class must xor to zero
        int rep = first.emplace(cover[v], v).first->second;
        if (rep != v) {
            value[v] = nextRandom();
            value[rep] ^= value[v];
        }
    }
    std::vector<uint64_t> label(n, 0);
    for (int v : order) {
        if (parent[v] >= 0) label[v] = label[parent[v]] ^ value[v];
    }
    int q;
    scanf("%d", &q);
    std::vector<char> out;
    for (int i = 0; i < q; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        a--;
        b--;
        const char *word = comp[a] == comp[b] && label[a] == label[b] ? "Yes\n" : "No\n";
        for (const char *c = word; *c; c++) out.push_back(*c);
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
