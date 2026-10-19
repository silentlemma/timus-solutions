import java.util.Scanner;

public class Main {
  private static final long FIRST = 2; // the first step removes every second day

  // among the first n days, step k removes every k-th of those still left,
  // which is n / k of a prefix of length n; it stops mattering once n < k
  private static long quiet(long n) {
    for (long k = FIRST; n >= k; k++) n -= n / k;
    return n;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long left = in.nextLong();
    long right = in.nextLong();
    System.out.println(quiet(right) - quiet(left - 1));
  }
}
