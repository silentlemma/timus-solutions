#include <cstdio>
constexpr int MAX_FOLDS = 30;

int main() {
    long long n;
    scanf("%lld", &n);
    // a fold of x cm needs x <= length - x, so a strip shrinks at best to
    // half its length, rounded up; folding exactly half each time reaches that
    // n <= 10^9 < 2^30, so at most 30 halvings reach length one.
    long long folds[MAX_FOLDS];
    int count = 0;
    while (n > 1) {
        folds[count++] = n / 2;
        n -= n / 2;
    }
    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf(i ? " %lld" : "%lld", folds[i]);
    }
    printf("\n");
}
