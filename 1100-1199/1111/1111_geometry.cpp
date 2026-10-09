#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <vector>

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const long long POINT_DEN = 4, SQUARE_DEN = 8;

struct Fraction {
    long long num, den;
};

// squared distance from P to the square with diagonal (x1, y1)-(x2, y2)
Fraction distance(long long x1, long long y1, long long x2, long long y2, long long px,
                  long long py) {
    // doubled coordinates of P relative to the centre, and the diagonal
    long long qx = 2 * px - x1 - x2, qy = 2 * py - y1 - y2;
    long long dx = x2 - x1, dy = y2 - y1, h = dx * dx + dy * dy;
    if (h == 0)
        return {qx * qx + qy * qy, POINT_DEN};
    // projections on the two side directions, the diagonal turned by +-45
    // degrees; inside the square both stay within h
    long long s1 = llabs(qx * (dx - dy) + qy * (dy + dx));
    long long s2 = llabs(qx * (dx + dy) + qy * (dy - dx));
    long long a = std::max(0LL, s1 - h), b = std::max(0LL, s2 - h);
    return {a * a + b * b, SQUARE_DEN * h};
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<long long> x1(n), y1(n), x2(n), y2(n);
    for (int i = 0; i < n; i++)
        scanf("%lld %lld %lld %lld", &x1[i], &y1[i], &x2[i], &y2[i]);
    long long px, py;
    scanf("%lld %lld", &px, &py);
    std::vector<Fraction> dist(n);
    for (int i = 0; i < n; i++)
        dist[i] = distance(x1[i], y1[i], x2[i], y2[i], px, py);
    // the cross products reach about 10^28, hence 128 bits
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::stable_sort(order.begin(), order.end(), [&](int i, int j) {
        return (__int128)dist[i].num * dist[j].den < (__int128)dist[j].num * dist[i].den;
    });
    for (int i = 0; i < n; i++)
        printf(i + 1 < n ? "%d " : "%d\n", order[i] + 1);
}
