#include <iostream>
#include <vector>
using namespace std;

int main() {
    long long k, p;
    cin >> k >> p;
    // an ent with w words teaches an old ent who ends with w + 1 words and a
    // young one who ends with 2w, so with g(m) ents knowing 2m (or 2m + 1)
    // words: g(1) = 1 and g(m) = g(m - 1) + g(m / 2)
    if (k < 2) {
        cout << 0 << "\n";
        return 0;
    }
    long long top = k / 2, half = top / 2; // only g up to half is looked up again
    vector<int> g(half + 1);
    long long cur = 1 % p;
    if (half >= 1)
        g[1] = cur;
    for (long long m = 2; m <= top; m++) {
        cur = (cur + g[m / 2]) % p;
        if (m <= half)
            g[m] = cur;
    }
    cout << cur << "\n";
}
