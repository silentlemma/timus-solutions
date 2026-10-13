#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

struct Vec {
    int x, y;
};

int half(const Vec &v) { return v.y > 0 || (v.y == 0 && v.x > 0) ? 0 : 1; }

int cross(const Vec &a, const Vec &b) { return a.x * b.y - a.y * b.x; }

int main() {
    int n;
    scanf("%d", &n);
    vector<Vec> vec(n);
    for (auto &v : vec)
        scanf("%d %d", &v.x, &v.y);
    for (int i = n - 1; i >= 0; i--) {
        vec[i].x -= vec[0].x;
        vec[i].y -= vec[0].y;
    }
    vector<int> order;
    for (int i = 1; i < n; i++)
        order.push_back(i);
    // by angle around the first pumpkin, nearer first on the same ray
    sort(order.begin(), order.end(), [&](int i, int j) {
        const Vec &a = vec[i], &b = vec[j];
        if (half(a) != half(b))
            return half(a) < half(b);
        int c = cross(a, b);
        if (c != 0)
            return c > 0;
        return abs(a.x) + abs(a.y) < abs(b.x) + abs(b.y);
    });
    // cut the circle after a turn of at least half a circle, if there is one:
    // then every step turns by less than that and the walk never meets itself
    int m = order.size(), start = 0;
    for (int k = 0; k < m; k++) {
        const Vec &a = vec[order[(k + m - 1) % m]], &b = vec[order[k]];
        int c = cross(a, b);
        if (c < 0 || (c == 0 && a.x * b.x + a.y * b.y < 0))
            start = k;
    }
    printf("%d\n1\n", n);
    for (int k = 0; k < m; k++)
        printf("%d\n", order[(start + k) % m] + 1);
}
