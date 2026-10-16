#include <algorithm>
#include <cstdio>
#include <cstdint>
#include <utility>
#include <vector>

const int MOD = 3, SHIFT = 32;
typedef std::pair<uint32_t, uint32_t> Vec;  // the coordinates equal to 1 and to 2

// the sum of two vectors over GF(3) kept as two bit masks
Vec add(Vec a, Vec b) {
    uint32_t t = (a.first | b.second) ^ (a.second | b.first);
    return {(a.second | b.second) ^ t, (a.first | b.first) ^ t};
}

int main() {
    int k, n;
    if (scanf("%d %d", &k, &n) != 2) return 0;
    std::vector<std::vector<int>> m(n, std::vector<int>(k));
    std::vector<int> target(k);
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < n; j++) scanf("%d", &m[j][i]);
        scanf("%d", &target[i]);
    }
    // vectors w that are orthogonal to the column of every variable span the
    // null space of the transposed matrix, and y is Ax for some x exactly when
    // every such w is orthogonal to y
    std::vector<int> pivots;
    std::vector<char> isPivot(k, 0);
    for (int c = 0; c < k; c++) {
        int r = pivots.size(), sel = -1;
        for (int i = r; i < n && sel == -1; i++) {
            if (m[i][c]) sel = i;
        }
        if (sel == -1) continue;
        std::swap(m[r], m[sel]);
        if (m[r][c] == 2) {
            for (int &v : m[r]) v = v * 2 % MOD;
        }
        for (int i = 0; i < n; i++) {
            if (i == r || !m[i][c]) continue;
            int f = m[i][c];
            for (int j = 0; j < k; j++) m[i][j] = ((m[i][j] - f * m[r][j]) % MOD + MOD) % MOD;
        }
        pivots.push_back(c);
        isPivot[c] = 1;
    }
    int rank = pivots.size();
    std::vector<std::vector<int>> basis;
    for (int free = 0; free < k; free++) {
        if (isPivot[free]) continue;
        std::vector<int> w(k, 0);
        w[free] = 1;
        for (int i = 0; i < rank; i++) w[pivots[i]] = (MOD - m[i][free]) % MOD;
        basis.push_back(w);
    }
    // the change that y_i = 1 makes to the syndromes w . y over the basis,
    // and y_i = 2 makes the opposite change, the two masks swapped
    std::vector<Vec> unit(k, {0, 0});
    for (int i = 0; i < k; i++) {
        for (size_t j = 0; j < basis.size(); j++) {
            if (basis[j][i] == 1) unit[i].first |= 1u << j;
            if (basis[j][i] == 2) unit[i].second |= 1u << j;
        }
    }
    auto syndromes = [&](int from, int to) {
        std::vector<Vec> sums = {{0, 0}};
        for (int i = from; i < to; i++) {
            std::vector<Vec> next;
            for (Vec s : sums) {
                for (int v = 0; v < MOD; v++) {
                    if (v == target[i]) continue;
                    Vec negated = {unit[i].second, unit[i].first};
                    next.push_back(v == 0 ? s : add(s, v == 1 ? unit[i] : negated));
                }
            }
            sums.swap(next);
        }
        return sums;
    };
    // every y_i has two allowed values: meet in the middle on syndromes
    int half = k / 2;
    std::vector<uint64_t> left;
    for (Vec s : syndromes(0, half)) left.push_back((uint64_t)s.first << SHIFT | s.second);
    std::sort(left.begin(), left.end());
    long long total = 0;
    for (Vec s : syndromes(half, k)) {
        uint64_t key = (uint64_t)s.second << SHIFT | s.first;
        auto range = std::equal_range(left.begin(), left.end(), key);
        total += range.second - range.first;
    }
    for (int i = rank; i < n; i++) total *= MOD;
    printf("%lld\n", total);
    return 0;
}
