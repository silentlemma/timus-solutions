import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static final long CENTS = 100, PEAK = 2 * CENTS, DIAGONAL = 4 * CENTS;
    static final BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens = new StringTokenizer("");
    static long a, b, k, best, bestX, bestY;

    static String next() throws IOException {
        while (!tokens.hasMoreTokens())
            tokens = new StringTokenizer(input.readLine());
        return tokens.nextToken();
    }

    static long cents(String text) {
        boolean negative = text.charAt(0) == '-';
        long value = 0;
        int fraction = 0;
        boolean point = false;
        for (int i = 0; i < text.length(); i++) {
            char digit = text.charAt(i);
            if (i == 0 && (digit == '-' || digit == '+'))
                continue;
            if (digit == '.')
                point = true;
            else {
                value = value * 10 + digit - '0';
                if (point)
                    fraction++;
            }
        }
        while (fraction++ < 2)
            value *= 10;
        return negative ? -value : value;
    }

    static long clamp(long value) { return Math.max(0, Math.min(k, value)); }

    static void consider(long x, long y) {
        if (x + y > k)
            return;
        long gain = a * x + b * y - CENTS * (x * x + y * y);
        if (gain > best || (gain == best && (x < bestX || (x == bestX && y < bestY)))) {
            best = gain;
            bestX = x;
            bestY = y;
        }
    }

    public static void main(String[] args) throws IOException {
        a = cents(next());
        b = cents(next());
        k = Long.parseLong(next());
        // Interior optima round both independent peaks. Each edge has one peak.
        for (long x : new long[] {clamp(a / PEAK), clamp(a / PEAK + 1)}) {
            consider(x, 0);
            for (long y : new long[] {clamp(b / PEAK), clamp(b / PEAK + 1)}) {
                consider(x, y);
                consider(0, y);
            }
        }
        long diagonal = (a - b + PEAK * k) / DIAGONAL;
        for (long x : new long[] {clamp(diagonal), clamp(diagonal + 1)})
            consider(x, k - x);
        System.out.printf("%d.%02d%n%d %d%n", best / CENTS, best % CENTS, bestX, bestY);
    }
}
