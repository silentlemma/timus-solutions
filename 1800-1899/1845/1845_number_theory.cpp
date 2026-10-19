#include <cstdio>
#include <utility>
#include <vector>

struct Gauss {
    long long re, im;
};

static Gauss sub(Gauss a, Gauss b) { return {a.re - b.re, a.im - b.im}; }

static Gauss mul(Gauss a, Gauss b) {
    return {a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re};
}

static long long norm(Gauss a) { return a.re * a.re + a.im * a.im; }

static long long floorDiv(long long a, long long b) {
    long long q = a / b;
    return (a % b != 0 && (a < 0) != (b < 0)) ? q - 1 : q;
}

// x / y rounded to the nearest Gaussian integer in both parts
static Gauss quotient(Gauss x, Gauss y) {
    long long n = norm(y);
    long long re = x.re * y.re + x.im * y.im, im = x.im * y.re - x.re * y.im;
    return {floorDiv(2 * re + n, 2 * n), floorDiv(2 * im + n, 2 * n)};
}

// what is left of x after taking away the nearest multiple of p: its norm
// is at most half the norm of p
static Gauss remainder(Gauss x, Gauss p) { return sub(x, mul(p, quotient(x, p))); }

static bool zero(Gauss a) { return a.re == 0 && a.im == 0; }

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<std::vector<Gauss>> a(n, std::vector<Gauss>(n));
    for (auto &row : a) {
        for (auto &x : row) scanf("%lld %lld", &x.re, &x.im);
    }
    Gauss p;
    scanf("%lld %lld", &p.re, &p.im);
    for (auto &row : a) {
        for (auto &x : row) x = remainder(x, p);
    }
    // elimination modulo p: the Euclidean algorithm on the Gaussian
    // integers clears each column below the diagonal with row operations,
    // which keep the determinant; the entries of the column only shrink
    Gauss det = {1, 0};
    for (int k = 0; k < n; k++) {
        for (int i = k + 1; i < n; i++) {
            while (!zero(a[i][k])) {
                Gauss q = quotient(a[k][k], a[i][k]);
                a[k][k] = sub(a[k][k], mul(q, a[i][k]));
                for (int j = k + 1; j < n; j++) {
                    a[k][j] = remainder(sub(a[k][j], mul(q, a[i][j])), p);
                }
                std::swap(a[k], a[i]);
                det = {-det.re, -det.im};
            }
        }
        det = remainder(mul(det, a[k][k]), p);
    }
    printf("%lld %lld\n", det.re, det.im);
    return 0;
}
