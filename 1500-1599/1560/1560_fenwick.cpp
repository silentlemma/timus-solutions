#include <cstdio>
#include <vector>
using namespace std;

const int MOST = 4; // the highest K asked for

long long power(long long b, long long e, long long mod) {
    long long r = 1;
    for (b %= mod; e > 0; e >>= 1, b = b * b % mod)
        if (e & 1)
            r = r * b % mod;
    return r;
}

int main() {
    int n, m;
    long long mod;
    if (scanf("%d %d", &n, &m) != 2 || scanf("%lld", &mod) != 1)
        return 0;
    vector<long long> values(n + 1);
    // trees[j] is a Fenwick tree of the power sums of a^j for j = 1..4; the
    // sums stay unreduced and are only reduced when a query reads them
    vector<vector<long long>> trees(MOST + 1, vector<long long>(n + 1, 0));
    for (int i = 1; i <= n; i++) {
        long long a;
        if (scanf("%lld", &a) != 1)
            return 0;
        values[i] = (a % mod + mod) % mod;
        long long p = 1;
        for (int j = 1; j <= MOST; j++) {
            p = p * values[i] % mod;
            trees[j][i] += p;
        }
    }
    for (int j = 1; j <= MOST; j++)
        for (int i = 1; i <= n; i++)
            if (i + (i & -i) <= n)
                trees[j][i + (i & -i)] += trees[j][i];
    long long inverse[MOST + 1] = {0};
    for (int k = 1; k <= MOST; k++)
        inverse[k] = power(k, mod - 2, mod);
    for (int q = 0; q < m; q++) {
        char kind[2];
        if (scanf("%1s", kind) != 1)
            return 0;
        if (kind[0] == 'I') {
            int i;
            long long delta;
            if (scanf("%d %lld", &i, &delta) != 2)
                return 0;
            long long old = values[i], now = ((old + delta) % mod + mod) % mod;
            values[i] = now;
            long long po = 1, pn = 1;
            for (int j = 1; j <= MOST; j++) {
                po = po * old % mod, pn = pn * now % mod;
                for (int k = i; k <= n; k += k & -k)
                    trees[j][k] += pn - po;
            }
        } else {
            int left, right, top;
            if (scanf("%d %d", &left, &right) != 2 || scanf("%d", &top) != 1)
                return 0;
            long long sums[MOST + 1] = {0}, e[MOST + 1] = {1};
            for (int j = 1; j <= top; j++) {
                long long total = 0;
                for (int k = right; k > 0; k -= k & -k)
                    total += trees[j][k];
                for (int k = left - 1; k > 0; k -= k & -k)
                    total -= trees[j][k];
                sums[j] = (total % mod + mod) % mod;
            }
            // Newton's identities: k e(k) is the alternating sum of e(k - i) p(i)
            for (int k = 1; k <= top; k++) {
                long long acc = 0;
                for (int i = 1; i <= k; i++) {
                    long long term = e[k - i] * sums[i] % mod;
                    acc += i % 2 ? term : mod - term;
                }
                e[k] = acc % mod * inverse[k] % mod;
            }
            for (int k = 0; k <= top; k++)
                printf(k ? " %lld" : "%lld", e[k]);
            printf("\n");
        }
    }
}
