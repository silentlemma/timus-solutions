#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<long long> a(n), b(n);
    for (auto &x : a) scanf("%lld", &x);
    for (auto &x : b) scanf("%lld", &x);
    long long p;
    scanf("%lld", &p);
    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());
    // The i-th weakest student can take any of the problems they can solve,
    // except the i problems already taken by weaker students.
    long long ways = 1 % p;
    int solvable = 0;
    for (int i = 0; i < n; i++) {
        while (solvable < n && b[solvable] <= a[i]) solvable++;
        ways = ways * ((solvable - i) % p) % p;
    }
    printf("%lld\n", ways);
    return 0;
}
