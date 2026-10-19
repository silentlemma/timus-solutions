#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

const long long FAR = 2;  // eyes lie closer to PR than twice its length

struct Eye {
    long long height, near, far;  // tan at P = height/near, at R = height/far
};

// a/b < c/d for positive denominators
bool less(long long a, long long b, long long c, long long d) { return a * d < c * b; }

struct Arc {
    long long px, py, qx, qy, rx, ry;
};

long long faces(const Arc &arc, const std::vector<long long> &xs,
                const std::vector<long long> &ys) {
    long long px = arc.px, py = arc.py, qx = arc.qx, qy = arc.qy, rx = arc.rx, ry = arc.ry;
    long long ux = rx - px, uy = ry - py;
    long long side = ux * (qy - py) - uy * (qx - px), span = ux * ux + uy * uy;
    std::vector<Eye> eyes;
    for (size_t i = 0; i < xs.size(); i++) {
        long long cross = ux * (ys[i] - py) - uy * (xs[i] - px);
        long long near = ux * (xs[i] - px) + uy * (ys[i] - py);
        long long far = -ux * (xs[i] - rx) - uy * (ys[i] - ry);
        // across PR from Q, both base angles acute, close enough to PR
        if ((cross > 0) == (side > 0) || cross == 0 || near <= 0 || far <= 0) continue;
        if (std::llabs(cross) >= FAR * span) continue;
        eyes.push_back({std::llabs(cross), near, far});
    }
    int k = eyes.size();
    // ranks of the angles at R, equal angles sharing a rank
    std::vector<int> byR(k), rank(k);
    std::iota(byR.begin(), byR.end(), 0);
    std::sort(byR.begin(), byR.end(), [&](int a, int b) {
        return less(eyes[a].height, eyes[a].far, eyes[b].height, eyes[b].far);
    });
    for (int i = 0, r = 0; i < k; i++) {
        if (i > 0 && less(eyes[byR[i - 1]].height, eyes[byR[i - 1]].far, eyes[byR[i]].height,
                          eyes[byR[i]].far)) {
            r++;
        }
        rank[byR[i]] = r + 1;
    }
    // the line through two eyes misses PR exactly when one eye is seen
    // higher from P and lower from R: count pairs in opposite orders
    std::vector<int> byP(k);
    std::iota(byP.begin(), byP.end(), 0);
    std::sort(byP.begin(), byP.end(), [&](int a, int b) {
        if (less(eyes[a].height, eyes[a].near, eyes[b].height, eyes[b].near)) return true;
        if (less(eyes[b].height, eyes[b].near, eyes[a].height, eyes[a].near)) return false;
        return rank[a] < rank[b];
    });
    std::vector<int> tree(k + 1, 0);
    long long pairs = 0;
    for (int seen = 0; seen < k; seen++) {
        int r = rank[byP[seen]], below = 0;
        for (int i = r; i > 0; i &= i - 1) below += tree[i];
        pairs += seen - below;
        for (int i = r; i <= k; i += i & -i) tree[i]++;
    }
    return pairs;
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    std::vector<Arc> arcs(n);
    std::vector<long long> xs(m), ys(m);
    for (auto &a : arcs) {
        scanf("%lld %lld %lld %lld %lld %lld", &a.px, &a.py, &a.qx, &a.qy, &a.rx, &a.ry);
    }
    for (int i = 0; i < m; i++) scanf("%lld %lld", &xs[i], &ys[i]);
    long long total = 0;
    for (const auto &a : arcs) total += faces(a, xs, ys);
    printf("%lld\n", total);
    return 0;
}
