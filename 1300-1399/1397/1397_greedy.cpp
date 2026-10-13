#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>
#include <vector>

using namespace std;

int main() {
    int n;
    while (scanf("%d", &n) == 1) {
        int m = 2 * n;
        vector<double> x(m), y(m), total(m, 0.0);
        for (int i = 0; i < m; i++)
            scanf("%lf %lf", &x[i], &y[i]);
        // total[i]: the sum of distances from point i to all the others
        for (int i = 0; i < m; i++)
            for (int j = i + 1; j < m; j++) {
                double d = sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
                total[i] += d;
                total[j] += d;
            }
        // a player's score is half the totals of the own points minus the
        // distances to the other colour, which both sides share: take the
        // largest total left, in turns
        sort(total.begin(), total.end(), greater<double>());
        double diff = 0;
        for (int i = 0; i < m; i++)
            diff += i % 2 == 0 ? total[i] : -total[i];
        printf("%.3f\n", fabs(diff / 2));
    }
}
