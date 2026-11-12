#include <cstdio>
#include <vector>

const int BASE = 10;

int main() {
    int n;
    if (std::scanf("%d", &n) != 1)
        return 0;

    std::vector<int> digits{0}; // D(1), least significant digit first.
    for (int k = 2; k <= n; ++k) {
        // D(k) = k * D(k - 1) + (-1)^k. For odd k, D(k - 1) is odd.
        int carry = k % 2 == 0 ? 1 : -1;
        for (int &digit : digits) {
            int value = k * digit + carry;
            digit = value % BASE;
            carry = value / BASE;
        }
        for (; carry > 0; carry /= BASE)
            digits.push_back(carry % BASE);
    }

    for (auto digit = digits.rbegin(); digit != digits.rend(); ++digit)
        std::putchar('0' + *digit);
    std::putchar('\n');
}
