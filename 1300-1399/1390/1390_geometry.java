import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final long DIGITS = 1000000000; // the time is printed with nine digits after the point
    static final int WALL = 4;             // numbers that describe a wall
    static final int TREE = 4;             // a segment tree over n leaves has under 4 n nodes

    static long[] lx, ly;
    // a wall is the line nx x + ny y = c with c > 0: a shot v hits it at time c / (n . v)
    static long[] nx, ny, cs;
    static int[] tree;

    static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static boolean half(long x, long y) { return y < 0 || (y == 0 && x < 0); }

    // counterclockwise order of directions, starting from the positive x axis
    static boolean before(long ax, long ay, long bx, long by) {
        boolean ha = half(ax, ay), hb = half(bx, by);
        if (ha != hb)
            return hb;
        return ax * by - ay * bx > 0;
    }

    // the first leaf not before the direction, or after it if strict
    static int bound(long x, long y, boolean strict) {
        long g = gcd(x, y);
        x /= g;
        y /= g;
        int lo = 0, hi = lx.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            boolean right =
                strict ? before(x, y, lx[mid], ly[mid]) : !before(lx[mid], ly[mid], x, y);
            if (right)
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }

    static boolean better(int w, int u, int leaf) {
        long vx = lx[leaf], vy = ly[leaf];
        return (nx[w] * vx + ny[w] * vy) * cs[u] > (nx[u] * vx + ny[u] * vy) * cs[w];
    }

    // Li Chao insertion: two walls swap places at most once on an arc below pi
    static void push(int node, int lo, int hi, int w) {
        while (true) {
            if (tree[node] < 0) {
                tree[node] = w;
                return;
            }
            int mid = (lo + hi) / 2;
            if (better(w, tree[node], mid)) {
                int t = tree[node];
                tree[node] = w;
                w = t;
            }
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

    static void insert(int node, int lo, int hi, int left, int right, int w) {
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

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        List<long[]> events = new ArrayList<>();
        while (in.nextToken() == StreamTokenizer.TT_WORD && !in.sval.equals("end")) {
            long[] e = new long[in.sval.equals("shot") ? 2 : WALL];
            for (int i = 0; i < e.length; i++) {
                in.nextToken();
                e[i] = (long)in.nval;
            }
            events.add(e);
        }
        // the leaves: distinct shot directions by angle
        List<long[]> dirs = new ArrayList<>();
        for (long[] e : events)
            if (e.length == 2) {
                long g = gcd(e[0], e[1]);
                dirs.add(new long[] {e[0] / g, e[1] / g});
            }
        dirs.sort((a, b)
                      -> before(a[0], a[1], b[0], b[1])   ? -1
                         : before(b[0], b[1], a[0], a[1]) ? 1
                                                          : 0);
        List<long[]> unique = new ArrayList<>();
        for (long[] d : dirs)
            if (unique.isEmpty() || unique.get(unique.size() - 1)[0] != d[0] ||
                unique.get(unique.size() - 1)[1] != d[1])
                unique.add(d);
        lx = new long[unique.size()];
        ly = new long[unique.size()];
        for (int i = 0; i < lx.length; i++) {
            lx[i] = unique.get(i)[0];
            ly[i] = unique.get(i)[1];
        }
        int size = Math.max(1, lx.length), walls = 0;
        tree = new int[TREE * size];
        Arrays.fill(tree, -1);
        nx = new long[events.size()];
        ny = new long[events.size()];
        cs = new long[events.size()];
        StringBuilder out = new StringBuilder();
        for (long[] e : events) {
            if (e.length == WALL) {
                if (lx.length == 0)
                    continue; // no shots at all
                long x1 = e[0], y1 = e[1], x2 = e[2], y2 = e[WALL - 1];
                if (x1 * y2 - y1 * x2 < 0) {
                    long t = x1;
                    x1 = x2;
                    x2 = t;
                    t = y1;
                    y1 = y2;
                    y2 = t;
                }
                nx[walls] = y2 - y1;
                ny[walls] = x1 - x2;
                cs[walls] = nx[walls] * x1 + ny[walls] * y1;
                int w = walls++;
                // the wall covers the directions from its first end counterclockwise to the second
                int lo = bound(x1, y1, false), hi = bound(x2, y2, true) - 1;
                if (before(x1, y1, x2, y2))
                    insert(1, 0, size - 1, lo, hi, w);
                else {
                    insert(1, 0, size - 1, lo, size - 1, w);
                    insert(1, 0, size - 1, 0, hi, w);
                }
                continue;
            }
            long vx = e[0], vy = e[1];
            int leaf = bound(vx, vy, false);
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
                out.append("Infinite\n");
            else {
                long den = nx[best] * vx + ny[best] * vy;
                long q = (2 * cs[best] * DIGITS + den) / (2 * den);
                // DIGITS + fraction keeps the leading zeros of the fraction
                String frac = Long.toString(DIGITS + q % DIGITS).substring(1);
                out.append(q / DIGITS).append('.').append(frac).append('\n');
            }
        }
        System.out.print(out);
    }
}
