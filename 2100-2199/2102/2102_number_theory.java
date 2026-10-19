import java.util.Scanner;

public class Main {
  private static final int TARGET = 20;
  private static final long BOUND = 2000000; // trial divisors; then at most two primes remain

  public static void main(String[] args) {
    long n = new Scanner(System.in).nextLong();
    int count = 0;
    long d = 2;
    for (; d <= BOUND && d * d <= n; d++) {
      while (n % d == 0) {
        n /= d;
        count++;
      }
    }
    if (n > 1) {
      // what is left is prime; otherwise n >= BOUND^2, the divided part is at
      // most 10^18 / BOUND^2, fewer than 18 factors, and the rest adds at most two
      count = d * d > n ? count + 1 : -1;
    }
    System.out.println(count == TARGET ? "Yes" : "No");
  }
}
