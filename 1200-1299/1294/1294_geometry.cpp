#include <cmath>
#include <cstdio>
#include <cstdlib>

const long long KM = 1000; // input distances are in thousands of kilometres
const int FIELDS = 4;

int main() {
    // a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
    // inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
    long long a = 0, b = 0, c = 0, d = 0;
    if (scanf("%lld %lld %lld %lld", &a, &b, &c, &d) != FIELDS)
        return 0;
    long long den = a * b - c * d;
    long long diff = a * a + b * b - c * c - d * d;
    if (den == 0 || llabs(diff) >= 2 * llabs(den) || b * c <= a * d) {
        puts("Impossible.");
        return 0;
    }
    long long num = a * b * (c * c + d * d) - c * d * (a * a + b * b);
    if (den < 0) {
        num = -num;
        den = -den;
    }
    long long km = (long long)(KM * std::sqrt((double)num / den));
    // Compare the half-kilometre boundary exactly, dividing before scaling.
    long long scale = 4 * KM * KM;
    long long bound = scale * (num / den) + scale * (num % den) / den;
    if ((2 * km + 1) * (2 * km + 1) <= bound)
        ++km;
    printf("Distance is %lld km.\n", km);
    return 0;
}
