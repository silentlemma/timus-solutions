#include <cstdio>
#include <vector>

const int POSITIONS = 32;

long long binom[POSITIONS + 1][POSITIONS + 1];

// how many numbers in [0, n] are sums of exactly k different powers of b,
// that is, have only digits 0 and 1 in base b with k ones
long long count_upto(long long n, int k, int b) {
    std::vector<int> digits;
    for (; n > 0; n /= b)
        digits.push_back(n % b);
    // a digit above 1 lets every smaller number with 0/1 digits through: it
    // and all digits after it may as well be 1
    for (int i = (int)digits.size() - 1; i >= 0; i--)
        if (digits[i] > 1) {
            for (int j = i; j >= 0; j--)
                digits[j] = 1;
            break;
        }
    // count 0/1 strings with k ones not above the digits, from the top
    long long total = 0;
    int ones = 0;
    for (int i = (int)digits.size() - 1; i >= 0 && ones <= k; i--)
        if (digits[i] == 1) {
            if (k - ones <= i)
                total += binom[i][k - ones];
            ones++;
        }
    return total + (ones == k ? 1 : 0);
}

int main() {
    for (int i = 0; i <= POSITIONS; i++) {
        binom[i][0] = 1;
        for (int j = 1; j <= i; j++)
            binom[i][j] = binom[i - 1][j - 1] + (j < i ? binom[i - 1][j] : 0);
    }
    long long x, y;
    int k, b;
    if (scanf("%lld %lld", &x, &y) != 2 || scanf("%d %d", &k, &b) != 2)
        return 0;
    printf("%lld\n", count_upto(y, k, b) - count_upto(x - 1, k, b));
}
