#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>

struct Cable {
    int owner;
    long long x, time;
};

struct Event {
    long long at;  // walking cost from the foot to the point
    int kind;      // 0 a landing, 1 a start: landings first at one point
    long long start, time;
};

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<long long> xs(n + 1), speed(n);
    for (auto &x : xs) scanf("%lld", &x);
    std::vector<Cable> cables;
    for (int i = 0; i < n; i++) {
        int m;
        scanf("%lld %d", &speed[i], &m);
        for (int j = 0; j < m; j++) {
            long long x, t;
            scanf("%lld %lld", &x, &t);
            // a start at the first vertex of a segment is the last point of
            // the segment before it
            cables.push_back({i > 0 && x == xs[i] ? i - 1 : i, x, t});
        }
    }
    std::vector<long long> walk(n + 1, 0);
    for (int i = 0; i < n; i++) walk[i + 1] = walk[i] + speed[i] * std::llabs(xs[i + 1] - xs[i]);
    auto cost = [&](int seg, long long x) {
        return walk[seg] + speed[seg] * std::llabs(x - xs[seg]);
    };
    // every point but the foot belongs to one segment, which owns its x
    // range without its first vertex; a cable lands on the first later
    // segment owning its x, found by painting the segments from the top down
    std::vector<long long> keys;
    for (auto &c : cables) keys.push_back(c.x);
    std::sort(keys.begin(), keys.end());
    keys.erase(std::unique(keys.begin(), keys.end()), keys.end());
    int size = 1;
    while (size < (int)keys.size()) size *= 2;
    std::vector<int> paint(2 * size, n);
    auto cover = [&](int lo, int hi, int seg) {
        for (lo += size, hi += size; lo < hi; lo /= 2, hi /= 2) {
            if (lo & 1) paint[lo++] = seg;
            if (hi & 1) paint[--hi] = seg;
        }
    };
    auto look = [&](int i) {
        // paints only go down, so the lowest segment is the latest one
        int best = n;
        for (i += size; i > 0; i /= 2) best = std::min(best, paint[i]);
        return best;
    };
    std::vector<std::vector<int>> byOwner(n);
    for (int k = 0; k < (int)cables.size(); k++) byOwner[cables[k].owner].push_back(k);
    std::vector<Event> events;
    for (int seg = n - 1; seg >= 0; seg--) {
        for (int k : byOwner[seg]) {
            const Cable &c = cables[k];
            int at = std::lower_bound(keys.begin(), keys.end(), c.x) - keys.begin();
            long long from = cost(c.owner, c.x);
            events.push_back({from, 1, 0, 0});
            events.push_back({cost(look(at), c.x), 0, from, c.time});
        }
        long long a = xs[seg], b = xs[seg + 1];
        long long lo = a < b ? a + 1 : b, hi = a < b ? b : a - 1;
        int from = std::lower_bound(keys.begin(), keys.end(), lo) - keys.begin();
        int to = std::upper_bound(keys.begin(), keys.end(), hi) - keys.begin();
        cover(from, to, seg);
    }
    std::sort(events.begin(), events.end(), [](const Event &p, const Event &q) {
        return p.at != q.at ? p.at < q.at : p.kind < q.kind;
    });
    // going up, the best time at a point is its walking cost plus the least
    // (time - walking cost) over the landings so far
    std::map<long long, long long> best;
    long long gain = 0;
    for (const auto &e : events) {
        if (e.kind == 0) {
            gain = std::min(gain, best[e.start] + e.time - e.at);
        } else {
            best[e.at] = e.at + gain;
        }
    }
    printf("%lld\n", walk[n] + gain);
    return 0;
}
