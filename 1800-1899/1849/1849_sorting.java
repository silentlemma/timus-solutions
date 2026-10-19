import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static final int SPAN = 10000; // coordinates lie in [-SPAN, SPAN]
    static final int REACH = 10; // direction parts lie in [-REACH, REACH]
    static final int WIDTH = 2 * SPAN + 1;
    static final int TURN = 2 * REACH + 1;

    static int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        int n = Integer.parseInt(st.nextToken());
        int[] rx = new int[n];
        int[] ry = new int[n];
        for (int i = 0; i < n; i++) {
            rx[i] = Integer.parseInt(st.nextToken());
            ry[i] = Integer.parseInt(st.nextToken());
        }
        int q = Integer.parseInt(st.nextToken());
        long x = Long.parseLong(st.nextToken());
        long y = Long.parseLong(st.nextToken());
        long vx = Long.parseLong(st.nextToken());
        long vy = Long.parseLong(st.nextToken());
        long ax = Long.parseLong(st.nextToken());
        long bx = Long.parseLong(st.nextToken());
        long ay = Long.parseLong(st.nextToken());
        long by = Long.parseLong(st.nextToken());
        long avx = Long.parseLong(st.nextToken());
        long bvx = Long.parseLong(st.nextToken());
        long avy = Long.parseLong(st.nextToken());
        long bvy = Long.parseLong(st.nextToken());
        // every direction is filed under its primitive vector
        List<int[]> primitive = new ArrayList<>();
        int[] code = new int[TURN * TURN];
        for (int dx = -REACH; dx <= REACH; dx++) {
            for (int dy = -REACH; dy <= REACH; dy++) {
                int g = gcd(dx, dy);
                if (g == 0) {
                    continue;
                }
                int k = 0;
                while (k < primitive.size()
                        && (primitive.get(k)[0] != dx / g || primitive.get(k)[1] != dy / g)) {
                    k++;
                }
                if (k == primitive.size()) {
                    primitive.add(new int[] {dx / g, dy / g});
                }
                code[(dx + REACH) * TURN + dy + REACH] = k;
            }
        }
        int kinds = primitive.size();
        int[] xs = new int[q];
        int[] ys = new int[q];
        int[] kind = new int[q];
        int[] start = new int[kinds + 1];
        for (int i = 0; i < q; i++) {
            xs[i] = (int) x;
            ys[i] = (int) y;
            kind[i] = code[(int) ((vx + REACH) * TURN + vy + REACH)];
            start[kind[i] + 1]++;
            x = (ax * (x + SPAN) + bx) % WIDTH - SPAN;
            y = (ay * (y + SPAN) + by) % WIDTH - SPAN;
            vx = (avx * (vx + REACH) + bvx) % TURN - REACH;
            vy = (avy * (vy + REACH) + bvy) % TURN - REACH;
        }
        // the shots in order of their direction, by counting
        for (int k = 0; k < kinds; k++) {
            start[k + 1] += start[k];
        }
        int[] shots = new int[q];
        int[] fill = Arrays.copyOf(start, kinds);
        for (int i = 0; i < q; i++) {
            shots[fill[kind[i]]++] = i;
        }
        int best = 0;
        int bestCount = -1;
        long[] rabbits = new long[n];
        for (int k = 0; k < kinds; k++) {
            if (start[k] == start[k + 1]) {
                continue;
            }
            int dx = primitive.get(k)[0];
            int dy = primitive.get(k)[1];
            // rabbits by the line along (dx, dy) and then by the place on it,
            // packed into one number: line * 2^32 + place
            for (int i = 0; i < n; i++) {
                rabbits[i] = pack(rx[i] * dy - ry[i] * dx, rx[i] * dx + ry[i] * dy);
            }
            Arrays.sort(rabbits);
            for (int j = start[k]; j < start[k + 1]; j++) {
                int i = shots[j];
                int line = xs[i] * dy - ys[i] * dx;
                int place = xs[i] * dx + ys[i] * dy;
                int from = lowerBound(rabbits, pack(line, place));
                int to = lowerBound(rabbits, pack(line + 1, Integer.MIN_VALUE));
                int got = to - from;
                // a later shot wins a tie
                if (got > bestCount || (got == bestCount && i > best)) {
                    best = i;
                    bestCount = got;
                }
            }
        }
        System.out.println((best + 1) + " " + bestCount);
    }

    static long pack(int line, int place) {
        return ((long) line << Integer.SIZE) + place;
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
}
