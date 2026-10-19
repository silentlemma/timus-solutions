import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Main {
    static final class Event {
        final long at; // walking cost from the foot to the point
        final int kind; // 0 a landing, 1 a start: landings first at one point
        final long start;
        final long time;

        Event(long at, int kind, long start, long time) {
            this.at = at;
            this.kind = kind;
            this.start = start;
            this.time = time;
        }
    }

    static DataInputStream in = new DataInputStream(System.in);
    static final int BUFFER_SIZE = 1 << 16;
    static byte[] buffer = new byte[BUFFER_SIZE];
    static int length;
    static int index;

    static int read() throws IOException {
        if (index == length) {
            length = in.read(buffer, 0, buffer.length);
            index = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[index++];
    }

    static long readLong() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            c = read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = read();
        }
        long v = 0;
        while (c >= '0' && c <= '9') {
            v = v * 10 + (c - '0');
            c = read();
        }
        return negative ? -v : v;
    }

    static int size;
    static int[] paint;
    static long[] xs;
    static long[] speed;
    static long[] walk;

    static long cost(int seg, long x) {
        return walk[seg] + speed[seg] * Math.abs(x - xs[seg]);
    }

    static void cover(int lo, int hi, int seg) {
        for (lo += size, hi += size; lo < hi; lo /= 2, hi /= 2) {
            if ((lo & 1) == 1) {
                paint[lo++] = seg;
            }
            if ((hi & 1) == 1) {
                paint[--hi] = seg;
            }
        }
    }

    static int look(int i, int n) {
        // paints only go down, so the lowest segment is the latest one
        int best = n;
        for (i += size; i > 0; i /= 2) {
            best = Math.min(best, paint[i]);
        }
        return best;
    }

    static int lowerBound(long[] keys, int count, long v) {
        int lo = 0;
        int hi = count;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (keys[mid] < v) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) readLong();
        xs = new long[n + 1];
        for (int i = 0; i <= n; i++) {
            xs[i] = readLong();
        }
        speed = new long[n];
        List<long[]> cables = new ArrayList<>(); // owner, x, time
        for (int i = 0; i < n; i++) {
            speed[i] = readLong();
            int m = (int) readLong();
            for (int j = 0; j < m; j++) {
                long x = readLong();
                long t = readLong();
                // a start at the first vertex of a segment is the last point
                // of the segment before it
                cables.add(new long[] {i > 0 && x == xs[i] ? i - 1 : i, x, t});
            }
        }
        walk = new long[n + 1];
        for (int i = 0; i < n; i++) {
            walk[i + 1] = walk[i] + speed[i] * Math.abs(xs[i + 1] - xs[i]);
        }
        // every point but the foot belongs to one segment, which owns its x
        // range without its first vertex; a cable lands on the first later
        // segment owning its x, found by painting the segments from the top down
        long[] keys = new long[cables.size()];
        for (int k = 0; k < keys.length; k++) {
            keys[k] = cables.get(k)[1];
        }
        Arrays.sort(keys);
        int count = 0;
        for (int k = 0; k < keys.length; k++) {
            if (k == 0 || keys[k] != keys[k - 1]) {
                keys[count++] = keys[k];
            }
        }
        size = 1;
        while (size < count) {
            size *= 2;
        }
        paint = new int[2 * size];
        Arrays.fill(paint, n);
        List<List<Integer>> byOwner = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            byOwner.add(new ArrayList<>());
        }
        for (int k = 0; k < cables.size(); k++) {
            byOwner.get((int) cables.get(k)[0]).add(k);
        }
        Event[] events = new Event[2 * cables.size()];
        int e = 0;
        for (int seg = n - 1; seg >= 0; seg--) {
            for (int k : byOwner.get(seg)) {
                long[] c = cables.get(k);
                int at = lowerBound(keys, count, c[1]);
                long from = cost(seg, c[1]);
                events[e++] = new Event(from, 1, 0, 0);
                events[e++] = new Event(cost(look(at, n), c[1]), 0, from, c[2]);
            }
            long a = xs[seg];
            long b = xs[seg + 1];
            long lo = a < b ? a + 1 : b;
            long hi = a < b ? b : a - 1;
            cover(lowerBound(keys, count, lo), lowerBound(keys, count, hi + 1), seg);
        }
        Arrays.sort(events, (p, q) -> p.at != q.at ? Long.compare(p.at, q.at)
                : Integer.compare(p.kind, q.kind));
        // going up, the best time at a point is its walking cost plus the
        // least (time - walking cost) over the landings so far
        HashMap<Long, Long> best = new HashMap<>();
        long gain = 0;
        for (Event ev : events) {
            if (ev.kind == 0) {
                gain = Math.min(gain, best.get(ev.start) + ev.time - ev.at);
            } else {
                best.put(ev.at, ev.at + gain);
            }
        }
        System.out.println(walk[n] + gain);
    }
}
