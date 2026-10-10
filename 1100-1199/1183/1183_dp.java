import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String s;
    // add[i][j]: fewest brackets to add so that s[i, j) becomes regular; how
    // it is best done: 0 pads a lone bracket, -1 wraps a pair, k splits at k
    static int[][] add, how;

    static boolean pair(char a, char b) { return (a == '(' && b == ')') || (a == '[' && b == ']'); }

    static void build(int i, int j, StringBuilder out) {
        if (i == j) {
            return;
        }
        int way = how[i][j];
        if (way == 0) {
            out.append(s.charAt(i) == '(' || s.charAt(i) == ')' ? "()" : "[]");
        } else if (way < 0) {
            out.append(s.charAt(i));
            build(i + 1, j - 1, out);
            out.append(s.charAt(j - 1));
        } else {
            build(i, way, out);
            build(way, j, out);
        }
    }

    public static void main(String[] args) throws IOException {
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine();
        s = line == null ? "" : line.trim();
        int n = s.length();
        add = new int[n + 1][n + 1];
        how = new int[n + 1][n + 1];
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i + length <= n; i++) {
                int j = i + length;
                if (length == 1) {
                    add[i][j] = 1;
                    continue;
                }
                int best = add[i][i + 1] + add[i + 1][j], way = i + 1;
                if (pair(s.charAt(i), s.charAt(j - 1)) && add[i + 1][j - 1] < best) {
                    best = add[i + 1][j - 1];
                    way = -1;
                }
                for (int k = i + 2; k < j; k++) {
                    if (add[i][k] + add[k][j] < best) {
                        best = add[i][k] + add[k][j];
                        way = k;
                    }
                }
                add[i][j] = best;
                how[i][j] = way;
            }
        }
        StringBuilder out = new StringBuilder();
        build(0, n, out);
        System.out.println(out);
    }
}
