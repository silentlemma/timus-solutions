import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // start of the lexicographically greatest suffix (the least one when
    // flip is set), by the comparison loop of the Two-Way algorithm
    static int suffixStart(char[] w, boolean flip) {
        int n = w.length;
        int best = -1;
        int j = 0;
        int k = 1;
        int p = 1;
        while (j + k < n) {
            char a = w[j + k];
            char b = w[best + k];
            if (a != b && (a < b) != flip) {
                j += k;
                k = 1;
                p = j - best;
            } else if (a == b) {
                if (k != p) {
                    k++;
                } else {
                    j += p;
                    k = 1;
                }
            } else {
                best = j;
                j = best + 1;
                k = 1;
                p = 1;
            }
        }
        return best + 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        char[] w = in.readLine().trim().toCharArray();
        int n = w.length;
        // the longest border gives the period of the word
        int[] border = new int[n];
        for (int i = 1, k = 0; i < n; i++) {
            while (k > 0 && w[k] != w[i]) {
                k = border[k - 1];
            }
            if (w[k] == w[i]) {
                k++;
            }
            border[i] = k;
        }
        // the critical factorization theorem: the split before the later of
        // the two greatest suffixes has a local root as long as the period
        // (both are the whole word only for a power of one letter)
        int split = Math.max(1, Math.max(suffixStart(w, false), suffixStart(w, true)));
        System.out.println(split + " " + (n - border[n - 1]));
    }
}
