#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const long long NONE = -1; // no subordinate yet: a private cannot be cut

int main() {
    int n;
    scanf("%d", &n);
    vector<int> boss(n + 1), price(n + 1);
    for (int i = 2; i <= n; i++)
        scanf("%d %d", &boss[i], &price[i]);
    // cut[v]: the cheapest way to separate v from every private below it
    vector<long long> cut(n + 1, NONE);
    for (int v = n; v >= 2; v--) {
        long long cost = cut[v] == NONE ? price[v] : min<long long>(price[v], cut[v]);
        int p = boss[v];
        cut[p] = cut[p] == NONE ? cost : cut[p] + cost;
    }
    printf("%lld.00\n", cut[1]);
}
