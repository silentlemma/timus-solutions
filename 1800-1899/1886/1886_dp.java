import java.io.IOException;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    static final double PERCENT = 100;
    static final int FIELDS = 6;
    static final int DIGITS = 10;
    // positions of the fields of a flight
    static final int DURATION = 3;
    static final int CHANCE = 4;
    static final int DELAY = 5;

    static final int CHUNK = 1 << 16;
    static byte[] buffer = new byte[CHUNK];
    static int length;
    static int at;
    static int n;
    // per airport, over the flights seen so far (latest first): departure
    // times, and the best expected arrival over the flights leaving at that
    // time or later
    static long[][] departs;
    static double[][] best;
    static int[] size;

    static int read() throws IOException {
        if (at == length) {
            length = System.in.read(buffer, 0, buffer.length);
            at = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[at++];
    }

    static long next() throws IOException {
        int c = read();
        while (c < '0') {
            c = read();
        }
        long v = 0;
        while (c >= '0') {
            v = v * DIGITS + c - '0';
            c = read();
        }
        return v;
    }

    // the best expected arrival for someone at airport a at this time
    static double expected(int a, long time) {
        if (a == n) {
            return time;
        }
        long[] late = departs[a];
        int lo = 0;
        int hi = size[a];
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (late[mid] >= time) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo > 0 ? best[a][lo - 1] : Double.POSITIVE_INFINITY;
    }

    public static void main(String[] args) throws IOException {
        n = (int) next();
        int m = (int) next();
        long[][] flights = new long[m][FIELDS];
        int[] count = new int[n + 1];
        for (long[] x : flights) {
            for (int k = 0; k < FIELDS; k++) {
                x[k] = next();
            }
            count[(int) x[0]]++;
        }
        departs = new long[n + 1][];
        best = new double[n + 1][];
        size = new int[n + 1];
        for (int a = 1; a <= n; a++) {
            departs[a] = new long[count[a]];
            best[a] = new double[count[a]];
        }
        // an arrival is always later than the departure, so taking flights from
        // the latest departure down sees every flight a connection could use
        Arrays.sort(flights, (x, y) -> Long.compare(y[2], x[2]));
        for (long[] x : flights) {
            int a = (int) x[0];
            int b = (int) x[1];
            long t = x[2];
            long f = x[DURATION];
            double p = x[CHANCE];
            long d = x[DELAY];
            double onTime = expected(b, t + f);
            double delayed = expected(b, t + f + d);
            double value = ((PERCENT - p) * onTime + p * delayed) / PERCENT;
            if (size[a] > 0) {
                value = Math.min(value, best[a][size[a] - 1]);
            }
            departs[a][size[a]] = t;
            best[a][size[a]++] = value;
        }
        double answer = expected(1, 0);
        if (Double.isInfinite(answer)) {
            System.out.println("Fail");
        } else {
            System.out.println(String.format(Locale.US, "%.6f", answer));
        }
    }
}
