import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static String a;

    // x + 1 for a decimal string
    static String inc(String x) {
        char[] b = x.toCharArray();
        int k = b.length - 1;
        while (k >= 0 && b[k] == '9') {
            b[k--] = '0';
        }
        if (k < 0) {
            return "1" + new String(b);
        }
        b[k]++;
        return new String(b);
    }

    // x - 1 for a positive decimal string
    static String dec(String x) {
        char[] b = x.toCharArray();
        int k = b.length - 1;
        while (b[k] == '0') {
            b[k--] = '9';
        }
        b[k]--;
        String r = new String(b);
        return r.charAt(0) == '0' && r.length() > 1 ? r.substring(1) : r;
    }

    // position in S of the digit s places before the start of x; the numbers
    // below 10^(d-1) take (d-1)·10^(d-1) - R(d-1) digits, where R(t) is the
    // repunit of t ones, which leaves d·x + 1 - R(d) for x itself
    static BigInteger position(String x, int s) {
        int d = x.length();
        BigInteger ones = new BigInteger(new String(new char[d]).replace('\0', '1'));
        return new BigInteger(x)
            .multiply(BigInteger.valueOf(d))
            .subtract(ones)
            .add(BigInteger.valueOf(1 - s));
    }

    // the number x can begin at position s of a, with its neighbours filling
    // the rest of a on both sides
    static boolean fits(int s, String x) {
        int n = a.length();
        if (!a.regionMatches(s, x, 0, Math.min(x.length(), n - s))) {
            return false;
        }
        int pos = s + x.length();
        String cur = x;
        while (pos < n) {
            cur = inc(cur);
            if (!a.regionMatches(pos, cur, 0, Math.min(cur.length(), n - pos))) {
                return false;
            }
            pos += cur.length();
        }
        pos = s;
        cur = x;
        while (pos > 0) {
            cur = dec(cur);
            if (cur.equals("0")) {
                return false;
            }
            int m = Math.min(pos, cur.length());
            if (!a.regionMatches(pos - m, cur, cur.length() - m, m)) {
                return false;
            }
            pos -= cur.length();
        }
        return true;
    }

    static BigInteger best;

    static void consider(int s, String x) {
        if (fits(s, x)) {
            BigInteger k = position(x, s);
            if (k.compareTo(best) < 0) {
                best = k;
            }
        }
    }

    public static void main(String[] args) {
        a = new Scanner(System.in).next();
        int n = a.length();
        // a inside one number, right after its first digit
        best = position("1" + a, -1);
        // some number lies in a completely
        for (int s = 0; s < n; s++) {
            if (a.charAt(s) != '0') {
                for (int e = s + 1; e <= n; e++) {
                    consider(s, a.substring(s, e));
                }
            }
        }
        // a is the end of y - 1 followed by the beginning of y; the last i
        // digits of y are those of y - 1 plus one, and they may overlap the
        // known beginning by j digits
        for (int i = 1; i < n; i++) {
            if (a.charAt(i) == '0') {
                continue;
            }
            String tail = inc(a.substring(0, i));
            tail = tail.substring(tail.length() - i);
            for (int j = 0; j <= Math.min(n - i, i); j++) {
                if (a.regionMatches(n - j, tail, 0, j)) {
                    consider(i, a.substring(i) + tail.substring(j));
                }
            }
        }
        System.out.println(best);
    }
}
