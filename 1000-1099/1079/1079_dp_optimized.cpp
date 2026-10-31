#include <algorithm>
#include <cstdint>
#include <cstdio>

const int TOP = 99999;
const int LAST_PARENT = (TOP + 1) / 2;

int main() {
    // n < 2^17 bounds every stern value by fibonacci(19) = 4181, fitting 16 bits.
    static std::uint16_t a[LAST_PARENT + 1], best[TOP + 1];
    a[1] = best[1] = 1;
    for (int i = 2; i <= TOP; i++) {
        std::uint16_t value = i % 2 == 0 ? a[i / 2] : a[i / 2] + a[i / 2 + 1];
        // later terms only refer to indices in the first half.
        if (i <= LAST_PARENT)
            a[i] = value;
        best[i] = std::max(best[i - 1], value);
    }
    int n;
    while (scanf("%d", &n) == 1 && n != 0)
        printf("%d\n", best[n]);
}
