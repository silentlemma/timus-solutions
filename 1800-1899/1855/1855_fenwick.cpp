#include <cstdio>
#include <vector>

// all sums are kept modulo 2^64: some of them overflow on the way, but the
// final total of a guild fits in a signed 64-bit number
using u64 = unsigned long long;

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    // sums of i and of i^2 for i up to x
    std::vector<u64> linear(n + 2, 0), square(n + 2, 0);
    for (int i = 1; i <= n + 1; i++) {
        linear[i] = linear[i - 1] + i;
        square[i] = square[i - 1] + (u64)i * i;
    }
    // toll t_i on segment i (cities i and i + 1) is the prefix sum of the
    // differences dif_j; the sum of i^k t_i over i <= x is
    // S_k(x) * (sum of dif_j) - (sum of dif_j * S_k(j - 1)) over j <= x
    int size = n + 1;
    std::vector<u64> plain(size + 1, 0), zero(size + 1, 0), one(size + 1, 0), two(size + 1, 0);
    auto add = [&](int j, u64 d) {
        u64 w0 = d * (j - 1), w1 = d * linear[j - 1], w2 = d * square[j - 1];
        for (; j <= size; j += j & -j) {
            plain[j] += d;
            zero[j] += w0;
            one[j] += w1;
            two[j] += w2;
        }
    };
    // the sums of t_i, i t_i and i^2 t_i over i <= x
    auto prefix = [&](int x, u64 &t0, u64 &t1, u64 &t2) {
        u64 s = 0, s0 = 0, s1 = 0, s2 = 0;
        for (int j = x; j > 0; j -= j & -j) {
            s += plain[j];
            s0 += zero[j];
            s1 += one[j];
            s2 += two[j];
        }
        t0 = x * s - s0;
        t1 = linear[x] * s - s1;
        t2 = square[x] * s - s2;
    };
    for (int e = 0; e < m; e++) {
        // "change" or "establish": the first letter tells them apart
        char kind;
        int a, b;
        scanf(" %c%*s %d %d", &kind, &a, &b);
        if (kind == 'c') {
            long long d;
            scanf("%lld", &d);
            add(a, (u64)d);
            add(b, (u64)-d);
            continue;
        }
        u64 h0, h1, h2, l0, l1, l2;
        prefix(b - 1, h0, h1, h2);
        prefix(a - 1, l0, l1, l2);
        // segment i lies on (i - a + 1)(b - i) of the guild's routes
        u64 total = (u64)(a + b - 1) * (h1 - l1) - (h2 - l2) +
                    (u64)((long long)b * (1 - a)) * (h0 - l0);
        long long routes = (long long)(b - a + 1) * (b - a) / 2;
        printf("%.8f\n", (double)(long long)total / routes);
    }
    return 0;
}
