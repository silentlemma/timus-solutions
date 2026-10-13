import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // a[k]: rooted trees with k vertices; s[k]: the sum of d a[d] over divisors d of k
        BigInteger[] a = new BigInteger[n + 1], s = new BigInteger[n + 1];
        a[1] = s[1] = BigInteger.ONE;
        for (int m = 1; m < n; m++) {
            // a(m + 1) = (s(1) a(m) + s(2) a(m - 1) + ... + s(m) a(1)) / m
            BigInteger total = BigInteger.ZERO;
            for (int k = 1; k <= m; k++)
                total = total.add(s[k].multiply(a[m - k + 1]));
            a[m + 1] = total.divide(BigInteger.valueOf(m));
            s[m + 1] = BigInteger.ZERO;
            for (int d = 1; d <= m + 1; d++)
                if ((m + 1) % d == 0)
                    s[m + 1] = s[m + 1].add(BigInteger.valueOf(d).multiply(a[d]));
        }
        System.out.println(a[n]);
    }
}
