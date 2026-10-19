import java.util.Scanner;

public class Main {
  private static final long SIDE_FACTOR = 4; // the area is 4a - 1/3

  public static void main(String[] args) {
    long a = new Scanner(System.in).nextLong();
    // 4a - 1/3 = (4a - 1) + 2/3, and 2/3 rounds to 0.6666666667
    System.out.println((SIDE_FACTOR * a - 1) + ".6666666667");
  }
}
