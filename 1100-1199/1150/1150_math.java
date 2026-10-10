import java.util.Scanner;

public class Main {
    static final int DIGITS = 10;

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        long[] count = new long[DIGITS];
        for (long p = 1; p <= n; p *= DIGITS) {
            // at this position the numbers up to n split into the part above,
            // the digit itself and the part below; every smaller upper part
            // repeats each digit p times here
            long high = n / (p * DIGITS), cur = n / p % DIGITS, low = n % p;
            for (int d = 1; d < DIGITS; d++) {
                count[d] += high * p + (d < cur ? p : d == cur ? low + 1 : 0);
            }
            // a zero needs a nonzero digit above it, so the upper part 0 is
            // skipped
            if (high > 0) {
                count[0] += (high - 1) * p + (cur > 0 ? p : low + 1);
            }
        }
        StringBuilder out = new StringBuilder();
        for (long c : count) {
            out.append(c).append('\n');
        }
        System.out.print(out);
    }
}
