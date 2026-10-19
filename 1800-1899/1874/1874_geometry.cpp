#include <cmath>
#include <cstdio>

int main() {
    double a, b;
    if (scanf("%lf %lf", &a, &b) != 2) return 0;
    // the right triangle on the birch and the ground holds at most a quarter
    // of the squared diagonal; with the triangle of the sticks added, the
    // total is largest when the sticks meet at 135 degrees
    double x = a / 2, y = b / 2;
    printf("%.9f\n", x * x + y * y + 2 * sqrt(2.0) * x * y);
    return 0;
}
