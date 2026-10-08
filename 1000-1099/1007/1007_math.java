import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // Undo at most one change: the sum of the positions (from 1) of the ones of
    // a sent word is divisible by n + 1.
    static String restore(String s, int n) {
        int mod = n + 1, len = s.length(), w = 0;
        for (int i = 0; i < len; i++) {
            if (s.charAt(i) == '1') {
                w += i + 1;
            }
        }
        if (len == n) {
            // a raised zero at position p adds exactly p to the weight
            int p = w % mod;
            return p == 0 ? s : s.substring(0, p - 1) + '0' + s.substring(p);
        }
        // onesAfter: ones to the right of the changed place; they shift by one
        int onesAfter = 0;
        if (len == n - 1) {
            for (int i = len; i >= 0; i--) {
                for (int d = 0; d <= 1; d++) {
                    if ((w + onesAfter + d * (i + 1)) % mod == 0) {
                        return s.substring(0, i) + (char)('0' + d) + s.substring(i);
                    }
                }
                if (i > 0 && s.charAt(i - 1) == '1') {
                    onesAfter++;
                }
            }
        } else {
            for (int i = len - 1; i >= 0; i--) {
                int d = s.charAt(i) - '0';
                if ((w - onesAfter - d * (i + 1)) % mod == 0) {
                    return s.substring(0, i) + s.substring(i + 1);
                }
                onesAfter += d;
            }
        }
        return s;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line; (line = in.readLine()) != null;) {
            text.append(line).append('\n');
        }
        StringTokenizer tokens = new StringTokenizer(text.toString());
        int n = Integer.parseInt(tokens.nextToken());
        StringBuilder out = new StringBuilder();
        while (tokens.hasMoreTokens()) {
            out.append(restore(tokens.nextToken(), n)).append('\n');
        }
        System.out.print(out);
    }
}
