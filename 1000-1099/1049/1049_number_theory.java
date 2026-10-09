import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final int COUNT = 10, BASE = 10;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // the exponents of the primes in the product of all the numbers
        Map<Integer, Integer> exponent = new HashMap<>();
        for (int i = 0; i < COUNT; i++) {
            int x = in.nextInt();
            for (int p = 2; p * p <= x; p++) {
                for (; x % p == 0; x /= p) {
                    exponent.merge(p, 1, Integer::sum);
                }
            }
            if (x > 1) {
                exponent.merge(x, 1, Integer::sum);
            }
        }
        // a divisor picks each prime from 0 to its exponent times
        int last = 1;
        for (int e : exponent.values()) {
            last = last * (e + 1) % BASE;
        }
        System.out.println(last);
    }
}
