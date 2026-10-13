#include <cstdio>
#include <string>
#include <vector>

using namespace std;

typedef __int128 Big;

Big gcd(Big a, Big b) {
    if (a < 0)
        a = -a;
    while (b) {
        Big t = a % b;
        a = b;
        b = t;
    }
    return a;
}

// an exact fraction p / q with q > 0, kept in lowest terms
struct Frac {
    Big p, q;
    Frac(Big p = 0, Big q = 1) : p(p), q(q) {
        Big g = gcd(p, q);
        if (g > 1) {
            this->p /= g;
            this->q /= g;
        }
    }
};

Frac operator+(const Frac &a, const Frac &b) { return Frac(a.p * b.q + b.p * a.q, a.q * b.q); }
Frac operator-(const Frac &a, const Frac &b) { return Frac(a.p * b.q - b.p * a.q, a.q * b.q); }
Frac operator*(const Frac &a, Big k) { return Frac(a.p * k, a.q); }
Frac operator/(const Frac &a, Big k) { return Frac(a.p, a.q * k); }

string text(Big x) {
    if (x < 0)
        return "-" + text(-x);
    string s;
    do
        s = char('0' + (int)(x % 10)) + s;
    while (x /= 10);
    return s;
}

int main() {
    int k;
    scanf("%d", &k);
    // binomial coefficients C(m, j) for m up to k + 1
    vector<vector<Big>> comb(k + 2, vector<Big>(k + 2, 0));
    for (int m = 0; m <= k + 1; m++) {
        comb[m][0] = 1;
        for (int j = 1; j <= m; j++)
            comb[m][j] = comb[m - 1][j - 1] + comb[m - 1][j];
    }
    // Bernoulli numbers with B1 = +1/2: the sum of C(m + 1, j) B_j over
    // j <= m equals m + 1, which gives B_m from the earlier ones
    vector<Frac> bern;
    for (int m = 0; m <= k; m++) {
        Frac rest;
        for (int j = 0; j < m; j++)
            rest = rest + bern[j] * comb[m + 1][j];
        bern.push_back((Frac(m + 1) - rest) / (m + 1));
    }
    // Faulhaber: the coefficient of N^(k + 1 - j) is C(k + 1, j) B_j / (k + 1)
    for (int j = 0; j <= k; j++) {
        Frac c = bern[j] * comb[k + 1][j] / (k + 1);
        printf("%s/%s ", text(c.p).c_str(), text(c.q).c_str());
    }
    printf("0/1\n");
}
