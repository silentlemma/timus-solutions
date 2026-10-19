import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int LONGEST = 50;
    static final int SHIFT = 28; // star counts fit in 28 bits
    static final int LENGTH_BITS = 6; // room for the length of a war
    static final int BUFFER = 1 << 16;
    static final int TABLE_BITS = 18; // twice the most wars
    static final long MIX = 0x9e3779b97f4a7c15L;

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int len = 0, pos = 0;

    static int read() throws IOException {
        if (pos == len) {
            len = in.read(buf, 0, BUFFER);
            pos = 0;
            if (len <= 0) {
                return -1;
            }
        }
        return buf[pos++];
    }

    static long readLong() throws IOException {
        int c = read();
        while (c < '0') {
            c = read();
        }
        long v = 0;
        while (c >= '0') {
            v = v * 10 + c - '0';
            c = read();
        }
        return v;
    }

    // an open-addressing set of keys plus one, so that 0 marks a free slot
    static long[] table = new long[1 << TABLE_BITS];

    static int slot(long key) {
        int i = (int) ((key * MIX) >>> (Long.SIZE - TABLE_BITS));
        while (table[i] != 0 && table[i] != key + 1) {
            i = (i + 1) & (table.length - 1);
        }
        return i;
    }

    static long key(long first, long last, int d) {
        return ((first << SHIFT | last) << LENGTH_BITS) | d;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) readLong();
        long[] stars = new long[n];
        for (int i = 0; i < n; i++) {
            stars[i] = readLong();
        }
        int m = (int) readLong();
        boolean[] lengths = new boolean[LONGEST + 1];
        for (int i = 0; i < m; i++) {
            long x = readLong(), y = readLong();
            int d = (int) readLong();
            lengths[d] = true;
            long k = key(x, y, d);
            table[slot(k)] = k + 1;
        }
        // a war of d days ending k days ago began k + d - 1 days ago; the
        // reach at k is the oldest day of a matching war ending k days ago
        int[] reach = new int[n];
        Arrays.fill(reach, -1);
        for (int d = 2; d <= Math.min(LONGEST, n); d++) {
            if (!lengths[d]) {
                continue;
            }
            for (int k = 0; k + d <= n; k++) {
                if (table[slot(key(stars[k + d - 1], stars[k], d))] != 0) {
                    reach[k] = Math.max(reach[k], k + d - 1);
                }
            }
        }
        StringBuilder out = new StringBuilder(n);
        int cover = -1;
        for (int k = 0; k < n; k++) {
            cover = Math.max(cover, reach[k]);
            out.append(cover >= k ? '1' : '0');
        }
        System.out.println(out);
    }
}
