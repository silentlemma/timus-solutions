#include <cstdio>
#include <initializer_list>

const int CORNERS = 3;
const double INNER = 0.5;  // inner points go this share of the way from the centre to a vertex
const double OUTER = 1 + INNER;  // outer points go this far the opposite way

int main() {
    double x[CORNERS], y[CORNERS], gx = 0, gy = 0;
    for (int i = 0; i < CORNERS; i++) {
        scanf("%lf %lf", &x[i], &y[i]);
        gx += x[i] / CORNERS;
        gy += y[i] / CORNERS;
    }
    for (double k : {INNER, -OUTER}) {
        for (int i = 0; i < CORNERS; i++) {
            printf("%.10f %.10f\n", gx + (x[i] - gx) * k, gy + (y[i] - gy) * k);
        }
    }
}
