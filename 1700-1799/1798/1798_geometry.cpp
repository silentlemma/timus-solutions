#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

typedef long long i64;
typedef __int128 i128;

const int QUARTERS = 4;

i64 isqrt(i64 v) {
    i64 r = (i64)std::sqrt((double)v);
    while (r * r > v) r--;
    while ((r + 1) * (r + 1) <= v) r++;
    return r;
}

// the sum of isqrt(n - x*x) over x = 0 .. m, where 2*m*m <= n, found by
// walking from m to the left along the upper hull of the lattice points
// in the disk; a vector (a, b) moves a columns left and b rows up
i64 columnSum(i64 n, i64 m) {
    i64 x = m, y = isqrt(n - m * m);
    i64 total = y;
    std::vector<std::pair<i64, i64>> stack = {{1, 0}, {1, 1}};
    auto inside = [n](i64 px, i64 py) { return px >= 0 && px * px + py * py <= n; };
    while (x > 0) {
        auto [a1, b1] = stack.back();
        stack.pop_back();
        while (inside(x - a1, y + b1)) {
            // the columns x - a1 .. x - 1 lie under this hull edge
            total += a1 * y + (a1 - 1) * (b1 - 1) / 2 + b1;
            x -= a1;
            y += b1;
        }
        if (x - a1 < 0) break;
        i64 a2 = a1, b2 = b1;
        while (true) {
            std::tie(a1, b1) = stack.back();
            if (inside(x - a1, y + b1)) break;
            a2 = a1;
            b2 = b1;
            stack.pop_back();
        }
        while (true) {
            i64 a12 = a1 + a2, b12 = b1 + b2, nx = x - a12;
            if (nx < 0) break;
            if (inside(nx, y + b12)) {
                stack.push_back({a12, b12});
                a1 = a12;
                b1 = b12;
            } else {
                // from the outside point nx, steps of (a1, b1) rise at least
                // as fast as the circle, so no inside point lies between
                if ((i128)(b1 * b1) * (n - nx * nx) >= (i128)(a1 * a1) * (nx * nx)) break;
                a2 = a12;
                b2 = b12;
            }
        }
    }
    for (i64 column = 0; column < x; column++) total += isqrt(n - column * column);
    return total;
}

int main() {
    i64 radius;
    if (!(std::cin >> radius)) return 0;
    // slab (x, y) of the first quarter burns when its nearest corner is
    // strictly inside the circle: x*x + y*y <= radius^2 - 1
    i64 n = radius * radius - 1, m = isqrt(n / 2);
    i64 total = columnSum(n, m);
    // points with x < y twice, then the diagonal once
    i64 quarter = 2 * (total - m * (m + 1) / 2) + m + 1;
    std::cout << QUARTERS * quarter << "\n";
    return 0;
}
