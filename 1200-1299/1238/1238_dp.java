import java.io.*;

public class Main {
    static String s;
    static int[][] best, cut; // cut > 0: split before s[cut]; < 0: -cut is the period

    // the shortest folding of s[i..j]
    static void fold(int i, int j, StringBuilder out) {
        int c = cut[i][j];
        if (c > 0) {
            fold(i, c - 1, out);
            fold(c, j, out);
        } else if (c < 0) {
            out.append((j - i + 1) / -c).append('(');
            fold(i, i - c - 1, out);
            out.append(')');
        } else {
            out.append(s, i, j + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        s = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        int n = s.length();
        best = new int[n][n];
        cut = new int[n][n];
        for (int size = 1; size <= n; size++)
            for (int i = 0; i + size <= n; i++) {
                int j = i + size - 1;
                best[i][j] = size;
                for (int k = i + 1; k <= j; k++)
                    if (best[i][k - 1] + best[k][j] < best[i][j]) {
                        best[i][j] = best[i][k - 1] + best[k][j];
                        cut[i][j] = k;
                    }
                // a period p repeats when the segment equals itself shifted by p
                for (int p = 1; p < size; p++) {
                    if (size % p != 0 || !s.regionMatches(i, s, i + p, size - p))
                        continue;
                    int l = Integer.toString(size / p).length() + 2 + best[i][i + p - 1];
                    if (l < best[i][j]) {
                        best[i][j] = l;
                        cut[i][j] = -p;
                    }
                }
            }
        StringBuilder out = new StringBuilder();
        fold(0, n - 1, out);
        System.out.println(out);
    }
}
