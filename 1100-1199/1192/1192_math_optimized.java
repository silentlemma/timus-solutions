import java.util.Locale;

public class Main {
    static final double GRAVITY = 10.0, PI = 3.1415926535, HALF_TURN = 180.0;

    // retain double parsing and formatting so rounding matches the simple version.
    private static double nextDouble() throws java.io.IOException {
        StringBuilder token = new StringBuilder();
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        while (c > ' ') {
            token.append((char)c);
            c = System.in.read();
        }
        return Double.parseDouble(token.toString());
    }

    public static void main(String[] args) throws java.io.IOException {
        double v = nextDouble(), a = nextDouble(), k = nextDouble();
        // one flight covers v^2 sin(2a) / g; every bounce keeps the angle and
        // divides v^2 by k, so the flights form a geometric series with
        // ratio 1/k
        double flight = v * v * Math.sin(2 * a * PI / HALF_TURN) / GRAVITY;
        System.out.println(String.format(Locale.US, "%.2f", flight * k / (k - 1)));
    }
}
