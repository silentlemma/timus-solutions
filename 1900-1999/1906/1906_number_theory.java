import java.io.BufferedInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class Main {
    private static final long MAX_VALUE = 1000000000L;

    private static long gcd(long a, long b) {
        while (b != 0) {
            long remainder = a % b;
            a = b;
            b = remainder;
        }
        return Math.abs(a);
    }

    private static long[] extendedGcd(long a, long b) {
        long x = 1;
        long nextX = 0;
        long y = 0;
        long nextY = 1;
        while (b != 0) {
            long quotient = a / b;
            long remainder = a - quotient * b;
            a = b;
            b = remainder;
            long value = x - quotient * nextX;
            x = nextX;
            nextX = value;
            value = y - quotient * nextY;
            y = nextY;
            nextY = value;
        }
        return new long[] {a, x, y};
    }

    private static long largestModulus(long d, long e, long constraint) {
        if (e % gcd(d, constraint) == 0) {
            return constraint;
        }
        long common = gcd(constraint, e);
        long remaining = constraint / common;
        long forbidden = d / gcd(d, e);
        while (true) {
            long divisor = gcd(remaining, forbidden);
            if (divisor == 1) {
                return common * remaining;
            }
            remaining /= divisor;
        }
    }

    private static long[] witness(int length, long d, long e, long constraint) {
        long modulus = constraint == 0 ? d * MAX_VALUE + 1 : largestModulus(d, e, constraint);
        long common = gcd(d, modulus);
        long reduced = modulus / common;
        long multiplier = 0;
        if (reduced != 1) {
            BigInteger mod = BigInteger.valueOf(reduced);
            BigInteger inverse = BigInteger.valueOf(d / common).modInverse(mod);
            multiplier = BigInteger.valueOf(e / common).multiply(inverse).mod(mod).longValueExact();
        }
        return new long[] {length, modulus, multiplier};
    }

    private static long[] solve(long[] values) {
        int n = values.length;
        if (values[0] == 0) {
            int length = 0;
            while (length < n && values[length] == 0) {
                length++;
            }
            return new long[] {length, 1, 0};
        }
        if (n == 1) {
            return new long[] {1, values[0] + 1, 0};
        }
        long d = values[0];
        long e = values[1];
        long constraint = 0;
        long largest = Math.max(d, e);
        int length = 2;
        for (int index = 1; index < n - 1; index++) {
            long a = values[index];
            long b = values[index + 1];
            if (a == 0) {
                if (b != 0) {
                    break;
                }
                length = index + 2;
                continue;
            }
            long divisor = gcd(d, a);
            BigInteger nextE = BigInteger.valueOf(e);
            if (divisor != d) {
                long[] coefficients = extendedGcd(d, a);
                nextE = BigInteger.valueOf(coefficients[1]).multiply(BigInteger.valueOf(e))
                    .add(BigInteger.valueOf(coefficients[2]).multiply(BigInteger.valueOf(b)));
            }
            BigInteger determinant = BigInteger.valueOf(d / divisor).multiply(BigInteger.valueOf(b))
                .subtract(BigInteger.valueOf(a / divisor).multiply(BigInteger.valueOf(e)));
            long nextConstraint = BigInteger.valueOf(constraint).gcd(determinant).longValueExact();
            if (nextConstraint != 0) {
                nextE = nextE.mod(BigInteger.valueOf(nextConstraint));
            }
            long nextValue = nextE.longValueExact();
            long nextLargest = Math.max(largest, b);
            if (nextConstraint != 0
                && largestModulus(divisor, nextValue, nextConstraint) <= nextLargest) {
                break;
            }
            d = divisor;
            e = nextValue;
            constraint = nextConstraint;
            largest = nextLargest;
            length = index + 2;
        }
        return witness(length, d, e, constraint);
    }

    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        int next() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c >= 0);
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.next();
        long[] values = new long[count];
        for (int i = 0; i < count; i++) {
            values[i] = input.next();
        }
        long[] answer = solve(values);
        System.out.println(answer[0] + " " + answer[1] + " " + answer[2]);
    }
}
