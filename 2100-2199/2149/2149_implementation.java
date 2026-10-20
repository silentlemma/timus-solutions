import java.util.Scanner;

public class Main {
  private static final int STEP = 5; // four characters of a pigeon and a separating column

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    String top = in.next();
    // halves counts the pigeons that break the pattern with the left half looking
    // left, parity those that break the pattern with even positions looking left,
    // and the two opposite patterns break exactly at the other pigeons
    int halves = 0;
    int parity = 0;
    for (int i = 0; i < n; i++) {
      boolean left = top.charAt(i * STEP) == '<';
      if (left != (i < n / 2)) halves++;
      if (left != (i % 2 == 0)) parity++;
    }
    System.out.println(Math.min(Math.min(halves, n - halves), Math.min(parity, n - parity)));
  }
}
