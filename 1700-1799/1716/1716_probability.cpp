#include <cstdio>

int main() {
    long long n, s;
    scanf("%lld %lld", &n, &s);
    long long yes = s - 2 * n;  // YES takes 3 bytes, NO takes 2
    long long no = n - yes;
    // the first test fails when its answer is NO, any later one when its
    // answer differs from the one before: no / n + (n - 1) * 2 yes no / (n (n - 1))
    printf("%.7f\n", (double)(no * (2 * yes + 1)) / n);
}
