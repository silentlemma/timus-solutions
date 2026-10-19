import java.util.Scanner;

public class Main {
    static final long MOD = 1_000_000_007L;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // F_n is the product of k^fib(n - k + 1) over k from 1 to n, with
        // fib(1) = fib(2) = 1; weight[k] = fib(n - k + 1) modulo MOD
        long[] fib = new long[n + 2];
        fib[1] = 1;
        for (int i = 2; i <= n + 1; i++) {
            fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
        }
        long[] weight = new long[n + 1];
        for (int k = 1; k <= n; k++) {
            weight[k] = fib[n - k + 1];
        }
        boolean[] composite = new boolean[n + 1];
        // the exponent of a prime p sums the weights of the multiples of p,
        // of p^2, and so on; the divisors number the product of exponents
        // plus 1
        long answer = 1;
        for (int p = 2; p <= n; p++) {
            if (composite[p]) {
                continue;
            }
            for (long q = (long) p * p; q <= n; q += p) {
                composite[(int) q] = true;
            }
            long exponent = 0;
            for (long power = p; power <= n; power *= p) {
                for (long k = power; k <= n; k += power) {
                    exponent += weight[(int) k];
                }
                exponent %= MOD;
            }
            answer = answer * ((exponent + 1) % MOD) % MOD;
        }
        System.out.println(answer);
    }
}
