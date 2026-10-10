import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int NEW = 0, PATH = 1, GOOD = 2;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tok = new StringTokenizer("");

    static int next() throws IOException {
        while (!tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return Integer.parseInt(tok.nextToken());
    }

    static boolean consistent(int[] names) {
        int n = names.length, zeros = 0;
        for (int k : names) {
            if (k == 0) {
                zeros++;
            }
        }
        if (zeros != 1) {
            return false;
        }
        int[] state = new int[n + 1], path = new int[n];
        for (int start = 1; start <= n; start++) {
            // follow the accusations until a confessor or a child already known
            // to lead to one; meeting the current path again means a ring
            int len = 0, v = start;
            while (v != 0 && state[v] == NEW) {
                state[v] = PATH;
                path[len++] = v;
                v = names[v - 1];
            }
            if (v != 0 && state[v] == PATH) {
                return false;
            }
            for (int i = 0; i < len; i++) {
                state[path[i]] = GOOD;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        int t = next();
        StringBuilder out = new StringBuilder();
        for (; t > 0; t--) {
            int[] names = new int[next()];
            for (int i = 0; i < names.length; i++) {
                names[i] = next();
            }
            out.append(consistent(names) ? "YES" : "NO").append('\n');
        }
        System.out.print(out);
    }
}
