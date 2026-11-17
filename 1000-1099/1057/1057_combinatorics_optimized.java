import java.io.IOException;
import java.io.InputStream;

public class Main {
    static final int DECIMAL = 10;

    static int readNumber(InputStream input) throws IOException {
        int ch;
        do {
            ch = input.read();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    static int choose(int size, int count) {
        if (count < 0 || count > size) {
            return 0;
        }
        long result = 1;
        for (int i = 1; i <= Math.min(count, size - count); i++) {
            result = result * (size + 1 - i) / i;
        }
        return (int)result;
    }

    static int count(int bound, int ones, int base) {
        int power = 1;
        int lower = 0;
        while (power <= bound / base) {
            power *= base;
            lower++;
        }
        int total = 0;
        while (power != 0) {
            int digit = bound / power;
            if (digit > 1) {
                return total + choose(lower + 1, ones);
            }
            if (digit != 0) {
                total += choose(lower, ones);
                if (ones-- == 0) {
                    return total;
                }
            }
            bound %= power;
            power /= base;
            lower--;
        }
        return total + (ones == 0 ? 1 : 0);
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        int lower = readNumber(input);
        int upper = readNumber(input);
        int ones = readNumber(input);
        int base = readNumber(input);
        System.out.println(count(upper, ones, base) - count(lower - 1, ones, base));
    }
}
