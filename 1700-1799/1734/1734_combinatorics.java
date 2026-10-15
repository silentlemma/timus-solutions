import java.util.Scanner;

public class Main {
    static final long MOD = 1000000007;
    static final long EDGE_KINDS = 3;
    static final long MIDDLE_KINDS = 4;
    static final long ONE_COLOUR_KINDS = 2;

    static long[] fact, inv;

    static long power(long a, long e) {
        long r = 1;
        for (a %= MOD; e > 0; e >>= 1, a = a * a % MOD) {
            if ((e & 1) == 1) {
                r = r * a % MOD;
            }
        }
        return r;
    }

    static long choose(int a, int b) {
        if (b < 0 || b > a) {
            return 0;
        }
        return fact[a] * inv[b] % MOD * inv[a - b] % MOD;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        int squares = n * n / 2, row = n / 2, middle = squares - 2 * row;
        fact = new long[squares + 1];
        inv = new long[squares + 1];
        fact[0] = 1;
        for (int i = 1; i <= squares; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        inv[squares] = power(fact[squares], MOD - 2);
        for (int i = squares; i > 0; i--) {
            inv[i - 1] = inv[i] * i % MOD;
        }
        // a dark square on the first or last row takes three kinds of piece
        // (the man that would be crowned there is out), any other square four
        long total = 0;
        for (int a = 0; a <= Math.min(2 * row, k); a++) {
            long edge = choose(2 * row, a) * power(EDGE_KINDS, a) % MOD;
            long rest = choose(middle, k - a) * power(MIDDLE_KINDS, k - a) % MOD;
            total = (total + edge * rest) % MOD;
        }
        // positions of one colour: on its last row only the king, elsewhere
        // the man or the king
        long one = 0;
        for (int a = 0; a <= Math.min(row, k); a++) {
            long rest = choose(middle + row, k - a) * power(ONE_COLOUR_KINDS, k - a) % MOD;
            one = (one + choose(row, a) * rest) % MOD;
        }
        System.out.println(((total - 2 * one) % MOD + MOD) % MOD);
    }
}
