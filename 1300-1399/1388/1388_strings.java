import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Main {
    static final int SHORT = 3; // any three points on both sides match

    static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    // the distinct directions as reduced p / q with q > 0, by increasing p / q
    static long[][] directions(List<long[]> trees) {
        long[][] d = new long[trees.size()][];
        for (int i = 0; i < d.length; i++) {
            long x = trees.get(i)[0], y = trees.get(i)[1];
            if (y < 0) {
                x = -x;
                y = -y;
            }
            long g = gcd(x, y);
            d[i] = new long[] {x / g, y / g};
        }
        Arrays.sort(d, (a, b) -> Long.compare(a[0] * b[1], b[0] * a[1]));
        List<long[]> out = new ArrayList<>();
        for (long[] t : d)
            if (out.isEmpty() || out.get(out.size() - 1)[0] != t[0] ||
                out.get(out.size() - 1)[1] != t[1])
                out.add(t);
        return out.toArray(new long[0][]);
    }

    // cross-ratio of every four consecutive directions, as reduced fractions
    static long[][] ratios(long[][] d) {
        long[][] out = new long[Math.max(0, d.length - SHORT)][];
        for (int i = 0; i < out.length; i++) {
            long p1 = d[i][0], q1 = d[i][1], p2 = d[i + 1][0], q2 = d[i + 1][1];
            long p3 = d[i + 2][0], q3 = d[i + 2][1], p4 = d[i + SHORT][0], q4 = d[i + SHORT][1];
            // (c - a)(d - b) / ((c - b)(d - a)); the denominators q cancel
            long num = (p3 * q1 - p1 * q3) * (p4 * q2 - p2 * q4);
            long den = (p3 * q2 - p2 * q3) * (p4 * q1 - p1 * q4);
            long g = gcd(num, den);
            out[i] = new long[] {num / g, den / g};
        }
        return out;
    }

    // longest common substring of two sequences, by a suffix automaton of a
    static int longestCommon(int[] a, int[] b, long symbols) {
        int cap = 2 * a.length + 2;
        int[] link = new int[cap], len = new int[cap], head = new int[cap];
        // at most 3 n - 4 transitions for n symbols
        int[] edgeSymbol = new int[cap + a.length + 2], edgeNext = new int[cap + a.length + 2];
        int states = 1, edges = 0;
        link[0] = -1;
        head[0] = -1;
        // trans[state * symbols + symbol]: the next state; each state lists its symbols
        HashMap<Long, Integer> trans = new HashMap<>();
        int last = 0;
        for (int ch : a) {
            int cur = states++;
            len[cur] = len[last] + 1;
            head[cur] = -1;
            int p = last;
            while (p != -1 && !trans.containsKey(p * symbols + ch)) {
                trans.put(p * symbols + ch, cur);
                edgeSymbol[edges] = ch;
                edgeNext[edges] = head[p];
                head[p] = edges++;
                p = link[p];
            }
            if (p != -1) {
                int q = trans.get(p * symbols + ch);
                if (len[p] + 1 == len[q])
                    link[cur] = q;
                else {
                    int clone = states++;
                    len[clone] = len[p] + 1;
                    link[clone] = link[q];
                    head[clone] = -1;
                    for (int e = head[q]; e != -1; e = edgeNext[e]) {
                        trans.put(clone * symbols + edgeSymbol[e],
                                  trans.get(q * symbols + edgeSymbol[e]));
                        edgeSymbol[edges] = edgeSymbol[e];
                        edgeNext[edges] = head[clone];
                        head[clone] = edges++;
                    }
                    while (p != -1) {
                        Integer t = trans.get(p * symbols + ch);
                        if (t == null || t != q)
                            break;
                        trans.put(p * symbols + ch, clone);
                        p = link[p];
                    }
                    link[q] = link[cur] = clone;
                }
            }
            last = cur;
        }
        int best = 0, state = 0, run = 0;
        for (int ch : b) {
            while (state != 0 && !trans.containsKey(state * symbols + ch)) {
                state = link[state];
                run = len[state];
            }
            Integer t = trans.get(state * symbols + ch);
            if (t != null) {
                state = t;
                run++;
            }
            best = Math.max(best, run);
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        List<long[]> upper = new ArrayList<>(), lower = new ArrayList<>();
        while (in.nextToken() != StreamTokenizer.TT_EOF) {
            long x = (long)in.nval;
            in.nextToken();
            long y = (long)in.nval;
            if (x == 0 && y == 0)
                break;
            (y > 0 ? upper : lower).add(new long[] {x, y});
        }
        long[][] up = directions(upper), low = directions(lower);
        int answer = Math.min(Math.min(up.length, low.length), SHORT);
        if (up.length > SHORT && low.length > SHORT) {
            // the fractions of both sides, sorted together, numbered by value
            long[][] ra = ratios(up), rb = ratios(low);
            Integer[] order = new Integer[ra.length + rb.length];
            long[][] all = new long[order.length][];
            for (int i = 0; i < order.length; i++) {
                order[i] = i;
                all[i] = i < ra.length ? ra[i] : rb[i - ra.length];
            }
            Arrays.sort(order,
                        (i, j)
                            -> all[i][0] != all[j][0] ? Long.compare(all[i][0], all[j][0])
                                                      : Long.compare(all[i][1], all[j][1]));
            int[] id = new int[order.length];
            int symbols = 0;
            for (int i = 0; i < order.length; i++) {
                if (i > 0 && (all[order[i]][0] != all[order[i - 1]][0] ||
                              all[order[i]][1] != all[order[i - 1]][1]))
                    symbols++;
                id[order[i]] = symbols;
            }
            int common = longestCommon(Arrays.copyOfRange(id, 0, ra.length),
                                       Arrays.copyOfRange(id, ra.length, id.length), symbols + 1);
            if (common > 0)
                answer = common + SHORT;
        }
        System.out.println(answer);
    }
}
