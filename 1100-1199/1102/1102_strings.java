import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final String[] WORDS = {"out", "output", "puton", "in", "input", "one"};
    // the longest word, so the window of the last letters can be that short
    static final int LONGEST = 6;

    public static void main(String[] args) throws IOException {
        InputStream in = new BufferedInputStream(System.in);
        int n = 0;
        int c = in.read();
        while (c < '0' || c > '9') {
            c = in.read();
        }
        for (; c >= '0' && c <= '9'; c = in.read()) {
            n = n * 10 + (c - '0');
        }
        StringBuilder out = new StringBuilder();
        // a line of millions of letters would not fit in 16 MB as a String, so
        // it is read letter by letter: good[i] says the first i letters split
        // into words, and only the last LONGEST + 1 values and letters are kept
        char[] last = new char[LONGEST + 1];
        boolean[] good = new boolean[LONGEST + 1];
        for (int line = 0; line < n; line++) {
            while (c < 'a' || c > 'z') {
                c = in.read();
            }
            int length = 0;
            good[0] = true;
            for (; c >= 'a' && c <= 'z'; c = in.read()) {
                length++;
                last[length % (LONGEST + 1)] = (char)c;
                boolean ok = false;
                for (String w : WORDS) {
                    int k = w.length();
                    if (k > length || !good[(length - k) % (LONGEST + 1)]) {
                        continue;
                    }
                    boolean same = true;
                    for (int j = 0; j < k && same; j++) {
                        same = last[(length - k + 1 + j) % (LONGEST + 1)] == w.charAt(j);
                    }
                    ok |= same;
                }
                good[length % (LONGEST + 1)] = ok;
            }
            out.append(good[length % (LONGEST + 1)] ? "YES\n" : "NO\n");
        }
        System.out.print(out);
    }
}
