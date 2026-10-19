import java.util.Scanner;

public class Main {
  private static final long BOUND = 1000000; // the cube root of the largest C

  private static long isqrt(long x) {
    long r = (long) Math.sqrt((double) x);
    while (r * r > x) r--;
    while ((r + 1) * (r + 1) <= x) r++;
    return r;
  }

  public static void main(String[] args) {
    long c = new Scanner(System.in).nextLong();
    if (c == 0) {
      System.out.println(1); // only 0 + 0
      return;
    }
    // sqrt A + sqrt B = sqrt C exactly when C = s^2 q with q square-free and
    // A = a^2 q, B = b^2 q, a + b = s; so the answer counts the pairs a <= b
    long root = 1;
    for (long d = 2; d <= BOUND && d * d <= c; d++) {
      while (c % (d * d) == 0) {
        c /= d * d;
        root *= d;
      }
      if (c % d == 0) c /= d;
    }
    // what is left has only prime factors above the bound, at most two of them,
    // so it holds a square factor only when it is a square itself
    long r = isqrt(c);
    if (c > 1 && r * r == c) root *= r;
    System.out.println(root / 2 + 1);
  }
}
