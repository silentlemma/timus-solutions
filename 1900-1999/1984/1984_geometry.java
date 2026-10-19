import java.util.Locale;
import java.util.Scanner;

public class Main {
  static double radius(int count) {
    if (count == 1)
      return 1;
    return 1 + 1 / Math.sin(Math.PI / count);
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.printf(Locale.US, "%.10f%n", radius(in.nextInt()));
  }
}
