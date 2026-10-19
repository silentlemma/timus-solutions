import java.io.BufferedInputStream;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  static final int DIMENSION = 3;
  static final int POINTS = 4;
  static final double AXIS_THRESHOLD = 1900;
  static final double AXIS_STEP = 2;
  static final int ANGLE = 180;

  static double dot(double[] a, double[] b) {
    double total = 0;
    for (int i = 0; i < DIMENSION; i++) total += a[i] * b[i];
    return total;
  }

  static double[] normalize(double[] a) {
    double length = Math.sqrt(dot(a, a));
    double[] result = new double[DIMENSION];
    for (int i = 0; i < DIMENSION; i++) result[i] = a[i] / length;
    return result;
  }

  static double[][] axis(
      double[] middle, double[] displacement, double[] direction, double[] difference) {
    double coefficient = dot(displacement, direction) / (2 * dot(direction, direction));
    double[] unit = normalize(direction);
    double[] center = new double[DIMENSION];
    for (int i = 0; i < DIMENSION; i++) center[i] = middle[i] + coefficient * difference[i];
    double projection = dot(center, unit);
    double[][] result = new double[2][DIMENSION];
    for (int i = 0; i < DIMENSION; i++) {
      result[0][i] = center[i] - projection * unit[i];
      result[1][i] = result[0][i] + AXIS_STEP * unit[i];
    }
    return result;
  }

  static double[][] solve(double[][] points) {
    double[] a = points[0], b = points[1], c = points[2], d = points[POINTS - 1];
    double[] first = new double[DIMENSION], second = new double[DIMENSION];
    double[] middle = new double[DIMENSION], displacement = new double[DIMENSION];
    for (int i = 0; i < DIMENSION; i++) {
      first[i] = b[i] - a[i];
      second[i] = d[i] - c[i];
      middle[i] = (a[i] + c[i]) / 2;
      displacement[i] = c[i] - a[i];
    }
    if (dot(first, second) < 0)
      for (int i = 0; i < DIMENSION; i++) second[i] = -second[i];
    double[] u = normalize(first), v = normalize(second);
    double[] plus = new double[DIMENSION], minus = new double[DIMENSION];
    for (int i = 0; i < DIMENSION; i++) {
      plus[i] = u[i] + v[i];
      minus[i] = u[i] - v[i];
    }
    double[][] result = axis(middle, displacement, plus, minus);
    if (dot(result[0], result[0]) > AXIS_THRESHOLD * AXIS_THRESHOLD)
      result = axis(middle, displacement, minus, plus);
    return result;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedInputStream(System.in));
    double[][] points = new double[POINTS][DIMENSION];
    for (double[] row : points)
      for (int i = 0; i < DIMENSION; i++) row[i] = in.nextInt();
    for (double[] row : solve(points))
      System.out.printf(Locale.US, "%.15f %.15f %.15f%n", row[0], row[1], row[2]);
    System.out.println(ANGLE);
  }
}
