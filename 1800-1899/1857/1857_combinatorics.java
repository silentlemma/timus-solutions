import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int n = in.nextInt();
        List<Integer> primes = new ArrayList<>();
        int rest = n;
        for (int p = 2; p * p <= rest; p++) {
            if (rest % p == 0) {
                primes.add(p);
                while (rest % p == 0) {
                    rest /= p;
                }
            }
        }
        if (rest > 1) {
            primes.add(rest);
        }
        // keys up to rotation without a shorter period are Lyndon words: by
        // Moebius inversion n times their number is the sum over square-free
        // divisors d of n of mu(d) a^(n / d)
        BigInteger total = BigInteger.ZERO;
        for (int mask = 0; mask < 1 << primes.size(); mask++) {
            int d = 1;
            boolean negative = false;
            for (int i = 0; i < primes.size(); i++) {
                if ((mask >> i & 1) == 1) {
                    d *= primes.get(i);
                    negative = !negative;
                }
            }
            BigInteger term = BigInteger.valueOf(a).pow(n / d);
            total = negative ? total.subtract(term) : total.add(term);
        }
        System.out.println(total.divide(BigInteger.valueOf(n)));
    }
}
