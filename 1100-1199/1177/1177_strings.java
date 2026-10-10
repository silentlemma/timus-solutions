import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Main {
    static final int BYTES = 256;
    static int after;

    // the text between quotes starting at p, with doubled quotes undone,
    // leaving after just past the closing quote
    static String quoted(String line, int p) {
        StringBuilder out = new StringBuilder();
        for (p++; p < line.length(); p++) {
            if (line.charAt(p) == '\'') {
                if (p + 1 < line.length() && line.charAt(p + 1) == '\'') {
                    out.append('\'');
                    p++;
                    continue;
                }
                p++;
                break;
            }
            out.append(line.charAt(p));
        }
        after = p;
        return out.toString();
    }

    static boolean like(String text, String pattern) {
        int n = text.length(), m = pattern.length();
        // reach[i]: the pattern so far can match exactly the first i bytes
        boolean[] reach = new boolean[n + 1];
        reach[0] = true;
        for (int j = 0; j < m;) {
            char c = pattern.charAt(j);
            boolean[] next = new boolean[n + 1];
            if (c == '%') {
                boolean seen = false;
                for (int i = 0; i <= n; i++) {
                    seen = seen || reach[i];
                    next[i] = seen;
                }
                j++;
            } else if (c == '[') {
                // a set of bytes, negated after ^, with ranges a-b unless b
                // is ]
                int k = j + 1;
                boolean negated = k < m && pattern.charAt(k) == '^';
                if (negated) {
                    k++;
                }
                boolean[] accepted = new boolean[BYTES];
                while (k < m && pattern.charAt(k) != ']') {
                    char lo = pattern.charAt(k), hi = lo;
                    if (k + 2 < m && pattern.charAt(k + 1) == '-' && pattern.charAt(k + 2) != ']') {
                        hi = pattern.charAt(k + 2);
                        k += 2;
                    }
                    for (int x = lo; x <= hi; x++) {
                        accepted[x] = true;
                    }
                    k++;
                }
                if (k == m) {
                    return false; // a [ with no closing ] never matches
                }
                for (int i = 0; i < n; i++) {
                    next[i + 1] = reach[i] && accepted[text.charAt(i)] != negated;
                }
                j = k + 1;
            } else {
                for (int i = 0; i < n; i++) {
                    next[i + 1] = reach[i] && (c == '_' || text.charAt(i) == c);
                }
                j++;
            }
            reach = next;
        }
        return reach[n];
    }

    public static void main(String[] args) throws IOException {
        // Latin-1 maps every byte to the char with the same code
        BufferedReader in =
            new BufferedReader(new InputStreamReader(System.in, StandardCharsets.ISO_8859_1));
        int n = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int q = 0; q < n; q++) {
            String line = in.readLine();
            String text = quoted(line, line.indexOf('\''));
            String pattern = quoted(line, line.indexOf('\'', after));
            out.append(like(text, pattern) ? "YES\n" : "NO\n");
        }
        System.out.print(out);
    }
}
