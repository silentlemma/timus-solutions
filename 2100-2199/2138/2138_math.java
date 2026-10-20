import java.util.Scanner;

public class Main {
  private static final int DIGITS = 4;
  private static final long BASE = 256;

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    in.next();
    long v = in.nextLong();
    // Both directions reverse the four base-256 digits, so the type does not matter.
    long sent = 0;
    for (int i = 0; i < DIGITS; i++) {
      sent = sent * BASE + v % BASE;
      v /= BASE;
    }
    System.out.println(sent);
  }
}
