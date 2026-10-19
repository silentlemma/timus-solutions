import java.util.Scanner;

public class Main {
  private static final int LIMIT = 1000000; // square root of the largest R

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long l = in.nextLong();
    long r = in.nextLong();
    boolean[] composite = new boolean[LIMIT + 1];
    composite[0] = composite[1] = true;
    for (int i = 2; (long) i * i <= LIMIT; i++)
      if (!composite[i]) for (int j = i * i; j <= LIMIT; j += i) composite[j] = true;
    // the only unsatisfying numbers are p^k, k >= 2, with k + 1 divisors and k + 1 prime
    long bad = 0;
    for (long p = 2; p * p <= r; p++) {
      if (composite[(int) p]) continue;
      long power = p * p;
      for (int k = 2; ; k++) {
        if (power >= l && !composite[k + 1]) bad++;
        if (power > r / p) break;
        power *= p;
      }
    }
    System.out.println(r - l + 1 - bad);
  }
}
