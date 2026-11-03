import java.io.IOException;

public class Main {
    static final long HUNDREDTHS = 100, WHOLE = 100 * HUNDREDTHS;

    static long percentage() throws IOException {
        int ch = System.in.read();
        while (ch <= ' ')
            ch = System.in.read();
        long value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = System.in.read();
        }
        value *= HUNDREDTHS;
        if (ch == '.') {
            long scale = HUNDREDTHS;
            for (ch = System.in.read(); ch >= '0' && ch <= '9'; ch = System.in.read()) {
                scale /= 10;
                value += (ch - '0') * scale;
            }
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        long p = percentage(), q = percentage(), a = 0, b = 1, c = 1, d = 0;
        while (true) {
            long numerator = a + c, denominator = b + d;
            if (WHOLE * numerator <= p * denominator) {
                // Maximal consecutive mediants outside the strict lower bound.
                long steps = (p * b - WHOLE * a) / (WHOLE * c - p * d);
                a += steps * c;
                b += steps * d;
            } else if (WHOLE * numerator >= q * denominator) {
                long steps = (WHOLE * c - q * d) / (q * b - WHOLE * a);
                c += steps * a;
                d += steps * b;
            } else {
                System.out.println(denominator);
                return;
            }
        }
    }
}
