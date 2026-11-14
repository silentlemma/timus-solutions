import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int OFFSET_PRODUCT_DIVISOR = 6;

    private static long number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = input.read();
        }
        return value;
    }

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }

    private static long pairs(long n, long page) {
        long last = n % page;
        return (n / page * page * (page - 1) + last * (last - 1)) / 2;
    }

    private static long answer(long a, long b, long n) {
        long large = Math.max(a, b);
        long small = Math.min(a, b);
        long stride = large % small;
        long loss = 0;
        if (stride != 0) {
            long unit = gcd(large, small);
            long count = small / unit;
            long period = large * count;
            if (period <= n) {
                // The nonzero offsets are the multiples of unit, in some order.
                long perPeriod =
                    unit * unit * count * (count - 1) * (count + 1) / OFFSET_PRODUCT_DIVISOR;
                loss = n / period * perPeriod;
            }
            long tail = n % period;
            for (long cut = large, left = stride; cut < tail; cut += large, left += stride) {
                if (left >= small) {
                    left -= small;
                }
                loss += left * Math.min(small - left, tail - cut);
            }
        }
        return pairs(n, a) - pairs(n, small) + loss;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        System.out.println(answer(number(input), number(input), number(input)));
    }
}
