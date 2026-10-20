import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long a = in.nextLong();
    long b = in.nextLong();
    long c = in.nextLong();
    long x = in.nextLong();
    long y = in.nextLong();
    long z = in.nextLong();
    // the dual lands first cover what the red and blue lands miss, and every
    // land left over pays for the mana of any color
    long missing = Math.max(0, x - a) + Math.max(0, y - b);
    boolean enough = missing <= c && a + b + c >= x + y + z;
    System.out.println(enough ? "It is a kind of magic" : "There are no miracles in life");
  }
}
