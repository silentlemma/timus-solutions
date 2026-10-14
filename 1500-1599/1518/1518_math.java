import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static long y;
    static int[] steps; // the j with C[n + 1 - j] = 1

    // p * q modulo the characteristic polynomial and y
    static long[] times(long[] p, long[] q) {
        long[] prod = new long[2 * n - 1];
        for (int i = 0; i < n; i++)
            if (p[i] != 0)
                for (int j = 0; j < n; j++)
                    prod[i + j] = (prod[i + j] + p[i] * q[j]) % y;
        // x^n is the sum of x^(n - j) over the steps
        for (int d = 2 * n - 2; d >= n; d--)
            if (prod[d] != 0)
                for (int j : steps)
                    prod[d - j] = (prod[d - j] + prod[d]) % y;
        return Arrays.copyOf(prod, n);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        n = (int)in.nval;
        in.nextToken();
        long x = (long)in.nval;
        in.nextToken();
        y = (long)in.nval;
        long[] keys = new long[n];
        int[] shifts = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            keys[i] = (long)in.nval;
        }
        for (int i = 0; i < n; i++) {
            in.nextToken();
            shifts[i] = (int)in.nval;
        }
        // K[i] = sum of K[i - j] * C[n + 1 - j] over j = 1 ... n
        List<Integer> list = new ArrayList<>();
        for (int j = 1; j <= n; j++)
            if (shifts[n - j] == 1)
                list.add(j);
        steps = list.stream().mapToInt(Integer::intValue).toArray();
        // K[x] is the x - 1 st term counting from K[1], and the coefficients of
        // x^(x - 1) reduced modulo the characteristic polynomial weigh K[1 ... n]
        long[] result = new long[n], base = new long[n];
        result[0] = 1;
        if (n > 1)
            base[1] = 1;
        else
            base[0] = shifts[0] % y;
        for (long e = x - 1; e > 0; e >>= 1) {
            if ((e & 1) == 1)
                result = times(result, base);
            base = times(base, base);
        }
        long answer = 0;
        for (int i = 0; i < n; i++)
            answer = (answer + result[i] * (keys[i] % y)) % y;
        System.out.println(answer);
    }
}
