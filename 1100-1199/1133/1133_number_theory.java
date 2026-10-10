import java.util.Scanner;

public class Main {
    // a prime above the 4e9 + 1 possible answers and below 2^32, so products
    // fit in 64 unsigned bits; no Fibonacci number with index up to 2000 is
    // divisible by it
    static final long P = 4294967291L;

    static long mul(long x, long y) { return Long.remainderUnsigned(x * y, P); }

    static long power(long b, long e) {
        long r = 1;
        for (; e > 0; e /= 2, b = mul(b, b)) {
            if (e % 2 == 1) {
                r = mul(r, b);
            }
        }
        return r;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long i = in.nextLong(), fi = in.nextLong(), j = in.nextLong(), fj = in.nextLong();
        long n = in.nextLong();
        if (i > j) {
            long t = i;
            i = j;
            j = t;
            t = fi;
            fi = fj;
            fj = t;
        }
        // F(j) = A F(i) + B F(i + 1), with A and B found by stepping coefficients
        long a = 1, b = 0, na = 0, nb = 1;
        for (long k = i; k < j; k++) {
            long sa = (a + na) % P, sb = (b + nb) % P;
            a = na;
            b = nb;
            na = sa;
            nb = sb;
        }
        long cur = Math.floorMod(fi, P);
        long next = mul((Math.floorMod(fj, P) + P - mul(a, cur)) % P, power(b, P - 2));
        for (long k = i; k < n; k++) {
            long s = (cur + next) % P;
            cur = next;
            next = s;
        }
        for (long k = i; k > n; k--) {
            long prev = (next + P - cur) % P;
            next = cur;
            cur = prev;
        }
        System.out.println(cur > P / 2 ? cur - P : cur);
    }
}
