import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Locale;
import java.util.Set;

public class Main {
    static final Set<String> KEYWORDS = new HashSet<>(
        Arrays.asList("and", "array", "begin", "case", "class", "const", "div", "do", "else", "end",
                      "for", "function", "if", "implementation", "interface", "mod", "not", "of",
                      "or", "procedure", "program", "record", "repeat", "shl", "shr", "string",
                      "then", "to", "type", "unit", "until", "uses", "var", "with", "while"));
    static final int BUFFER = 1 << 16;

    static boolean isDigit(byte c) { return c >= '0' && c <= '9'; }

    static boolean isWord(byte c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || c == '_';
    }

    static ByteArrayOutputStream out = new ByteArrayOutputStream();

    static void wrap(String kind, byte[] text, int from, int to) {
        byte[] open = ("<span class=" + kind + ">").getBytes();
        out.write(open, 0, open.length);
        out.write(text, from, to - from);
        byte[] close = "</span>".getBytes();
        out.write(close, 0, close.length);
    }

    static int find(byte[] text, int n, int from, byte target) {
        for (int k = from; k < n; k++) {
            if (text[k] == target)
                return k;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream rawStream = new ByteArrayOutputStream();
        byte[] chunk = new byte[BUFFER];
        for (int r = in.read(chunk); r > 0; r = in.read(chunk))
            rawStream.write(chunk, 0, r);
        byte[] raw = rawStream.toByteArray();
        byte[] text = new byte[raw.length];
        int n = 0;
        for (int k = 0; k < raw.length; k++) {
            if (!(raw[k] == '\r' && k + 1 < raw.length && raw[k + 1] == '\n'))
                text[n++] = raw[k];
        }
        int i = 0;
        while (i < n) {
            byte c = text[i];
            int j = i + 1;
            if (c == '{') {
                int k = find(text, n, i, (byte)'}');
                j = k < 0 ? n : k + 1;
                wrap("comment", text, i, j);
            } else if (c == '/' && i + 1 < n && text[i + 1] == '/') {
                int k = find(text, n, i, (byte)'\n'); // the line break is not part of it
                j = k < 0 ? n : k;
                wrap("comment", text, i, j);
            } else if (c == '\'') {
                int k = find(text, n, i + 1, (byte)'\'');
                j = k < 0 ? n : k + 1;
                wrap("string", text, i, j);
            } else if (c == '#' && i + 1 < n && isDigit(text[i + 1])) {
                for (j = i + 1; j < n && isDigit(text[j]); j++) {
                }
                wrap("string", text, i, j);
            } else if (isDigit(c)) {
                for (j = i; j < n && isDigit(text[j]); j++) {
                }
                // one point is allowed, but only with digits after it
                if (j + 1 < n && text[j] == '.' && isDigit(text[j + 1])) {
                    for (j++; j < n && isDigit(text[j]); j++) {
                    }
                }
                wrap("number", text, i, j);
            } else if (isWord(c)) {
                for (j = i; j < n && (isWord(text[j]) || isDigit(text[j])); j++) {
                }
                String word = new String(text, i, j - i, "ISO-8859-1").toLowerCase(Locale.ROOT);
                if (KEYWORDS.contains(word))
                    wrap("keyword", text, i, j);
                else
                    out.write(text, i, j - i);
            } else {
                out.write(c);
            }
            i = j;
        }
        System.out.write(out.toByteArray());
        System.out.flush();
    }
}
