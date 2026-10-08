import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_WORD_LENGTH = 50;
    private static final String KEYPAD = "22233344115566070778889990";
    private static final String END_OF_INPUT = "-1";

    private static BufferedReader in;
    private static StringTokenizer tokens = new StringTokenizer("");

    private static String next() throws IOException {
        while (!tokens.hasMoreTokens()) {
            tokens = new StringTokenizer(in.readLine());
        }
        return tokens.nextToken();
    }

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        String phone;
        while (!(phone = next()).equals(END_OF_INPUT)) {
            int n = Integer.parseInt(next());
            String[] words = new String[n];
            HashMap<String, Integer> byDigits = new HashMap<>();
            for (int i = 0; i < n; i++) {
                words[i] = next();
                char[] digits = words[i].toCharArray();
                for (int j = 0; j < digits.length; j++) {
                    digits[j] = KEYPAD.charAt(digits[j] - 'a');
                }
                byDigits.putIfAbsent(new String(digits), i);
            }
            // best[i]: fewest words for the first i digits; how[i]: last word used
            int m = phone.length();
            int[] best = new int[m + 1];
            int[] how = new int[m + 1];
            Arrays.fill(best, -1);
            best[0] = 0;
            for (int i = 0; i < m; i++) {
                if (best[i] < 0) {
                    continue;
                }
                for (int len = 1; len <= MAX_WORD_LENGTH && i + len <= m; len++) {
                    Integer w = byDigits.get(phone.substring(i, i + len));
                    if (w != null && (best[i + len] < 0 || best[i] + 1 < best[i + len])) {
                        best[i + len] = best[i] + 1;
                        how[i + len] = w;
                    }
                }
            }
            if (best[m] < 0) {
                out.println("No solution.");
                continue;
            }
            List<String> used = new ArrayList<>();
            for (int pos = m; pos > 0; pos -= words[how[pos]].length()) {
                used.add(words[how[pos]]);
            }
            StringBuilder line = new StringBuilder();
            for (int i = used.size() - 1; i >= 0; i--) {
                line.append(used.get(i));
                if (i > 0) {
                    line.append(' ');
                }
            }
            out.println(line);
        }
        out.flush();
    }
}
