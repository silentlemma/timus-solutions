import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static final int NINE = 9;
    static final int CLASSES = 4; // positions grouped by the signs of the two rules
    static final int BOTH_UP = 0, X_UP = 1, Y_UP = 2, BOTH_DOWN = 3;

    static int[] s;
    static int size;

    static class Combo {
        int[] wx, wy, cls, tail; // tail[k]: sum of wx from k on
        int[][] cnt = new int[CLASSES][];
        long[] px, py;

        Combo(int[] wx, int[] wy) {
            this.wx = wx;
            this.wy = wy;
            cls = new int[size];
            tail = new int[size + 1];
            for (int c = 0; c < CLASSES; c++)
                cnt[c] = new int[size + 1];
            px = new long[size + 1];
            py = new long[size + 1];
            for (int k = 0; k < size; k++) {
                cls[k] = (wx[k] > 0 ? 0 : 2) + (wy[k] > 0 ? 0 : 1);
                for (int c = 0; c < CLASSES; c++)
                    cnt[c][k + 1] = cnt[c][k] + (cls[k] == c ? 1 : 0);
                px[k + 1] = px[k] + wx[k] * s[k];
                py[k + 1] = py[k] + wy[k] * s[k];
            }
            for (int k = size - 1; k >= 0; k--)
                tail[k] = tail[k + 1] + wx[k];
        }

        // digits before j give sums sx, sy; j in [loJ, hiJ], free up to p,
        // p at most 8, nines after p; t must balance wx, t + 1 must balance wy
        boolean feasible(long sx, long sy, int j, int p, int loJ, int hiJ) {
            long a = -sx - NINE * tail[p + 1], b = -sy - wy[p];
            long[] lo = new long[CLASSES], hi = new long[CLASSES];
            for (int c = 0; c < CLASSES; c++)
                hi[c] = NINE * (cnt[c][p + 1] - cnt[c][j]);
            hi[cls[j]] += hiJ - NINE;
            lo[cls[j]] += loJ;
            if (p > j)
                hi[cls[p]] -= 1;
            if ((a + b) % 2 != 0)
                return false;
            long u = (a + b) / 2, v = (a - b) / 2;
            return lo[BOTH_UP] - hi[BOTH_DOWN] <= u && u <= hi[BOTH_UP] - lo[BOTH_DOWN] &&
                lo[X_UP] - hi[Y_UP] <= v && v <= hi[X_UP] - lo[Y_UP];
        }

        // t from s up to j, then d, then the smallest digits that still fit, then nines after p
        int[] build(int p, int j, int d) {
            int[] t = new int[size];
            Arrays.fill(t, NINE);
            if (j > p) { // t keeps s up to p and has nines after it
                System.arraycopy(s, 0, t, 0, p + 1);
                return t;
            }
            System.arraycopy(s, 0, t, 0, j);
            t[j] = d;
            long sx = px[j] + wx[j] * d, sy = py[j] + wy[j] * d;
            for (int k = j + 1; k <= p; k++) {
                int x = 0;
                while (!feasible(sx, sy, k, p, x, x))
                    x++;
                t[k] = x;
                sx += wx[k] * x;
                sy += wy[k] * x;
            }
            return t;
        }
    }

    static boolean less(int[] a, int[] b) {
        for (int k = 0; k < a.length; k++)
            if (a[k] != b[k])
                return a[k] < b[k];
        return false;
    }

    public static void main(String[] args) throws IOException {
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        size = line.length();
        s = new int[size];
        for (int k = 0; k < size; k++)
            s[k] = line.charAt(k) - '0';
        int half = size / 2;
        int[] ruleA = new int[size], ruleB = new int[size];
        for (int k = 0; k < size; k++) {
            ruleA[k] = k < half ? 1 : -1;
            ruleB[k] = k % 2 == 0 ? 1 : -1;
        }
        int[][] rules = {ruleA, ruleB};
        // best: the first position where t leaves s (later is better), then the digit there
        int bestDev = -1, bestDigit = NINE + 1;
        int[] best = null;
        for (int[] x : rules)
            for (int[] y : rules) { // the rule for t, then the rule for t + 1
                Combo c = new Combo(x, y);
                for (int p = 0; p < size; p++) {
                    int dev = -1, digit = 0, j = -1, d = 0;
                    if (s[p] < NINE && c.px[p + 1] + NINE * c.tail[p + 1] == 0 &&
                        c.py[p + 1] + c.wy[p] == 0) {
                        dev = size;
                        for (int k = p + 1; k < size; k++)
                            if (s[k] < NINE) {
                                dev = k;
                                break;
                            }
                        digit = NINE;
                        j = p + 1;
                    } else {
                        for (int q = p; q >= 0 && dev < 0; q--) {
                            int top = q == p ? NINE - 1 : NINE;
                            if (s[q] + 1 > top ||
                                !c.feasible(c.px[q], c.py[q], q, p, s[q] + 1, top))
                                continue;
                            d = s[q] + 1;
                            while (!c.feasible(c.px[q], c.py[q], q, p, d, d))
                                d++;
                            dev = j = q;
                            digit = d;
                        }
                    }
                    if (dev < 0 || dev < bestDev || (dev == bestDev && digit > bestDigit))
                        continue;
                    int[] t = c.build(p, j, d);
                    if (best == null || dev > bestDev || digit < bestDigit || less(t, best)) {
                        best = t;
                        bestDev = dev;
                        bestDigit = digit;
                    }
                }
            }
        if (best == null) {
            System.out.println("No solution");
            return;
        }
        int[] next = best.clone();
        int k = size - 1;
        while (next[k] == NINE)
            next[k--] = 0;
        next[k]++;
        StringBuilder a = new StringBuilder(), b = new StringBuilder();
        for (int i = 0; i < size; i++) {
            a.append((char)('0' + best[i]));
            b.append((char)('0' + next[i]));
        }
        System.out.println(a + " " + b);
    }
}
