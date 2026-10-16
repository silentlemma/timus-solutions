#include <cmath>
#include <cstdio>

int main() {
    double rim, book, shelf;
    if (scanf("%lf %lf %lf", &rim, &book, &shelf) < 1) return 0;
    // with the foot at distance x from the rim and r = hypot(x, rim), the book
    // leans on the rim top and its middle lies x * (book / 2r - 1) to the left,
    // which is largest where r cubed is book * rim * rim / 2
    double r = std::cbrt(book * rim * rim / 2);
    double shift = 0;
    if (r > rim) {
        double x = std::sqrt(r * r - rim * rim);
        shift = x * (book / (2 * r) - 1);
    }
    printf("%.6f\n", shift);
    return 0;
}
