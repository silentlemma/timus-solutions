#include <cstdio>
#include <vector>

const long long MOD = 1000000007;

int main() {
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);
    // one[i], two[i]: sequences of length i that end with a run of ones or twos,
    // the empty sequence counts once on both sides, so one[0] = two[0] = 1
    std::vector<long long> one(n + 1), two(n + 1), sumOne(n + 1), sumTwo(n + 1);
    one[0] = two[0] = sumOne[0] = sumTwo[0] = 1;
    for (int i = 1; i <= n; i++) {
        // the last run of ones has length 1..a and follows a sequence ending in twos
        one[i] = sumTwo[i - 1] - (i - a - 1 >= 0 ? sumTwo[i - a - 1] : 0);
        two[i] = sumOne[i - 1] - (i - b - 1 >= 0 ? sumOne[i - b - 1] : 0);
        one[i] = (one[i] % MOD + MOD) % MOD;
        two[i] = (two[i] % MOD + MOD) % MOD;
        sumOne[i] = (sumOne[i - 1] + one[i]) % MOD;
        sumTwo[i] = (sumTwo[i - 1] + two[i]) % MOD;
    }
    printf("%lld\n", (one[n] + two[n]) % MOD);
}
