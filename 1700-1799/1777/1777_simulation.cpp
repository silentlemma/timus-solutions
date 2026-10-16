#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long ll;

int main() {
    std::vector<ll> piles;
    for (ll v; scanf("%lld", &v) == 1;) piles.push_back(v);
    int asked = 0;
    while (true) {
        asked++;
        // the closest two piles differ least among neighbours in sorted order
        std::sort(piles.begin(), piles.end());
        ll gap = piles[1] - piles[0];
        for (size_t i = 2; i < piles.size(); i++) gap = std::min(gap, piles[i] - piles[i - 1]);
        if (gap == 0) break;
        piles.push_back(gap);
    }
    printf("%d\n", asked);
    return 0;
}
