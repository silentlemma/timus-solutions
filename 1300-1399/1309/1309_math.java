import java.util.*;

public class Main {
    static final long MOD = 9973;
    static final long COEF_X = 3, COEF_Y = 7;

    // g(x, y) = y (x^5 - x + 7) + (x^3 + 3x - x^5) is the map y -> a y + b
    // modulo 9973, and it depends only on x mod 9973
    static long[] step(long x) {
        long x3 = x * x % MOD * x % MOD, x5 = x3 * x % MOD * x % MOD;
        return new long[] {Math.floorMod(x5 - x + COEF_Y, MOD),
                           Math.floorMod(x3 + COEF_X * x - x5, MOD)};
    }

    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        long whole = n / MOD, rest = n % MOD;
        // x = 1 .. 9973 compose into one map, the same for every full period
        long bigA = 1, bigB = 0;
        for (long x = 1; x <= MOD; x++) {
            long[] ab = step(x);
            bigB = (ab[0] * bigB + ab[1]) % MOD;
            bigA = ab[0] * bigA % MOD;
        }
        long y = 0;
        for (long k = 0; k < whole; k++)
            y = (bigA * y + bigB) % MOD;
        for (long x = 1; x <= rest; x++) {
            long[] ab = step(x);
            y = (ab[0] * y + ab[1]) % MOD;
        }
        System.out.println(y);
    }
}
