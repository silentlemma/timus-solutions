#include <algorithm>
#include <cmath>
#include <cstdio>
#include <map>
#include <utility>
#include <vector>

typedef std::pair<double, double> P;

int n;
std::vector<std::vector<P>> rivers;
std::vector<std::vector<int>> tributaries;

double cross(P o, P a, P b) {
    return (a.first - o.first) * (b.second - o.second) -
           (a.second - o.second) * (b.first - o.first);
}

// area of the convex hull, by the monotone chain and the shoelace
double hullArea(std::vector<P> pts) {
    std::sort(pts.begin(), pts.end());
    pts.erase(std::unique(pts.begin(), pts.end()), pts.end());
    std::vector<P> h(2 * pts.size());
    int k = 0;
    for (size_t i = 0; i < pts.size(); i++) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], pts[i]) <= 0)
            k--;
        h[k++] = pts[i];
    }
    for (int i = (int)pts.size() - 2, t = k + 1; i >= 0; i--) {
        while (k >= t && cross(h[k - 2], h[k - 1], pts[i]) <= 0)
            k--;
        h[k++] = pts[i];
    }
    double area = 0;
    for (int i = 0; i + 1 < k; i++)
        area += h[i].first * h[i + 1].second - h[i].second * h[i + 1].first;
    return std::fabs(area) / 2;
}

void basin(int i, std::vector<P> &out) {
    out.insert(out.end(), rivers[i].begin(), rivers[i].end());
    for (int t : tributaries[i])
        basin(t, out);
}

int main() {
    scanf("%d", &n);
    rivers.resize(n);
    tributaries.resize(n);
    for (auto &r : rivers) {
        int k;
        scanf("%d", &k);
        r.resize(k);
        for (P &p : r)
            scanf("%lf %lf", &p.first, &p.second);
    }
    // a river is a tributary of the one whose inner vertex is its mouth
    std::map<P, int> owner;
    for (int i = 0; i < n; i++)
        for (size_t j = 1; j + 1 < rivers[i].size(); j++)
            owner[rivers[i][j]] = i;
    for (int i = 0; i < n; i++) {
        auto it = owner.find(rivers[i].back());
        if (it != owner.end() && it->second != i)
            tributaries[it->second].push_back(i);
    }
    double best = 0;
    for (int i = 0; i < n; i++) {
        std::vector<P> pts;
        basin(i, pts);
        best = std::max(best, hullArea(pts));
    }
    printf("%.2f\n", best);
}
