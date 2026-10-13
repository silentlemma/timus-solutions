#include <algorithm>
#include <array>
#include <cstdio>
#include <numeric>
#include <set>
#include <vector>

using namespace std;

const int AXES = 3;
typedef array<long long, AXES> Vec;

Vec cross(const Vec &a, const Vec &b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}

long long dot(const Vec &a, const Vec &b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }

int main() {
    int n;
    scanf("%d", &n);
    vector<Vec> points(n);
    for (auto &p : points)
        scanf("%lld %lld %lld", &p[0], &p[1], &p[2]);

    // every plane through the origin and two non-parallel points, once
    set<Vec> normals;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            Vec c = cross(points[i], points[j]);
            long long g = gcd(gcd(c[0], c[1]), c[2]);
            if (g == 0)
                continue;
            for (auto &x : c)
                x /= g;
            long long lead = c[0] ? c[0] : c[1] ? c[1] : c[2];
            if (lead < 0)
                for (auto &x : c)
                    x = -x;
            normals.insert(c);
        }

    int best = 1; // a single airplane is always visible
    for (const Vec &normal : normals) {
        int above = 0, below = 0;
        vector<Vec> circle;
        for (const Vec &p : points) {
            long long s = dot(normal, p);
            if (s > 0)
                above++;
            else if (s < 0)
                below++;
            else
                circle.push_back(p);
        }
        // a slight tilt shows the points of the circle in its best open half:
        // its edge passes through one of them, which a tilt adds as well
        int half = 0;
        for (const Vec &z : circle) {
            Vec edge = cross(normal, z);
            int ahead = 0, behind = 0;
            for (const Vec &p : circle) {
                long long s = dot(edge, p);
                ahead += s > 0;
                behind += s < 0;
            }
            half = max({half, ahead + 1, behind + 1});
        }
        best = max({best, above + half, below + half});
    }
    printf("%d\n", best);
}
