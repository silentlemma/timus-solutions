#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

const long long HUNDREDTHS = 100, WHOLE = 100 * HUNDREDTHS;

// A percentage with at most two decimals, in hundredths of a percent.
long long hundredths(const char *s) {
    long long whole = 0, fraction = 0, scale = HUNDREDTHS;
    const char *dot = strchr(s, '.');
    for (const char *c = s; *c && c != dot; c++)
        whole = whole * 10 + (*c - '0');
    for (const char *c = dot ? dot + 1 : s + strlen(s); *c && scale > 1; c++) {
        scale /= 10;
        fraction += (*c - '0') * scale;
    }
    return whole * HUNDREDTHS + fraction;
}

int main() {
    std::string a, b;
    if (!(std::cin >> a >> b))
        return 1;
    long long p = hundredths(a.c_str()), q = hundredths(b.c_str());
    // Stern-Brocot descent between 0/1 and 1/0: the first mediant inside
    // the open interval (p, q) / WHOLE has the smallest denominator
    long long ln = 0, ld = 1, rn = 1, rd = 0;
    while (true) {
        long long m = ln + rn, n = ld + rd;
        if (m * WHOLE <= p * n)
            ln = m, ld = n;
        else if (m * WHOLE >= q * n)
            rn = m, rd = n;
        else {
            printf("%lld\n", n);
            return 0;
        }
    }
}
