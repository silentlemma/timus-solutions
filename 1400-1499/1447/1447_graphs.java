import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    static final int BUFFER = 1 << 16;
    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int bufLen = 0, bufPos = 0;

    static int read() throws IOException {
        if (bufPos == bufLen) {
            bufLen = in.read(buf, 0, BUFFER);
            bufPos = 0;
            if (bufLen <= 0)
                return -1;
        }
        return buf[bufPos++];
    }

    static int readInt() throws IOException {
        int c = read();
        while (c < '0')
            c = read();
        int x = 0;
        for (; c >= '0'; c = read())
            x = x * 10 + c - '0';
        return x;
    }

    static int n;
    static int[] cost, dist; // n by n, 0 marks a missing link, real values are positive
    static long tc, td;

    // Prim on the weights c q - d p, exact integers; returns the tree's
    // total weight and sets its cost and length
    static long tree(long p, long q) {
        long[] best = new long[n], bc = new long[n], bd = new long[n];
        boolean[] used = new boolean[n];
        Arrays.fill(best, Long.MAX_VALUE);
        best[0] = 0;
        long total = 0;
        tc = td = 0;
        for (int step = 0; step < n; step++) {
            int u = -1;
            for (int v = 0; v < n; v++)
                if (!used[v] && (u < 0 || best[v] < best[u]))
                    u = v;
            used[u] = true;
            total += best[u];
            tc += bc[u];
            td += bd[u];
            int row = u * n;
            for (int v = 0; v < n; v++) {
                int c = cost[row + v];
                if (c != 0 && !used[v]) {
                    long w = c * q - dist[row + v] * p;
                    if (w < best[v]) {
                        best[v] = w;
                        bc[v] = c;
                        bd[v] = dist[row + v];
                    }
                }
            }
        }
        return total;
    }

    static long gcd(long a, long b) { return b == 0 ? a : gcd(b, a % b); }

    public static void main(String[] args) throws IOException {
        n = readInt();
        int m = readInt();
        cost = new int[n * n];
        dist = new int[n * n];
        for (int i = 0; i < m; i++) {
            int a = readInt() - 1, b = readInt() - 1, d = readInt(), c = readInt();
            cost[a * n + b] = cost[b * n + a] = c;
            dist[a * n + b] = dist[b * n + a] = d;
        }
        // Dinkelbach: the ratio p / q of the last tree drops until no tree beats it
        tree(0, 1);
        long p = tc, q = td;
        while (tree(p, q) < 0) {
            long g = gcd(tc, td);
            p = tc / g;
            q = td / g;
        }
        System.out.printf(Locale.US, "%.10f%n", (double)p / q);
    }
}
