#include <algorithm>
#include <cstdio>

// stdio only: the memory limit is half a megabyte
const int MAXN = 1000;

int need[MAXN];   // goblets each knight still has to gain (or lose)
int visits[MAXN]; // signed visits to the pair (i, i + K); + brings, - takes
int cycle[MAXN], sgn[MAXN], base[MAXN], cut[MAXN];

int main() {
    int n, k, f;
    scanf("%d %d %d", &n, &k, &f);
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        need[i] = f - a;
    }
    static bool seen[MAXN];
    for (int s = 0; s < n; s++) {
        if (seen[s])
            continue;
        // the knights s, s + K, s + 2K, ... form a cycle; pair e_i joins the
        // i-th and the next. With x_0 = t, the rule x_(i-1) + x_i = need of
        // the i-th knight gives x_i = sgn_i * t + base_i
        int len = 0;
        for (int v = s; !seen[v]; v = (v + k) % n) {
            seen[v] = true;
            cycle[len++] = v;
        }
        sgn[0] = 1, base[0] = 0;
        for (int i = 1; i < len; i++)
            sgn[i] = -sgn[i - 1], base[i] = need[cycle[i]] - base[i - 1];
        // the last pair and the first must give the first knight its share
        int rest = need[cycle[0]] - base[len - 1];
        long long t;
        if (len % 2 == 1) {
            // odd cycle: 2t = rest, a single solution
            if (rest % 2 != 0) {
                printf("-1\n");
                return 0;
            }
            t = rest / 2;
        } else {
            // even cycle: any t works if rest is 0; the sum of |t - cut_i|
            // is least at a median
            if (rest != 0) {
                printf("-1\n");
                return 0;
            }
            for (int i = 0; i < len; i++)
                cut[i] = -base[i] * sgn[i];
            std::nth_element(cut, cut + len / 2, cut + len);
            t = cut[len / 2];
        }
        for (int i = 0; i < len; i++)
            visits[cycle[i]] = sgn[i] * t + base[i];
    }
    long long total = 0;
    for (int i = 0; i < n; i++)
        total += visits[i] < 0 ? -visits[i] : visits[i];
    printf("%lld\n", total);
    // bring everything first, so that no knight ever runs short
    for (int pass = 0; pass < 2; pass++)
        for (int i = 0; i < n; i++) {
            int x = visits[i];
            if ((pass == 0 && x > 0) || (pass == 1 && x < 0))
                for (int r = 0; r < (x < 0 ? -x : x); r++)
                    printf("%d %d %c\n", i + 1, (i + k) % n + 1, pass == 0 ? '+' : '-');
        }
}
