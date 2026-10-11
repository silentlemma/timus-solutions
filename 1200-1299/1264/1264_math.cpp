#include <cstdio>

int main() {
    long long n, m;
    scanf("%lld %lld", &n, &m);
    // one line for each element and each value 0..M
    printf("%lld\n", n * (m + 1));
}
