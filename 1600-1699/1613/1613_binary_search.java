import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int BUFFER = 1 << 16;
    static final int CITY_BITS = 17; // cities number less than 2^17

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buf = new byte[BUFFER];
    static int len;
    static int pos;

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

    static int next() throws IOException {
        int c = read();
        while (c < '0') {
            c = read();
        }
        int v = 0;
        while (c >= '0') {
            v = v * 10 + c - '0';
            c = read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        // (passengers, city) pairs packed in longs and sorted: the cities with
        // one count are consecutive and sorted by number
        long[] pairs = new long[n];
        for (int i = 0; i < n; i++) {
            pairs[i] = (long)next() << CITY_BITS | (i + 1);
        }
        Arrays.sort(pairs);
        int q = next();
        char[] out = new char[q];
        for (int i = 0; i < q; i++) {
            int lo = next();
            int hi = next();
            int x = next();
            // the first city with count x and number at least lo
            long key = (long)x << CITY_BITS | lo;
            int k = Arrays.binarySearch(pairs, key);
            if (k < 0) {
                k = -k - 1;
            }
            boolean found =
                k < n && pairs[k] >>> CITY_BITS == x && (pairs[k] & ((1 << CITY_BITS) - 1)) <= hi;
            out[i] = found ? '1' : '0';
        }
        System.out.println(new String(out));
    }
}
