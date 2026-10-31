#include <cstdio>

const int DIGITS = 10, MAX_HALF = 4;

int main() {
    int n;
    scanf("%d", &n);
    int half = n / 2, limit = 1;
    for (int i = 0; i < half; ++i)
        limit *= DIGITS;
    // ways[s]: how many halves (numbers below 10^half) have digit sum s
    // n <= 8: a half has at most four digits and digit sum at most 36.
    long long ways[(DIGITS - 1) * MAX_HALF + 1] = {};
    for (int x = 0; x < limit; ++x) {
        int sum = 0;
        for (int y = x; y > 0; y /= DIGITS)
            sum += y % DIGITS;
        ++ways[sum];
    }
    // the two halves are chosen independently with the same sum
    long long total = 0;
    for (long long count : ways)
        total += count * count;
    printf("%lld\n", total);
}
