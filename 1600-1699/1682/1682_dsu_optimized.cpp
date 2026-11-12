#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

const int CYCLE_MULTIPLE = 3;

struct DSU {
    std::vector<int32_t> parent{0};
    int find(int v) {
        int root = v;
        while (parent[root] >= 0)
            root = parent[root];
        while (v != root) {
            int next = parent[v];
            parent[v] = root;
            v = next;
        }
        return root;
    }
    bool join(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b)
            return false;
        if (parent[a] > parent[b])
            std::swap(a, b);
        parent[a] += parent[b];
        parent[b] = a;
        return true;
    }
};

int main() {
    int k = 0;
    if (scanf("%d", &k) != 1)
        return 0;
    std::vector<uint32_t> square(k), rootHead(k), rootNext(k), writtenHead(k), writtenNext{0};
    for (int s = 0; s < k; ++s) {
        uint32_t remainder = uint32_t(uint64_t(s) * s % k);
        square[s] = remainder ? uint32_t(k) - remainder : 0;
        rootNext[s] = rootHead[square[s]];
        rootHead[square[s]] = uint32_t(s + 1);
    }
    DSU dsu;
    for (int a = 1; a <= CYCLE_MULTIPLE * k; ++a) {
        dsu.parent.push_back(-1);
        int residue = a % k;
        auto connect = [&](uint32_t s) {
            for (uint32_t b = writtenHead[s]; b; b = writtenNext[b])
                if (!dsu.join(a, int(b)))
                    return false;
            return true;
        };
        if (!connect(square[residue])) {
            printf("%d\n", a);
            return 0;
        }
        for (uint32_t node = rootHead[residue]; node; node = rootNext[node - 1]) {
            uint32_t s = node - 1;
            if (s != square[residue] && !connect(s)) {
                printf("%d\n", a);
                return 0;
            }
        }
        writtenNext.push_back(writtenHead[residue]);
        writtenHead[residue] = uint32_t(a);
    }
    puts("-1");
}
