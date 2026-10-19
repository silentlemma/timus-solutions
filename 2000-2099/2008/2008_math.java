import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  private static final long GRAVITY_NUMERATOR = 49;
  private static final long GRAVITY_DENOMINATOR = 5;
  private static final int POINT_COUNT = 3;
  private static final int BASE = 10;

  private static boolean canReach(long speed, long dx, long dy) {
    long threshold = GRAVITY_DENOMINATOR * speed * speed - GRAVITY_NUMERATOR * dy;
    return threshold >= 0
        && threshold * threshold >= GRAVITY_NUMERATOR * GRAVITY_NUMERATOR * (dx * dx + dy * dy);
  }

  private static boolean jump(long speed, long[] start, long[] target) {
    return canReach(speed, target[0] - start[0], target[1] - start[1]);
  }

  private static boolean solve(long speed, long[] head, long[] left, long[] right) {
    return jump(speed, left, right) && jump(speed, right, left)
        && (jump(speed, left, head) || jump(speed, right, head));
  }

  private static long readLong(BufferedInputStream input) throws IOException {
    int ch;
    do {
      ch = input.read();
    } while (ch <= ' ' && ch != -1);
    long value = 0;
    while (ch > ' ') {
      value = value * BASE + ch - '0';
      ch = input.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream input = new BufferedInputStream(System.in);
    long speed = readLong(input);
    long[][] points = new long[POINT_COUNT][2];
    for (long[] point : points) {
      point[0] = readLong(input);
      point[1] = readLong(input);
    }
    System.out.println(solve(speed, points[0], points[1], points[2]) ? "Yes" : "No");
  }
}
