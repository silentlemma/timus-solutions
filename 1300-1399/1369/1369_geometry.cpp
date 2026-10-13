#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;
typedef __int128 Fixed; // a coordinate times 10^SCALE, exact

const int SCALE = 30;       // decimal digits kept after the point
const int LANDMARKS = 1024; // evenly spread start points for the walks

// error bounds of the floating-point filters
const double ORIENT_ERR = 3.3306690621773722e-16;
const double IN_CIRCLE_ERR = 1.1102230246251565e-15;
const int QUAD = 4;     // edges in a group: an edge and its rotations
const int LAST_ROT = 3; // the last rotation, also the mask of the rotations
const int FIXED_LIMBS = 4;
const int MAX_DIGITS = 128;
const int TEN = 10;

// A signed integer modulo 2^512 in 32-bit limbs; every value used here is far
// below 2^511, so the arithmetic is exact.
const int LIMBS = 16;
const int LIMB_BITS = 32;
struct Big {
    uint32_t a[LIMBS];
};

Big fromFixed(Fixed v) {
    Big r;
    unsigned __int128 u = (unsigned __int128)v;
    uint32_t fill = v < 0 ? ~0u : 0;
    for (int i = 0; i < LIMBS; i++) {
        r.a[i] = i < FIXED_LIMBS ? (uint32_t)u : fill;
        u >>= LIMB_BITS;
    }
    return r;
}

Big add(const Big &x, const Big &y) {
    Big r;
    uint64_t carry = 0;
    for (int i = 0; i < LIMBS; i++) {
        carry += (uint64_t)x.a[i] + y.a[i];
        r.a[i] = (uint32_t)carry;
        carry >>= LIMB_BITS;
    }
    return r;
}

Big sub(const Big &x, const Big &y) {
    Big r;
    int64_t borrow = 0;
    for (int i = 0; i < LIMBS; i++) {
        int64_t z = (int64_t)x.a[i] - y.a[i] + borrow;
        r.a[i] = (uint32_t)z;
        borrow = z < 0 ? -1 : 0;
    }
    return r;
}

Big mul(const Big &x, const Big &y) {
    uint64_t acc[LIMBS] = {};
    for (int i = 0; i < LIMBS; i++) {
        if (!x.a[i])
            continue;
        uint64_t carry = 0;
        for (int j = 0; i + j < LIMBS; j++) {
            uint64_t z = (uint64_t)x.a[i] * y.a[j] + acc[i + j] + carry;
            acc[i + j] = (uint32_t)z;
            carry = z >> LIMB_BITS;
        }
    }
    Big r;
    for (int i = 0; i < LIMBS; i++)
        r.a[i] = (uint32_t)acc[i];
    return r;
}

int sign(const Big &x) {
    if (x.a[LIMBS - 1] >> (LIMB_BITS - 1))
        return -1;
    for (int i = 0; i < LIMBS; i++)
        if (x.a[i])
            return 1;
    return 0;
}

int compare(const Big &x, const Big &y) { return sign(sub(x, y)); }

struct Point {
    Fixed x, y;
    double fx, fy;
    int first, last; // the cockroaches at this point: ids[first..last)
};
vector<Point> pts;

// The squared distance from point i to (qx, qy), exact: SCALE * 2 digits.
Big dist2(int i, Fixed qx, Fixed qy) {
    Fixed dx = pts[i].x - qx, dy = pts[i].y - qy;
    Big bx = fromFixed(dx < 0 ? -dx : dx), by = fromFixed(dy < 0 ? -dy : dy);
    return add(mul(bx, bx), mul(by, by));
}

double dist2f(int i, double x, double y) {
    double dx = pts[i].fx - x, dy = pts[i].fy - y;
    return dx * dx + dy * dy;
}

// ---------------------------------------------------------------- predicates
// Each is evaluated in doubles first; when the result is within the rounding
// error, it is recomputed exactly on the decimal coordinates.
int exactOrient(int a, int b, int c) {
    Big ax = fromFixed(pts[a].x - pts[c].x), ay = fromFixed(pts[a].y - pts[c].y);
    Big bx = fromFixed(pts[b].x - pts[c].x), by = fromFixed(pts[b].y - pts[c].y);
    return sign(sub(mul(ax, by), mul(ay, bx)));
}

int orient(int a, int b, int c) {
    double l = (pts[a].fx - pts[c].fx) * (pts[b].fy - pts[c].fy);
    double r = (pts[a].fy - pts[c].fy) * (pts[b].fx - pts[c].fx);
    double det = l - r, err = ORIENT_ERR * fabs(l + r);
    if (det > err)
        return 1;
    if (det < -err)
        return -1;
    return exactOrient(a, b, c);
}

bool exactInCircle(int a, int b, int c, int d) {
    Big adx = fromFixed(pts[a].x - pts[d].x), ady = fromFixed(pts[a].y - pts[d].y);
    Big bdx = fromFixed(pts[b].x - pts[d].x), bdy = fromFixed(pts[b].y - pts[d].y);
    Big cdx = fromFixed(pts[c].x - pts[d].x), cdy = fromFixed(pts[c].y - pts[d].y);
    Big ab = sub(mul(adx, bdy), mul(bdx, ady));
    Big bc = sub(mul(bdx, cdy), mul(cdx, bdy));
    Big ca = sub(mul(cdx, ady), mul(adx, cdy));
    Big al = add(mul(adx, adx), mul(ady, ady));
    Big bl = add(mul(bdx, bdx), mul(bdy, bdy));
    Big cl = add(mul(cdx, cdx), mul(cdy, cdy));
    return sign(add(add(mul(al, bc), mul(bl, ca)), mul(cl, ab))) > 0;
}

// d lies strictly inside the circle through a, b, c (counterclockwise)
bool inCircle(int a, int b, int c, int d) {
    double adx = pts[a].fx - pts[d].fx, ady = pts[a].fy - pts[d].fy;
    double bdx = pts[b].fx - pts[d].fx, bdy = pts[b].fy - pts[d].fy;
    double cdx = pts[c].fx - pts[d].fx, cdy = pts[c].fy - pts[d].fy;
    double bdxcdy = bdx * cdy, cdxbdy = cdx * bdy;
    double cdxady = cdx * ady, adxcdy = adx * cdy;
    double adxbdy = adx * bdy, bdxady = bdx * ady;
    double al = adx * adx + ady * ady, bl = bdx * bdx + bdy * bdy, cl = cdx * cdx + cdy * cdy;
    double det = al * (bdxcdy - cdxbdy) + bl * (cdxady - adxcdy) + cl * (adxbdy - bdxady);
    double permanent = (fabs(bdxcdy) + fabs(cdxbdy)) * al + (fabs(cdxady) + fabs(adxcdy)) * bl +
                       (fabs(adxbdy) + fabs(bdxady)) * cl;
    double err = IN_CIRCLE_ERR * permanent;
    if (det > err)
        return true;
    if (det < -err)
        return false;
    return exactInCircle(a, b, c, d);
}

// ---------------------------------------------------------------- triangulation
// Delaunay triangulation by divide and conquer on quad-edges: edge e, its
// rotations e+1..e+3 within one group of four, rev(e) the same edge reversed.
vector<int> orig, nextEdge, freeEdges;
vector<char> active;

int rot(int e) { return (e & ~LAST_ROT) | ((e + 1) & LAST_ROT); }
int invrot(int e) { return (e & ~LAST_ROT) | ((e + LAST_ROT) & LAST_ROT); }
int rev(int e) { return e ^ 2; }
int dest(int e) { return orig[rev(e)]; }
int lnext(int e) { return rot(nextEdge[invrot(e)]); }
int oprev(int e) { return rot(nextEdge[rot(e)]); }

int makeEdge(int a, int b) {
    int e;
    if (!freeEdges.empty()) {
        e = freeEdges.back();
        freeEdges.pop_back();
    } else {
        e = orig.size();
        orig.resize(e + QUAD);
        nextEdge.resize(e + QUAD);
        active.push_back(0);
    }
    orig[e] = a, orig[e + 1] = -1, orig[e + 2] = b, orig[e + LAST_ROT] = -1;
    nextEdge[e] = e, nextEdge[e + 2] = e + 2;
    nextEdge[e + 1] = e + LAST_ROT, nextEdge[e + LAST_ROT] = e + 1;
    active[e >> 2] = 1;
    return e;
}

void splice(int a, int b) {
    int alpha = rot(nextEdge[a]), beta = rot(nextEdge[b]);
    swap(nextEdge[alpha], nextEdge[beta]);
    swap(nextEdge[a], nextEdge[b]);
}

void deleteEdge(int e) {
    splice(e, oprev(e));
    splice(rev(e), oprev(rev(e)));
    active[e >> 2] = 0;
    freeEdges.push_back(e & ~LAST_ROT);
}

int connect(int a, int b) {
    int e = makeEdge(dest(a), orig[b]);
    splice(e, lnext(a));
    splice(rev(e), b);
    return e;
}

bool leftOf(int p, int e) { return orient(orig[e], dest(e), p) > 0; }
bool rightOf(int p, int e) { return orient(orig[e], dest(e), p) < 0; }

// points l..r (sorted by x, then y); returns the counterclockwise hull edge
// out of the leftmost point and the clockwise one out of the rightmost
pair<int, int> build(int l, int r) {
    if (r - l == 1) {
        int e = makeEdge(l, r);
        return {e, rev(e)};
    }
    if (r - l == 2) {
        int a = makeEdge(l, l + 1), b = makeEdge(l + 1, r);
        splice(rev(a), b);
        int turn = orient(l, l + 1, r);
        if (turn == 0)
            return {a, rev(b)};
        int c = connect(b, a);
        if (turn > 0)
            return {a, rev(b)};
        return {rev(c), c};
    }
    int mid = (l + r) / 2;
    auto [ldo, ldi] = build(l, mid);
    auto [rdi, rdo] = build(mid + 1, r);
    for (;;) { // the lower common tangent
        if (leftOf(orig[rdi], ldi))
            ldi = lnext(ldi);
        else if (rightOf(orig[ldi], rdi))
            rdi = nextEdge[rev(rdi)];
        else
            break;
    }
    int basel = connect(rev(rdi), ldi);
    auto valid = [&](int e) { return rightOf(dest(e), basel); };
    if (orig[ldi] == orig[ldo])
        ldo = rev(basel);
    if (orig[rdi] == orig[rdo])
        rdo = basel;
    for (;;) { // zip the halves upward
        int lc = nextEdge[rev(basel)];
        if (valid(lc))
            while (inCircle(dest(basel), orig[basel], dest(lc), dest(nextEdge[lc]))) {
                int t = nextEdge[lc];
                deleteEdge(lc);
                lc = t;
            }
        int rc = oprev(basel);
        if (valid(rc))
            while (inCircle(dest(basel), orig[basel], dest(rc), dest(oprev(rc)))) {
                int t = oprev(rc);
                deleteEdge(rc);
                rc = t;
            }
        bool lv = valid(lc), rv = valid(rc);
        if (!lv && !rv)
            break;
        if (!lv || (rv && inCircle(dest(lc), orig[lc], orig[rc], dest(rc))))
            basel = connect(rc, rev(basel));
        else
            basel = connect(rev(basel), rev(lc));
    }
    return {ldo, rdo};
}

// ---------------------------------------------------------------- the graph
// The triangulation plus the neighbours in the order by x and by y, as
// adjacency lists offset[v]..offset[v+1] in adj.
vector<int> offsetOf, adj;

void makeGraph(vector<uint64_t> &keys, int n) {
    sort(keys.begin(), keys.end());
    keys.erase(unique(keys.begin(), keys.end()), keys.end());
    offsetOf.assign(n + 1, 0);
    for (uint64_t k : keys)
        offsetOf[(k >> LIMB_BITS) + 1]++, offsetOf[(uint32_t)k + 1]++;
    for (int i = 0; i < n; i++)
        offsetOf[i + 1] += offsetOf[i];
    vector<int> at(offsetOf.begin(), offsetOf.end() - 1);
    adj.resize(offsetOf[n]);
    for (uint64_t k : keys) {
        int a = k >> LIMB_BITS, b = (uint32_t)k;
        adj[at[a]++] = b;
        adj[at[b]++] = a;
    }
}

uint64_t edgeKey(int a, int b) {
    if (a > b)
        swap(a, b);
    return (uint64_t)a << LIMB_BITS | (uint32_t)b;
}

// ---------------------------------------------------------------- input
char *in;

char *token() {
    while (*in && *in <= ' ')
        in++;
    char *s = in;
    while (*in > ' ')
        in++;
    if (*in)
        *in++ = 0;
    return s;
}

// a decimal number times 10^SCALE, digits beyond that dropped
Fixed parseFixed(const char *s) {
    bool negative = *s == '-';
    if (*s == '-' || *s == '+')
        s++;
    char digits[MAX_DIGITS];
    int count = 0, fraction = 0, exponent = 0;
    bool dot = false;
    for (; *s && *s != 'e' && *s != 'E'; s++) {
        if (*s == '.') {
            dot = true;
            continue;
        }
        if (count < (int)sizeof digits)
            digits[count++] = *s - '0';
        fraction += dot;
    }
    if (*s)
        exponent = atoi(s + 1);
    int shift = SCALE - fraction + exponent, keep = count;
    if (shift < 0)
        keep = max(0, count + shift);
    Fixed v = 0;
    for (int i = 0; i < keep; i++)
        v = v * TEN + digits[i];
    for (int i = 0; i < shift; i++)
        v *= TEN;
    return negative ? -v : v;
}

// the point nearest to the sweet: a walk on doubles, then an exact one
int nearestPoint(int seed, Fixed qx, Fixed qy, double x, double y) {
    int cur = seed;
    for (;;) {
        int best = cur;
        double bd = dist2f(cur, x, y);
        for (int k = offsetOf[cur]; k < offsetOf[cur + 1]; k++) {
            double z = dist2f(adj[k], x, y);
            if (z < bd)
                bd = z, best = adj[k];
        }
        if (best == cur)
            break;
        cur = best;
    }
    for (;;) {
        int best = cur;
        Big bd = dist2(cur, qx, qy);
        for (int k = offsetOf[cur]; k < offsetOf[cur + 1]; k++) {
            Big z = dist2(adj[k], qx, qy);
            if (compare(z, bd) < 0)
                bd = z, best = adj[k];
        }
        if (best == cur)
            return cur;
        cur = best;
    }
}

int main() {
    vector<char> buf;
    {
        const size_t CHUNK = 1 << 16;
        size_t n = 0;
        for (;;) {
            buf.resize(n + CHUNK + 1);
            size_t got = fread(buf.data() + n, 1, CHUNK, stdin);
            n += got;
            if (!got)
                break;
        }
        buf[n] = 0;
    }
    in = buf.data();
    int m = atoi(token());
    vector<Point> raw(m);
    for (int i = 0; i < m; i++) {
        char *tx = token(), *ty = token();
        raw[i] = Point{parseFixed(tx), parseFixed(ty), strtod(tx, nullptr), strtod(ty, nullptr), i,
                       i + 1};
    }
    int n = atoi(token());
    if (n == 0)
        return 0;
    // equal points become one, keeping all their cockroaches
    sort(raw.begin(), raw.end(), [](const Point &a, const Point &b) {
        if (a.x != b.x)
            return a.x < b.x;
        if (a.y != b.y)
            return a.y < b.y;
        return a.first < b.first;
    });
    vector<int> ids;
    for (int i = 0; i < m;) {
        int j = i, start = ids.size();
        for (; j < m && raw[j].x == raw[i].x && raw[j].y == raw[i].y; j++)
            ids.push_back(raw[j].first + 1);
        Point p = raw[i];
        p.first = start, p.last = ids.size();
        pts.push_back(p);
        i = j;
    }
    int k = pts.size();
    vector<uint64_t> keys;
    bool collinear = true;
    for (int i = 2; i < k && collinear; i++)
        collinear = orient(0, 1, i) == 0;
    if (k > 2 && !collinear) {
        build(0, k - 1);
        for (size_t q = 0; q < active.size(); q++)
            if (active[q])
                keys.push_back(edgeKey(orig[q * QUAD], orig[q * QUAD + 2]));
        vector<int> byY(k);
        for (int i = 0; i < k; i++)
            byY[i] = i;
        sort(byY.begin(), byY.end(), [](int a, int b) {
            if (pts[a].y != pts[b].y)
                return pts[a].y < pts[b].y;
            return pts[a].x < pts[b].x;
        });
        for (int i = 1; i < k; i++)
            keys.push_back(edgeKey(byY[i - 1], byY[i]));
    }
    for (int i = 1; i < k; i++) // neighbours by x; on a line, all edges
        keys.push_back(edgeKey(i - 1, i));
    makeGraph(keys, k);

    // the answer: the nearest point and every point closer than it plus EPS,
    // found by a search through the graph from it
    Big ten60 = fromFixed(1);
    Big ten = fromFixed(TEN);
    for (int i = 0; i < 2 * SCALE; i++)
        ten60 = mul(ten60, ten);
    const int EPS_BITS = 24; // EPS = 2^-24 on squared distances
    Big eps = ten60;         // EPS times 10^(2 * SCALE), an integer
    for (int i = 0; i < EPS_BITS; i++) {
        uint32_t carry = 0;
        for (int j = LIMBS - 1; j >= 0; j--) {
            uint32_t low = eps.a[j] & 1;
            eps.a[j] = eps.a[j] >> 1 | carry << (LIMB_BITS - 1);
            carry = low;
        }
    }
    int marks = min(LANDMARKS, k);
    vector<int> landmark(marks);
    for (int i = 0; i < marks; i++)
        landmark[i] = (long long)i * (k - 1) / max(1, marks - 1);
    vector<int> seen(k, 0), queue, answer;
    int prev = 0;
    for (int stamp = 1; stamp <= n; stamp++) {
        char *tx = token(), *ty = token();
        Fixed qx = parseFixed(tx), qy = parseFixed(ty);
        double x = strtod(tx, nullptr), y = strtod(ty, nullptr);
        int seed = prev;
        double bd = dist2f(seed, x, y);
        for (int v : landmark)
            if (dist2f(v, x, y) < bd)
                bd = dist2f(v, x, y), seed = v;
        int best = nearestPoint(seed, qx, qy, x, y);
        prev = best;
        Big limit = add(dist2(best, qx, qy), eps);
        queue.assign(1, best);
        answer.clear();
        seen[best] = stamp;
        for (size_t h = 0; h < queue.size(); h++) {
            int v = queue[h];
            if (compare(dist2(v, qx, qy), limit) >= 0)
                continue;
            answer.insert(answer.end(), ids.begin() + pts[v].first, ids.begin() + pts[v].last);
            for (int e = offsetOf[v]; e < offsetOf[v + 1]; e++)
                if (seen[adj[e]] != stamp) {
                    seen[adj[e]] = stamp;
                    queue.push_back(adj[e]);
                }
        }
        sort(answer.begin(), answer.end());
        for (size_t i = 0; i < answer.size(); i++)
            printf(i ? " %d" : "%d", answer[i]);
        printf("\n");
    }
}
