import java.util.Scanner;

public class Main {
    static final long MOD = 1000000007;

    static long power(long base, long exp) {
        long result = 1;
        base %= MOD;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
        }
        return result;
    }

    static long[] fact;
    static long[] inv;

    static long choose(int a, int b) {
        return fact[a] * inv[b] % MOD * inv[a - b] % MOD;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m = in.nextInt();
        int n = in.nextInt();
        int k = in.nextInt();
        int l = in.nextInt();
        int top = Math.max(m, n);
        fact = new long[top + 1];
        inv = new long[top + 1];
        fact[0] = 1;
        for (int i = 1; i <= top; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        inv[top] = power(fact[top], MOD - 2);
        for (int i = top; i > 0; i--) {
            inv[i - 1] = inv[i] * i % MOD;
        }
        // the other a x b cells must leave no row and no column empty. With j of
        // the b columns forced empty, each of the a rows is any nonzero pattern
        // on the rest; inclusion-exclusion over j, along the shorter side
        int a = Math.min(m - k, n - l);
        int b = Math.max(m - k, n - l);
        long rest = 0;
        for (int j = 0; j <= a; j++) {
            long term = choose(a, j) * power((power(2, a - j) - 1 + MOD) % MOD, b) % MOD;
            rest = (rest + (j % 2 == 1 ? MOD - term : term)) % MOD;
        }
        System.out.println(choose(m, k) * choose(n, l) % MOD * rest % MOD);
    }
}
