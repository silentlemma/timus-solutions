import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    static final int NONE = 1000000000;
    static int[] black, prev, cur;

    // horses j..i-1 in one stable: black times white
    static int cost(int j, int i) {
        int b = black[i] - black[j];
        return b * (i - j - b);
    }

    // fills cur[lo..hi] knowing that their best last splits lie in
    // [optLo, optHi]
    static void solve(int lo, int hi, int optLo, int optHi) {
        if (lo > hi) {
            return;
        }
        int mid = (lo + hi) / 2, best = -1, arg = optLo;
        for (int j = optLo; j <= Math.min(mid - 1, optHi); j++) {
            int v = prev[j] + cost(j, mid);
            if (best < 0 || v < best) {
                best = v;
                arg = j;
            }
        }
        cur[mid] = best;
        solve(lo, mid - 1, optLo, arg);
        solve(mid + 1, hi, arg, optHi);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        black = new int[n + 1];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            black[i + 1] = black[i] + (int)in.nval;
        }
        // prev[j]: the least unhappiness of the first j horses in the stables
        // so far; with no stables only j = 0 is possible
        prev = new int[n + 1];
        Arrays.fill(prev, 1, n + 1, NONE);
        for (int stables = 1; stables <= k; stables++) {
            // the best last split never moves left as i grows (the
            // black-white cost satisfies the quadrangle inequality)
            cur = new int[n + 1];
            solve(stables, n, stables - 1, n - 1);
            prev = cur;
        }
        System.out.println(prev[n]);
    }
}
