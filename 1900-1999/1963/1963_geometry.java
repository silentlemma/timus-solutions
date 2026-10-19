import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  static final int VERTEX_COUNT = 4;

  static void addDistinct(List<long[]> points, long[] point) {
    for (long[] old : points) {
      if (old[0] == point[0] && old[1] == point[1])
        return;
    }
    points.add(point);
  }

  static int boundaryCount(long[][] points) {
    List<long[]> boundary = new ArrayList<>();
    for (int shift = 0; shift < VERTEX_COUNT; shift++) {
      long[] a, b;
      if (shift % 2 == 0) {
        int first = shift / 2, opposite = (first + 2) % VERTEX_COUNT;
        a = new long[] {2 * points[first][0], 2 * points[first][1]};
        b = new long[] {2 * points[opposite][0], 2 * points[opposite][1]};
      } else {
        a = new long[] {points[0][0] + points[shift][0], points[0][1] + points[shift][1]};
        int[] remaining = new int[2];
        int count = 0;
        for (int i = 0; i < VERTEX_COUNT; i++) {
          if (i != 0 && i != shift)
            remaining[count++] = i;
        }
        long[] p = points[remaining[0]], q = points[remaining[1]];
        b = new long[] {p[0] + q[0], p[1] + q[1]};
      }
      long dx = b[0] - a[0], dy = b[1] - a[1];
      if (dx == 0 && dy == 0)
        continue;
      boolean valid = true;
      for (int i = 0; i < VERTEX_COUNT; i++) {
        long[] p = points[i], q = points[(shift - i + VERTEX_COUNT) % VERTEX_COUNT];
        if ((p[0] + q[0] - a[0]) * dy != (p[1] + q[1] - a[1]) * dx
            || (p[0] - q[0]) * dx + (p[1] - q[1]) * dy != 0) {
          valid = false;
          break;
        }
      }
      if (valid) {
        addDistinct(boundary, a);
        addDistinct(boundary, b);
      }
    }
    return boundary.size();
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      long[][] points = new long[VERTEX_COUNT][2];
      for (long[] point : points) {
        point[0] = input.nextLong();
        point[1] = input.nextLong();
      }
      System.out.println(boundaryCount(points));
    }
  }
}
