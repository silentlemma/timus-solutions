#include <cstdio>

int main() {
    long long n, m;
    scanf("%lld %lld", &n, &m);
    // every full lap turns four times and peels two rows and two columns; the
    // spiral ends in the middle of the shorter side, so only that side counts
    printf("%lld\n", n <= m ? 2 * (n - 1) : 2 * m - 1);
}
