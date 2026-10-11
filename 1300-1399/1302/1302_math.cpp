#include <cmath>
#include <cstdio>
#include <cstdlib>

typedef long long ll;

const int AXES = 3; // the row and the two diagonal strips

// the row of cell n and its two diagonal strips, from the left and from
// the right; one step across an edge changes exactly one of them
void strips(ll n, ll out[AXES]) {
    ll row = (ll)std::sqrt((double)(n - 1));
    while (row * row > n - 1)
        row--;
    while ((row + 1) * (row + 1) <= n - 1)
        row++;
    row++;
    ll place = n - (row - 1) * (row - 1); // 1 .. 2 row - 1 within the row
    out[0] = row;
    out[1] = (place + 1) / 2;
    out[2] = (2 * row - place + 1) / 2;
}

int main() {
    ll m = 0, n = 0;
    if (scanf("%lld %lld", &m, &n) != 2)
        return 0;
    ll a[AXES], b[AXES];
    strips(m, a);
    strips(n, b);
    printf("%lld\n", llabs(a[0] - b[0]) + llabs(a[1] - b[1]) + llabs(a[2] - b[2]));
    return 0;
}
