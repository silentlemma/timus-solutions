#include <algorithm>
#include <cmath>
#include <cstdio>

const int DIM = 8;

int main() {
    long long a[DIM], b[DIM], c[DIM], r;
    for (long long &x : a)
        scanf("%lld", &x);
    for (long long &x : b)
        scanf("%lld", &x);
    for (long long &x : c)
        scanf("%lld", &x);
    scanf("%lld", &r);
    long long length2 = 0, ca2 = 0, cb2 = 0, dot = 0;
    for (int i = 0; i < DIM; i++) {
        long long ab = b[i] - a[i], ac = c[i] - a[i], bc = c[i] - b[i];
        length2 += ab * ab, ca2 += ac * ac, cb2 += bc * bc, dot += ab * ac;
    }
    // the segment enters the ball when the closest point of it to C lies
    // strictly inside; outside 0 <= t <= 1 the closest point is an end, and
    // both ends are outside: |AC|^2 |AB|^2 - (AB . AC)^2 < R^2 |AB|^2
    if (length2 == 0 || dot <= 0 || dot >= length2 ||
        ca2 * length2 - dot * dot >= r * r * length2) {
        printf("%.2f\n", std::sqrt((double)length2));
        return 0;
    }
    // otherwise, in the plane of A, B and C: a tangent from A, an arc of the
    // great circle and a tangent to B
    double da = std::sqrt((double)ca2), db = std::sqrt((double)cb2);
    double angle = std::acos(std::max(-1.0, std::min(1.0, (ca2 + cb2 - length2) / (2 * da * db))));
    double arc = angle - std::acos(r / da) - std::acos(r / db);
    printf("%.2f\n", std::sqrt((double)(ca2 - r * r)) + std::sqrt((double)(cb2 - r * r)) + r * arc);
}
