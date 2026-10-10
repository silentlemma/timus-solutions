#include <cstdio>

int main() {
    long long n, k;
    scanf("%lld %lld", &n, &k);
    // every two hobbits shake hands exactly once, when their groups part,
    // except the married couples, who go home together and never part
    printf("%lld\n", n * (n - 1) / 2 - k);
}
