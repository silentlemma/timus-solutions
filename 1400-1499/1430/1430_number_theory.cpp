#include <algorithm>
#include <cstdio>
#include <utility>

int main() {
    long long a, b, n;
    scanf("%lld %lld %lld", &a, &b, &n);
    bool swapped = a < b;
    if (swapped)
        std::swap(a, b);
    // b items of price a can always become a items of price b, so x below b is enough,
    // with a >= b either b or n / a is at most sqrt(n)
    long long spent = -1, bx = 0, by = 0;
    for (long long x = 0; x <= std::min(n / a, b - 1) && spent != n; x++) {
        long long y = (n - x * a) / b;
        if (x * a + y * b > spent)
            spent = x * a + y * b, bx = x, by = y;
    }
    if (swapped)
        std::swap(bx, by);
    printf("%lld %lld\n", bx, by);
}
