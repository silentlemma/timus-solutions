import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int QUARTIC = 5; // coefficients of a degree-4 polynomial
    static final long DISCRIMINANT = 4; // t^2 - at + e has discriminant a^2 - 4e

    // the positive and negative divisors of v != 0
    static List<Long> divisors(long v) {
        v = Math.abs(v);
        List<Long> out = new ArrayList<>();
        for (long d = 1; d * d <= v; d++) {
            if (v % d == 0) {
                out.add(d);
                out.add(-d);
                out.add(v / d);
                out.add(-(v / d));
            }
        }
        return out;
    }

    static long value(long[] poly, long x) {
        long result = 0;
        for (long c : poly) {
            result = result * x + c;
        }
        return result;
    }

    // an integer root of a monic polynomial, or null: it divides the constant term
    static Long root(long[] poly) {
        long constant = poly[poly.length - 1];
        if (constant == 0) {
            return 0L;
        }
        for (long d : divisors(constant)) {
            if (value(poly, d) == 0) {
                return d;
            }
        }
        return null;
    }

    static long exactRoot(long v) {
        long s = (long) Math.sqrt((double) v);
        while (s * s > v) {
            s--;
        }
        while ((s + 1) * (s + 1) <= v) {
            s++;
        }
        return s;
    }

    // (x^2 + px + q)(x^2 + rx + s) with qs = d, p + r = a, q + s + pr = b,
    // ps + qr = c; null if there is no such split
    static long[][] quadratics(long[] poly) {
        long a = poly[1];
        long b = poly[2];
        long c = poly[QUARTIC - 2];
        long d = poly[QUARTIC - 1];
        for (long q : divisors(d)) {
            long s = d / q;
            long p;
            if (q != s) {
                if ((c - a * q) % (s - q) != 0) {
                    continue;
                }
                p = (c - a * q) / (s - q);
            } else {
                // then p and r are the roots of t^2 - at + (b - 2q)
                long disc = a * a - DISCRIMINANT * (b - 2 * q);
                if (disc < 0) {
                    continue;
                }
                long root = exactRoot(disc);
                if (root * root != disc || (a + root) % 2 != 0) {
                    continue;
                }
                p = (a + root) / 2;
            }
            long r = a - p;
            if (q + s + p * r == b && p * s + q * r == c) {
                return new long[][] {{1, p, q}, {1, r, s}};
            }
        }
        return null;
    }

    static String show(long[] poly) {
        int deg = poly.length - 1;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i <= deg; i++) {
            long c = poly[i];
            if (c == 0) {
                continue;
            }
            int power = deg - i;
            if (c < 0) {
                out.append('-');
            } else if (out.length() > 0) {
                out.append('+');
            }
            if (Math.abs(c) != 1 || power == 0) {
                out.append(Math.abs(c));
            }
            if (power > 0) {
                out.append('x');
            }
            if (power > 1) {
                out.append(power);
            }
        }
        return "(" + out + ")";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long[] poly = new long[QUARTIC];
        poly[0] = 1;
        for (int i = 1; i < QUARTIC; i++) {
            poly[i] = in.nextLong();
        }
        List<long[]> factors = new ArrayList<>();
        Long r;
        while (poly.length > 2 && (r = root(poly)) != null) {
            factors.add(new long[] {1, -r});
            long[] quotient = new long[poly.length - 1];
            quotient[0] = 1;
            for (int i = 1; i < quotient.length; i++) {
                quotient[i] = poly[i] + r * quotient[i - 1];
            }
            poly = quotient;
        }
        if (poly.length == QUARTIC) {
            long[][] split = quadratics(poly);
            if (split == null) {
                System.out.println("Irreducible");
                return;
            }
            factors.add(split[0]);
            factors.add(split[1]);
        } else if (poly.length > 1) {
            factors.add(poly);
        }
        StringBuilder out = new StringBuilder();
        for (long[] f : factors) {
            out.append(show(f));
        }
        System.out.println(out);
    }
}
