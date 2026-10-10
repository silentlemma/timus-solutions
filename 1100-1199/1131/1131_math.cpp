#include <cstdio>

int main() {
    long long n, k;
    if (scanf("%lld %lld", &n, &k) != 2)
        return 0;
    // as long as fewer computers than cables have the program, each hour doubles
    // the count; after that k computers get it each hour
    long long have = 1, hours = 0;
    while (have < n && have < k) {
        have *= 2;
        hours++;
    }
    if (have < n)
        hours += (n - have + k - 1) / k;
    printf("%lld\n", hours);
}
