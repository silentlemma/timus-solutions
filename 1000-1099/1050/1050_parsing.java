import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int BUFFER = 1 << 16;
    // what happens to a double quote
    static final byte KEEP = 0, OPEN = 1, CLOSE = 2, DROP = 3;

    static byte[] mark;
    static List<Integer> quotes = new ArrayList<>();

    static boolean blank(byte c) {
        return c == ' ' || c == '\t' || c == '\r' || c == '\u000B' || c == '\f';
    }

    static boolean letter(byte c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

    // pairs the quotes of the finished paragraph; an unpaired last one goes away
    static void close() {
        if (quotes.size() % 2 == 1) {
            mark[quotes.remove(quotes.size() - 1)] = DROP;
        }
        for (int k = 0; k < quotes.size(); k++) {
            mark[quotes.get(k)] = k % 2 == 0 ? OPEN : CLOSE;
        }
        quotes.clear();
    }

    public static void main(String[] args) throws IOException {
        // the text is handled as bytes: letters above 127 are copied as they are
        InputStream in = System.in;
        ByteArrayOutputStream all = new ByteArrayOutputStream();
        byte[] buf = new byte[BUFFER];
        for (int k; (k = in.read(buf)) > 0;) {
            all.write(buf, 0, k);
        }
        byte[] s = all.toByteArray();
        int n = s.length;
        mark = new byte[n];
        for (int i = 0; i < n;) {
            if (s[i] == '\\') {
                // \" is an umlaut; otherwise the command name is the letters after \.
                if (i + 1 < n && s[i + 1] == '"') {
                    i += 2;
                    continue;
                }
                int j = i + 1;
                while (j < n && letter(s[j])) {
                    j++;
                }
                if (j - i - 1 == "par".length() && new String(s, i + 1, j - i - 1).equals("par")) {
                    close();
                }
                i = j;
            } else if (s[i] == '"') {
                quotes.add(i++);
            } else {
                // a line of only whitespace that ends with a line break ends a paragraph
                if (s[i] == '\n') {
                    int j = i + 1;
                    while (j < n && blank(s[j])) {
                        j++;
                    }
                    if (j < n && s[j] == '\n') {
                        close();
                    }
                }
                i++;
            }
        }
        close();
        ByteArrayOutputStream out = new ByteArrayOutputStream(n + n / 2);
        for (int i = 0; i < n; i++) {
            if (mark[i] == KEEP) {
                out.write(s[i]);
            } else if (mark[i] == OPEN) {
                out.write('`');
                out.write('`');
            } else if (mark[i] == CLOSE) {
                out.write('\'');
                out.write('\'');
            }
        }
        System.out.write(out.toByteArray());
        System.out.flush();
    }
}
