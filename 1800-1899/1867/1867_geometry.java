import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static int n;
    static long[][] d;
    static long[] xs;
    static long[] ys;

    static long isqrt(long v) {
        long r = (long) Math.sqrt((double) v);
        while (r * r > v) {
            r--;
        }
        while ((r + 1) * (r + 1) <= v) {
            r++;
        }
        return r;
    }

    // atom 0 at the origin, atom p at (a, b); every other atom follows from its
    // distances to these two up to a reflection in the line through them, and
    // the first atom off that line picks the side by flip
    static boolean place(int p, long a, long b, boolean flip) {
        long big = a * a + b * b;
        long[] signs = flip ? new long[] {-1, 1} : new long[] {1, -1};
        xs = new long[n];
        ys = new long[n];
        for (int i = 1; i < n; i++) {
            long twice = d[0][i] - d[p][i] + big; // twice the dot product with (a, b)
            if (twice % 2 != 0) {
                return false;
            }
            long dot = twice / 2;
            long square = big * d[0][i] - dot * dot; // the cross product, squared
            if (square < 0) {
                return false;
            }
            long cross = isqrt(square);
            if (cross * cross != square) {
                return false;
            }
            boolean done = false;
            for (long sign : signs) {
                long nx = a * dot + b * sign * cross;
                long ny = b * dot - a * sign * cross;
                if (nx % big != 0 || ny % big != 0) {
                    continue;
                }
                long x = nx / big;
                long y = ny / big;
                boolean fits = true;
                for (int j = 0; j < i && fits; j++) {
                    fits = (x - xs[j]) * (x - xs[j]) + (y - ys[j]) * (y - ys[j]) == d[i][j];
                }
                if (fits) {
                    xs[i] = x;
                    ys[i] = y;
                    done = true;
                    break;
                }
            }
            if (!done) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        n = (int) in.nval;
        d = new long[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                in.nextToken();
                d[i][j] = (long) in.nval;
            }
        }
        int p = 0;
        for (int i = 1; i < n && p == 0; i++) {
            if (d[0][i] != 0) {
                p = i;
            }
        }
        StringBuilder out = new StringBuilder();
        if (p == 0) {
            // everything sits at the origin
            for (long[] row : d) {
                for (long v : row) {
                    if (v != 0) {
                        System.out.println("Impossible");
                        return;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                out.append("0 0\n");
            }
            System.out.print(out);
            return;
        }
        long big = d[0][p];
        // the symmetries of the grid bring atom p to (a, b) with 0 <= a <= b
        for (long a = 0; 2 * a * a <= big; a++) {
            long b = isqrt(big - a * a);
            if (a * a + b * b != big) {
                continue;
            }
            for (boolean flip : new boolean[] {false, true}) {
                if (place(p, a, b, flip)) {
                    for (int i = 0; i < n; i++) {
                        out.append(xs[i]).append(' ').append(ys[i]).append('\n');
                    }
                    System.out.print(out);
                    return;
                }
            }
        }
        System.out.println("Impossible");
    }
}
