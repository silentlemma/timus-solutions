import java.util.Scanner;

public class Main {
    // the exponent of the prime p in x! (Legendre's formula)
    static long exponent(long x, long p) {
        long e = 0;
        for (; x > 0; x /= p) {
            e += x / p;
        }
        return e;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        boolean[] composite = new boolean[n + 1];
        int count = 0;
        for (int p = 2; p <= n; p++) {
            if (composite[p]) {
                continue;
            }
            for (long q = (long)p * p; q <= n; q += p) {
                composite[(int)q] = true;
            }
            if (exponent(n, p) - exponent(m, p) - exponent(n - m, p) > 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
