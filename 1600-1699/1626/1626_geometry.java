import java.io.*;
import java.util.*;

public class Main {
    static final int WORD = 64;
    static int n, words;
    static long[] xs, ys;
    static long lastMask;

    static long cross(long ox, long oy, long ax, long ay, long bx, long by) {
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
    }

    static long next(StreamTokenizer in) throws IOException {
        in.nextToken();
        return (long)in.nval;
    }

    static long cross(int o, int a, int b) {
        return cross(xs[o], ys[o], xs[a], ys[a], xs[b], ys[b]);
    }

    static void set(long[] b, int base, int k) {
        b[base + k / WORD] |= 1L << (k % WORD);
    }

    static boolean has(long[] b, int base, int k) {
        return (b[base + k / WORD] >>> (k % WORD) & 1) != 0;
    }

    static void clear(long[] b, int base, int k) {
        b[base + k / WORD] &= ~(1L << (k % WORD));
    }

    // j lies strictly inside the interior angle of the polygon at i
    static boolean inCone(int i, int j) {
        int prv = (i + n - 1) % n, nxt = (i + 1) % n;
        long base = cross(i, nxt, prv);
        long toNext = cross(i, nxt, j), toPrev = cross(i, prv, j);
        if (base >= 0)
            return toNext > 0 && toPrev < 0;
        return toNext > 0 || toPrev < 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        n = (int)in.nval;
        xs = new long[n];
        ys = new long[n];
        int[] orig = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = (long)in.nval;
            in.nextToken();
            ys[i] = (long)in.nval;
            orig[i] = i;
        }
        long sx1 = next(in), sy1 = next(in), sx2 = next(in), sy2 = next(in);
        long area = 0;
        for (int i = 0; i < n; i++)
            area += xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i];
        if (area < 0) // counterclockwise from now on
            for (int l = 0, r = n - 1; l < r; l++, r--) {
                long t = xs[l];
                xs[l] = xs[r];
                xs[r] = t;
                t = ys[l];
                ys[l] = ys[r];
                ys[r] = t;
                int o = orig[l];
                orig[l] = orig[r];
                orig[r] = o;
            }
        words = (n + WORD - 1) / WORD;
        lastMask = n % WORD != 0 ? (1L << (n % WORD)) - 1 : -1L;

        // left[a][b] for a < b: the vertices strictly left of the line a -> b
        int[] pairIndex = new int[n * n];
        int pairs = 0;
        for (int a = 0; a < n; a++)
            for (int b = a + 1; b < n; b++) {
                pairIndex[a * n + b] = pairs;
                pairIndex[b * n + a] = pairs++;
            }
        // the hot loop in int arithmetic: |coordinates| <= 10^4 keeps it below 2^31
        int[] xi = new int[n], yi = new int[n];
        for (int i = 0; i < n; i++) {
            xi[i] = (int)xs[i];
            yi[i] = (int)ys[i];
        }
        long[] left = new long[pairs * words];
        for (int a = 0; a < n; a++)
            for (int b = a + 1; b < n; b++) {
                int base = pairIndex[a * n + b] * words;
                int dx = xi[b] - xi[a], dy = yi[b] - yi[a], c0 = dy * xi[a] - dx * yi[a];
                for (int w = 0; w < words; w++) {
                    long bits = 0;
                    for (int k = w * WORD, hi = Math.min(n, k + WORD); k < hi; k++)
                        if (dx * yi[k] - dy * xi[k] + c0 > 0)
                            bits |= 1L << (k - w * WORD);
                    left[base + w] = bits;
                }
            }
        // bit k: the vertex is strictly left of edge k -> k + 1
        long[] edgeLeft = new long[n * words];
        for (int v = 0; v < n; v++)
            for (int k = 0; k < n; k++)
                if (cross(k, (k + 1) % n, v) > 0)
                    set(edgeLeft, v * words, k);

        // vis[a]: the vertices joined to a by an edge or a diagonal
        long[] vis = new long[n * words];
        for (int i = 0; i < n; i++) {
            set(vis, i * words, (i + 1) % n);
            set(vis, (i + 1) % n * words, i);
        }
        long[] hits = new long[words];
        for (int i = 0; i < n; i++)
            for (int j = i + 2; j < n; j++) {
                if ((j + 1) % n == i || !inCone(i, j) || !inCone(j, i))
                    continue;
                int line = pairIndex[i * n + j] * words, eli = i * words, elj = j * words;
                // edges whose ends lie on different sides of the line, and whose
                // line separates i from j; those touching i or j cannot cross
                for (int w = 0; w < words; w++) {
                    long shifted = left[line + w] >>> 1;
                    if (w + 1 < words)
                        shifted |= left[line + w + 1] << (WORD - 1);
                    hits[w] = (left[line + w] ^ shifted) & (edgeLeft[eli + w] ^ edgeLeft[elj + w]);
                }
                clear(hits, 0, n - 1); // edge n - 1 -> 0 wraps around
                if (has(left, line, 0) != has(left, line, n - 1)
                    && has(edgeLeft, eli, n - 1) != has(edgeLeft, elj, n - 1))
                    set(hits, 0, n - 1);
                hits[words - 1] &= lastMask;
                for (int k : new int[] {(i + n - 1) % n, i, (j + n - 1) % n, j})
                    clear(hits, 0, k);
                boolean crossing = false;
                for (int w = 0; w < words && !crossing; w++)
                    for (long m = hits[w]; m != 0; m &= m - 1) {
                        int k = w * WORD + Long.numberOfTrailingZeros(m);
                        long d1 = cross(i, j, k), d2 = cross(i, j, (k + 1) % n);
                        if ((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) {
                            crossing = true;
                            break;
                        }
                    }
                if (crossing)
                    continue;
                boolean blocked = false; // a vertex on the open segment
                for (int k = 0; k < n && !blocked; k++)
                    if (k != i && k != j && cross(i, j, k) == 0) {
                        long dot = (xs[k] - xs[i]) * (xs[k] - xs[j]);
                        dot += (ys[k] - ys[i]) * (ys[k] - ys[j]);
                        blocked = dot < 0;
                    }
                if (!blocked) {
                    set(vis, i * words, j);
                    set(vis, j * words, i);
                }
            }

        // bit k: k strictly left of the line a -> s1 (and a -> s2)
        long[] left1 = new long[n * words], left2 = new long[n * words];
        for (int a = 0; a < n; a++)
            for (int k = 0; k < n; k++) {
                if (cross(xs[a], ys[a], sx1, sy1, xs[k], ys[k]) > 0)
                    set(left1, a * words, k);
                if (cross(xs[a], ys[a], sx2, sy2, xs[k], ys[k]) > 0)
                    set(left2, a * words, k);
            }
        // a triangle a, b, k counterclockwise whose sides are edges or diagonals,
        // with both ends of S strictly inside and no vertex inside
        long[] right1 = new long[words], right2 = new long[words], cand = new long[words];
        long[] ab = new long[words], bk = new long[words], ka = new long[words];
        for (int b = 0; b < n; b++) {
            Arrays.fill(right1, 0);
            Arrays.fill(right2, 0);
            for (int k = 0; k < n; k++) {
                if (cross(xs[b], ys[b], sx1, sy1, xs[k], ys[k]) < 0)
                    set(right1, 0, k);
                if (cross(xs[b], ys[b], sx2, sy2, xs[k], ys[k]) < 0)
                    set(right2, 0, k);
            }
            for (int a = 0; a < n; a++) {
                if (a == b || !has(vis, a * words, b))
                    continue;
                if (cross(xs[a], ys[a], xs[b], ys[b], sx1, sy1) <= 0
                    || cross(xs[a], ys[a], xs[b], ys[b], sx2, sy2) <= 0)
                    continue;
                for (int w = 0; w < words; w++)
                    cand[w] = vis[a * words + w] & vis[b * words + w] & left1[a * words + w]
                        & left2[a * words + w] & right1[w] & right2[w];
                clear(cand, 0, a);
                clear(cand, 0, b);
                strictlyLeft(left, pairIndex, a, b, ab);
                for (int w = 0; w < words; w++)
                    for (long m = cand[w]; m != 0; m &= m - 1) {
                        int k = w * WORD + Long.numberOfTrailingZeros(m);
                        strictlyLeft(left, pairIndex, b, k, bk);
                        strictlyLeft(left, pairIndex, k, a, ka);
                        boolean empty = true;
                        for (int u = 0; u < words && empty; u++) {
                            long inside = ab[u] & bk[u] & ka[u];
                            for (int v : new int[] {a, b, k})
                                if (v / WORD == u)
                                    inside &= ~(1L << (v % WORD));
                            empty = inside == 0;
                        }
                        if (empty) {
                            int[] tri = {orig[a] + 1, orig[b] + 1, orig[k] + 1};
                            System.out.println(tri[0] + " " + tri[1] + " " + tri[2]);
                            return;
                        }
                    }
            }
        }
        System.out.println("Impossible");
    }

    // when a comes after b: the complement of the other side, which also
    // counts the points on the line; used only where those cannot occur
    static void strictlyLeft(long[] left, int[] pairIndex, int a, int b, long[] out) {
        int base = pairIndex[a * n + b] * words;
        for (int w = 0; w < words; w++)
            out[w] = a < b ? left[base + w] : ~left[base + w];
        out[words - 1] &= lastMask;
    }
}
