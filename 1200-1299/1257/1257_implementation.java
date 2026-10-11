import java.io.*;
import java.nio.charset.StandardCharsets;

public class Main {
    static final int WIDTH = 40;
    static final int CHUNK = 1 << 16;

    static boolean isLetter(char c) { return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'); }

    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buf = new byte[CHUNK];
        for (int k; (k = System.in.read(buf)) > 0;)
            bytes.write(buf, 0, k);
        String data =
            new String(bytes.toByteArray(), StandardCharsets.ISO_8859_1).replace("\r", "");
        String[] lines = data.split("\n", -1);
        int n = Integer.parseInt(lines[0].trim());
        // a rule s1-s2 matches words ending in s1s2 and carries s2 over
        String[] patterns = new String[n];
        int[] cuts = new int[n];
        for (int i = 0; i < n; i++) {
            String line = lines[1 + i].trim();
            int dash = line.indexOf('-');
            patterns[i] = (line.substring(0, dash) + line.substring(dash + 1)).toLowerCase();
            cuts[i] = line.length() - dash - 1;
        }
        StringBuilder rest = new StringBuilder();
        for (int i = n + 1; i < lines.length; i++) {
            if (i > n + 1)
                rest.append('\n');
            rest.append(lines[i]);
        }
        String text = rest.toString();
        StringBuilder out = new StringBuilder();
        int col = 0;
        for (int i = 0; i < text.length();) {
            char c = text.charAt(i);
            if (c == '\n') {
                out.append(c);
                col = 0;
                i++;
                continue;
            }
            if (!isLetter(c)) {
                // a full line moves a separator to the next one
                if (col == WIDTH) {
                    out.append('\n');
                    col = 0;
                }
                out.append(c);
                col++;
                i++;
                continue;
            }
            int start = i;
            while (i < text.length() && isLetter(text.charAt(i)))
                i++;
            String word = text.substring(start, i), low = word.toLowerCase();
            int len = word.length();
            if (col + len <= WIDTH) {
                out.append(word);
                col += len;
                continue;
            }
            // the shortest carried part whose head and '-' still fit
            int carry = 0;
            for (int r = 0; r < n; r++) {
                boolean fits = col + len - cuts[r] + 1 <= WIDTH;
                if (low.endsWith(patterns[r]) && fits && (carry == 0 || cuts[r] < carry))
                    carry = cuts[r];
            }
            if (carry > 0) {
                out.append(word, 0, len - carry).append("-\n").append(word, len - carry, len);
            } else {
                out.append('\n').append(word);
                carry = len;
            }
            col = carry;
        }
        PrintStream ps = new PrintStream(System.out, false, "ISO-8859-1");
        ps.print(out);
        ps.flush();
    }
}
