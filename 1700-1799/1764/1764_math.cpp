#include <cstdio>
#include <vector>

typedef long long ll;
typedef std::vector<ll> Row;

const int ROUTES = 4, BRIDGES = 6;
// each bridge lies on exactly two of the four routes, one pair per bridge,
// in the input order: Nizhny Novgorod, Kotelnich, Perm, Kazan, Vyatskiye
// Polyany, Sarapul
const int PAIRS[BRIDGES][2] = {{0, 3}, {0, 2}, {2, 3}, {1, 2}, {1, 3}, {0, 1}};

struct Constraint {
    Row a;
    ll b;
};

// determinant of a small integer matrix, expanded along the first row
ll det(const std::vector<Row> &rows) {
    int n = rows.size();
    if (n == 1) return rows[0][0];
    ll total = 0;
    for (int j = 0; j < n; j++) {
        if (!rows[0][j]) continue;
        std::vector<Row> minor;
        for (int r = 1; r < n; r++) {
            Row row;
            for (int c = 0; c < n; c++)
                if (c != j) row.push_back(rows[r][c]);
            minor.push_back(row);
        }
        total += (j % 2 ? -1 : 1) * rows[0][j] * det(minor);
    }
    return total;
}

int main() {
    std::vector<Constraint> cons;
    for (int k = 0; k < BRIDGES; k++) {
        ll cap;
        if (scanf("%lld", &cap) != 1) return 0;
        Row a(ROUTES, 0);
        a[PAIRS[k][0]] = a[PAIRS[k][1]] = 1;
        cons.push_back({a, cap});
    }
    for (int i = 0; i < ROUTES; i++) {
        Row a(ROUTES, 0);
        a[i] = -1;
        cons.push_back({a, 0});
    }
    // the best plan is a corner where four constraints are tight; each
    // corner is solved exactly by Cramer's rule, as numerators over a
    // common positive denominator
    int total = cons.size();
    ll bestNum = -1, bestDen = 1;
    Row best;
    for (int mask = 0; mask < 1 << total; mask++) {
        if (__builtin_popcount(mask) != ROUTES) continue;
        std::vector<int> chosen;
        for (int k = 0; k < total; k++)
            if (mask >> k & 1) chosen.push_back(k);
        std::vector<Row> matrix;
        for (int k : chosen) matrix.push_back(cons[k].a);
        ll den = det(matrix);
        if (den == 0) continue;
        Row nums(ROUTES);
        for (int c = 0; c < ROUTES; c++) {
            std::vector<Row> swapped = matrix;
            for (int r = 0; r < ROUTES; r++) swapped[r][c] = cons[chosen[r]].b;
            nums[c] = det(swapped);
        }
        if (den < 0) {
            den = -den;
            for (ll &v : nums) v = -v;
        }
        bool ok = true;
        for (const Constraint &con : cons) {
            ll lhs = 0;
            for (int c = 0; c < ROUTES; c++) lhs += con.a[c] * nums[c];
            if (lhs > con.b * den) ok = false;
        }
        ll sum = 0;
        for (ll v : nums) sum += v;
        if (ok && sum * bestDen > bestNum * den) {
            bestNum = sum;
            bestDen = den;
            best = nums;
        }
    }
    for (int c = 0; c < ROUTES; c++) printf(c ? " %.3f" : "%.3f", (double)best[c] / bestDen);
    printf("\n");
    return 0;
}
