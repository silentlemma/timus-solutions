import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Main {
  private static final long SMALL = 50; // small primes: walk the whole sequence
  private static final long FIVE = 5;
  private static final long QUAD = 4; // the discriminant of a y^2 + b y + c is b^2 - 4 a c

  private static long p;

  private static long power(long b, long e) {
    long r = 1;
    for (b %= p; e > 0; e >>= 1, b = b * b % p) if ((e & 1) == 1) r = r * b % p;
    return r;
  }

  // a square root of a modulo the odd prime p, or -1 (Tonelli-Shanks)
  private static long sqrtMod(long a) {
    a %= p;
    if (a == 0) return 0;
    if (power(a, (p - 1) / 2) != 1) return -1;
    long q = p - 1;
    long s = 0;
    while (q % 2 == 0) {
      q /= 2;
      s++;
    }
    long z = 2;
    while (power(z, (p - 1) / 2) != p - 1) z++;
    long m = s;
    long c = power(z, q);
    long t = power(a, q);
    long r = power(a, (q + 1) / 2);
    while (t != 1) {
      long i = 0;
      for (long t2 = t; t2 != 1; t2 = t2 * t2 % p) i++;
      long b = power(c, 1L << (m - i - 1));
      m = i;
      c = b * b % p;
      t = t * c % p;
      r = r * b % p;
    }
    return r;
  }

  // (a t + b)(c t + d) with t^2 = t + 1, an element packed as a * p + b
  private static long mul(long u, long v) {
    long a = u / p;
    long b = u % p;
    long c = v / p;
    long d = v % p;
    long ac = a * c % p;
    long cross = (a * d + b * c) % p;
    return (ac + cross) % p * p + (ac + b * d) % p;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    p = in.nextLong();
    long x = in.nextLong();
    TreeSet<Long> found = new TreeSet<>();
    if (p <= SMALL) {
      // the pairs (F(k), F(k + 1)) repeat with a period of at most 4p + 4
      long a = 0;
      long b = 1;
      do {
        if (a == x) found.add(b);
        long c = (a + b) % p;
        a = b;
        b = c;
      } while (a != 0 || b != 1);
    } else {
      // t^k = F(k) t + F(k - 1), and Cassini's identity
      // F(k + 1)^2 - F(k + 1) F(k) - F(k)^2 = (-1)^k limits y = F(k + 1)
      // to the roots of y^2 - x y - x^2 - s = 0, s = 1 or -1
      Set<Long> candidates = new HashSet<>();
      long half = (p + 1) / 2;
      for (long s = 1; s >= -1; s -= 2) {
        long root = sqrtMod(((x * x + QUAD * (x * x + s)) % p + p) % p);
        if (root < 0) continue;
        candidates.add((x + root) % p * half % p);
        candidates.add((x - root + p) % p * half % p);
      }
      // a pair is a power of t when the discrete logarithm exists: baby steps
      // t^j, giant steps by t^-m; the period divides p - 1 or 2 (p + 1)
      long bound = p % FIVE == 1 || p % FIVE == FIVE - 1 ? p - 1 : 2 * (p + 1);
      long m = (long) Math.sqrt((double) bound) + 1;
      Set<Long> baby = new HashSet<>();
      long e = 1; // the element 0 t + 1
      for (long j = 0; j < m; j++) {
        baby.add(e);
        e = mul(e, p);
      }
      long back = 1;
      long inverse = p + p - 1; // t^-m = (t - 1)^m
      for (long k = m; k > 0; k >>= 1, inverse = mul(inverse, inverse))
        if ((k & 1) == 1) back = mul(back, inverse);
      for (long y : candidates) {
        e = x * p + (y - x + p) % p;
        for (long i = 0; i <= m; i++, e = mul(e, back))
          if (baby.contains(e)) {
            found.add(y);
            break;
          }
      }
    }
    StringBuilder out = new StringBuilder();
    out.append(found.size()).append('\n');
    if (!found.isEmpty()) {
      for (long y : found) out.append(y).append(' ');
      out.setLength(out.length() - 1);
      out.append('\n');
    }
    System.out.print(out);
  }
}
