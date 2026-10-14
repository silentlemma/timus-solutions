#include <cmath>
#include <cstdio>

const double QUARTER = 0.25, THIRD = 1.0 / 3;

double a, half;

// the volume of the pineapple between its middle and height z: the cross-section
// at z is a disc of area pi (a / 2)^2 (1 - (z / half)^2)
double below(double z) {
    return acos(-1.0) * a * a * QUARTER * (z - z * z * z * THIRD / (half * half));
}

int main() {
    double b;
    int n;
    if (scanf("%lf %lf", &a, &b) != 2 || scanf("%d", &n) != 1)
        return 0;
    half = b / 2;
    for (int i = 0; i < n; i++)
        printf("%.6f\n", below(-half + b * (i + 1) / n) - below(-half + b * i / n));
}
