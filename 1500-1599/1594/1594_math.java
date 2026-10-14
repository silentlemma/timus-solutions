import java.util.*;

public class Main {
    static final long MOD = 1000000007;

    static long power(long b, long e) {
        long r = 1;
        for (b %= MOD; e > 0; e >>= 1, b = b * b % MOD)
            if ((e & 1) == 1)
                r = r * b % MOD;
        return r;
    }

    // monic polynomial, lowest coefficient first, whose roots are
    // 4 cos^2(j pi / (m + 1)) for j = 1 .. ceil(m / 2)
    static long[] rootsPoly(int m) {
        // S_k(x) = U_k(x / 2) grows by S_(k+1) = x S_k - S_(k-1) from S_0 = 1 and
        // S_1 = x, and its roots are 2 cos(j pi / (m + 1)) for j = 1 .. m
        long[] prev = {1}, cur = {0, 1};
        for (int k = 1; k < m; k++) {
            long[] next = new long[cur.length + 1];
            System.arraycopy(cur, 0, next, 1, cur.length);
            for (int i = 0; i < prev.length; i++)
                next[i] = (next[i] - prev[i] + MOD) % MOD;
            prev = cur;
            cur = next;
        }
        // the roots come in pairs +-x, plus 0 when m is odd, so an extra factor x
        // when m is odd makes every power even, and x^2 -> y keeps one per pair
        int shift = m % 2;
        long[] result = new long[(cur.length + shift + 1) / 2];
        for (int i = 0; i < result.length; i++) {
            int from = 2 * i - shift;
            result[i] = from >= 0 ? cur[from] : 0;
        }
        return result;
    }

    static long det(long[][] a) {
        int size = a.length;
        long result = 1;
        for (int col = 0; col < size; col++) {
            int pivot = col;
            while (pivot < size && a[pivot][col] == 0)
                pivot++;
            if (pivot == size)
                return 0;
            if (pivot != col) {
                long[] t = a[pivot];
                a[pivot] = a[col];
                a[col] = t;
                result = (MOD - result) % MOD;
            }
            result = result * a[col][col] % MOD;
            long inv = power(a[col][col], MOD - 2);
            for (int r = col + 1; r < size; r++) {
                long f = a[r][col] * inv % MOD;
                if (f == 0)
                    continue;
                for (int c = col; c < size; c++)
                    a[r][c] = ((a[r][c] - f * a[col][c]) % MOD + MOD) % MOD;
            }
        }
        return result;
    }

    // Res(p, q) as the determinant of the Sylvester matrix
    static long resultant(long[] p, long[] q) {
        int d = p.length - 1, e = q.length - 1, size = d + e;
        long[][] rows = new long[size][size];
        for (int i = 0; i < e; i++)
            for (int k = 0; k <= d; k++)
                rows[i][i + k] = p[d - k];
        for (int i = 0; i < d; i++)
            for (int k = 0; k <= e; k++)
                rows[e + i][i + k] = q[e - k];
        return det(rows);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextInt())
            return;
        int m = in.nextInt(), n = in.nextInt();
        // Kasteleyn: the number of tilings is the product of a_j + b_k over the
        // roots a_j of rootsPoly(m) and b_k of rootsPoly(n), which is the
        // resultant of the first with the monic polynomial whose roots are -b_k
        long[] p = rootsPoly(m), q = rootsPoly(n);
        // (-1)^e q(-y) is monic with roots -b_k: coefficient i gets (-1)^(e - i)
        int e = q.length - 1;
        for (int i = 0; i <= e; i++)
            if ((e - i) % 2 == 1)
                q[i] = (MOD - q[i]) % MOD;
        System.out.println(resultant(p, q));
    }
}
