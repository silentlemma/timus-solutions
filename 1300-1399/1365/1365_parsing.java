import java.io.*;
import java.util.ArrayList;

public class Main {
    static final long NONE = -1; // no term starts here
    static final int BASE = 10;

    static String s;
    static int pos;

    static boolean accept(char c) {
        if (pos < s.length() && s.charAt(pos) == c) {
            pos++;
            return true;
        }
        return false;
    }

    static boolean digitAt(int i) { return i < s.length() && Character.isDigit(s.charAt(i)); }

    // a number, an operation with its arguments, or a bracket
    static long term() {
        if (digitAt(pos)) {
            long v = 0;
            while (digitAt(pos))
                v = v * BASE + (s.charAt(pos++) - '0');
            return v;
        }
        for (char sign : "+*/".toCharArray())
            if (accept(sign))
                return fold(sign);
        if (accept('(')) {
            long x = glue(false);
            accept(')');
            return x;
        }
        return NONE;
    }

    // the arguments of an operation are glued terms split by ';'
    static long fold(char sign) {
        long a = glue(true);
        while (accept(';')) {
            long b = glue(true);
            if (sign == '+')
                a += b;
            else if (sign == '*')
                a *= b;
            else
                a = b == 0 ? 0 : a / b;
        }
        return a;
    }

    // terms one after another are glued as decimal strings; inside an
    // operation ';' ends the argument, elsewhere it glues the whole rest,
    // and a missing term counts as 1
    static long glue(boolean inside) {
        ArrayList<Long> parts = new ArrayList<Long>();
        for (long x = term(); x != NONE || parts.isEmpty(); x = term()) {
            parts.add(x);
            if (pos < s.length() && s.charAt(pos) == ';') {
                if (inside)
                    break;
                pos++;
                parts.add(glue(false));
            }
        }
        StringBuilder text = new StringBuilder();
        for (long x : parts)
            text.append(Math.abs(x));
        try {
            return Long.parseLong(text.toString());
        } catch (NumberFormatException e) {
            return Long.MAX_VALUE; // a glued number that does not fit is cut
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        String line;
        for (int i = 1; (line = in.readLine()) != null; i++) {
            s = line;
            pos = 0;
            out.append("Expression ").append(i).append(" evaluates to: ");
            out.append(glue(false)).append('\n');
        }
        System.out.print(out);
    }
}
