import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  static final int DIMENSIONS = 3;
  static final long RADIUS = 100;
  static final int MAX_CUTS = 4;

  static long dot(long[] a, long[] b) {
    long result = 0;
    for (int i = 0; i < DIMENSIONS; i++) result += a[i] * b[i];
    return result;
  }

  static long[] cross(long[] a, long[] b) {
    return new long[] {
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
  }

  static double area(long[][] points) {
    long[] first = new long[DIMENSIONS], second = new long[DIMENSIONS];
    for (int i = 0; i < DIMENSIONS; i++) {
      first[i] = points[1][i] - points[0][i];
      second[i] = points[2][i] - points[0][i];
    }
    long[] normal = cross(first, second);
    long normSquared = dot(normal, normal), offset = dot(normal, points[0]);
    long residual = RADIUS * RADIUS * normSquared - offset * offset;
    if (residual <= 0)
      return 0;
    double radiusSquared = (double) residual / normSquared;
    double[] axis = new double[DIMENSIONS], unitNormal = new double[DIMENSIONS];
    for (int i = 0; i < DIMENSIONS; i++) {
      axis[i] = first[i] / Math.sqrt(dot(first, first));
      unitNormal[i] = normal[i] / Math.sqrt(normSquared);
    }
    double[] other = {unitNormal[1] * axis[2] - unitNormal[2] * axis[1],
        unitNormal[2] * axis[0] - unitNormal[0] * axis[2],
        unitNormal[0] * axis[1] - unitNormal[1] * axis[0]};
    double[][] projected = new double[DIMENSIONS][2];
    for (int i = 0; i < DIMENSIONS; i++) {
      for (int j = 0; j < DIMENSIONS; j++) {
        projected[i][0] += points[i][j] * axis[j];
        projected[i][1] += points[i][j] * other[j];
      }
    }
    double total = 0;
    for (int i = 0; i < DIMENSIONS; i++) {
      int following = (i + 1) % DIMENSIONS;
      long[] delta = new long[DIMENSIONS];
      for (int j = 0; j < DIMENSIONS; j++) delta[j] = points[following][j] - points[i][j];
      long quadratic = dot(delta, delta), linear = dot(points[i], delta);
      long constant = dot(points[i], points[i]) - RADIUS * RADIUS;
      long discriminant = linear * linear - quadratic * constant;
      double[] cuts = new double[MAX_CUTS];
      cuts[1] = 1;
      int count = 2;
      double low = 1, high = 0;
      if (discriminant > 0) {
        double stable = -linear - Math.copySign(Math.sqrt(discriminant), linear);
        low = stable / quadratic;
        high = constant / stable;
        if (low > high) {
          double temp = low;
          low = high;
          high = temp;
        }
        if (0 < low && low < 1)
          cuts[count++] = low;
        if (0 < high && high < 1)
          cuts[count++] = high;
      }
      Arrays.sort(cuts, 0, count);
      double x = projected[i][0], y = projected[i][1];
      double dx = projected[following][0] - x, dy = projected[following][1] - y;
      for (int j = 1; j < count; j++) {
        double left = cuts[j - 1], right = cuts[j];
        double ax = x + left * dx, ay = y + left * dy, bx = x + right * dx, by = y + right * dy;
        double signed = ax * by - ay * bx, middle = (left + right) / 2;
        total += low < middle && middle < high
            ? signed
            : radiusSquared * Math.atan2(signed, ax* bx + ay * by);
      }
    }
    return Math.abs(total) / 2;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long[][] points = new long[DIMENSIONS][DIMENSIONS];
    for (long[] point : points) {
      for (int i = 0; i < DIMENSIONS; i++) point[i] = in.nextLong();
    }
    System.out.printf(Locale.US, "%.10f%n", area(points));
  }
}
