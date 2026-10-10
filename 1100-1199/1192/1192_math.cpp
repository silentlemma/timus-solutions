#include <cmath>
#include <cstdio>

int main() {
    const double GRAVITY = 10.0, PI = 3.1415926535, HALF_TURN = 180.0;
    double v, a, k;
    scanf("%lf %lf %lf", &v, &a, &k);
    // one flight covers v^2 sin(2a) / g; every bounce keeps the angle and
    // divides v^2 by k, so the flights form a geometric series with ratio 1/k
    double flight = v * v * std::sin(2 * a * PI / HALF_TURN) / GRAVITY;
    printf("%.2f\n", flight * k / (k - 1));
}
