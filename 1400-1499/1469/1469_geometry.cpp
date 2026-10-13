#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <tuple>
#include <vector>

using namespace std;

const long long SHEAR = 20001; // x' = SHEAR x + y keeps all points apart and no segment vertical

struct Pt {
    long long x, y;
};

int sign(long long v) { return (v > 0) - (v < 0); }

int orient(Pt a, Pt b, Pt c) { return sign((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)); }

bool onBox(Pt a, Pt b, Pt c) {
    return min(a.x, b.x) <= c.x && c.x <= max(a.x, b.x) && min(a.y, b.y) <= c.y &&
           c.y <= max(a.y, b.y);
}

// closed segments pq and rs share a point
bool touch(Pt p, Pt q, Pt r, Pt s) {
    int o1 = orient(p, q, r), o2 = orient(p, q, s), o3 = orient(r, s, p), o4 = orient(r, s, q);
    if (o1 * o2 < 0 && o3 * o4 < 0)
        return true;
    return (o1 == 0 && onBox(p, q, r)) || (o2 == 0 && onBox(p, q, s)) ||
           (o3 == 0 && onBox(r, s, p)) || (o4 == 0 && onBox(r, s, q));
}

vector<Pt> from, to, lo, hi; // original ends, and sheared ends sorted by x

// the sign of the height of segment i above point p, at the x of p
int side(int i, Pt p) {
    Pt a = lo[i], b = hi[i];
    return sign(a.y * (b.x - a.x) + (b.y - a.y) * (p.x - a.x) - p.y * (b.x - a.x));
}

bool slopeLess(int i, int j) {
    return (hi[i].y - lo[i].y) * (hi[j].x - lo[j].x) < (hi[j].y - lo[j].y) * (hi[i].x - lo[i].x);
}

void meet(int i, int j) {
    if (touch(from[i], to[i], from[j], to[j])) {
        printf("YES\n%d %d\n", i + 1, j + 1);
        exit(0);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    from.resize(n);
    to.resize(n);
    lo.resize(n);
    hi.resize(n);
    vector<tuple<long long, int, int>> events; // x, start before end, segment
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld %lld", &from[i].x, &from[i].y, &to[i].x, &to[i].y);
        Pt a = {SHEAR * from[i].x + from[i].y, from[i].y}, b = {SHEAR * to[i].x + to[i].y, to[i].y};
        if (b.x < a.x)
            swap(a, b);
        lo[i] = a;
        hi[i] = b;
        events.push_back({a.x, 0, i});
        events.push_back({b.x, 1, i});
    }
    // Shamos-Hoey: sweep a vertical line over the sheared plane, keep the
    // segments it crosses ordered by height, and test only neighbours
    sort(events.begin(), events.end());
    vector<int> line;
    for (auto [x, kind, i] : events) {
        if (kind == 0) {
            Pt p = lo[i];
            int l = 0, h = line.size();
            while (l < h) {
                int mid = (l + h) / 2, c = side(line[mid], p);
                if (c < 0 || (c == 0 && slopeLess(line[mid], i)))
                    l = mid + 1;
                else
                    h = mid;
            }
            line.insert(line.begin() + l, i);
            if (l > 0)
                meet(i, line[l - 1]);
            if (l + 1 < (int)line.size())
                meet(i, line[l + 1]);
        } else {
            Pt p = hi[i];
            int l = 0, h = line.size();
            while (l < h) {
                int mid = (l + h) / 2;
                if (side(line[mid], p) < 0)
                    l = mid + 1;
                else
                    h = mid;
            }
            int k = l;
            while (k < (int)line.size() && line[k] != i)
                k++;
            if (k == (int)line.size())
                k = find(line.begin(), line.end(), i) - line.begin();
            line.erase(line.begin() + k);
            if (k > 0 && k < (int)line.size())
                meet(line[k - 1], line[k]);
        }
    }
    puts("NO");
}
