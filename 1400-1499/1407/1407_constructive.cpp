#include <algorithm>
#include <cstdio>
#include <string>

typedef unsigned __int128 u128;

int main() {
    int n;
    scanf("%d", &n);
    // a number of k digits 1 and 2 divisible by 2^k: put 1 or 2 in front of the
    // one for k - 1, whichever keeps one more factor 2; only the lowest n + 1
    // bits matter, so the sums may wrap around in 128 bits
    u128 value = 0, power = 1;
    std::string digits;
    for (int k = 0; k < n; k++) {
        u128 mask = ((u128)2 << k) - 1;
        int d = ((value + power) & mask) == 0 ? 1 : 2;
        value += d * power;
        digits += char('0' + d);
        power *= 10;
    }
    std::reverse(digits.begin(), digits.end());
    puts(digits.c_str());
}
