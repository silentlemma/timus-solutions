import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static long n;
    static long[] start;
    static long[] rest;
    static long shallowest;
    static long deepest;

    // a signing of the second half with this total and these lowest and
    // highest running sums fits after depth x exactly when
    // -low <= x <= n - high, and it ends at x + total
    static void walk(int i, long total, long low, long high) {
        if (i == rest.length) {
            int first = lowerBound(start, -low);
            if (first == start.length || start[first] > n - high) {
                return;
            }
            shallowest = Math.min(shallowest, start[first] + total);
            int last = lowerBound(start, n - high + 1) - 1;
            deepest = Math.max(deepest, start[last] + total);
            return;
        }
        for (long u = total + rest[i]; ; u = total - rest[i]) {
            long a = Math.min(low, u);
            long b = Math.max(high, u);
            if (b - a <= n) {
                walk(i + 1, u, a, b);
            }
            if (u < total) {
                break;
            }
        }
    }

    static int lowerBound(long[] a, long key) {
        int lo = 0;
        int hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] < key) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        n = Long.parseLong(st.nextToken());
        long s = Long.parseLong(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        long[] moves = new long[k];
        for (int i = 0; i < k; i++) {
            moves[i] = Long.parseLong(st.nextToken());
        }
        int half = k / 2;
        // the depths the first half of the moves can reach without leaving
        // [0, n]; equal depths are kept once
        start = new long[] {s};
        for (int i = 0; i < half; i++) {
            long[] next = new long[2 * start.length];
            int size = 0;
            for (long p : start) {
                if (p + moves[i] <= n) {
                    next[size++] = p + moves[i];
                }
                if (p - moves[i] >= 0) {
                    next[size++] = p - moves[i];
                }
            }
            Arrays.sort(next, 0, size);
            int unique = 0;
            for (int j = 0; j < size; j++) {
                if (j == 0 || next[j] != next[j - 1]) {
                    next[unique++] = next[j];
                }
            }
            start = Arrays.copyOf(next, unique);
        }
        rest = Arrays.copyOfRange(moves, half, k);
        shallowest = n + 1;
        deepest = -1;
        walk(0, 0, 0, 0);
        System.out.println(shallowest + " " + deepest);
    }
}
