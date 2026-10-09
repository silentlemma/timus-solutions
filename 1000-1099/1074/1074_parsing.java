import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;

public class Main {
    // exponents beyond this either give zero or an answer longer than allowed
    static final int EXP_LIMIT = 1000;
    static final String FAIL = "Not a floating point number";
    static final int BUFFER = 1 << 16;

    static String s;
    static int pos;

    static boolean isDigit(char c) { return c >= '0' && c <= '9'; }

    static String run() {
        int start = pos;
        while (pos < s.length() && isDigit(s.charAt(pos))) {
            pos++;
        }
        return s.substring(start, pos);
    }

    static boolean at(String chars) {
        return pos < s.length() && chars.indexOf(s.charAt(pos)) >= 0;
    }

    static String convert(String line, int n) {
        s = line;
        pos = 0;
        boolean negative = false;
        if (at("+-")) {
            negative = s.charAt(pos++) == '-';
        }
        String whole = run();
        String frac = "";
        if (at(".")) {
            pos++;
            frac = run();
            if (frac.isEmpty()) {
                return FAIL;
            }
        } else if (whole.isEmpty()) {
            return FAIL;
        }
        int exp = 0;
        if (at("eE")) {
            pos++;
            int sign = 1;
            if (at("+-")) {
                sign = s.charAt(pos++) == '-' ? -1 : 1;
            }
            String power = run();
            if (power.isEmpty()) {
                return FAIL;
            }
            for (char c : power.toCharArray()) {
                exp = Math.min(exp * 10 + (c - '0'), EXP_LIMIT);
            }
            exp *= sign;
        }
        if (pos != s.length()) {
            return FAIL;
        }
        // the digits of the number with the decimal point after `point` of them
        String mantissa = whole + frac;
        int point = whole.length() + exp;
        if (mantissa.replace("0", "").isEmpty()) {
            point = 0;
        }
        StringBuilder head = new StringBuilder();
        StringBuilder tail = new StringBuilder();
        for (int i = 0; i < point; i++) {
            char d = i < mantissa.length() ? mantissa.charAt(i) : '0';
            if (head.length() > 0 || d != '0') {
                head.append(d);
            }
        }
        if (head.length() == 0) {
            head.append('0');
        }
        for (int i = point; i < point + n; i++) {
            tail.append(i >= 0 && i < mantissa.length() ? mantissa.charAt(i) : '0');
        }
        String out = head + (n > 0 ? "." + tail : "");
        if (negative && !(head.toString() + tail).replace("0", "").isEmpty()) {
            out = "-" + out;
        }
        return out;
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buf = new byte[BUFFER];
        for (int r; (r = in.read(buf)) > 0;) {
            bytes.write(buf, 0, r);
        }
        String[] lines =
            new String(bytes.toByteArray(), StandardCharsets.ISO_8859_1).split("\n", -1);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i + 1 < lines.length; i += 2) {
            String line = lines[i];
            if (line.endsWith("\r")) {
                line = line.substring(0, line.length() - 1);
            }
            if (line.equals("#")) {
                break;
            }
            out.append(convert(line, Integer.parseInt(lines[i + 1].trim()))).append('\n');
        }
        System.out.print(out);
    }
}
