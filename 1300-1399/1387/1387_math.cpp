#include <cstdio>
#include <string>
#include <vector>

using namespace std;

typedef unsigned __int128 u128;

string toString(u128 v) {
    string s;
    do {
        s.insert(s.begin(), char('0' + int(v % 10)));
        v /= 10;
    } while (v > 0);
    return s;
}

int main() {
    int n;
    scanf("%d", &n);
    // a[k]: rooted trees with k vertices; s[k]: the sum of d a[d] over divisors d of k
    vector<u128> a(n + 1), s(n + 1);
    a[1] = s[1] = 1;
    for (int m = 1; m < n; m++) {
        // a(m + 1) = (s(1) a(m) + s(2) a(m - 1) + ... + s(m) a(1)) / m
        u128 total = 0;
        for (int k = 1; k <= m; k++)
            total += s[k] * a[m - k + 1];
        a[m + 1] = total / m;
        for (int d = 1; d <= m + 1; d++)
            if ((m + 1) % d == 0)
                s[m + 1] += d * a[d];
    }
    printf("%s\n", toString(a[n]).c_str());
}
