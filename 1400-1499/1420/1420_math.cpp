#include <cstdio>

long long floorDiv(long long a, long long b) {
    long long q = a / b;
    return q * b > a ? q - 1 : q;
}

int main() {
    long long ar, ai, br, bi;
    scanf("%lld %lld %lld %lld", &ar, &ai, &br, &bi);
    long long norm = br * br + bi * bi;
    if (norm == 0) {
        printf("0\n"); // no remainder is shorter than zero
        return 0;
    }
    // a / b = (x + y i) / norm; every quotient q lies within 1 of it
    long long x = ar * br + ai * bi, y = ai * br - ar * bi;
    long long fx = floorDiv(x, norm), fy = floorDiv(y, norm);
    int count = 0;
    for (long long qr = fx - 1; qr <= fx + 1; qr++)
        for (long long qi = fy - 1; qi <= fy + 1; qi++) {
            long long rr = ar - (br * qr - bi * qi), ri = ai - (br * qi + bi * qr);
            count += rr * rr + ri * ri < norm;
        }
    printf("%d\n", count);
}
