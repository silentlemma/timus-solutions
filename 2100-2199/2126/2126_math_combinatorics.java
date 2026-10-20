import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final long CHOICES = 3;
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static long readLong() throws IOException {
        int symbol;
        do {
            symbol = INPUT.read();
        } while (symbol <= ' ' && symbol != -1);
        long value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = INPUT.read();
        }
        return value;
    }

    private static long power(long base, long exponent, long modulus) {
        long result = 1;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                result = result * base % modulus;
            }
            base = base * base % modulus;
            exponent /= 2;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        long n = readLong();
        long modulus = readLong();
        long half = (modulus - 1) / 2;
        long exponent = 0;
        long[] digits = new long[Long.SIZE];
        int count = 0;
        for (long remaining = n; remaining > 0; remaining /= modulus) {
            long digit = remaining % modulus;
            // Reflect central trinomial coefficients into the lower half.
            if (digit > half) {
                digit = modulus - 1 - digit;
                exponent += half - digit;
            }
            digits[count++] = digit;
        }
        Arrays.sort(digits, 0, count);

        long index = 0;
        long previous = 1;
        long current = 1;
        long factorial = 1;
        long numerator = 1;
        long denominator = 1;
        for (int position = 0; position < count; ++position) {
            while (index < digits[position]) {
                ++index;
                long before = index - 1;
                // F_i = i! * T_i avoids division inside the recurrence.
                long next = ((2 * index - 1) * current
                        + CHOICES * before * before * previous) % modulus;
                previous = current;
                current = next;
                factorial = factorial * index % modulus;
            }
            numerator = numerator * current % modulus;
            denominator = denominator * factorial % modulus;
        }

        long draws = numerator * power(denominator, modulus - 2, modulus) % modulus;
        draws = draws * power(modulus - CHOICES, exponent, modulus) % modulus;
        long total = power(CHOICES, n, modulus);
        long answer = (total - draws + modulus) % modulus * ((modulus + 1) / 2) % modulus;
        System.out.println(answer);
    }
}
