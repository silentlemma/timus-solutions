import java.io.IOException;
import java.util.Arrays;

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
        GoalInput in = new GoalInput();
        int n = in.nextInt();
        int size = Integer.highestOneBit(LOAD * n);
        keys = new long[size];
        vals = new int[size];
        mask = size - 1;
        long[] a = new long[n];
        int m = 0;
        for (int i = 1; i <= n; i++) {
            long s = in.nextLong();
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

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    static final class GoalInput {
        private final byte[] data = new byte[4096];
        private int position, length;
        private String pending;
        double nval;
        String sval;

        int read() throws IOException {
            if (position >= length) {
                length = System.in.read(data);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return data[position++] & 255;
        }

        private int first() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            return c;
        }

        long nextLong() throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        int nextInt() throws IOException { return (int)nextLong(); }

        String next() throws IOException {
            if (pending != null) {
                String word = pending;
                pending = null;
                return word;
            }
            int c = first();
            if (c < 0)
                return null;
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }

        boolean hasNext() throws IOException {
            if (pending == null)
                pending = next();
            return pending != null;
        }

        void nextToken() throws IOException {
            int c = first();
            if ((c >= '0' && c <= '9') || c == '-' || c == '+') {
                boolean negative = c == '-';
                if (negative || c == '+')
                    c = read();
                long value = 0;
                while (c >= '0' && c <= '9') {
                    value = value * 10 + c - '0';
                    c = read();
                }
                nval = negative ? -value : value;
                sval = null;
            } else {
                StringBuilder word = new StringBuilder();
                while (c > ' ') {
                    word.append((char)c);
                    c = read();
                }
                sval = word.toString();
            }
        }

        long scaled(int scale) throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            boolean fraction = false;
            while (c > ' ') {
                if (c == '.')
                    fraction = true;
                else {
                    value = value * 10 + c - '0';
                    if (fraction)
                        scale /= 10;
                }
                c = read();
            }
            value *= scale;
            return negative ? -value : value;
        }
    }
}
