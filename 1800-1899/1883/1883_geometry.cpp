#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;

const ll EDGE = 1000000000;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    vector<pair<ll, ll>> candles(n);
    for (auto& c : candles) scanf("%lld %lld", &c.first, &c.second);
    sort(candles.begin(), candles.end());
    // take the first k candles from the left, ties broken from below: all
    // columns left of candle k, and its own column up to it; the cut from it
    // to (x - 1, EDGE) leaves the rest of its column outside
    ll x = candles[k - 1].first, y = candles[k - 1].second;
    vector<pair<ll, ll>> polygon = {{-EDGE, -EDGE}, {x, -EDGE}, {x, y}};
    if (x - 1 > -EDGE) polygon.push_back({x - 1, EDGE});
    polygon.push_back({-EDGE, EDGE});
    printf("%d\n", (int)polygon.size());
    for (auto& p : polygon) printf("%lld %lld\n", p.first, p.second);
    return 0;
}
