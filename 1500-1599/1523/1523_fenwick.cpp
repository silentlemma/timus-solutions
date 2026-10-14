#include <cstdio>
#include <vector>

using namespace std;

const long long MOD = 1000000000;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    // count values from the top, so that "larger" becomes a prefix
    vector<int> flipped(n);
    for (int &v : flipped) {
        scanf("%d", &v);
        v = n + 1 - v;
    }
    // ends[i]: decreasing runs of the current length that end at position i
    vector<long long> ends(n, 1);
    for (int len = 2; len <= k; len++) {
        vector<long long> tree(n + 1, 0), next(n);
        for (int i = 0; i < n; i++) {
            // the runs one shorter that end earlier at a larger value
            long long s = 0;
            for (int j = flipped[i] - 1; j > 0; j &= j - 1)
                s += tree[j];
            next[i] = s % MOD;
            for (int j = flipped[i]; j <= n; j += j & -j)
                tree[j] = (tree[j] + ends[i]) % MOD;
        }
        ends.swap(next);
    }
    long long total = 0;
    for (long long e : ends)
        total = (total + e) % MOD;
    printf("%lld\n", total);
}
