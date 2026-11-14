import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;

    private static long nextLong(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        boolean negative = ch == '-';
        if (negative || ch == '+') {
            ch = input.read();
        }
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * DECIMAL + (ch - '0');
            ch = input.read();
        }
        return negative ? -value : value;
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return Math.abs(a);
    }

    private static boolean reachable(long p, long q, long dx, long dy) {
        long step = gcd(p, q);
        if (step == 0) {
            return dx == 0 && dy == 0;
        }
        if (dx % step != 0 || dy % step != 0) {
            return false;
        }
        // Coprime normalized steps have the same parity exactly when both are odd.
        return (p + q) % (2 * step) != 0 || (dx + dy) % (2 * step) == 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        long p = nextLong(input);
        long q = nextLong(input);
        long x = nextLong(input);
        long y = nextLong(input);
        System.out.println(reachable(p, q, nextLong(input) - x, nextLong(input) - y) ? "YES"
                                                                                     : "NO");
    }
}
