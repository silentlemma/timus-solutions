#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<ll> xs(n), ys(n);
    for (int i = 0; i < n; i++)
        if (scanf("%lld %lld", &xs[i], &ys[i]) != 2)
            return 0;
    int m;
    if (scanf("%d", &m) != 1)
        return 0;
    string out;
    for (int j = 0; j < m; j++) {
        ll px, py;
        if (scanf("%lld %lld", &px, &py) != 2)
            return 0;
        int turns = 0;
        bool onEdge = false;
        for (int i = 0; i < n && !onEdge; i++) {
            ll ax = xs[i], ay = ys[i], bx = xs[(i + 1) % n], by = ys[(i + 1) % n];
            // each product is below 4 10^18, so the difference fits in 64 bits
            ll cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax);
            if (cross == 0 && min(ax, bx) <= px && px <= max(ax, bx) && min(ay, by) <= py &&
                py <= max(ay, by)) {
                onEdge = true;
            } else if (ay <= py && py < by) {
                // upwards past the point on its left: one more turn
                if (cross > 0)
                    turns++;
            } else if (by <= py && py < ay) {
                // downwards past the point on its right: one turn less
                if (cross < 0)
                    turns--;
            }
        }
        out += onEdge ? "EDGE" : to_string(turns);
        out += '\n';
    }
    fputs(out.c_str(), stdout);
}
