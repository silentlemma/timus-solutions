import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static long readLong(BufferedInputStream input) throws IOException {
        int character = input.read();
        while (character >= 0 && character <= ' ') {
            character = input.read();
        }
        long value = 0;
        while (character >= '0' && character <= '9') {
            value = value * 10 + character - '0';
            character = input.read();
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

    private static long inverse(long value, long modulus) {
        long remainder = modulus;
        long coefficient = 1;
        long nextCoefficient = 0;
        while (remainder != 0) {
            long quotient = value / remainder;
            long nextRemainder = value - quotient * remainder;
            value = remainder;
            remainder = nextRemainder;
            long next = coefficient - quotient * nextCoefficient;
            coefficient = nextCoefficient;
            nextCoefficient = next;
        }
        return Math.floorMod(coefficient, modulus);
    }

    private static long visits(long a, long b, long x, long y, long n) {
        if (x <= a || y <= b) {
            return n;
        }
        long divisorA = gcd(a, x);
        long divisorB = gcd(b, y);
        long periodA = x / divisorA;
        long periodB = y / divisorB;
        long eventsA = a / divisorA;
        long eventsB = b / divisorB;
        long common = gcd(periodA, periodB);
        long modulus = periodB / common;
        long multiplier = inverse(periodA / common, modulus);
        long period = periodA * modulus;
        long answer = (n * a + x - 1) / x + (n * b + y - 1) / y;

        // Purchase indices are floor(j * period / events), starting with index zero.
        for (long i = 0; i < eventsA; i++) {
            long first = i * periodA / eventsA;
            for (long j = 0; j < eventsB; j++) {
                long second = j * periodB / eventsB;
                long difference = second - first;
                if (difference % common != 0) {
                    continue;
                }
                // CRT gives one shared purchase index per common period.
                long shift = Math.floorMod(difference / common * multiplier, modulus);
                long start = first + periodA * shift;
                if (start < n) {
                    answer -= 1 + (n - 1 - start) / period;
                }
            }
        }
        return answer;
    }

    public static void main(String[] arguments) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        long a = readLong(input);
        long b = readLong(input);
        long x = readLong(input);
        long y = readLong(input);
        long n = readLong(input);
        System.out.println(visits(a, b, x, y, n));
    }
}
