#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;

const int WORD = 64;

int n, words;
vector<long long> xs, ys;
uint64_t lastMask;

long long cross(long long ox, long long oy, long long ax, long long ay, long long bx,
                long long by) {
    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
}

void setBit(uint64_t *b, int k) { b[k / WORD] |= 1ULL << (k % WORD); }
bool hasBit(const uint64_t *b, int k) { return b[k / WORD] >> (k % WORD) & 1; }
void clearBit(uint64_t *b, int k) { b[k / WORD] &= ~(1ULL << (k % WORD)); }

// j lies strictly inside the interior angle of the polygon at i
bool inCone(int i, int j) {
    int prv = (i + n - 1) % n, nxt = (i + 1) % n;
    long long base = cross(xs[i], ys[i], xs[nxt], ys[nxt], xs[prv], ys[prv]);
    long long toNext = cross(xs[i], ys[i], xs[nxt], ys[nxt], xs[j], ys[j]);
    long long toPrev = cross(xs[i], ys[i], xs[prv], ys[prv], xs[j], ys[j]);
    if (base >= 0)
        return toNext > 0 && toPrev < 0;
    return toNext > 0 || toPrev < 0;
}

int main() {
    if (scanf("%d", &n) != 1)
        return 0;
    xs.resize(n), ys.resize(n);
    vector<int> orig(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &xs[i], &ys[i]);
        orig[i] = i;
    }
    long long sx1, sy1, sx2, sy2;
    scanf("%lld %lld %lld %lld", &sx1, &sy1, &sx2, &sy2);
    long long area = 0;
    for (int i = 0; i < n; i++)
        area += xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i];
    if (area < 0) // counterclockwise from now on
        for (int l = 0, r = n - 1; l < r; l++, r--) {
            swap(xs[l], xs[r]);
            swap(ys[l], ys[r]);
            swap(orig[l], orig[r]);
        }
    words = (n + WORD - 1) / WORD;
    lastMask = n % WORD ? (1ULL << (n % WORD)) - 1 : ~0ULL;

    // left[a][b] for a < b: the vertices strictly left of the line a -> b
    vector<int> pairIndex(n * n);
    int pairs = 0;
    for (int a = 0; a < n; a++)
        for (int b = a + 1; b < n; b++)
            pairIndex[a * n + b] = pairIndex[b * n + a] = pairs++;
    vector<uint64_t> left((size_t)pairs * words, 0);
    for (int a = 0; a < n; a++)
        for (int b = a + 1; b < n; b++) {
            uint64_t *bs = &left[(size_t)pairIndex[a * n + b] * words];
            for (int k = 0; k < n; k++)
                if (cross(xs[a], ys[a], xs[b], ys[b], xs[k], ys[k]) > 0)
                    setBit(bs, k);
        }
    // when a comes after b: the complement of the other side, which also
    // counts the points on the line; used only where those cannot occur
    auto strictlyLeft = [&](int a, int b, uint64_t *out) {
        const uint64_t *src = &left[(size_t)pairIndex[a * n + b] * words];
        for (int w = 0; w < words; w++)
            out[w] = a < b ? src[w] : ~src[w];
        out[words - 1] &= lastMask;
    };
    // bit k: the vertex is strictly left of edge k -> k + 1
    vector<uint64_t> edgeLeft(n * words, 0);
    for (int v = 0; v < n; v++)
        for (int k = 0; k < n; k++) {
            int kn = (k + 1) % n;
            if (cross(xs[k], ys[k], xs[kn], ys[kn], xs[v], ys[v]) > 0)
                setBit(&edgeLeft[v * words], k);
        }

    // vis[a]: the vertices joined to a by an edge or a diagonal
    vector<uint64_t> vis(n * words, 0);
    for (int i = 0; i < n; i++) {
        setBit(&vis[i * words], (i + 1) % n);
        setBit(&vis[(i + 1) % n * words], i);
    }
    vector<uint64_t> hits(words);
    for (int i = 0; i < n; i++)
        for (int j = i + 2; j < n; j++) {
            if ((j + 1) % n == i || !inCone(i, j) || !inCone(j, i))
                continue;
            const uint64_t *line = &left[(size_t)pairIndex[i * n + j] * words];
            const uint64_t *eli = &edgeLeft[i * words], *elj = &edgeLeft[j * words];
            // edges whose ends lie on different sides of the line, and whose
            // line separates i from j; those touching i or j cannot cross
            for (int w = 0; w < words; w++) {
                uint64_t shifted = line[w] >> 1;
                if (w + 1 < words)
                    shifted |= line[w + 1] << (WORD - 1);
                hits[w] = (line[w] ^ shifted) & (eli[w] ^ elj[w]);
            }
            clearBit(hits.data(), n - 1); // edge n - 1 -> 0 wraps around
            if (hasBit(line, 0) != hasBit(line, n - 1) && hasBit(eli, n - 1) != hasBit(elj, n - 1))
                setBit(hits.data(), n - 1);
            hits[words - 1] &= lastMask;
            for (int k : {(i + n - 1) % n, i, (j + n - 1) % n, j})
                clearBit(hits.data(), k);
            bool crossing = false;
            for (int w = 0; w < words && !crossing; w++)
                for (uint64_t m = hits[w]; m; m &= m - 1) {
                    int k = w * WORD + __builtin_ctzll(m), kn = (k + 1) % n;
                    long long d1 = cross(xs[i], ys[i], xs[j], ys[j], xs[k], ys[k]);
                    long long d2 = cross(xs[i], ys[i], xs[j], ys[j], xs[kn], ys[kn]);
                    if ((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) {
                        crossing = true;
                        break;
                    }
                }
            if (crossing)
                continue;
            bool blocked = false; // a vertex on the open segment
            for (int k = 0; k < n && !blocked; k++)
                if (k != i && k != j && cross(xs[i], ys[i], xs[j], ys[j], xs[k], ys[k]) == 0 &&
                    (xs[k] - xs[i]) * (xs[k] - xs[j]) + (ys[k] - ys[i]) * (ys[k] - ys[j]) < 0)
                    blocked = true;
            if (!blocked) {
                setBit(&vis[i * words], j);
                setBit(&vis[j * words], i);
            }
        }

    vector<uint64_t> left1(n * words, 0), left2(n * words, 0); // k strictly left of a -> s
    for (int a = 0; a < n; a++)
        for (int k = 0; k < n; k++) {
            if (cross(xs[a], ys[a], sx1, sy1, xs[k], ys[k]) > 0)
                setBit(&left1[a * words], k);
            if (cross(xs[a], ys[a], sx2, sy2, xs[k], ys[k]) > 0)
                setBit(&left2[a * words], k);
        }
    // a triangle a, b, k counterclockwise whose sides are edges or diagonals,
    // with both ends of S strictly inside and no vertex inside
    vector<uint64_t> right1(words), right2(words), cand(words), ab(words), bk(words), ka(words);
    for (int b = 0; b < n; b++) {
        fill(right1.begin(), right1.end(), 0);
        fill(right2.begin(), right2.end(), 0);
        for (int k = 0; k < n; k++) {
            if (cross(xs[b], ys[b], sx1, sy1, xs[k], ys[k]) < 0)
                setBit(right1.data(), k);
            if (cross(xs[b], ys[b], sx2, sy2, xs[k], ys[k]) < 0)
                setBit(right2.data(), k);
        }
        for (int a = 0; a < n; a++) {
            if (a == b || !hasBit(&vis[a * words], b))
                continue;
            if (cross(xs[a], ys[a], xs[b], ys[b], sx1, sy1) <= 0 ||
                cross(xs[a], ys[a], xs[b], ys[b], sx2, sy2) <= 0)
                continue;
            for (int w = 0; w < words; w++)
                cand[w] = vis[a * words + w] & vis[b * words + w] & left1[a * words + w] &
                          left2[a * words + w] & right1[w] & right2[w];
            clearBit(cand.data(), a);
            clearBit(cand.data(), b);
            strictlyLeft(a, b, ab.data());
            for (int w = 0; w < words; w++)
                for (uint64_t m = cand[w]; m; m &= m - 1) {
                    int k = w * WORD + __builtin_ctzll(m);
                    strictlyLeft(b, k, bk.data());
                    strictlyLeft(k, a, ka.data());
                    bool empty = true;
                    for (int u = 0; u < words && empty; u++) {
                        uint64_t inside = ab[u] & bk[u] & ka[u];
                        for (int v : {a, b, k})
                            if (v / WORD == u)
                                inside &= ~(1ULL << (v % WORD));
                        empty = inside == 0;
                    }
                    if (empty) {
                        printf("%d %d %d\n", orig[a] + 1, orig[b] + 1, orig[k] + 1);
                        return 0;
                    }
                }
        }
    }
    printf("Impossible\n");
}
