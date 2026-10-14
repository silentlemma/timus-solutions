#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MOD = 1000000007;

int main() {
    string a, b;
    cin >> a >> b;
    int n = a.size(), m = b.size();
    // length[j] and count[j]: the shortest common supersequences of a[i:] and
    // b[j:], their length and number; row i needs only row i + 1
    vector<int> length(m + 1), count(m + 1, 1), belowLen, belowCnt;
    for (int j = 0; j <= m; j++)
        length[j] = m - j; // i = n: only b[j:] itself
    for (int i = n - 1; i >= 0; i--) {
        belowLen.swap(length);
        belowCnt.swap(count);
        length.assign(m + 1, 0);
        count.assign(m + 1, 0);
        length[m] = n - i, count[m] = 1; // only a[i:] itself
        for (int j = m - 1; j >= 0; j--) {
            if (a[i] == b[j]) {
                // the first letter is the common one and covers both
                length[j] = belowLen[j + 1] + 1;
                count[j] = belowCnt[j + 1];
                continue;
            }
            // the first letter is a[i] or b[j]; the two kinds of strings differ
            // in their first letter, so their numbers add up
            int takeA = belowLen[j], takeB = length[j + 1], best = min(takeA, takeB);
            length[j] = best + 1;
            long long ways = 0;
            if (takeA == best)
                ways += belowCnt[j];
            if (takeB == best)
                ways += count[j + 1];
            count[j] = ways % MOD;
        }
    }
    cout << count[0] << endl;
}
