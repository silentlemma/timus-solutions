#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> v(n), h(m);
    for (int& x : v) scanf("%d", &x);
    for (int& x : h) scanf("%d", &x);
    int maxV = *max_element(v.begin(), v.end());
    int maxH = *max_element(h.begin(), h.end());
    // one turn: down the left street and along the bottom, or along the top and down the right
    int best = max(min(v[0], h[m - 1]), min(h[0], v[n - 1]));
    // two turns: the middle street is the best one of its kind
    best = max(best, min({h[0], maxV, h[m - 1]}));
    best = max(best, min({v[0], maxH, v[n - 1]}));
    printf("%d\n", best);
}
