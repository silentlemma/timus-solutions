import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final long GOLDEN = 0x9E3779B97F4A7C15L; // Fibonacci hashing
    static final int SHIFT = 40;
    static final int LOAD = 4; // the table is at least twice as large as needed
    static long[] keys;
    static int[] vals;
    static int mask;

    // an open-addressing table from a value to the number of one element holding it
    static int find(long key) {
        int h = (int)(key * GOLDEN >>> SHIFT) & mask;
        while (vals[h] != 0 && keys[h] != key)
            h = (h + 1) & mask;
        return h;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        int size = Integer.highestOneBit(LOAD * n);
        keys = new long[size];
        vals = new int[size];
        mask = size - 1;
        long[] a = new long[n];
        int m = 0;
        StringTokenizer st = new StringTokenizer(in.readLine());
        for (int i = 1; i <= n; i++) {
            while (!st.hasMoreTokens())
                st = new StringTokenizer(in.readLine());
            long s = Long.parseLong(st.nextToken());
            int h = find(s);
            if (vals[h] == 0) {
                keys[h] = s;
                vals[h] = i;
                a[m++] = s;
            }
        }
        a = Arrays.copyOf(a, m);
        Arrays.sort(a);
        int bestLength = 1;
        long bestFirst = a[0], bestStep = 1;
        for (int i = 0; i < m; i++)
            for (int j = i + 1; j < m; j++) {
                long d = a[j] - a[i];
                // walk each progression only from its first member, so every
                // pair of neighbours in it is visited once
                if (vals[find(a[i] - d)] != 0)
                    continue;
                int length = 2;
                long last = a[j];
                while (vals[find(last + d)] != 0) {
                    last += d;
                    length++;
                }
                if (length > bestLength) {
                    bestLength = length;
                    bestFirst = a[i];
                    bestStep = d;
                }
            }
        StringBuilder out = new StringBuilder();
        out.append(bestLength).append('\n');
        for (int k = 0; k < bestLength; k++)
            out.append(vals[find(bestFirst + k * bestStep)])
                .append(k + 1 == bestLength ? '\n' : ' ');
        System.out.print(out);
    }
}
