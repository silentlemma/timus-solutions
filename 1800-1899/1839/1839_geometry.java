import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final long FAR = 2; // eyes lie closer to PR than twice its length
    static final int SIDES = 6; // numbers per arc

    static long[] height, near, far;

    // tan at P = height/near, at R = height/far, compared exactly
    static int atP(int a, int b) {
        return Long.compare(height[a] * near[b], height[b] * near[a]);
    }

    static int atR(int a, int b) {
        return Long.compare(height[a] * far[b], height[b] * far[a]);
    }

    static long faces(long[] arc, long[] xs, long[] ys) {
        int c = 0;
        long px = arc[c++], py = arc[c++], qx = arc[c++], qy = arc[c++];
        long rx = arc[c++], ry = arc[c];
        long ux = rx - px, uy = ry - py;
        long side = ux * (qy - py) - uy * (qx - px), span = ux * ux + uy * uy;
        int m = xs.length, k = 0;
        height = new long[m];
        near = new long[m];
        far = new long[m];
        for (int i = 0; i < m; i++) {
            long cross = ux * (ys[i] - py) - uy * (xs[i] - px);
            long n = ux * (xs[i] - px) + uy * (ys[i] - py);
            long f = -ux * (xs[i] - rx) - uy * (ys[i] - ry);
            // across PR from Q, both base angles acute, close enough to PR
            if (cross == 0 || (cross > 0) == (side > 0) || n <= 0 || f <= 0) {
                continue;
            }
            if (Math.abs(cross) >= FAR * span) {
                continue;
            }
            height[k] = Math.abs(cross);
            near[k] = n;
            far[k] = f;
            k++;
        }
        // ranks of the angles at R, equal angles sharing a rank
        Integer[] byR = new Integer[k];
        for (int i = 0; i < k; i++) {
            byR[i] = i;
        }
        Arrays.sort(byR, Main::atR);
        int[] rank = new int[k];
        for (int i = 0, r = 0; i < k; i++) {
            if (i > 0 && atR(byR[i - 1], byR[i]) < 0) {
                r++;
            }
            rank[byR[i]] = r + 1;
        }
        // the line through two eyes misses PR exactly when one eye is seen
        // higher from P and lower from R: count pairs in opposite orders
        Integer[] byP = byR.clone();
        Arrays.sort(byP, (a, b) -> {
            int cmp = atP(a, b);
            return cmp != 0 ? cmp : Integer.compare(rank[a], rank[b]);
        });
        int[] tree = new int[k + 1];
        long pairs = 0;
        for (int seen = 0; seen < k; seen++) {
            int r = rank[byP[seen]], below = 0;
            for (int i = r; i > 0; i &= i - 1) {
                below += tree[i];
            }
            pairs += seen - below;
            for (int i = r; i <= k; i += i & -i) {
                tree[i]++;
            }
        }
        return pairs;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
                new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int) in.nval;
        in.nextToken();
        int m = (int) in.nval;
        long[][] arcs = new long[n][SIDES];
        for (long[] arc : arcs) {
            for (int j = 0; j < SIDES; j++) {
                in.nextToken();
                arc[j] = (long) in.nval;
            }
        }
        long[] xs = new long[m], ys = new long[m];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            xs[i] = (long) in.nval;
            in.nextToken();
            ys[i] = (long) in.nval;
        }
        long total = 0;
        for (long[] arc : arcs) {
            total += faces(arc, xs, ys);
        }
        System.out.println(total);
    }
}
