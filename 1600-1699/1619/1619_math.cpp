#include <cstdio>

int main() {
    int t;
    if (scanf("%d", &t) != 1)
        return 0;
    while (t--) {
        long long k, m;
        if (scanf("%lld %lld", &k, &m) != 2)
            return 0;
        // the ballot theorem: the elder stays ahead or level with this chance
        if (m > k)
            printf("0\n");
        else
            printf("%.10f\n", double(k - m + 1) / double(k + 1));
    }
}
