import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int WORD_BITS = 64;

    static boolean get(long[] row, int c) {
        return (row[c / WORD_BITS] >>> (c % WORD_BITS) & 1) == 1;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        // equation v over GF(2): the chosen technicians turn valve v an odd number
        // of times; bit n of an equation is its right-hand side
        int words = n / WORD_BITS + 1;
        long[][] eq = new long[n][words];
        for (long[] e : eq) {
            e[n / WORD_BITS] |= 1L << (n % WORD_BITS);
        }
        for (int t = 0; t < n; t++) {
            while (true) {
                in.nextToken();
                int v = (int)in.nval;
                if (v == -1) {
                    break;
                }
                eq[v - 1][t / WORD_BITS] |= 1L << (t % WORD_BITS);
            }
        }
        // Gauss-Jordan elimination: column c ends with a single 1, in its pivot row
        int[] pivotOf = new int[n];
        int rank = 0;
        for (int c = 0; c < n; c++) {
            pivotOf[c] = -1;
            int r = rank;
            while (r < n && !get(eq[r], c)) {
                r++;
            }
            if (r == n) {
                continue;
            }
            long[] tmp = eq[r];
            eq[r] = eq[rank];
            eq[rank] = tmp;
            for (int i = 0; i < n; i++) {
                if (i != rank && get(eq[i], c)) {
                    for (int k = 0; k < words; k++) {
                        eq[i][k] ^= eq[rank][k];
                    }
                }
            }
            pivotOf[c] = rank++;
        }
        for (int r = rank; r < n; r++) {
            if (get(eq[r], n)) {
                System.out.println("No solution");
                return;
            }
        }
        // independent technicians make the solution unique, so it is also the shortest
        StringBuilder out = new StringBuilder();
        for (int c = 0; c < n; c++) {
            if (pivotOf[c] >= 0 && get(eq[pivotOf[c]], n)) {
                if (out.length() > 0) {
                    out.append(' ');
                }
                out.append(c + 1);
            }
        }
        System.out.println(out);
    }
}
