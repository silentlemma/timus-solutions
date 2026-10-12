import java.util.Scanner;

public class Main {
    static final int DIGITS = 12;
    static final long[] BASES = {2, 3, 5, 7, 11, 13}; // enough for every number below 3 * 10^12
    static final int HALF = 20;
    static final long LOW = (1L << HALF) - 1;

    // a * b mod n for n below 2^40: b is split into 20-bit halves so that no
    // product passes 2^60
    static long mulmod(long a, long b, long n) {
        long high = a * (b >> HALF) % n;
        return ((high << HALF) % n + a * (b & LOW)) % n;
    }

    static long powmod(long a, long e, long n) {
        long r = 1;
        for (a %= n; e > 0; e >>= 1, a = mulmod(a, a, n)) {
            if ((e & 1) == 1)
                r = mulmod(r, a, n);
        }
        return r;
    }

    // Miller-Rabin with fixed bases, exact for all 12-digit numbers
    static boolean isPrime(long n) {
        if (n < 2)
            return false;
        for (long p : BASES) {
            if (n % p == 0)
                return n == p;
        }
        long d = n - 1;
        int s = 0;
        for (; d % 2 == 0; d /= 2)
            s++;
        for (long a : BASES) {
            long x = powmod(a, d, n);
            boolean witness = x != 1 && x != n - 1;
            for (int i = 1; i < s && witness; i++) {
                x = mulmod(x, x, n);
                witness = x != n - 1;
            }
            if (witness)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        StringBuilder digits = new StringBuilder();
        while (in.hasNext())
            digits.append(in.next()); // the digits, together or apart
        String prefix = digits.substring(0, Math.min(count, digits.length()));
        long number = prefix.isEmpty() ? 0 : Long.parseLong(prefix);
        for (int i = count; i < DIGITS; i++)
            number *= 10;
        if (count < DIGITS) {
            while (!isPrime(number))
                number++;
        }
        System.out.println(String.format("%0" + DIGITS + "d", number));
    }
}
