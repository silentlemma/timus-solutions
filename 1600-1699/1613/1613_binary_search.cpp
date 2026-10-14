#include <algorithm>
#include <cstdio>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    // (passengers, city) pairs in order: the cities with one count are
    // consecutive and sorted by number
    vector<pair<int, int>> pairs(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &pairs[i].first);
        pairs[i].second = i + 1;
    }
    sort(pairs.begin(), pairs.end());
    int q;
    scanf("%d", &q);
    string out(q, '0');
    for (int i = 0; i < q; i++) {
        int lo, hi, x;
        scanf("%d %d %d", &lo, &hi, &x);
        // the first city with count x and number at least lo
        auto it = lower_bound(pairs.begin(), pairs.end(), make_pair(x, lo));
        if (it != pairs.end() && it->first == x && it->second <= hi)
            out[i] = '1';
    }
    printf("%s\n", out.c_str());
}
