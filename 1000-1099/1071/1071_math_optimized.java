import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static final int DECIMAL = 10;

    static int number(BufferedInputStream in) throws IOException {
        int c = in.read();
        while (c >= 0 && c <= ' ') {
            c = in.read();
        }
        int result = 0;
        while (c >= '0' && c <= '9') {
            result = result * DECIMAL + c - '0';
            c = in.read();
        }
        return result;
    }

    static boolean fits(int x, int y, int base) {
        // Match the subsequence starting with the least significant digit.
        int wanted = y % base;
        while (x > y) {
            int digit = x % base;
            x /= base;
            if (digit == wanted) {
                y /= base;
                if (y == 0) {
                    return true;
                }
                wanted = y % base;
            }
        }
        return x == y;
    }

    static int answer(int x, int y) {
        int base = 2;
        for (; base * base <= x; base++) {
            if (fits(x, y, base)) {
                return base;
            }
        }
        int best = x + 1;
        int low = Math.max(base, x / (y + 1) + 1);
        if (low <= x / y) {
            best = low;
        }
        int difference = x - y;
        // Larger divisors of the complement correspond to smaller bases.
        for (int d = difference / Math.max(base, y + 1); d > 0; d--) {
            if (difference % d == 0) {
                best = Math.min(best, difference / d);
                break;
            }
        }
        return best <= x ? best : 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int best = answer(number(in), number(in));
        if (best == 0) {
            System.out.println("No solution");
        } else {
            System.out.println(best);
        }
    }
}
