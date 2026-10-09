#include <cstdio>
#include <vector>

const int DIGITS = 10;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int half = n / 2, limit = 1;
    for (int i = 0; i < half; i++)
        limit *= DIGITS;
    // ways[s]: how many halves (numbers below 10^half) have digit sum s
    std::vector<long long> ways((DIGITS - 1) * half + 1, 0);
    for (int x = 0; x < limit; x++) {
        int s = 0;
        for (int y = x; y > 0; y /= DIGITS)
            s += y % DIGITS;
        ways[s]++;
    }
    // the two halves are chosen independently with the same sum
    long long total = 0;
    for (long long w : ways)
        total += w * w;
    printf("%lld\n", total);
}
