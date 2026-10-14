import java.io.*;
import java.util.*;

public class Main {
    static final long SHIFT = 1L << 16; // packs a direction into one long
    static final long STEPS = 1L << 14; // packs the steps below the direction
    static final double HALF = 0.5;     // rounds to the nearest mile

    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        if (in.nextToken() == StreamTokenizer.TT_EOF)
            return;
        int n = (int)in.nval;
        int[] xs = new int[n], ys = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            xs[i] = (int)in.nval;
            in.nextToken();
            ys[i] = (int)in.nval;
        }
        double total = 0;
        long[] keys = new long[n];
        for (int i = 0; i < n; i++) {
            // every other city as its reduced direction from city i and the steps to it
            int m = 0;
            for (int j = 0; j < n; j++) {
                if (j == i)
                    continue;
                int dx = xs[j] - xs[i], dy = ys[j] - ys[i];
                int g = gcd(dx, dy);
                keys[m++] = ((dx / g) * SHIFT + dy / g) * STEPS + g;
            }
            Arrays.sort(keys, 0, m);
            for (int k = 0; k < m; k++) {
                long dir = Math.floorDiv(keys[k], STEPS);
                if (k + 1 < m && Math.floorDiv(keys[k + 1], STEPS) == dir)
                    continue; // the farthest city of a direction comes last
                // city i ends the road in this direction when nothing lies behind it
                int at = Arrays.binarySearch(keys, 0, m, -dir * STEPS);
                if (at < 0)
                    at = -at - 1;
                if (at < m && Math.floorDiv(keys[at], STEPS) == -dir)
                    continue;
                long a = Math.floorDiv(dir + SHIFT / 2, SHIFT);
                long b = dir - a * SHIFT;
                total += Math.floorMod(keys[k], STEPS) * Math.hypot(a, b);
            }
        }
        // every road is found from both of its ends
        System.out.println((long)Math.floor(total / 2 + HALF));
    }
}
