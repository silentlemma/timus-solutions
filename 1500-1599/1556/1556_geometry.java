import java.io.*;
import java.util.*;

public class Main {
    static final double TAU = 2 * Math.PI;
    static final double EPS = 1e-12; // events closer than this in angle happen together
    static final long PERCENT = 100;
    static final double HALF = 0.5;
    static final int MOST_HITS = 5;        // an arrow stops after the fifth cow
    static final int ENTER = 0, LEAVE = 1; // at one angle, rays start touching before they stop

    static int k, size;
    static double[] turn, angle;
    static int[] kind, cut, used;

    // the angle in [0, 2 pi); a tiny negative angle may round up to 2 pi
    static double norm(double a) {
        a %= TAU;
        if (a < 0)
            a += TAU;
        return a >= TAU ? 0.0 : a;
    }

    // the angle a seen by arrow i: the events of one arrow come in this order
    static double turned(double a, int i) { return a >= turn[i] ? a - turn[i] : a - turn[i] + TAU; }

    static int at(int i) { return (cut[i] + used[i]) % size; }

    // the arrow whose next event comes first, or -1 when all are done
    static int pick() {
        int choice = -1, choiceKind = 0;
        double choiceAngle = 0;
        for (int i = 0; i < k; i++) {
            if (used[i] == size)
                continue;
            int e = at(i);
            double a = turned(angle[e], i);
            if (choice < 0 || a < choiceAngle || (a == choiceAngle && kind[e] < choiceKind)) {
                choice = i;
                choiceAngle = a;
                choiceKind = kind[e];
            }
        }
        return choice;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int read = 0;
        String line;
        List<String> words = new ArrayList<>();
        while ((line = in.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
            while (st.hasMoreTokens())
                words.add(st.nextToken());
        }
        int n = Integer.parseInt(words.get(read++));
        k = Integer.parseInt(words.get(read++));
        long p = Long.parseLong(words.get(read++));
        double r = Double.parseDouble(words.get(read++));
        double vx = Double.parseDouble(words.get(read++));
        double vy = Double.parseDouble(words.get(read++));
        // expected hits of an arrow whose ray meets m cows, kept exact as integers
        // in units of 1 / 100^4: each further cow adds p / 100 of the last addition
        long scale = 1;
        for (int m = 1; m < MOST_HITS; m++)
            scale *= PERCENT;
        long[] gain = new long[n + 1];
        long term = scale;
        for (int m = 1; m <= n; m++) {
            gain[m] = gain[m - 1] + (m <= MOST_HITS ? term : 0);
            if (m < MOST_HITS)
                term = term / PERCENT * p;
        }
        turn = new double[k];
        for (int i = 0; i < k; i++)
            turn[i] = norm(Math.atan((double)i / (k - 1) - HALF));
        // rays meet a cow at angles within asin(R / d) of its centre, and
        // each arrow sees the same angular intervals turned back by its offset
        size = 2 * n;
        long[] keys = new long[size];
        int[] count = new int[k];
        for (int j = 0; j < n; j++) {
            double x = Double.parseDouble(words.get(read++)) - vx;
            double y = Double.parseDouble(words.get(read++)) - vy;
            double centre = Math.atan2(y, x), width = Math.asin(Math.min(1, r / Math.hypot(x, y)));
            double lo = norm(centre - width), hi = norm(centre + width);
            // the bits of a non-negative double sort like the double itself as
            // unsigned numbers; flipping the top bit makes them sort as signed
            keys[2 * j] = (Double.doubleToLongBits(lo) << 1 | ENTER) ^ Long.MIN_VALUE;
            keys[2 * j + 1] = (Double.doubleToLongBits(hi) << 1 | LEAVE) ^ Long.MIN_VALUE;
            // the intervals that wrap hold the angle 0 of the arrow
            for (int i = 0; i < k; i++)
                if (turned(lo, i) > turned(hi, i))
                    count[i]++;
        }
        Arrays.sort(keys);
        angle = new double[size];
        kind = new int[size];
        for (int e = 0; e < size; e++) {
            keys[e] ^= Long.MIN_VALUE;
            angle[e] = Double.longBitsToDouble(keys[e] >>> 1);
            kind[e] = (int)(keys[e] & 1);
        }
        // arrow i takes the sorted events from cut[i] on, wrapping around once
        cut = new int[k];
        used = new int[k];
        for (int i = 0; i < k; i++) {
            int lo = 0, hi = size;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (angle[mid] >= turn[i])
                    hi = mid;
                else
                    lo = mid + 1;
            }
            cut[i] = lo;
        }
        int[] leaving = new int[size];
        long best = -1, total = 0;
        double bestAngle = 0;
        for (int i = 0; i < k; i++)
            total += gain[count[i]];
        int next = pick();
        double first = turned(angle[at(next)], next);
        while (next >= 0) {
            double x = turned(angle[at(next)], next);
            int left = 0;
            while (next >= 0 && turned(angle[at(next)], next) - x <= EPS) {
                if (kind[at(next)] == ENTER) {
                    total += gain[count[next] + 1] - gain[count[next]];
                    count[next]++;
                } else
                    leaving[left++] = next;
                used[next]++;
                next = pick();
            }
            // at the angle itself, touching counts: new cows join, none leave yet
            long point = total;
            for (int j = 0; j < left; j++) {
                int i = leaving[j];
                count[i]--;
                total -= gain[count[i] + 1] - gain[count[i]];
            }
            // after the last event the stretch runs on past 2 pi to the first one
            double following = next >= 0 ? turned(angle[at(next)], next) : TAU + first;
            // an open stretch is safer than a single tangent angle, so it wins ties
            if (following - x > EPS && total >= best) {
                best = total;
                bestAngle = (x + following) / 2;
            }
            if (point > best) {
                best = point;
                bestAngle = x;
            }
        }
        System.out.printf(Locale.US,
                          "The best shot at (%.10f;%.10f) gives Vasya %.4f average hits.\n",
                          Math.cos(bestAngle), Math.sin(bestAngle), (double)best / scale);
    }
}
