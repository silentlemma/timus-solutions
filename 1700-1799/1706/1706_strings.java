import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int COPIES = 4; // the text repeated so that every comparison below stays inside it

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            all.append(line).append(' ');
        }
        StringTokenizer tokens = new StringTokenizer(all.toString());
        int k = Integer.parseInt(tokens.nextToken());
        String s = tokens.nextToken();
        int n = s.length();
        StringBuilder repeated = new StringBuilder();
        for (int c = 0; c < COPIES; c++) {
            repeated.append(s);
        }
        char[] t = repeated.toString().toCharArray();
        // a substring is counted at its leftmost start j in the window [a, a + k):
        // its lengths up to a + k - j minus the longest common prefix of j with an
        // earlier start of the window, best[j]; going down over a adds start a
        int top = n + 2 * k;
        int[] common = new int[k]; // common[d] = lcp of positions a and a + d
        int[] best = new int[top + k];
        long[] answers = new long[n];
        for (int a = top; a >= 0; a--) {
            char ca = t[a];
            for (int d = 1; d < k; d++) {
                int j = a + d;
                if (t[j] == ca) {
                    common[d]++;
                    if (common[d] > best[j]) {
                        best[j] = common[d];
                    }
                } else {
                    common[d] = 0;
                }
            }
            if (a < n) {
                int end = a + k;
                long total = 0;
                for (int j = a; j < end; j++) {
                    int fresh = end - j - best[j];
                    if (fresh > 0) {
                        total += fresh;
                    }
                }
                answers[a] = total;
            }
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                out.append(' ');
            }
            out.append(answers[i]);
        }
        System.out.println(out);
    }
}
