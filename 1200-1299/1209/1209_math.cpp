#include <cmath>
#include <cstdio>
#include <string>

// Whether v is a perfect square, with the floating root corrected exactly.
static bool square(long long v) {
    long long r = (long long)std::sqrt((double)v);
    while (r * r > v) {
        r--;
    }
    while ((r + 1) * (r + 1) <= v) {
        r++;
    }
    return r * r == v;
}

int main() {
    const long long SQUARE = 8;
    int n;
    scanf("%d", &n);
    std::string out;
    for (int i = 0; i < n; i++) {
        long long k;
        scanf("%lld", &k);
        // the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
        // perfect square
        out += square(SQUARE * (k - 1) + 1) ? '1' : '0';
        out += i + 1 < n ? ' ' : '\n';
    }
    fputs(out.c_str(), stdout);
}
