#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>

// all comparisons are exact: the center is (ux / d, uy / d) and the radius
// times d is the square root of rho2
typedef __int128 big;

big d, ux, uy, rho2;

int sign(big v) { return (v > 0) - (v < 0); }

// the sign of alpha - gamma * sqrt(rho2)
int sign_minus(big alpha, big gamma) {
    if (gamma == 0)
        return sign(alpha);
    if (gamma > 0)
        return alpha <= 0 ? -1 : sign(alpha * alpha - gamma * gamma * rho2);
    return alpha >= 0 ? 1 : sign(gamma * gamma * rho2 - alpha * alpha);
}

// the smallest integer k with k >= (u + sqrt(rho2)) / d
long long ceil_plus(big u) {
    long long k = (long long)std::floor(((double)u + std::sqrt((double)rho2)) / (double)d) - 2;
    while (true) {
        big t = k * d - u;
        if (t >= 0 && t * t >= rho2)
            return k;
        k++;
    }
}

// the largest integer k with k <= (u - sqrt(rho2)) / d
long long floor_minus(big u) {
    long long k = (long long)std::ceil(((double)u - std::sqrt((double)rho2)) / (double)d) + 2;
    while (true) {
        big t = u - k * d;
        if (t >= 0 && t * t >= rho2)
            return k;
        k--;
    }
}

int main() {
    long long ax, ay, bx, by, cx, cy;
    std::cin >> ax >> ay >> bx >> by >> cx >> cy;
    long long a2 = ax * ax + ay * ay, b2 = bx * bx + by * by, c2 = cx * cx + cy * cy;
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
    ux = (big)a2 * (by - cy) + (big)b2 * (cy - ay) + (big)c2 * (ay - by);
    uy = (big)a2 * (cx - bx) + (big)b2 * (ax - cx) + (big)c2 * (bx - ax);
    if (d < 0) {
        d = -d;
        ux = -ux;
        uy = -uy;
    }
    rho2 = (ax * d - ux) * (ax * d - ux) + (ay * d - uy) * (ay * d - uy);
    // an extreme point of the circle is on the arc when it lies on the same side
    // of the chord AB as C; side(P) * d = alpha - gamma * sqrt(rho2)
    long long ex = bx - ax, ey = by - ay;
    int side_c = sign((big)ex * (cy - ay) - (big)ey * (cx - ax));
    big alpha = ex * (uy - ay * d) - ey * (ux - ax * d);
    long long lo_x = std::min(ax, bx), hi_x = std::max(ax, bx);
    long long lo_y = std::min(ay, by), hi_y = std::max(ay, by);
    if (sign_minus(alpha, ey) == side_c)
        hi_x = std::max(hi_x, ceil_plus(ux));
    if (sign_minus(alpha, -ey) == side_c)
        lo_x = std::min(lo_x, floor_minus(ux));
    if (sign_minus(alpha, -ex) == side_c)
        hi_y = std::max(hi_y, ceil_plus(uy));
    if (sign_minus(alpha, ex) == side_c)
        lo_y = std::min(lo_y, floor_minus(uy));
    printf("%lld\n", (hi_x - lo_x) * (hi_y - lo_y));
}
