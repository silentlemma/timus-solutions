import java.util.*;

public class Main {
    static final int CHUNK = 2; // bits of b taken at a time in mulmod
    static final long MASK = 3; // the low CHUNK bits
    static final int MASK_INT = 3;
    static final long GOLDEN = 0x9E3779B97F4A7C15L; // multiplicative hashing
    static final int HASH_SHIFT = 32; // the high half of the product makes the slot
    static final int TOP = 62;  // the highest even bit position a 60-bit number needs

    static final long[] times = new long[MASK_INT + 1]; // 0, a, 2 a and 3 a

    // a b mod m for a, b < m < 2^60: with two bits of b at a time, r 4 + a 3
    // stays below 7 m < 2^63, and three subtractions bring it back below m
    // (no long division: it is slow on a 32-bit JVM)
    static long mulmod(long a, long b, long m) {
        times[1] = a;
        times[2] = a << 1;
        times[MASK_INT] = (a << 1) + a;
        long m2 = m << 1, m4 = m << 2;
        long r = 0;
        for (int shift = TOP; shift >= 0; shift -= CHUNK) {
            r = (r << CHUNK) + times[(int)((b >>> shift) & MASK)];
            if (r >= m4)
                r -= m4;
            if (r >= m2)
                r -= m2;
            if (r >= m)
                r -= m;
        }
        return r;
    }

    static long power(long b, long e, long m) {
        long r = 1 % m;
        for (b %= m; e > 0; e >>= 1, b = mulmod(b, b, m))
            if ((e & 1) == 1)
                r = mulmod(r, b, m);
        return r;
    }

    // the x in [0, q) with g^x = y modulo p, where g has order q: baby steps
    // g^j for j < m in a table of plain arrays (0, never a power of g, marks
    // an empty slot), then giant steps y g^(-m i)
    static long discreteLog(long g, long y, long p, long q) {
        long m = (long)Math.sqrt((double)q) + 1;
        int size = Integer.highestOneBit((int)m) << 2;
        long[] keys = new long[size];
        int[] vals = new int[size];
        long cur = 1;
        for (int j = 0; j < m; j++) {
            int h = slot(cur, size);
            while (keys[h] != 0 && keys[h] != cur)
                h = (h + 1) & (size - 1);
            if (keys[h] == 0) {
                keys[h] = cur;
                vals[h] = j;
            }
            cur = mulmod(cur, g, p);
        }
        long step = power(g, (q - m % q) % q, p); // g^(-m), since g^q = 1
        cur = y % p;
        for (long i = 0; i <= m; i++) {
            for (int h = slot(cur, size); keys[h] != 0; h = (h + 1) & (size - 1))
                if (keys[h] == cur)
                    return (i * m + vals[h]) % q;
            cur = mulmod(cur, step, p);
        }
        return 0;
    }

    static int slot(long key, int size) {
        long h = key * GOLDEN;
        return (int)(h >>> HASH_SHIFT) & (size - 1);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextLong())
            return;
        long nBits = in.nextLong(), lBits = in.nextLong();
        long q = in.nextLong(), p = in.nextLong(), g = in.nextLong(), y = in.nextLong();
        long h = in.nextLong();
        // the hash is fixed, so the signature needs the secret key x itself
        long x = discreteLog(g, y, p, q);
        for (long k = 1;; k++) {
            long r = power(g, k, p) % q;
            if (r == 0)
                continue;
            // q is prime, so k^(q-2) is the inverse of k
            long s = mulmod(power(k, q - 2, q), (h + mulmod(x, r, q)) % q, q);
            if (s != 0) {
                System.out.println(r + " " + s);
                return;
            }
        }
    }
}
