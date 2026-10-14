#include <cstdio>
#include <vector>

using namespace std;

const int BASE = 10;
const int ODD = 3;  // the factor of the power of two for odd n
const int LESS = 4; // every count is that power times 1 or ODD, minus LESS

// digits from the lowest, multiplied by a small factor in place
void times(vector<int> &digits, int factor) {
    int carry = 0;
    for (int &d : digits) {
        int v = d * factor + carry;
        d = v % BASE;
        carry = v / BASE;
    }
    for (; carry > 0; carry /= BASE)
        digits.push_back(carry % BASE);
}

int main() {
    int n;
    scanf("%d", &n);
    if (n == 1) {
        printf("1\n");
        return 0;
    }
    // the counts of polygons grow by 4, 4, 8, 8, 16, 16, ... from zone 3 on:
    // 2^(n / 2 + 2) - 4 for even n and 3 * 2^(n / 2 + 1) - 4 for odd n
    vector<int> digits = {n % 2 == 0 ? 1 : ODD};
    for (int i = 0; i < n / 2 + 2 - n % 2; i++)
        times(digits, 2);
    // subtract LESS; the number is at least 8, so the borrow stops early
    digits[0] -= LESS;
    for (size_t i = 0; digits[i] < 0; i++) {
        digits[i] += BASE;
        digits[i + 1]--;
    }
    while (digits.size() > 1 && digits.back() == 0)
        digits.pop_back();
    for (size_t i = digits.size(); i-- > 0;)
        putchar('0' + digits[i]);
    putchar('\n');
}
