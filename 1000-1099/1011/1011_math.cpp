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
    // the fewest conductors above p are p*n/WHOLE + 1, and n is the answer
    // as soon as their share is below q
    for (long long n = 1;; n++) {
        long long c = p * n / WHOLE + 1;
        if (c * WHOLE < q * n) {
            printf("%lld\n", n);
            return 0;
        }
    }
}
