#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const int ENOUGH = 9; // any 9 points, no three on a line, hold a convex pentagon
const int SIDES = 5;

struct Point {
    long long x, y;
    int id;
    bool operator<(const Point &o) const { return x != o.x ? x < o.x : y < o.y; }
};

long long cross(const Point &o, const Point &a, const Point &b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

// the convex hull of the points, counterclockwise
vector<Point> hull(vector<Point> points) {
    sort(points.begin(), points.end());
    vector<Point> h;
    for (int pass = 0; pass < 2; pass++) {
        size_t start = h.size();
        for (const Point &p : points) {
            while (h.size() >= start + 2 && cross(h[h.size() - 2], h.back(), p) <= 0)
                h.pop_back();
            h.push_back(p);
        }
        h.pop_back();
        reverse(points.begin(), points.end());
    }
    return h;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // by the Erdos-Szekeres theorem the first nine points are enough
    int m = min(n, ENOUGH);
    vector<Point> points(m);
    for (int i = 0; i < m; i++) {
        if (scanf("%lld %lld", &points[i].x, &points[i].y) != 2)
            return 0;
        points[i].id = i + 1;
    }
    for (int mask = 0; mask < 1 << m; mask++) {
        if (__builtin_popcount(mask) != SIDES)
            continue;
        vector<Point> five;
        for (int i = 0; i < m; i++)
            if (mask >> i & 1)
                five.push_back(points[i]);
        vector<Point> h = hull(five);
        if ((int)h.size() == SIDES) {
            printf("Yes\n");
            for (int i = 0; i < SIDES; i++)
                printf(i ? " %d" : "%d", h[i].id);
            printf("\n");
            return 0;
        }
    }
    printf("No\n");
}
