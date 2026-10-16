import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final long MOD = 1000000007;

    // a 2 x 2 matrix rows first: a b / c d
    static final class Matrix {
        final long a, b, c, d;

        Matrix(long a, long b, long c, long d) {
            this.a = a;
            this.b = b;
            this.c = c;
            this.d = d;
        }
    }

    static Matrix mul(Matrix x, Matrix y) {
        return new Matrix((x.a * y.a + x.b * y.c) % MOD, (x.a * y.b + x.b * y.d) % MOD,
            (x.c * y.a + x.d * y.c) % MOD, (x.c * y.b + x.d * y.d) % MOD);
    }

    // [p_k p_(k-1); q_k q_(k-1)] grows by the factor [a 1; 1 0]
    static Matrix term(long a) {
        return new Matrix(a % MOD, 1, 1, 0);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long x = in.nextLong(), k = in.nextLong();
        long a0 = (long) Math.sqrt((double) x);
        while (a0 * a0 > x) a0--;
        while ((a0 + 1) * (a0 + 1) <= x) a0++;
        // the partial quotients of sqrt(x) repeat with a period that ends at
        // the first term equal to 2 a0
        List<Long> period = new ArrayList<>();
        long m = 0, d = 1, a = a0;
        while (a != 2 * a0) {
            m = d * a - m;
            d = (x - m * m) / d;
            a = (a0 + m) / d;
            period.add(a);
        }
        Matrix cycle = new Matrix(1, 0, 0, 1);
        for (long v : period) cycle = mul(cycle, term(v));
        Matrix result = term(a0), power = cycle;
        long length = period.size();
        for (long full = k / length; full > 0; full >>= 1) {
            if ((full & 1) == 1) result = mul(result, power);
            power = mul(power, power);
        }
        for (int i = 0; i < k % length; i++) result = mul(result, term(period.get(i)));
        // convergents are always in lowest terms
        System.out.println(result.a + "/" + result.c);
    }
}
