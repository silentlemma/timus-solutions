#include <cstdio>
#include <cstdlib>
#include <numeric>

int main() {
    long long p, q, x, y, x1, y1;
    scanf("%lld %lld %lld %lld %lld %lld", &p, &q, &x, &y, &x1, &y1);
    long long dx = x1 - x, dy = y1 - y, g = std::gcd(std::llabs(p), std::llabs(q));
    bool ok;
    if (g == 0) {
        ok = dx == 0 && dy == 0;
    } else if (dx % g != 0 || dy % g != 0) {
        ok = false;
    } else {
        // with p/g and q/g coprime, the moves reach every point of the
        // lattice g Z^2, except that when both are odd every move keeps the
        // parity of (dx + dy) / g
        bool bothOdd = (p / g) % 2 != 0 && (q / g) % 2 != 0;
        ok = !bothOdd || (dx / g + dy / g) % 2 == 0;
    }
    printf(ok ? "YES\n" : "NO\n");
}
