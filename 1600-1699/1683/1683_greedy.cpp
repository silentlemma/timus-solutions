#include <cstdio>
#include <vector>

int main() {
    long long n;
    scanf("%lld", &n);
    // a fold of x cm needs x <= length - x, so a strip shrinks at best to
    // half its length, rounded up; folding exactly half each time reaches that
    std::vector<long long> folds;
    while (n > 1) {
        folds.push_back(n / 2);
        n -= n / 2;
    }
    printf("%d\n", (int)folds.size());
    for (size_t i = 0; i < folds.size(); i++) {
        printf(i ? " %lld" : "%lld", folds[i]);
    }
    printf("\n");
}
