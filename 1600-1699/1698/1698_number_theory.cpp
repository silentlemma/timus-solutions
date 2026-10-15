#include <cstdio>
#include <vector>

const int BASE = 10;
const int FIVE = 5;  // the last digit of one of the two endless solutions of x^2 = x

int main() {
    int n;
    scanf("%d", &n);
    // x^2 ends with x exactly when x^2 = x mod 10^d for its d digits; besides
    // 0 and 1 the solutions are the endings of two 10-adic numbers, ...0625
    // and ...9376, whose digits other than the last add up to 9 place by place

    std::vector<int> digits = {FIVE};  // the 5-adic one, lowest digit first
    long long carry = FIVE * FIVE / BASE;  // carry into position d of the square so far
    for (int d = 1; d < n; d++) {
        // digit d of x^2: the products x_i x_j with i + j = d, plus the carry, and
        // a new digit c adds 2 * 5 * c, a multiple of 10: c is forced
        long long total = carry;
        for (int i = 1; i < d; i++) {
            total += digits[i] * digits[d - i];
        }
        int c = total % BASE;
        digits.push_back(c);
        carry = (total + 2 * FIVE * c) / BASE;
    }
    int count = 1 + 2;  // the numbers 1, 5 and 6
    for (int d = 1; d < n; d++) {
        // a d + 1 digit number needs a nonzero leading digit
        count += (digits[d] != 0) + (digits[d] != BASE - 1);
    }
    printf("%d\n", count);
}
