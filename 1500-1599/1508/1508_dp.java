import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[] dots;

    // whether a group can cover the cells s ... s + length - 1
    static boolean fits(int s, int length) {
        return s >= 0 && s + length <= n && dots[s + length] == dots[s];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String s; (s = br.readLine()) != null;)
            all.append(s).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int[] groups = new int[k];
        for (int j = 0; j < k; j++)
            groups[j] = Integer.parseInt(st.nextToken());
        char[] line = st.nextToken().toCharArray();
        dots = new int[n + 1]; // dots[i]: known empty cells among the first i
        for (int i = 0; i < n; i++)
            dots[i + 1] = dots[i] + (line[i] == '.' ? 1 : 0);
        // pre[i][j]: the first i cells can hold the first j groups
        boolean[][] pre = new boolean[n + 1][k + 1];
        pre[0][0] = true;
        for (int i = 1; i <= n; i++)
            for (int j = 0; j <= k; j++) {
                boolean ok = line[i - 1] != 'X' && pre[i - 1][j];
                if (!ok && j > 0 && fits(i - groups[j - 1], groups[j - 1])) {
                    int s = i - groups[j - 1];
                    ok = s == 0 ? j == 1 : line[s - 1] != 'X' && pre[s - 1][j - 1];
                }
                pre[i][j] = ok;
            }
        if (!pre[n][k]) {
            System.out.println("Impossible");
            return;
        }
        // suf[i][j]: the cells from i on can hold the groups from j on
        boolean[][] suf = new boolean[n + 2][k + 1];
        suf[n][k] = true;
        for (int i = n - 1; i >= 0; i--)
            for (int j = k; j >= 0; j--) {
                boolean ok = line[i] != 'X' && suf[i + 1][j];
                if (!ok && j < k && fits(i, groups[j])) {
                    int end = i + groups[j];
                    ok = end == n ? j + 1 == k : line[end] != 'X' && suf[end + 1][j + 1];
                }
                suf[i][j] = ok;
            }
        int[] cover = new int[n + 1]; // difference array of the cells some group can cover
        for (int j = 0; j < k; j++)
            for (int s = 0; s + groups[j] <= n; s++) {
                int end = s + groups[j];
                if (!fits(s, groups[j]))
                    continue;
                boolean left = s == 0 ? j == 0 : line[s - 1] != 'X' && pre[s - 1][j];
                boolean right = end == n ? j + 1 == k : line[end] != 'X' && suf[end + 1][j + 1];
                if (left && right) {
                    cover[s]++;
                    cover[end]--;
                }
            }
        char[] out = new char[n];
        for (int c = 0, run = 0; c < n; c++) {
            run += cover[c];
            boolean white = false;
            for (int j = 0; j <= k && line[c] != 'X'; j++)
                white = white || (pre[c][j] && suf[c + 1][j]);
            out[c] = white && run > 0 ? '?' : (white ? '.' : 'X');
        }
        System.out.println(new String(out));
    }
}
