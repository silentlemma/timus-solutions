#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // rows of the ages 1..k starting with 1: a(k) = a(k-1) + a(k-3) + 1,
    // with a(1) = 1 and the rule run back to a(0) = 0, a(-1) = -1
    long long older = -1, old = 0, cur = 1;
    for (int i = 1; i < n; i++) {
        long long next = cur + older + 1;
        older = old;
        old = cur;
        cur = next;
    }
    printf("%lld\n", cur);
}
