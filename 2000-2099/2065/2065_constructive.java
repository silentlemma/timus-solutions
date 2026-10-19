import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt();
    // n - k + 1 zeros, then 1, -1, 2, -2, ...: k distinct values and only k
    // distinct segment sums, the least possible
    StringBuilder out = new StringBuilder("0");
    for (int i = 1; i < n - k + 1; ++i) out.append(" 0");
    for (int i = 1; i < k; ++i) out.append(' ').append(i % 2 == 1 ? (i + 1) / 2 : -(i / 2));
    System.out.println(out);
  }
}
