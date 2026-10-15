#include <algorithm>
#include <cstdio>
#include <vector>

std::vector<int> parent;

int find(int x) {
    int root = x;
    while (parent[root] != root) {
        root = parent[root];
    }
    while (parent[x] != root) {
        int next = parent[x];
        parent[x] = root;
        x = next;
    }
    return root;
}

int main() {
    long long k;
    scanf("%lld", &k);
    // roots[v]: the residues s with v + s * s = 0 (mod k), the residues of
    // the earlier numbers b joined to a number a = v by a + b * b = 0
    std::vector<std::vector<int>> roots(k), written(k);
    for (long long s = 0; s < k; s++) {
        roots[(k - s * s % k) % k].push_back(s);
    }
    parent.push_back(0);
    for (int a = 1;; a++) {
        parent.push_back(a);
        long long r = a % k;
        std::vector<int> near = roots[r];
        near.push_back((k - r * r % k) % k);
        std::sort(near.begin(), near.end());
        near.erase(std::unique(near.begin(), near.end()), near.end());
        for (int s : near) {
            for (int b : written[s]) {
                // every edge either joins two trees or closes the first cycle
                int ra = find(a), rb = find(b);
                if (ra == rb) {
                    printf("%d\n", a);
                    return 0;
                }
                parent[rb] = ra;
            }
        }
        written[r].push_back(a);
    }
}
