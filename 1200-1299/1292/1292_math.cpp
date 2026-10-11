#include <cstdio>

const long long FIXED = 153; // 1 + 125 + 27: every multiple of 3 ends here
const long long TEN = 10;
const int FIELDS = 3;

long long cubes(long long x) {
    long long s = 0;
    for (; x > 0; x /= TEN) {
        long long d = x % TEN;
        s += d * d * d;
    }
    return s;
}

int main() {
    int t = 0;
    if (scanf("%d", &t) != 1)
        return 0;
    for (int i = 0; i < t; i++) {
        long long n = 0, k = 0, l = 0;
        if (scanf("%lld %lld %lld", &n, &k, &l) != FIELDS)
            return 0;
        // the gap before base N is F applied N - 1 times to K; from a
        // multiple of 3 it reaches 153 within 14 steps and stays there
        long long gap = k;
        for (long long step = 0; step < n - 1 && gap != FIXED; step++)
            gap = cubes(gap);
        printf("%lld\n", gap - l);
    }
    return 0;
}
