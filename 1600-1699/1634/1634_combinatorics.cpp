#include <cstdio>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

const double EPS = 1e-9;  // keeps an exact integer whole; no expectation lies that close below one

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // dp[s][l]: the chance that a random permutation of s elements has only
    // cycles of the lengths seen so far, and that their lcm is l
    vector<map<long long, double>> dp(n + 1);
    dp[0][1] = 1;
    for (int k = 1; k <= n; k++) {
        vector<map<long long, double>> next = dp;
        for (int s = 0; s < n; s++)
            for (const auto &[lcm, w] : dp[s]) {
                long long joined = lcm / gcd(lcm, (long long)k) * k;
                double weight = w;
                for (int m = 1; s + m * k <= n; m++) {
                    weight /= (double)k * m;  // m cycles of length k: 1 / (k^m m!)
                    next[s + m * k][joined] += weight;
                }
            }
        dp.swap(next);
    }
    double expected = 0;
    for (const auto &[lcm, w] : dp[n])
        expected += lcm * w;
    printf("%lld\n", (long long)(expected + EPS));
}
