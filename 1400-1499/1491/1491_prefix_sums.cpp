#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    // every gift adds c to the knights a..b: mark it at both ends of the
    // range, then a running sum gives each knight's total
    vector<long long> diff(n + 2, 0);
    for (int k = 0; k <= n; k++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        diff[a] += c;
        diff[b + 1] -= c;
    }
    long long total = 0;
    for (int i = 1; i <= n; i++) {
        total += diff[i];
        printf("%lld%c", total, i < n ? ' ' : '\n');
    }
}
