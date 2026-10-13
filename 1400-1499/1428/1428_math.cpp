#include <cstdio>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    // 2^(C-1) + 2^(C-1) = 2^C, and A and B both divide C - 1
    printf("%lld\n%lld\n2\n", 1LL << ((c - 1) / a), 1LL << ((c - 1) / b));
}
