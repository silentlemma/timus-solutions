#include <cmath>
#include <cstdio>

const double TOTAL = 1000, HALF = 0.5;
const int OUTCOMES = 3;

int main() {
    double inverse = 0;
    for (int i = 0; i < OUTCOMES; i++) {
        double k;
        if (scanf("%lf", &k) != 1)
            return 0;
        inverse += 1 / k;
    }
    // betting in proportion to 1 / k on every outcome pays the same whatever
    // happens, and any other split pays less on some outcome
    printf("%.0f\n", floor(TOTAL / inverse + HALF));
}
