#include <cmath>
#include <cstdio>

const int SIDES = 4;

int main() {
    int a, r;
    if (scanf("%d %d", &a, &r) != 2)
        return 0;
    double half = a / 2.0, area;
    if (r <= half) {
        area = std::acos(-1.0) * r * r;
    } else if (r * r >= 2 * half * half) {
        area = (double)a * a;
    } else {
        // the circle minus the four caps cut off by the sides
        double cap = (double)r * r * std::acos(half / r) - half * std::sqrt(r * r - half * half);
        area = std::acos(-1.0) * r * r - SIDES * cap;
    }
    printf("%.3f\n", area);
}
