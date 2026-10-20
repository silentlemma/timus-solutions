import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long cx = in.nextLong();
    long cy = in.nextLong();
    long r = in.nextLong();
    long ax = in.nextLong();
    long ay = in.nextLong();
    long bx = in.nextLong();
    long by = in.nextLong();
    // The players are equally far from the centre, so the mirror point lies on
    // the bisector of the angle between them, in the direction w = A + B - 2C.
    long wx = ax + bx - 2 * cx;
    long wy = ay + by - 2 * cy;
    // Both shots stay outside the tank exactly when each player is strictly
    // beyond the tangent line at that point: (A - C) . w > r |w|.
    long dot = (ax - cx) * wx + (ay - cy) * wy;
    long norm = wx * wx + wy * wy;
    if (dot <= 0 || dot * dot <= r * r * norm) {
      System.out.println("No way");
      return;
    }
    double scale = r / Math.sqrt((double) norm);
    System.out.println(String.format(Locale.US, "%.9f %.9f", cx + wx * scale, cy + wy * scale));
  }
}
