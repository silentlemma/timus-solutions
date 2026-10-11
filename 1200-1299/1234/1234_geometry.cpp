#include <algorithm>
#include <cmath>
#include <cstdio>

const int TENTHS = 10, BRICK_SIDES = 3, HOLE_SIDES = 2;

// whether a p x q rectangle (p >= q) fits into an a x b one (a >= b); a
// turned fit (p > a, q <= b) needs ((a+b)/(p+q))^2 + ((a-b)/(p-q))^2 >= 2
// by Carver's criterion, multiplied out here to stay in integers
bool fits(long long p, long long q, long long a, long long b) {
    if (q > b)
        return false;
    if (p <= a)
        return true;
    long long s = (p + q) * (p + q), d = (p - q) * (p - q);
    return (a + b) * (a + b) * d + (a - b) * (a - b) * s >= 2 * s * d;
}

int main() {
    long long brick[BRICK_SIDES], hole[HOLE_SIDES];
    for (long long &x : brick) {
        double v;
        scanf("%lf", &v);
        x = std::llround(v * TENTHS);
    }
    for (long long &x : hole) {
        double v;
        scanf("%lf", &v);
        x = std::llround(v * TENTHS);
    }
    std::sort(brick, brick + BRICK_SIDES);
    std::sort(hole, hole + HOLE_SIDES);
    // the face of the two shorter sides is the easiest to put through
    puts(fits(brick[1], brick[0], hole[1], hole[0]) ? "YES" : "NO");
}
