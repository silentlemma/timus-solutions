#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

typedef long long ll;

const ll MOST = 1000000000;  // nobody but Vasily earns more; nobody earns less than 0

std::vector<int> parent, sizes;
std::vector<ll> offset;

int find(int x) {
    std::vector<int> path;
    while (parent[x] != x) {
        path.push_back(x);
        x = parent[x];
    }
    // compress: walk back from the node nearest to the root
    ll total = 0;
    for (auto it = path.rbegin(); it != path.rend(); ++it) {
        total += offset[*it];
        offset[*it] = total;
        parent[*it] = x;
    }
    return x;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    // a weighted union-find: salary[x] = salary[root] + offset[x], and every
    // root keeps the range its own salary may take so that all salaries of
    // its set stay in [0, MOST]; Vasily (0) is pinned to 0
    parent.resize(n);
    sizes.assign(n, 1);
    offset.assign(n, 0);
    std::vector<ll> low(n, 0), high(n, MOST);
    high[0] = 0;
    for (int x = 0; x < n; x++) {
        parent[x] = x;
    }
    for (int k = 1; k <= m; k++) {
        int i, j;
        ll d;
        scanf("%d %d %lld", &i, &j, &d);
        int ri = find(i), rj = find(j);
        // salary[i] - salary[j] = d means salary[rj] = salary[ri] + shift
        ll shift = offset[i] - offset[j] - d;
        bool ok;
        if (ri == rj) {
            ok = shift == 0;
        } else {
            if (sizes[ri] < sizes[rj]) {
                std::swap(ri, rj);
                shift = -shift;
            }
            // salary[rj] lies in [low[rj], high[rj]], so salary[ri] in that minus shift
            low[ri] = std::max(low[ri], low[rj] - shift);
            high[ri] = std::min(high[ri], high[rj] - shift);
            ok = low[ri] <= high[ri];
            parent[rj] = ri;
            offset[rj] = shift;
            sizes[ri] += sizes[rj];
        }
        if (!ok) {
            printf("Impossible after %d statements\n", k);
            return 0;
        }
    }
    std::string out = "Possible\n";
    for (int x = 0; x < n; x++) {
        int r = find(x);
        out += std::to_string(low[r] + offset[x]) + "\n";
    }
    fputs(out.c_str(), stdout);
}
