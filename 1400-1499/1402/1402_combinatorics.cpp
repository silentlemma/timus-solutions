#include <cstdio>
#include <string>

typedef unsigned __int128 u128;

int main() {
    int n;
    scanf("%d", &n);
    // ordered choices of k different drinks: n (n - 1) ... (n - k + 1), for k from 2,
    // the sum for n = 21 needs more than 64 bits
    u128 total = 0, ways = n;
    for (int k = 2; k <= n; k++) {
        ways *= n - k + 1;
        total += ways;
    }
    std::string digits;
    do {
        digits.insert(digits.begin(), char('0' + int(total % 10)));
        total /= 10;
    } while (total > 0);
    puts(digits.c_str());
}
