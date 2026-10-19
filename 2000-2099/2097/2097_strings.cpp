#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;
typedef long long ll;

vector<ll> secondDifferences(const vector<ll>& h) {
    vector<ll> d;
    for (size_t i = 0; i + 2 < h.size(); i++) d.push_back(h[i + 2] - 2 * h[i + 1] + h[i]);
    return d;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<ll> x(m + 1);
    for (ll& v : x) scanf("%lld", &v);
    // a section is similar exactly when the second differences agree, and then
    // a is the difference of the first steps of the two sections
    vector<ll> pattern = secondDifferences(x);
    size_t len = pattern.size();
    vector<size_t> pi(len, 0);
    for (size_t i = 1; i < len; i++) {
        size_t k = pi[i - 1];
        while (k && pattern[i] != pattern[k]) k = pi[k - 1];
        if (pattern[i] == pattern[k]) k++;
        pi[i] = k;
    }
    bool found = false;
    ll bestA = 0;
    int bestSlope = 0, bestStart = 0;
    for (int slope = 1; slope <= n; slope++) {
        int length;
        scanf("%d", &length);
        vector<ll> y(length + 1);
        for (ll& v : y) scanf("%lld", &v);
        if (length < m) continue;
        vector<ll> text = secondDifferences(y);
        size_t k = 0;
        for (size_t i = 0; i <= text.size(); i++) {
            if (k == len) {
                size_t start = i - len;
                ll a = llabs((x[1] - x[0]) - (y[start + 1] - y[start]));
                if (!found || a < bestA)
                    found = true, bestA = a, bestSlope = slope, bestStart = start;
                if (len) k = pi[k - 1];
            }
            if (i == text.size() || !len) continue;
            while (k && text[i] != pattern[k]) k = pi[k - 1];
            if (text[i] == pattern[k]) k++;
        }
    }
    if (found)
        printf("%d %d\n", bestSlope, bestStart);
    else
        puts("-1");
}
