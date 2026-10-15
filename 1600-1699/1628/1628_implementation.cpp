#include <algorithm>
#include <cstdio>
#include <set>
#include <utility>
#include <vector>
using namespace std;

int main() {
    int m, n, k;
    if (scanf("%d %d", &m, &n) != 2 || scanf("%d", &k) != 1)
        return 0;
    set<pair<int, int>> black;
    vector<vector<int>> rows(m + 2), cols(n + 2);
    for (int i = 0; i < k; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 0;
        black.insert({x, y});
        rows[x].push_back(y);
        cols[y].push_back(x);
    }
    auto closed = [&](int x, int y) {
        return x < 1 || x > m || y < 1 || y > n || black.count({x, y});
    };
    long long count = 0;
    // A white run of length 2 or more is a strip by itself; a single white
    // cell is one only if it is closed in the other direction too.
    for (int x = 1; x <= m; x++) {
        auto &r = rows[x];
        sort(r.begin(), r.end());
        r.push_back(n + 1);
        int prev = 0;
        for (int b : r) {
            int length = b - prev - 1;
            if (length >= 2 || (length == 1 && closed(x - 1, prev + 1) && closed(x + 1, prev + 1)))
                count++;
            prev = b;
        }
    }
    for (int y = 1; y <= n; y++) {
        auto &c = cols[y];
        sort(c.begin(), c.end());
        c.push_back(m + 1);
        int prev = 0;
        for (int b : c) {
            if (b - prev - 1 >= 2)
                count++;
            prev = b;
        }
    }
    printf("%lld\n", count);
}
