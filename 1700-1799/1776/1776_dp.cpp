#include <cstdio>
#include <vector>

const double SECONDS = 10;
// once a whole line is done with this certainty the rest of the sum is lost
// in rounding
const double SURE = 1e-15;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int m = n - 2;
    // done[i]: the chance that i rockets between two launched ones are all
    // launched within the volleys counted so far; a stretch of i rockets
    // splits at a random one into stretches of l and i - 1 - l
    std::vector<double> done(m + 1, 0.0), before;
    done[0] = 1;
    double volleys = 0;
    for (int j = 1; j <= m; j++) {
        volleys += 1 - done[m];
        before = done;
        for (int i = 0; i <= m; i++) {
            if (i <= j) {
                done[i] = 1;
                continue;
            }
            double sum = 0;
            for (int l = 0; l < i; l++) sum += before[l] * before[i - 1 - l];
            done[i] = sum / i;
        }
        if (1 - done[m] < SURE) break;
    }
    printf("%.11f\n", SECONDS * volleys);
    return 0;
}
