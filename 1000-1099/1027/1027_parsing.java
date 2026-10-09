import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int BUFFER = 1 << 12;
    // characters allowed inside an arithmetic expression besides the brackets
    static final String EXPRESSION = "=+-*/0123456789\r\n";

    static boolean valid(String s) {
        int depth = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (s.startsWith("(*", i)) {
                // a comment ends at the first *) after its opening pair
                int end = s.indexOf("*)", i + 2);
                if (end < 0) {
                    return false;
                }
                i = end + 1;
            } else if (c == '(') {
                depth++;
            } else if (c == ')') {
                if (depth == 0) {
                    return false;
                }
                depth--;
            } else if (depth > 0 && EXPRESSION.indexOf(c) < 0) {
                return false;
            }
        }
        return depth == 0;
    }

    static String readAll(InputStream in) throws IOException {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buffer = new byte[BUFFER];
        for (int n; (n = in.read(buffer)) > 0;) {
            bytes.write(buffer, 0, n);
        }
        return bytes.toString("ISO-8859-1");
    }

    public static void main(String[] args) throws IOException {
        System.out.println(valid(readAll(System.in)) ? "YES" : "NO");
    }
}
