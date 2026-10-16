import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    // counts are capped here: two ways already make the answer ambiguous
    static final int MANY = 2;

    // whether digit c of the paper may be bit b
    static boolean fits(char c, int b) {
        return c == '?' || c - '0' == b;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String k = in.readLine().trim(), x = in.readLine().trim();
        int n = k.length();
        // the Gray code of k has digit x(i) = k(i) xor k(i - 1), with a 0 before
        // the first digit; ways[b][i] counts the readings of the first i + 1
        // digits that end with k(i) = b
        int[][] ways = new int[2][n];
        int[] w = {1, 0};
        for (int i = 0; i < n; i++) {
            int[] next = new int[2];
            for (int cur = 0; cur < 2; cur++) {
                if (!fits(k.charAt(i), cur)) continue;
                for (int prev = 0; prev < 2; prev++) {
                    if (fits(x.charAt(i), prev ^ cur)) {
                        next[cur] = Math.min(MANY, next[cur] + w[prev]);
                    }
                }
            }
            w = next;
            ways[0][i] = w[0];
            ways[1][i] = w[1];
        }
        if (w[0] + w[1] == 0) {
            System.out.println("Impossible");
            return;
        }
        if (w[0] + w[1] > 1) {
            System.out.println("Ambiguity");
            return;
        }
        // walk back along the single reading: exactly one earlier digit of k
        // with a reading of its own leads on to the next one
        char[] bits = new char[n], code = new char[n];
        int cur = w[1] > 0 ? 1 : 0;
        bits[n - 1] = (char) ('0' + cur);
        for (int i = n - 1; i > 0; i--) {
            for (int prev = 0; prev < 2; prev++) {
                if (ways[prev][i - 1] > 0 && fits(x.charAt(i), prev ^ cur)) {
                    bits[i - 1] = (char) ('0' + prev);
                    code[i] = (char) ('0' + (prev ^ cur));
                }
            }
            cur = bits[i - 1] - '0';
        }
        code[0] = bits[0];
        System.out.println(new String(bits) + "\n" + new String(code));
    }
}
