#include <algorithm>
#include <bitset>
#include <cstdio>
#include <map>
#include <string>
#include <vector>

using namespace std;

const int MAXN = 640;      // N^2 is at most 400 000
const int INDEX_BITS = 10; // edges are packed as length, then both indices
const long long INDEX_MASK = (1 << INDEX_BITS) - 1;
typedef bitset<MAXN + 1> Counts; // bit k: k bases are possible

int parent[MAXN];

int find(int x) {
    while (parent[x] != x)
        x = parent[x] = parent[parent[x]];
    return x;
}

string solve(const vector<long long> &xs, const vector<long long> &ys) {
    int n = xs.size();
    auto dist = [&](int a, int b) {
        return (xs[a] - xs[b]) * (xs[a] - xs[b]) + (ys[a] - ys[b]) * (ys[a] - ys[b]);
    };
    vector<long long> edges;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            edges.push_back(dist(i, j) << (2 * INDEX_BITS) | (long long)i << INDEX_BITS | j);
    sort(edges.begin(), edges.end());

    // the single-linkage tree: nodes 0 .. n-1 are the objects, then each
    // component formed after a group of equal distances is a new node
    vector<vector<int>> kids(n), members(n);
    vector<long long> width(n, 0), out(n, -1), compWidth(n, 0);
    vector<int> compNode(n);
    for (int i = 0; i < n; i++) {
        parent[i] = i;
        members[i] = {i};
        compNode[i] = i;
    }
    for (size_t e = 0; e < edges.size();) {
        long long w = edges[e] >> (2 * INDEX_BITS);
        map<int, vector<int>> grown; // a root -> the nodes it swallowed in this group
        for (; e < edges.size() && edges[e] >> (2 * INDEX_BITS) == w; e++) {
            int ra = find(edges[e] >> INDEX_BITS & INDEX_MASK), rb = find(edges[e] & INDEX_MASK);
            if (ra == rb)
                continue;
            long long far = max(compWidth[ra], compWidth[rb]);
            for (int p : members[ra])
                for (int q : members[rb])
                    far = max(far, dist(p, q));
            parent[rb] = ra;
            members[ra].insert(members[ra].end(), members[rb].begin(), members[rb].end());
            compWidth[ra] = far;
            vector<int> swallowed = grown.count(ra) ? grown[ra] : vector<int>{compNode[ra]};
            if (grown.count(rb)) {
                swallowed.insert(swallowed.end(), grown[rb].begin(), grown[rb].end());
                grown.erase(rb);
            } else
                swallowed.push_back(compNode[rb]);
            grown[ra] = swallowed;
        }
        for (auto &[root, swallowed] : grown) {
            for (int c : swallowed)
                out[c] = w;
            compNode[root] = kids.size();
            kids.push_back(swallowed);
            width.push_back(compWidth[root]);
            out.push_back(-1);
        }
    }

    // a node can be a base when it is narrower than its distance to the rest
    vector<Counts> counts(kids.size());
    for (size_t v = 0; v < kids.size(); v++) {
        if (out[v] < 0 || width[v] < out[v])
            counts[v][1] = 1;
        if (kids[v].empty())
            continue;
        Counts total;
        total[0] = 1;
        for (int c : kids[v]) {
            Counts combined;
            for (int k = 1; k <= n; k++)
                if (counts[c][k])
                    combined |= total << k;
            total = combined;
        }
        counts[v] |= total;
    }
    string s;
    for (int k = 1; k <= n; k++)
        s += counts.back()[k] ? '1' : '0';
    return s;
}

int main() {
    int n;
    while (scanf("%d", &n) == 1 && n > 0) {
        vector<long long> xs(n), ys(n);
        for (int i = 0; i < n; i++)
            scanf("%lld %lld", &xs[i], &ys[i]);
        printf("%s\n", solve(xs, ys).c_str());
    }
}
