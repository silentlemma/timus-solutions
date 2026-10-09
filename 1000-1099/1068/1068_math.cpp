#include <cstdio>
#include <cstdlib>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // the numbers between 1 and N form one interval whichever side N is on,
    // and its sum is the count times the average of the ends
    long long count = std::abs(n - 1) + 1;
    printf("%lld\n", (1 + n) * count / 2);
}
