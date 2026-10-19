import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static final long MOD = 1_000_000_007L;

    public static void main(String[] args) {
        long level = new Scanner(System.in).nextLong();
        // the numbers form a perfect binary tree, and the mole walks the
        // tree distance; summing over every edge the nodes below it times the
        // nodes above it gives 2^l ((l - 1)(2^l + 1) - 2 (2^l - 2))
        BigInteger modulus = BigInteger.valueOf(MOD);
        long power = BigInteger.valueOf(2).modPow(BigInteger.valueOf(level), modulus).longValue();
        long l = level % MOD;
        long inner = ((l - 1 + MOD) % MOD * ((power + 1) % MOD) % MOD
                - 2 * ((power - 2 + MOD) % MOD) % MOD + MOD) % MOD;
        System.out.println(power * inner % MOD);
    }
}
