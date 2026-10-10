import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    static final long BASE = 10, ELEVEN = 11;

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        TreeSet<Long> found = new TreeSet<>();
        // strike digit d at place k from x = (a * 10 + d) * 10^k + b with
        // b < 10^k: then y = a * 10^k + b and x + y = (11a + d) * 10^k + 2b
        for (long power = 1; power <= n; power *= BASE) {
            for (long carry = 0; carry < 2; carry++) {
                long twice = n % power + carry * power;
                if (twice % 2 == 0 && twice / 2 < power) {
                    long b = twice / 2, q = (n - twice) / power;
                    long a = q / ELEVEN, d = q % ELEVEN;
                    long x = (a * BASE + d) * power + b;
                    // x has at least two digits and starts with a nonzero
                    // digit
                    if (d < BASE && x >= BASE && (a > 0 || d > 0)) {
                        found.add(x);
                    }
                }
            }
        }
        StringBuilder out = new StringBuilder().append(found.size()).append('\n');
        for (long x : found) {
            int width = Long.toString(x).length() - 1;
            out.append(String.format("%d + %0" + width + "d = %d%n", x, n - x, n));
        }
        System.out.print(out);
    }
}
