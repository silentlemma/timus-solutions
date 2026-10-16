#include <cstdio>
#include <vector>

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    std::vector<bool> broken(n, false);
    for (int i = 0; i < k; i++) {
        int x;
        scanf("%d", &x);
        broken[x - 1] = true;
    }
    std::vector<int> primes;
    int m = n;
    for (int d = 2; d * d <= m; d++) {
        if (m % d == 0) {
            primes.push_back(d);
            while (m % d == 0) m /= d;
        }
    }
    if (m > 1) primes.push_back(m);
    // a balanced set of tips is a union of disjoint regular p-gons and q-gons,
    // and blades n / (p q) apart form a p by q grid whose rows are the q-gons
    // and whose columns are the p-gons
    int p = primes[0], q = primes.size() > 1 ? primes[1] : 1;
    int classes = n / (p * q);
    std::vector<int> remove;
    for (int base = 0; base < classes; base++) {
        std::vector<bool> badRow(p, false), badCol(q, false);
        int rows = 0, cols = 0;
        for (int t = 0; t < p * q; t++) {
            if (!broken[base + t * classes]) continue;
            if (!badRow[t % p]) rows++;
            if (!badCol[t % q]) cols++;
            badRow[t % p] = badCol[t % q] = true;
        }
        if (rows == 0) continue;
        // a row and a column always share a cell, so the kept blades are
        // either all clean rows or all clean columns, whichever hold more, and
        // with one prime the rows are single blades that never balance
        bool byRows = q > 1 && (p - rows) * q >= (q - cols) * p;
        for (int t = 0; t < p * q; t++) {
            int c = base + t * classes;
            bool dropped = byRows ? badRow[t % p] : badCol[t % q];
            if (dropped && !broken[c]) remove.push_back(c + 1);
        }
    }
    if ((int)remove.size() + k == n) {
        printf("-1\n");
        return 0;
    }
    printf("%d\n", (int)remove.size());
    for (size_t i = 0; i < remove.size(); i++) printf(i ? " %d" : "%d", remove[i]);
    printf("\n");
    return 0;
}
