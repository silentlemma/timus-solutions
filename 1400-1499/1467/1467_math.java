import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    // an exact fraction p / q with q > 0, kept in lowest terms
    static BigInteger[] frac(BigInteger p, BigInteger q) {
        if (q.signum() < 0) {
            p = p.negate();
            q = q.negate();
        }
        BigInteger g = p.gcd(q);
        return g.signum() == 0 ? new BigInteger[] {p, q}
                               : new BigInteger[] {p.divide(g), q.divide(g)};
    }

    static BigInteger[] add(BigInteger[] a, BigInteger[] b) {
        return frac(a[0].multiply(b[1]).add(b[0].multiply(a[1])), a[1].multiply(b[1]));
    }

    static BigInteger[] scale(BigInteger[] a, BigInteger times, BigInteger over) {
        return frac(a[0].multiply(times), a[1].multiply(over));
    }

    public static void main(String[] args) {
        int k = new Scanner(System.in).nextInt();
        BigInteger[][] comb = new BigInteger[k + 2][k + 2];
        for (int m = 0; m <= k + 1; m++) {
            comb[m][0] = BigInteger.ONE;
            for (int j = 1; j <= m; j++)
                comb[m][j] = comb[m - 1][j - 1].add(j < m ? comb[m - 1][j] : BigInteger.ZERO);
        }
        // Bernoulli numbers with B1 = +1/2: the sum of C(m + 1, j) B_j over
        // j <= m equals m + 1, which gives B_m from the earlier ones
        List<BigInteger[]> bern = new ArrayList<>();
        for (int m = 0; m <= k; m++) {
            BigInteger[] rest = {BigInteger.ZERO, BigInteger.ONE};
            for (int j = 0; j < m; j++)
                rest = add(rest, scale(bern.get(j), comb[m + 1][j], BigInteger.ONE));
            BigInteger size = BigInteger.valueOf(m + 1);
            BigInteger[] left = add(new BigInteger[] {size, BigInteger.ONE},
                                    new BigInteger[] {rest[0].negate(), rest[1]});
            bern.add(scale(left, BigInteger.ONE, size));
        }
        // Faulhaber: the coefficient of N^(k + 1 - j) is C(k + 1, j) B_j / (k + 1)
        StringBuilder out = new StringBuilder();
        for (int j = 0; j <= k; j++) {
            BigInteger[] c = scale(bern.get(j), comb[k + 1][j], BigInteger.valueOf(k + 1));
            out.append(c[0]).append('/').append(c[1]).append(' ');
        }
        out.append("0/1");
        System.out.println(out);
    }
}
