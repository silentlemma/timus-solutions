import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    static final int BITS = 128;
    static final int HALF = 64;
    static final int WORD = 32;
    static final long MASK = 0xFFFFFFFFL;
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");

    static long next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(in.readLine());
        return Long.parseLong(words.nextToken());
    }

    public static void main(String[] args) throws IOException {
        int n = (int)next();
        long[] hi = new long[n], lo = new long[n];
        for (int i = 0; i < n; i++) {
            long w1 = next(), w2 = next(), w3 = next(), w4 = next();
            hi[i] = w1 << WORD | w2;
            lo[i] = w3 << WORD | w4;
        }
        // a number of bit length L is at least every power of ten that is
        // shorter, and at least the one power of length L only if it reaches it
        int[] base = new int[BITS + 1];
        boolean[] has = new boolean[BITS + 1];
        long[] limitHi = new long[BITS + 1], limitLo = new long[BITS + 1];
        for (BigInteger p = BigInteger.TEN; p.bitLength() <= BITS; p = p.multiply(BigInteger.TEN)) {
            int len = p.bitLength();
            has[len] = true;
            limitHi[len] = p.shiftRight(HALF).longValue();
            limitLo[len] = p.longValue();
            for (int l = len + 1; l <= BITS; l++)
                base[l]++;
        }
        long total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long xh = hi[i] ^ hi[j], xl = lo[i] ^ lo[j];
                int len = xh != 0 ? BITS - Long.numberOfLeadingZeros(xh)
                                  : HALF - Long.numberOfLeadingZeros(xl);
                total += base[len];
                if (has[len]) {
                    int c = Long.compareUnsigned(xh, limitHi[len]);
                    if (c > 0 || (c == 0 && Long.compareUnsigned(xl, limitLo[len]) >= 0))
                        total++;
                }
            }
        }
        System.out.println(2 * total); // every pair counts in both orders
    }
}
