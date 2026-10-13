#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <vector>

using namespace std;

typedef long long ll;

const ll DIGITS = 1000000000; // the time is printed with nine digits after the point
const int WALL = 4;           // numbers that describe a wall
const int TREE = 4;           // a segment tree over n leaves has under 4 n nodes

struct Dir {
    ll x, y;
    bool operator==(const Dir &o) const { return x == o.x && y == o.y; }
};

Dir reduced(ll x, ll y) {
    ll g = gcd(llabs(x), llabs(y));
    return {x / g, y / g};
}

// counterclockwise order of directions, starting from the positive x axis
bool before(const Dir &a, const Dir &b) {
    bool ha = a.y < 0 || (a.y == 0 && a.x < 0), hb = b.y < 0 || (b.y == 0 && b.x < 0);
    if (ha != hb)
        return hb;
    return a.x * b.y - a.y * b.x > 0;
}

vector<Dir> leaves;
// a wall is the line nx x + ny y = c with c > 0: a shot v hits it at time c / (n . v)
vector<ll> nx, ny, cs;
vector<int> tree;

bool better(int w, int u, int leaf) {
    ll vx = leaves[leaf].x, vy = leaves[leaf].y;
    return (nx[w] * vx + ny[w] * vy) * cs[u] > (nx[u] * vx + ny[u] * vy) * cs[w];
}

// Li Chao insertion: two walls swap places at most once on an arc below pi
void push(int node, int lo, int hi, int w) {
    while (true) {
        if (tree[node] < 0) {
            tree[node] = w;
            return;
        }
        int mid = (lo + hi) / 2;
        if (better(w, tree[node], mid))
            swap(w, tree[node]);
        if (lo == hi)
            return;
        if (better(w, tree[node], lo)) {
            node = 2 * node;
            hi = mid;
        } else if (better(w, tree[node], hi)) {
            node = 2 * node + 1;
            lo = mid + 1;
        } else
            return;
    }
}

void insert(int node, int lo, int hi, int left, int right, int w) {
    if (right < lo || hi < left)
        return;
    if (left <= lo && hi <= right) {
        push(node, lo, hi, w);
        return;
    }
    int mid = (lo + hi) / 2;
    insert(2 * node, lo, mid, left, right, w);
    insert(2 * node + 1, mid + 1, hi, left, right, w);
}

int main() {
    vector<vector<ll>> events;
    char word;
    // only the first letter of each word matters
    while (scanf(" %c%*s", &word) == 1 && word != 'e') {
        int count = word == 's' ? 2 : WALL;
        vector<ll> e(count);
        for (ll &v : e)
            scanf("%lld", &v);
        events.push_back(e);
    }
    // the leaves: distinct shot directions by angle
    for (auto &e : events)
        if (e.size() == 2)
            leaves.push_back(reduced(e[0], e[1]));
    sort(leaves.begin(), leaves.end(), before);
    leaves.erase(unique(leaves.begin(), leaves.end()), leaves.end());
    int size = max(1, (int)leaves.size());
    tree.assign(TREE * size, -1);
    for (auto &e : events) {
        if (e.size() == WALL) {
            if (leaves.empty())
                continue; // no shots at all
            ll x1 = e[0], y1 = e[1], x2 = e[2], y2 = e[WALL - 1];
            if (x1 * y2 - y1 * x2 < 0) {
                swap(x1, x2);
                swap(y1, y2);
            }
            ll a = y2 - y1, b = x1 - x2;
            nx.push_back(a);
            ny.push_back(b);
            cs.push_back(a * x1 + b * y1);
            int w = (int)cs.size() - 1;
            // the wall covers the directions from its first end counterclockwise to the second
            Dir first = reduced(x1, y1), last = reduced(x2, y2);
            int lo = lower_bound(leaves.begin(), leaves.end(), first, before) - leaves.begin();
            int hi = upper_bound(leaves.begin(), leaves.end(), last, before) - leaves.begin() - 1;
            if (before(first, last))
                insert(1, 0, size - 1, lo, hi, w);
            else {
                insert(1, 0, size - 1, lo, size - 1, w);
                insert(1, 0, size - 1, 0, hi, w);
            }
            continue;
        }
        ll vx = e[0], vy = e[1];
        int leaf =
            lower_bound(leaves.begin(), leaves.end(), reduced(vx, vy), before) - leaves.begin();
        int node = 1, lo = 0, hi = size - 1, best = -1;
        while (true) {
            int cur = tree[node];
            if (cur >= 0 && (best < 0 || better(cur, best, leaf)))
                best = cur;
            if (lo == hi)
                break;
            int mid = (lo + hi) / 2;
            if (leaf <= mid) {
                node = 2 * node;
                hi = mid;
            } else {
                node = 2 * node + 1;
                lo = mid + 1;
            }
        }
        if (best < 0)
            printf("Infinite\n");
        else {
            ll den = nx[best] * vx + ny[best] * vy;
            ll q = (2 * cs[best] * DIGITS + den) / (2 * den);
            printf("%lld.%09lld\n", q / DIGITS, q % DIGITS);
        }
    }
}
