#include <cmath>
#include <cstdio>

const int MAX_BOMBS = 10, STRIPS = 4096, FIELDS = 3;
const double PERCENT = 100, MIDDLE = 0.5;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    double cx[MAX_BOMBS], cy[MAX_BOMBS], rr[MAX_BOMBS];
    double low[MAX_BOMBS], high[MAX_BOMBS];
    for (int i = 0; i < n; i++) {
        double radius;
        if (scanf("%lf %lf %lf", &cx[i], &cy[i], &radius) != FIELDS)
            return 0;
        rr[i] = radius * radius;
    }
    double covered = 0;
    // Midpoint error<=2*sum(r)/STRIPS, below0.005 area units for at most10 discs.
    // Reuse at most10 intervals, sorted by their lower ends with insertion.
    for (int k = 0; k < STRIPS; k++) {
        double x = (k + MIDDLE) / STRIPS;
        int count = 0;
        for (int i = 0; i < n; i++) {
            double dx = x - cx[i], square = rr[i] - dx * dx;
            if (square <= 0)
                continue;
            double half = std::sqrt(square);
            double a = cy[i] - half, b = cy[i] + half;
            if (a < 0)
                a = 0;
            if (b > 1)
                b = 1;
            if (a >= b)
                continue;
            int j = count++;
            while (j > 0 && low[j - 1] > a) {
                low[j] = low[j - 1];
                high[j] = high[j - 1];
                j--;
            }
            low[j] = a;
            high[j] = b;
        }
        double end = 0;
        for (int i = 0; i < count; i++)
            if (high[i] > end) {
                covered += high[i] - (low[i] > end ? low[i] : end);
                end = high[i];
            }
    }
    printf("%.6f\n", covered / STRIPS * PERCENT);
}
