import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
    static final int SCALE = 30;       // decimal digits kept after the point
    static final int LANDMARKS = 1024; // evenly spread start points for the walks

    // error bounds of the floating-point filters
    static final double ORIENT_ERR = 3.3306690621773722e-16;
    static final double IN_CIRCLE_ERR = 1.1102230246251565e-15;
    static final int QUAD = 4;     // edges in a group: an edge and its rotations
    static final int LAST_ROT = 3; // the last rotation, also the mask of the rotations
    static final int FIXED_LIMBS = 4;
    static final int HALF_BITS = 16;
    static final long HALF_MASK = (1L << HALF_BITS) - 1;
    static final int BUF_SIZE = 1 << 16;
    static final int TEN = 10;
    static final int LIMBS = 16;
    static final int LIMB_BITS = 32;
    static final long LIMB_MASK = 0xffffffffL;
    static final int KEY_BITS = 32;
    static final int EPS_BITS = 24; // EPS = 2^-24 on squared distances
    static final double EPS_FLOAT = 1.0 / (1 << EPS_BITS);
    // above the rounding error of a difference of squared distances
    static final double SLACK = 1e-6;
    static final double RELATIVE_SLACK = 1e-12;
    static int[] eps; // EPS times 10^(2 * SCALE)

    // A big number is a signed integer modulo 2^512 in 32-bit limbs; every
    // value used here is far below 2^511, so the arithmetic is exact.
    static int[] fromFixed(long hi, long lo) {
        int[] r = new int[LIMBS];
        int fill = hi < 0 ? -1 : 0;
        Arrays.fill(r, fill);
        long[] halves = {lo, hi};
        for (int i = 0; i < FIXED_LIMBS; i++) {
            r[i] = (int)(halves[i / 2] >>> (LIMB_BITS * (i % 2)));
        }
        return r;
    }

    static int[] add(int[] x, int[] y) {
        int[] r = new int[LIMBS];
        long carry = 0;
        for (int i = 0; i < LIMBS; i++) {
            carry += (x[i] & LIMB_MASK) + (y[i] & LIMB_MASK);
            r[i] = (int)carry;
            carry >>>= LIMB_BITS;
        }
        return r;
    }

    static int[] sub(int[] x, int[] y) {
        int[] r = new int[LIMBS];
        long borrow = 0;
        for (int i = 0; i < LIMBS; i++) {
            long z = (x[i] & LIMB_MASK) - (y[i] & LIMB_MASK) + borrow;
            r[i] = (int)z;
            borrow = z < 0 ? -1 : 0;
        }
        return r;
    }

    static int[] negate(int[] x) { return sub(new int[LIMBS], x); }

    // the limbs below the highest nonzero one
    static int used(int[] x) {
        int n = LIMBS;
        while (n > 0 && x[n - 1] == 0) {
            n--;
        }
        return n;
    }

    // multiplies the magnitudes over their used limbs only, then sets the sign
    static int[] mul(int[] x, int[] y) {
        boolean negative = (x[LIMBS - 1] < 0) != (y[LIMBS - 1] < 0);
        if (x[LIMBS - 1] < 0) {
            x = negate(x);
        }
        if (y[LIMBS - 1] < 0) {
            y = negate(y);
        }
        int nx = used(x);
        int ny = used(y);
        long[] acc = new long[LIMBS];
        for (int i = 0; i < nx; i++) {
            if (x[i] == 0) {
                continue;
            }
            long xi = x[i] & LIMB_MASK;
            long carry = 0;
            for (int j = 0; i + j < LIMBS && (j < ny || carry != 0); j++) {
                long lowPart = xi * (y[j] & HALF_MASK);
                long highPart = xi * ((y[j] >>> HALF_BITS) & HALF_MASK);
                // xi * y[j] can reach 2^64: add it in two halves of y[j]
                long z = acc[i + j] + carry + (lowPart & LIMB_MASK) +
                         ((highPart & HALF_MASK) << HALF_BITS);
                acc[i + j] = z & LIMB_MASK;
                carry = (z >>> LIMB_BITS) + (lowPart >>> LIMB_BITS) + (highPart >>> HALF_BITS);
            }
        }
        int[] r = new int[LIMBS];
        for (int i = 0; i < LIMBS; i++) {
            r[i] = (int)acc[i];
        }
        return negative ? negate(r) : r;
    }

    static int sign(int[] x) {
        if (x[LIMBS - 1] < 0) {
            return -1;
        }
        for (int v : x) {
            if (v != 0) {
                return 1;
            }
        }
        return 0;
    }

    static boolean less(int[] x, int[] y) { return sign(sub(x, y)) < 0; }

    // the points: coordinates times 10^SCALE as 128-bit numbers (hi, lo)
    static long[] xHi, xLo, yHi, yLo;
    static double[] fx, fy;
    static int[] first, last; // the cockroaches at a point: ids[first..last)

    // a - b for 128-bit numbers, as a big number
    static int[] diff(long aHi, long aLo, long bHi, long bLo) {
        long lo = aLo - bLo;
        long hi = aHi - bHi - (Long.compareUnsigned(aLo, bLo) < 0 ? 1 : 0);
        return fromFixed(hi, lo);
    }

    static int[] dx(int a, int b) { return diff(xHi[a], xLo[a], xHi[b], xLo[b]); }

    static int[] dy(int a, int b) { return diff(yHi[a], yLo[a], yHi[b], yLo[b]); }

    static int compare128(long aHi, long aLo, long bHi, long bLo) {
        if (aHi != bHi) {
            return Long.compare(aHi, bHi);
        }
        return Long.compareUnsigned(aLo, bLo);
    }

    // Each predicate is evaluated in floating point first; when the result is
    // within the rounding error, it is recomputed exactly on the decimals.
    static int orient(int a, int b, int c) {
        double l = (fx[a] - fx[c]) * (fy[b] - fy[c]);
        double r = (fy[a] - fy[c]) * (fx[b] - fx[c]);
        double det = l - r;
        double err = ORIENT_ERR * Math.abs(l + r);
        if (det > err) {
            return 1;
        }
        if (det < -err) {
            return -1;
        }
        return sign(sub(mul(dx(a, c), dy(b, c)), mul(dy(a, c), dx(b, c))));
    }

    static boolean exactInCircle(int a, int b, int c, int d) {
        int[] adx = dx(a, d);
        int[] ady = dy(a, d);
        int[] bdx = dx(b, d);
        int[] bdy = dy(b, d);
        int[] cdx = dx(c, d);
        int[] cdy = dy(c, d);
        int[] ab = sub(mul(adx, bdy), mul(bdx, ady));
        int[] bc = sub(mul(bdx, cdy), mul(cdx, bdy));
        int[] ca = sub(mul(cdx, ady), mul(adx, cdy));
        int[] al = add(mul(adx, adx), mul(ady, ady));
        int[] bl = add(mul(bdx, bdx), mul(bdy, bdy));
        int[] cl = add(mul(cdx, cdx), mul(cdy, cdy));
        return sign(add(add(mul(al, bc), mul(bl, ca)), mul(cl, ab))) > 0;
    }

    // d lies strictly inside the circle through a, b, c (counterclockwise)
    static boolean inCircle(int a, int b, int c, int d) {
        double adx = fx[a] - fx[d];
        double ady = fy[a] - fy[d];
        double bdx = fx[b] - fx[d];
        double bdy = fy[b] - fy[d];
        double cdx = fx[c] - fx[d];
        double cdy = fy[c] - fy[d];
        double bdxcdy = bdx * cdy;
        double cdxbdy = cdx * bdy;
        double cdxady = cdx * ady;
        double adxcdy = adx * cdy;
        double adxbdy = adx * bdy;
        double bdxady = bdx * ady;
        double al = adx * adx + ady * ady;
        double bl = bdx * bdx + bdy * bdy;
        double cl = cdx * cdx + cdy * cdy;
        double det = al * (bdxcdy - cdxbdy) + bl * (cdxady - adxcdy) + cl * (adxbdy - bdxady);
        double permanent = (Math.abs(bdxcdy) + Math.abs(cdxbdy)) * al +
                           (Math.abs(cdxady) + Math.abs(adxcdy)) * bl +
                           (Math.abs(adxbdy) + Math.abs(bdxady)) * cl;
        double err = IN_CIRCLE_ERR * permanent;
        if (det > err) {
            return true;
        }
        if (det < -err) {
            return false;
        }
        return exactInCircle(a, b, c, d);
    }

    // Delaunay triangulation by divide and conquer on quad-edges: edge e, its
    // rotations within one group of four, rev(e) the same edge reversed.
    static int[] orig = new int[LIMBS];
    static int[] nextEdge = new int[LIMBS];
    static boolean[] active = new boolean[LIMBS];
    static int edges;
    static int[] freeEdges = new int[LIMBS];
    static int freeCount;

    static int rot(int e) { return (e & ~LAST_ROT) | ((e + 1) & LAST_ROT); }

    static int invrot(int e) { return (e & ~LAST_ROT) | ((e + LAST_ROT) & LAST_ROT); }

    static int rev(int e) { return e ^ 2; }

    static int dest(int e) { return orig[rev(e)]; }

    static int lnext(int e) { return rot(nextEdge[invrot(e)]); }

    static int oprev(int e) { return rot(nextEdge[rot(e)]); }

    static int makeEdge(int a, int b) {
        int e;
        if (freeCount > 0) {
            e = freeEdges[--freeCount];
        } else {
            e = edges;
            edges += QUAD;
            if (edges > orig.length) {
                orig = Arrays.copyOf(orig, orig.length * 2);
                nextEdge = Arrays.copyOf(nextEdge, nextEdge.length * 2);
                active = Arrays.copyOf(active, active.length * 2);
            }
        }
        orig[e] = a;
        orig[e + 1] = -1;
        orig[e + 2] = b;
        orig[e + LAST_ROT] = -1;
        nextEdge[e] = e;
        nextEdge[e + 1] = e + LAST_ROT;
        nextEdge[e + 2] = e + 2;
        nextEdge[e + LAST_ROT] = e + 1;
        active[e >> 2] = true;
        return e;
    }

    static void splice(int a, int b) {
        int alpha = rot(nextEdge[a]);
        int beta = rot(nextEdge[b]);
        int t = nextEdge[alpha];
        nextEdge[alpha] = nextEdge[beta];
        nextEdge[beta] = t;
        t = nextEdge[a];
        nextEdge[a] = nextEdge[b];
        nextEdge[b] = t;
    }

    static void deleteEdge(int e) {
        splice(e, oprev(e));
        splice(rev(e), oprev(rev(e)));
        active[e >> 2] = false;
        if (freeCount == freeEdges.length) {
            freeEdges = Arrays.copyOf(freeEdges, freeCount * 2);
        }
        freeEdges[freeCount++] = e & ~LAST_ROT;
    }

    static int connect(int a, int b) {
        int e = makeEdge(dest(a), orig[b]);
        splice(e, lnext(a));
        splice(rev(e), b);
        return e;
    }

    static boolean leftOf(int p, int e) { return orient(orig[e], dest(e), p) > 0; }

    static boolean rightOf(int p, int e) { return orient(orig[e], dest(e), p) < 0; }

    // points l..r (sorted by x, then y); returns the counterclockwise hull edge
    // out of the leftmost point and the clockwise one out of the rightmost
    static int[] build(int l, int r) {
        if (r - l == 1) {
            int e = makeEdge(l, r);
            return new int[] {e, rev(e)};
        }
        if (r - l == 2) {
            int a = makeEdge(l, l + 1);
            int b = makeEdge(l + 1, r);
            splice(rev(a), b);
            int turn = orient(l, l + 1, r);
            if (turn == 0) {
                return new int[] {a, rev(b)};
            }
            int c = connect(b, a);
            return turn > 0 ? new int[] {a, rev(b)} : new int[] {rev(c), c};
        }
        int mid = (l + r) / 2;
        int[] left = build(l, mid);
        int[] right = build(mid + 1, r);
        int ldo = left[0];
        int ldi = left[1];
        int rdi = right[0];
        int rdo = right[1];
        for (;;) { // the lower common tangent
            if (leftOf(orig[rdi], ldi)) {
                ldi = lnext(ldi);
            } else if (rightOf(orig[ldi], rdi)) {
                rdi = nextEdge[rev(rdi)];
            } else {
                break;
            }
        }
        int basel = connect(rev(rdi), ldi);
        if (orig[ldi] == orig[ldo]) {
            ldo = rev(basel);
        }
        if (orig[rdi] == orig[rdo]) {
            rdo = basel;
        }
        for (;;) { // zip the halves upward
            int lc = nextEdge[rev(basel)];
            if (rightOf(dest(lc), basel)) {
                while (inCircle(dest(basel), orig[basel], dest(lc), dest(nextEdge[lc]))) {
                    int t = nextEdge[lc];
                    deleteEdge(lc);
                    lc = t;
                }
            }
            int rc = oprev(basel);
            if (rightOf(dest(rc), basel)) {
                while (inCircle(dest(basel), orig[basel], dest(rc), dest(oprev(rc)))) {
                    int t = oprev(rc);
                    deleteEdge(rc);
                    rc = t;
                }
            }
            boolean lv = rightOf(dest(lc), basel);
            boolean rv = rightOf(dest(rc), basel);
            if (!lv && !rv) {
                break;
            }
            if (!lv || (rv && inCircle(dest(lc), orig[lc], orig[rc], dest(rc)))) {
                basel = connect(rc, rev(basel));
            } else {
                basel = connect(rev(basel), rev(lc));
            }
        }
        return new int[] {ldo, rdo};
    }

    // ---------------------------------------------------------------- input
    static DataInputStream in;
    static byte[] buf = new byte[BUF_SIZE];
    static int bufLen;
    static int bufPos;
    static byte[] tok = new byte[LIMBS * LIMBS];
    static int tokLen;

    static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, buf.length);
            bufPos = 0;
            if (bufLen <= 0) {
                return -1;
            }
        }
        return buf[bufPos++];
    }

    static void token() throws IOException {
        int c = read();
        while (c != -1 && c <= ' ') {
            c = read();
        }
        tokLen = 0;
        while (c > ' ') {
            if (tokLen == tok.length) {
                tok = Arrays.copyOf(tok, tokLen * 2);
            }
            tok[tokLen++] = (byte)c;
            c = read();
        }
    }

    static String tokenString() { return new String(tok, 0, tokLen); }

    static long parsedHi;
    static long parsedLo;

    // the token times 10^SCALE, digits beyond that dropped, into parsedHi/Lo
    static void parseFixed() {
        int i = 0;
        boolean negative = tok[0] == '-';
        if (tok[0] == '-' || tok[0] == '+') {
            i++;
        }
        int[] digits = new int[tokLen];
        int count = 0;
        int fraction = 0;
        int exponent = 0;
        boolean dot = false;
        for (; i < tokLen && tok[i] != 'e' && tok[i] != 'E'; i++) {
            if (tok[i] == '.') {
                dot = true;
                continue;
            }
            digits[count++] = tok[i] - '0';
            if (dot) {
                fraction++;
            }
        }
        if (i < tokLen) {
            exponent = Integer.parseInt(new String(tok, i + 1, tokLen - i - 1));
        }
        int shift = SCALE - fraction + exponent;
        int keep = shift < 0 ? Math.max(0, count + shift) : count;
        long[] limb = new long[FIXED_LIMBS]; // 32-bit limbs of the absolute value
        for (int j = 0; j < keep + Math.max(0, shift); j++) {
            long carry = j < keep ? digits[j] : 0;
            for (int t = 0; t < limb.length; t++) {
                long z = limb[t] * TEN + carry;
                limb[t] = z & LIMB_MASK;
                carry = z >>> LIMB_BITS;
            }
        }
        long[] halves = new long[2];
        for (int t = 0; t < FIXED_LIMBS; t++) {
            halves[t / 2] |= limb[t] << (LIMB_BITS * (t % 2));
        }
        long lo = halves[0];
        long hi = halves[1];
        if (negative) {
            lo = -lo;
            hi = ~hi + (lo == 0 ? 1 : 0);
        }
        parsedHi = hi;
        parsedLo = lo;
    }

    static int[] offsetOf;
    static int[] adj;
    static long qxHi, qxLo, qyHi, qyLo;
    static double qx, qy;

    // the squared distance from point i to the sweet, exact: SCALE * 2 digits
    static int[] dist2(int i) {
        int[] ddx = diff(xHi[i], xLo[i], qxHi, qxLo);
        int[] ddy = diff(yHi[i], yLo[i], qyHi, qyLo);
        return add(mul(ddx, ddx), mul(ddy, ddy));
    }

    static double dist2f(int i) {
        double ddx = fx[i] - qx;
        double ddy = fy[i] - qy;
        return ddx * ddx + ddy * ddy;
    }

    // the point nearest to the sweet: a walk on floating point, then an exact one
    static int nearestPoint(int seed) {
        int cur = seed;
        for (;;) {
            int best = cur;
            double bd = dist2f(cur);
            for (int k = offsetOf[cur]; k < offsetOf[cur + 1]; k++) {
                double z = dist2f(adj[k]);
                if (z < bd) {
                    bd = z;
                    best = adj[k];
                }
            }
            if (best == cur) {
                break;
            }
            cur = best;
        }
        for (;;) {
            int best = cur;
            for (int k = offsetOf[cur]; k < offsetOf[cur + 1]; k++) {
                if (beyond(best, adj[k], 0) > 0) {
                    best = adj[k];
                }
            }
            if (best == cur) {
                return cur;
            }
            cur = best;
        }
    }

    // the sign of dist2(a) - dist2(b) - shift, in doubles when they decide it:
    // rounding errs by less than the slack, otherwise it is computed exactly
    static int beyond(int a, int b, double shift) {
        double fa = dist2f(a);
        double fb = dist2f(b);
        double diff = fa - fb - shift;
        double slack = SLACK + RELATIVE_SLACK * (fa + fb);
        if (diff > slack) {
            return 1;
        }
        if (diff < -slack) {
            return -1;
        }
        int[] exact = sub(dist2(a), dist2(b));
        return sign(shift == 0 ? exact : sub(exact, eps));
    }

    // the indices 0..count-1 sorted by the 128-bit keys (aHi, aLo), then
    // (bHi, bLo), then index: a merge sort without boxing
    static int[] sortedBy(int count, long[] aHi, long[] aLo, long[] bHi, long[] bLo) {
        int[] idx = new int[count];
        int[] tmp = new int[count];
        for (int i = 0; i < count; i++) {
            idx[i] = i;
        }
        for (int width = 1; width < count; width *= 2) {
            for (int lo = 0; lo < count; lo += 2 * width) {
                int mid = Math.min(lo + width, count);
                int hi = Math.min(lo + 2 * width, count);
                int i = lo;
                int j = mid;
                for (int t = lo; t < hi; t++) {
                    boolean left = j >= hi;
                    if (i < mid && j < hi) {
                        int p = idx[i];
                        int q = idx[j];
                        int c = compare128(aHi[p], aLo[p], aHi[q], aLo[q]);
                        if (c == 0) {
                            c = compare128(bHi[p], bLo[p], bHi[q], bLo[q]);
                        }
                        left = c < 0 || (c == 0 && p < q);
                    }
                    tmp[t] = left ? idx[i++] : idx[j++];
                }
            }
            int[] swap = idx;
            idx = tmp;
            tmp = swap;
        }
        return idx;
    }

    static long edgeKey(int a, int b) {
        return a < b ? (long)a << KEY_BITS | b : (long)b << KEY_BITS | a;
    }

    public static void main(String[] args) throws IOException {
        in = new DataInputStream(System.in);
        token();
        int m = Integer.parseInt(tokenString());
        long[] rxHi = new long[m];
        long[] rxLo = new long[m];
        long[] ryHi = new long[m];
        long[] ryLo = new long[m];
        double[] rfx = new double[m];
        double[] rfy = new double[m];
        for (int i = 0; i < m; i++) {
            token();
            parseFixed();
            rxHi[i] = parsedHi;
            rxLo[i] = parsedLo;
            rfx[i] = Double.parseDouble(tokenString());
            token();
            parseFixed();
            ryHi[i] = parsedHi;
            ryLo[i] = parsedLo;
            rfy[i] = Double.parseDouble(tokenString());
        }
        token();
        int n = Integer.parseInt(tokenString());
        if (n == 0) {
            return;
        }
        // equal points become one, keeping all their cockroaches
        int[] order = sortedBy(m, rxHi, rxLo, ryHi, ryLo);
        int[] ids = new int[m];
        xHi = new long[m];
        xLo = new long[m];
        yHi = new long[m];
        yLo = new long[m];
        fx = new double[m];
        fy = new double[m];
        first = new int[m];
        last = new int[m];
        int k = 0;
        for (int i = 0; i < m;) {
            int a = order[i];
            int j = i;
            while (j < m && rxHi[order[j]] == rxHi[a] && rxLo[order[j]] == rxLo[a] &&
                   ryHi[order[j]] == ryHi[a] && ryLo[order[j]] == ryLo[a]) {
                ids[j] = order[j] + 1;
                j++;
            }
            xHi[k] = rxHi[a];
            xLo[k] = rxLo[a];
            yHi[k] = ryHi[a];
            yLo[k] = ryLo[a];
            fx[k] = rfx[a];
            fy[k] = rfy[a];
            first[k] = i;
            last[k] = j;
            k++;
            i = j;
        }
        long[] keys = new long[LIMBS];
        int keyCount = 0;
        boolean collinear = true;
        for (int i = 2; i < k && collinear; i++) {
            collinear = orient(0, 1, i) == 0;
        }
        if (k > 2 && !collinear) {
            build(0, k - 1);
            keys = new long[edges / QUAD + 2 * k];
            for (int q = 0; q < edges / QUAD; q++) {
                if (active[q]) {
                    keys[keyCount++] = edgeKey(orig[q * QUAD], orig[q * QUAD + 2]);
                }
            }
            int[] byY = sortedBy(k, yHi, yLo, xHi, xLo);
            for (int i = 1; i < k; i++) {
                keys[keyCount++] = edgeKey(byY[i - 1], byY[i]);
            }
        } else {
            keys = new long[k];
        }
        for (int i = 1; i < k; i++) { // neighbours by x; on a line, all edges
            keys[keyCount++] = edgeKey(i - 1, i);
        }
        // the graph: the triangulation plus the neighbours in the order by x
        // and by y, as adjacency lists adj[offsetOf[v]..offsetOf[v + 1])
        Arrays.sort(keys, 0, keyCount);
        int unique = 0;
        for (int i = 0; i < keyCount; i++) {
            if (unique == 0 || keys[unique - 1] != keys[i]) {
                keys[unique++] = keys[i];
            }
        }
        offsetOf = new int[k + 1];
        for (int i = 0; i < unique; i++) {
            offsetOf[(int)(keys[i] >>> KEY_BITS) + 1]++;
            offsetOf[(int)keys[i] + 1]++;
        }
        for (int i = 0; i < k; i++) {
            offsetOf[i + 1] += offsetOf[i];
        }
        int[] at = Arrays.copyOf(offsetOf, k);
        adj = new int[offsetOf[k]];
        for (int i = 0; i < unique; i++) {
            int a = (int)(keys[i] >>> KEY_BITS);
            int b = (int)keys[i];
            adj[at[a]++] = b;
            adj[at[b]++] = a;
        }

        // the answer: the nearest point and every point closer than it plus
        // EPS, found by a search through the graph from it
        int[] ten = fromFixed(0, TEN);
        eps = fromFixed(0, 1);
        for (int i = 0; i < 2 * SCALE; i++) {
            eps = mul(eps, ten);
        }
        for (int i = 0; i < EPS_BITS; i++) { // EPS times 10^(2 * SCALE), an integer
            int carry = 0;
            for (int j = LIMBS - 1; j >= 0; j--) {
                int low = eps[j] & 1;
                eps[j] = eps[j] >>> 1 | carry << (LIMB_BITS - 1);
                carry = low;
            }
        }
        int marks = Math.min(LANDMARKS, k);
        int[] landmark = new int[marks];
        for (int i = 0; i < marks; i++) {
            landmark[i] = marks > 1 ? (int)((long)i * (k - 1) / (marks - 1)) : 0;
        }
        int[] seen = new int[k];
        int[] queue = new int[k];
        int[] answer = new int[m];
        int prev = 0;
        PrintWriter out = new PrintWriter(System.out);
        StringBuilder line = new StringBuilder();
        for (int stamp = 1; stamp <= n; stamp++) {
            token();
            parseFixed();
            qxHi = parsedHi;
            qxLo = parsedLo;
            qx = Double.parseDouble(tokenString());
            token();
            parseFixed();
            qyHi = parsedHi;
            qyLo = parsedLo;
            qy = Double.parseDouble(tokenString());
            int seed = prev;
            double bd = dist2f(seed);
            for (int v : landmark) {
                double z = dist2f(v);
                if (z < bd) {
                    bd = z;
                    seed = v;
                }
            }
            int best = nearestPoint(seed);
            prev = best;
            int head = 0;
            int tail = 0;
            int count = 0;
            queue[tail++] = best;
            seen[best] = stamp;
            while (head < tail) {
                int v = queue[head++];
                if (beyond(v, best, EPS_FLOAT) >= 0) {
                    continue;
                }
                for (int t = first[v]; t < last[v]; t++) {
                    answer[count++] = ids[t];
                }
                for (int e = offsetOf[v]; e < offsetOf[v + 1]; e++) {
                    if (seen[adj[e]] != stamp) {
                        seen[adj[e]] = stamp;
                        queue[tail++] = adj[e];
                    }
                }
            }
            Arrays.sort(answer, 0, count);
            line.setLength(0);
            for (int i = 0; i < count; i++) {
                if (i > 0) {
                    line.append(' ');
                }
                line.append(answer[i]);
            }
            out.println(line);
        }
        out.flush();
    }
}
