import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    // linear independence is tested modulo a large prime: exact, and a set that is
    // independent modulo the prime is independent over the rationals
    static final long P = 2147483647L;

    static long power(long b, long e) {
        long r = 1;
        for (b %= P; e > 0; e /= 2, b = b * b % P) {
            if (e % 2 == 1) {
                r = r * b % P;
            }
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        int n = (int)in.nval;
        long[][] vec = new long[m][n];
        for (int i = 0; i < m; i++) {
            for (int k = 0; k < n; k++) {
                in.nextToken();
                vec[i][k] = ((long)in.nval % P + P) % P;
            }
        }
        int[] cost = new int[m];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            cost[i] = (int)in.nval;
        }
        // the greedy algorithm of a matroid: the cheapest vectors first, and among
        // equal prices the smaller numbers first, which gives the smallest list too
        Integer[] order = new Integer[m];
        for (int i = 0; i < m; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> cost[a] != cost[b] ? cost[a] - cost[b] : a - b);
        // rows of the basis, each with a pivot coordinate equal to 1 and zero in
        // the pivots of the rows before it
        List<long[]> rows = new ArrayList<>();
        List<Integer> pivots = new ArrayList<>();
        List<Integer> chosen = new ArrayList<>();
        for (int i : order) {
            if (chosen.size() == n) {
                break;
            }
            long[] v = vec[i].clone();
            for (int r = 0; r < rows.size(); r++) {
                long f = v[pivots.get(r)];
                if (f == 0) {
                    continue;
                }
                long[] row = rows.get(r);
                for (int k = 0; k < n; k++) {
                    v[k] = ((v[k] - f * row[k]) % P + P) % P;
                }
            }
            int piv = 0;
            while (piv < n && v[piv] == 0) {
                piv++;
            }
            if (piv == n) {
                continue;
            }
            long inv = power(v[piv], P - 2);
            for (int k = 0; k < n; k++) {
                v[k] = v[k] * inv % P;
            }
            rows.add(v);
            pivots.add(piv);
            chosen.add(i);
        }
        if (chosen.size() < n) {
            System.out.println(0);
            return;
        }
        long total = 0;
        for (int i : chosen) {
            total += cost[i];
        }
        chosen.sort(null);
        StringBuilder out = new StringBuilder();
        out.append(total).append('\n');
        for (int i : chosen) {
            out.append(i + 1).append('\n');
        }
        System.out.print(out);
    }
}
