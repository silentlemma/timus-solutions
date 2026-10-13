import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    // weights in grams, times in minutes
    static final long TRUCK = 3000000;
    static final long CUP = 100;
    static final long ORDER = 10000000;
    static final int DAY = 24 * 60;

    static int n;
    // roads as linked lists in arrays: head, next, target, time and limit per road end
    static int[] head, next, to, time;
    static long[] limit;

    static final int SHIFT = 32; // a heap entry is time << SHIFT | vertex
    static final long VERTEX = (1L << SHIFT) - 1;
    static int[] dist;
    static long[] heap; // a binary min-heap of plain longs: no objects per step
    static int size;

    static void push(long x) {
        int i = size++;
        while (i > 0 && heap[(i - 1) / 2] > x) {
            heap[i] = heap[(i - 1) / 2];
            i = (i - 1) / 2;
        }
        heap[i] = x;
    }

    static long pop() {
        long top = heap[0], x = heap[--size];
        int i = 0;
        while (2 * i + 1 < size) {
            int c = 2 * i + 1;
            if (c + 1 < size && heap[c + 1] < heap[c])
                c++;
            if (heap[c] >= x)
                break;
            heap[i] = heap[c];
            i = c;
        }
        heap[i] = x;
        return top;
    }

    // can a truck of this weight reach n within a day
    static boolean inTime(long weight) {
        Arrays.fill(dist, DAY + 1);
        dist[1] = 0;
        size = 0;
        push(1);
        while (size > 0) {
            long top = pop();
            int d = (int)(top >>> SHIFT), v = (int)(top & VERTEX);
            if (v == n)
                return true;
            if (d > dist[v])
                continue;
            for (int e = head[v]; e >= 0; e = next[e])
                if (limit[e] >= weight && d + time[e] < dist[to[e]]) {
                    dist[to[e]] = d + time[e];
                    push((long)dist[to[e]] << SHIFT | to[e]);
                }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        if (n == 1) {
            System.out.println(ORDER); // the cups are already there
            return;
        }
        head = new int[n + 1];
        Arrays.fill(head, -1);
        next = new int[2 * m];
        to = new int[2 * m];
        time = new int[2 * m];
        limit = new long[2 * m];
        dist = new int[n + 1];
        heap = new long[2 * m + 1]; // one entry per improvement, at most one per road end
        long[] limits = new long[m];
        int count = 0;
        for (int i = 0; i < m; i++) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            in.nextToken();
            int t = (int)in.nval;
            in.nextToken();
            long cap = (long)in.nval;
            for (int side = 0; side < 2; side++) {
                int e = 2 * i + side, from = side == 0 ? a : b;
                to[e] = side == 0 ? b : a;
                time[e] = t;
                limit[e] = cap;
                next[e] = head[from];
                head[from] = e;
            }
            if (cap >= TRUCK)
                limits[count++] = cap;
        }
        // the heaviest possible truck weighs as much as some road allows, and
        // fewer roads are open to a heavier one, so search the road limits
        long[] sorted = Arrays.copyOf(limits, count);
        Arrays.sort(sorted);
        long best = -1;
        int lo = 0, hi = count - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (inTime(sorted[mid])) {
                best = sorted[mid];
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        System.out.println(best < 0 ? 0 : Math.min(ORDER, (best - TRUCK) / CUP));
    }
}
