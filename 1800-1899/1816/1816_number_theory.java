import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        List<Long> primes = new ArrayList<>();
        List<Integer> exps = new ArrayList<>();
        long rest = n;
        for (long p = 2; p * p <= rest; p++) {
            if (rest % p != 0) continue;
            int e = 0;
            while (rest % p == 0) {
                rest /= p;
                e++;
            }
            primes.add(p);
            exps.add(e);
        }
        if (rest > 1) {
            primes.add(rest);
            exps.add(1);
        }
        // a divisor is its exponent vector, numbered in mixed radix: every
        // proper divisor of a divisor gets a smaller number
        int k = primes.size();
        int[] radix = new int[k + 1];
        radix[0] = 1;
        for (int i = 0; i < k; i++) radix[i + 1] = radix[i] * (exps.get(i) + 1);
        int count = radix[k];
        double[] expected = new double[count];
        for (int index = 0; index < count; index++) {
            int total = 0;
            int[] offsets = {0};
            double[] chances = {1};
            for (int i = 0; i < k; i++) {
                int top = index / radix[i] % (exps.get(i) + 1);
                total += top;
                // gcd(m, r) for a uniform r splits over the primes: the
                // exponent of p in it is b < top with chance (1 - 1/p) / p^b,
                // or top with chance 1/p^top
                double q = primes.get(i);
                int size = offsets.length * (top + 1);
                int[] nextOffsets = new int[size];
                double[] nextChances = new double[size];
                int at = 0;
                for (int j = 0; j < offsets.length; j++) {
                    double scale = 1;
                    for (int b = 0; b <= top; b++) {
                        double factor = b < top ? (1 - 1 / q) / scale : 1 / scale;
                        nextOffsets[at] = offsets[j] + b * radix[i];
                        nextChances[at++] = chances[j] * factor;
                        scale *= q;
                    }
                }
                offsets = nextOffsets;
                chances = nextChances;
            }
            if (total <= 1) continue; // 1 or a prime: no gcd is taken
            int last = offsets.length - 1;
            double stay = chances[0] + chances[last];
            double sum = 1;
            for (int j = 1; j < last; j++) {
                sum += chances[j] * (expected[offsets[j]] + expected[index - offsets[j]]);
            }
            expected[index] = sum / (1 - stay);
        }
        System.out.println(String.format("%.10f", expected[count - 1]));
    }
}
