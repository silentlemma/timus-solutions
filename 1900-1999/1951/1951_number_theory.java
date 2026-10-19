import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int SIEVE_LIMIT = 10000, LOWER_MODULUS = 5000, MODULUS_COUNT = 510;
    private static final int DECIMAL_BASE = 10;
    private static final long[] MODULI = primeModuli();

    static final class ComplexPair {
        final long real, imaginary;

        ComplexPair(long real, long imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }
    }

    static long[] primeModuli() {
        boolean[] prime = new boolean[SIEVE_LIMIT + 1];
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;
        for (int value = 2; value * value <= SIEVE_LIMIT; ++value) {
            if (prime[value]) {
                for (int multiple = value * value; multiple <= SIEVE_LIMIT; multiple += value)
                    prime[multiple] = false;
            }
        }
        long[] result = new long[MODULUS_COUNT];
        int count = 0;
        for (int value = LOWER_MODULUS; value <= SIEVE_LIMIT && count < MODULUS_COUNT; ++value) {
            if (prime[value])
                result[count++] = value;
        }
        return result;
    }

    static long nextLong(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        boolean negative = symbol == '-';
        if (negative)
            symbol = in.read();
        long value = 0;
        while (symbol >= '0' && symbol <= '9') {
            value = value * DECIMAL_BASE + symbol - '0';
            symbol = in.read();
        }
        return negative ? -value : value;
    }

    static long normalize(long value, long modulus) {
        long remainder = value % modulus;
        return remainder < 0 ? remainder + modulus : remainder;
    }

    static ComplexPair multiply(ComplexPair first, ComplexPair second, long modulus) {
        return new ComplexPair(
            normalize(first.real * second.real - first.imaginary * second.imaginary, modulus),
            normalize(first.real * second.imaginary + first.imaginary * second.real, modulus));
    }

    static ComplexPair power(long real, long imaginary, int exponent, long modulus) {
        ComplexPair base = new ComplexPair(normalize(real, modulus), normalize(imaginary, modulus));
        ComplexPair result = new ComplexPair(1, 0);
        while (exponent > 0) {
            if ((exponent & 1) != 0)
                result = multiply(result, base, modulus);
            base = multiply(base, base, modulus);
            exponent >>= 1;
        }
        return result;
    }

    static int gcd(int first, int second) {
        while (second != 0) {
            int remainder = first % second;
            first = second;
            second = remainder;
        }
        return first;
    }

    static int countRoots(long a, long b, int n, long c, long d, int m) {
        int common = gcd(n, m);
        for (long modulus : MODULI) {
            ComplexPair first = power(a, b, m / common, modulus);
            ComplexPair second = power(c, d, n / common, modulus);
            if (first.real != second.real || first.imaginary != second.imaginary)
                return 0;
        }
        return common;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        long a = nextLong(in), b = nextLong(in);
        int n = (int)nextLong(in);
        long c = nextLong(in), d = nextLong(in);
        int m = (int)nextLong(in);
        System.out.println(countRoots(a, b, n, c, d, m));
    }
}
