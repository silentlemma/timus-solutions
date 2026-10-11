import java.util.*;

public class Main {
    static final int MOD = 100;
    static final int BASES = 4;
    static final int TEN = 10;

    static int power(int base, int n) {
        int r = 1;
        for (; n > 0; n >>= 1, base = base * base % MOD) {
            if ((n & 1) == 1)
                r = r * base % MOD;
        }
        return r;
    }

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // from the second power on the sum is even but never divisible by 8,
        // so it ends in at most two zeros and its remainder mod 100 decides
        int s = 0;
        for (int b = 1; b <= BASES; b++)
            s = (s + power(b, n)) % MOD;
        System.out.println(s == 0 ? 2 : s % TEN == 0 ? 1 : 0);
    }
}
