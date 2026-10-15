#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

typedef long long ll;
const ll FAR = 1LL << 62;

int main() {
    int n, m;
    scanf("%d", &n);
    std::vector<ll> xs(n), ys(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &xs[i], &ys[i]);
    }
    scanf("%d", &m);
    // half-edge 2i runs from ends[i] to tips[i], 2i + 1 back; pipe m is an
    // extra edge from the source, leaving to the left, round the outside to
    // the sink, arriving from the right
    std::vector<int> ends(m + 1), tips(m + 1);
    std::vector<ll> caps(m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d %lld", &ends[i], &tips[i], &caps[i]);
        ends[i]--, tips[i]--;
    }
    ends[m] = 0, tips[m] = n - 1;
    int halves = 2 * m + 2;
    std::vector<int> origin(halves);
    std::vector<ll> dx(halves), dy(halves);
    for (int i = 0; i <= m; i++) {
        int a = ends[i], b = tips[i];
        origin[2 * i] = a, origin[2 * i + 1] = b;
        dx[2 * i] = xs[b] - xs[a], dy[2 * i] = ys[b] - ys[a];
        dx[2 * i + 1] = -dx[2 * i], dy[2 * i + 1] = -dy[2 * i];
    }
    dx[2 * m] = -1, dy[2 * m] = 0, dx[2 * m + 1] = 1, dy[2 * m + 1] = 0;
    std::vector<std::vector<int>> around(n);
    for (int h = 0; h < halves; h++) {
        around[origin[h]].push_back(h);
    }
    // counterclockwise from the +x axis, compared exactly
    auto before = [&](int g, int h) {
        bool lowG = dy[g] < 0 || (dy[g] == 0 && dx[g] < 0);
        bool lowH = dy[h] < 0 || (dy[h] == 0 && dx[h] < 0);
        if (lowG != lowH) {
            return lowH;
        }
        return dx[g] * dy[h] - dy[g] * dx[h] > 0;
    };
    std::vector<int> pos(halves);
    for (auto& out : around) {
        std::sort(out.begin(), out.end(), before);
        for (int k = 0; k < (int)out.size(); k++) {
            pos[out[k]] = k;
        }
    }
    // faces: after arriving at a vertex, leave by the next edge clockwise
    std::vector<int> face(halves, -1);
    int faces = 0;
    for (int h = 0; h < halves; h++) {
        if (face[h] >= 0) {
            continue;
        }
        for (int g = h; face[g] < 0;) {
            face[g] = faces;
            const std::vector<int>& out = around[origin[g ^ 1]];
            int k = pos[g ^ 1];
            g = out[k == 0 ? out.size() - 1 : k - 1];
        }
        faces++;
    }
    // the minimum cut is the shortest path between the two faces next to
    // the extra edge, with pipe capacities as lengths
    std::vector<std::vector<std::pair<int, ll>>> links(faces);
    for (int i = 0; i < m; i++) {
        int a = face[2 * i], b = face[2 * i + 1];
        links[a].push_back({b, caps[i]});
        links[b].push_back({a, caps[i]});
    }
    std::vector<ll> dist(faces, FAR);
    typedef std::pair<ll, int> Item;
    std::priority_queue<Item, std::vector<Item>, std::greater<Item>> heap;
    dist[face[2 * m]] = 0;
    heap.push({0, face[2 * m]});
    while (!heap.empty()) {
        auto [d, f] = heap.top();
        heap.pop();
        if (d > dist[f]) {
            continue;
        }
        for (auto [g, c] : links[f]) {
            if (d + c < dist[g]) {
                dist[g] = d + c;
                heap.push({d + c, g});
            }
        }
    }
    // the flow from ends[i] to tips[i] is the difference of the distances
    // of the faces on its two sides
    std::vector<ll> flow(m, 0);
    ll total = 0;
    for (int i = 0; i < m; i++) {
        ll left = dist[face[2 * i]], right = dist[face[2 * i + 1]];
        if (left != FAR && right != FAR) {
            flow[i] = right - left;
        }
        total += ends[i] == 0 ? flow[i] : tips[i] == 0 ? -flow[i] : 0;
    }
    int sign = total >= 0 ? 1 : -1;
    printf("%lld\n", total * sign);
    for (int i = 0; i < m; i++) {
        ll f = flow[i] * sign;
        if (f >= 0) {
            printf("%d %d %lld\n", ends[i] + 1, tips[i] + 1, f);
        } else {
            printf("%d %d %lld\n", tips[i] + 1, ends[i] + 1, -f);
        }
    }
}
