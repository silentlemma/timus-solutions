import java.util.Scanner;

public class Main {
  private static final long PERCENT = 100;

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long b = in.nextLong();
    long c = in.nextLong();
    long d = in.nextLong();
    long k = in.nextLong();
    long p = in.nextLong();
    // the usual insurance for the next k years; registering the accident costs
    // p percent of it on top, paying cash costs b on top
    long usual = k * c + d * k * (k + 1) / 2;
    // both sides times 100, so everything stays in integers
    long gap = usual * p - b * PERCENT;
    System.out.println(gap > 0 ? "Cash" : "Insurance");
    long cents = Math.abs(gap);
    System.out.println(cents / PERCENT + "." + String.format("%02d", cents % PERCENT));
  }
}
