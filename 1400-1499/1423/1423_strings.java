import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in =
            new BufferedReader(new InputStreamReader(System.in, StandardCharsets.ISO_8859_1));
        int n = Integer.parseInt(in.readLine().trim());
        char[] s = in.readLine().toCharArray(), t = in.readLine().toCharArray();
        // t is s turned left by k, that is right by n - k: find it in s + s with KMP
        int[] fail = new int[n];
        for (int i = 1, k = 0; i < n; i++) {
            while (k > 0 && t[i] != t[k])
                k = fail[k - 1];
            if (t[i] == t[k])
                k++;
            fail[i] = k;
        }
        for (int i = 0, k = 0; i + 1 < 2 * n; i++) {
            char c = s[i % n];
            while (k > 0 && c != t[k])
                k = fail[k - 1];
            if (c == t[k])
                k++;
            if (k == n) {
                int start = i - n + 1;
                System.out.println((n - start) % n);
                return;
            }
        }
        System.out.println(-1);
    }
}
