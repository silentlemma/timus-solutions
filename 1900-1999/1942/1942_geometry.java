import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Locale;

public class Main {
    private static final int SCALE = 1000;
    private static final int FRACTION_DIGITS = 3;

    static int scaled(String token) {
        int sign = 1, fraction = 0, digits = 0;
        boolean afterPoint = false;
        for (int index = 0; index < token.length(); ++index) {
            char symbol = token.charAt(index);
            if (symbol == '-')
                sign = -1;
            else if (symbol == '+')
                continue;
            else if (symbol == '.')
                afterPoint = true;
            else if (afterPoint) {
                fraction = fraction * 10 + symbol - '0';
                ++digits;
            }
        }
        while (digits++ < FRACTION_DIGITS)
            fraction *= 10;
        return sign * fraction;
    }

    static int[] bestGroup(int[] xs, int[] ys) {
        int[] counts = new int[SCALE * SCALE];
        int bestCount = 0, bestNorm = 0;
        for (int index = 0; index < xs.length; ++index) {
            int rx = (xs[index] % SCALE + SCALE) % SCALE;
            int ry = (ys[index] % SCALE + SCALE) % SCALE;
            int count = ++counts[rx * SCALE + ry];
            int dx = Math.min(rx, SCALE - rx), dy = Math.min(ry, SCALE - ry);
            int norm = dx * dx + dy * dy;
            if (count > bestCount || (count == bestCount && norm < bestNorm)) {
                bestCount = count;
                bestNorm = norm;
            }
        }
        return new int[] {bestCount, bestNorm};
    }

    static String nextToken(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        StringBuilder token = new StringBuilder();
        while (symbol > ' ') {
            token.append((char)symbol);
            symbol = in.read();
        }
        return token.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int size = Integer.parseInt(nextToken(in));
        int[] xs = new int[size], ys = new int[size];
        for (int index = 0; index < size; ++index) {
            xs[index] = scaled(nextToken(in));
            ys[index] = scaled(nextToken(in));
        }
        int[] best = bestGroup(xs, ys);
        System.out.printf(Locale.US, "%d %.9f%n", best[0], Math.sqrt(best[1]) / SCALE);
    }
}
