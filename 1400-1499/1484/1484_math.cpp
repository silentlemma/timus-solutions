#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;
const ll TOP = 10;    // the highest vote
const ll HALVES = 20; // a rating counts in half tenths
const int TEXT = 16;

ll tenths(const char *s) {
    ll whole = 0, part = 0;
    const char *dot = strchr(s, '.');
    for (const char *c = s; *c && c != dot; c++)
        whole = whole * 10 + (*c - '0');
    if (dot && dot[1])
        part = dot[1] - '0';
    return whole * 10 + part;
}

int main() {
    char xs[TEXT], ys[TEXT];
    ll n;
    scanf("%15s %15s %lld", xs, ys, &n);
    ll x = tenths(xs), y = tenths(ys);
    // n votes from 1 to 10 show x when (2x - 1) n <= 20 sum < (2x + 1) n,
    // and the worst case is the largest such sum, and there may be none at all
    ll total = min(TOP * n, ((2 * x + 1) * n - 1) / HALVES);
    ll least = max(n, ((2 * x - 1) * n + HALVES - 1) / HALVES);
    // k votes of 1 show at most y when 20 (total + k) < (2y + 1)(n + k)
    ll excess = HALVES * total - (2 * y + 1) * n, step = 2 * y + 1 - HALVES;
    if (least > total || (excess >= 0 && step <= 0))
        puts("Impossible");
    else if (excess < 0)
        puts("0");
    else
        printf("%lld\n", excess / step + 1);
}
