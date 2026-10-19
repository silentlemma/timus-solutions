import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  private static final int DIMENSIONS = 3;
  private static final int CIRCLES = 3;
  private static final int PERIOD_SHIFTS = 2;
  private static final double TAU = 2 * Math.PI;

  private static double[] add(double[] a, double[] b) {
    double[] result = new double[DIMENSIONS];
    for (int i = 0; i < DIMENSIONS; ++i) result[i] = a[i] + b[i];
    return result;
  }
  private static double[] sub(double[] a, double[] b) {
    double[] result = new double[DIMENSIONS];
    for (int i = 0; i < DIMENSIONS; ++i) result[i] = a[i] - b[i];
    return result;
  }
  private static double[] scale(double[] a, double value) {
    double[] result = new double[DIMENSIONS];
    for (int i = 0; i < DIMENSIONS; ++i) result[i] = a[i] * value;
    return result;
  }
  private static double sumThree(double a, double b, double c) {
    double sum = 0, correction = 0;
    for (double value : new double[] {a, b, c}) {
      double next = sum + value;
      correction += Math.abs(sum) >= Math.abs(value) ? (sum - next) + value : (value - next) + sum;
      sum = next;
    }
    return sum + correction;
  }
  private static double dot(double[] a, double[] b) {
    return sumThree(a[0] * b[0], a[1] * b[1], a[2] * b[2]);
  }
  private static double[] cross(double[] a, double[] b) {
    return new double[] {
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
  }
  private static double length(double[] a) {
    return Math.sqrt(dot(a, a));
  }
  private static double[] unit(double[] a) {
    return scale(a, 1 / length(a));
  }
  private static double above(double[] center, double radius, double[] radial, double[] tangent,
      double angle, double height) {
    double amplitude = radius * Math.hypot(radial[2], tangent[2]);
    if (amplitude == 0)
      return center[2] >= height ? radius * angle : 0;
    double ratio = (height - center[2]) / amplitude;
    if (ratio <= -1)
      return radius * angle;
    if (ratio >= 1)
      return 0;
    double half = Math.acos(ratio), phase = Math.atan2(tangent[2], radial[2]), measure = 0;
    for (int shift = -PERIOD_SHIFTS; shift <= PERIOD_SHIFTS; ++shift) {
      double left = phase - half + shift * TAU, right = phase + half + shift * TAU;
      measure += Math.max(0, Math.min(angle, right) - Math.max(0, left));
    }
    return radius * measure;
  }
  private static double solve(int speed, int acceleration, double[][] centers) {
    double[] start = scale(centers[0], -1);
    double squared = dot(start, start), radius = length(start);
    double[] radial = unit(start), raw = {-centers[0][1], centers[0][0], 0};
    double[] tangent = unit(cross(raw, radial));
    double height = (double) speed * speed / (2 * acceleration), answer = 0;
    for (int i = 0; i < CIRCLES; ++i) {
      double angle = TAU, rho = 0, distance = 0;
      double[] relative = new double[DIMENSIONS], normal = new double[DIMENSIONS],
               toward = new double[DIMENSIONS];
      if (i + 1 < CIRCLES) {
        relative = sub(centers[i + 1], centers[i]);
        double normalLength = length(raw);
        normal = scale(raw, 1 / normalLength);
        double[] product = cross(raw, relative);
        double crossLength = length(product);
        double[] direction = scale(product, 1 / crossLength);
        toward = unit(cross(direction, normal));
        rho = crossLength / normalLength;
        distance = dot(relative, raw) / normalLength;
        angle = Math.atan2(dot(toward, tangent), dot(toward, radial));
        if (angle <= 0)
          angle += TAU;
      }
      answer += above(centers[i], radius, radial, tangent, angle, height);
      if (i + 1 < CIRCLES) {
        double difference = sumThree(squared, -dot(relative, relative), distance * distance);
        double delta = difference / (radius + rho);
        radius = Math.hypot(delta, distance);
        radial = scale(sub(scale(toward, delta), scale(normal, distance)), 1 / radius);
        squared = sumThree(delta * delta, distance * distance, 0);
        if (distance == 0) {
          if (delta < 0)
            raw = scale(raw, -1);
        } else
          raw = add(scale(normal, delta), scale(toward, distance));
        tangent = unit(cross(raw, radial));
      }
    }
    return answer;
  }
  private static int readInt(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= ' ' && c >= 0);
    int sign = 1;
    if (c == '-') {
      sign = -1;
      c = in.read();
    }
    int value = 0;
    while (c > ' ') {
      value = value * 10 + c - '0';
      c = in.read();
    }
    return sign * value;
  }
  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int count = readInt(in);
    StringBuilder out = new StringBuilder();
    while (count-- > 0) {
      int speed = readInt(in), acceleration = readInt(in);
      double[][] centers = new double[CIRCLES][DIMENSIONS];
      for (double[] center : centers)
        for (int j = 0; j < DIMENSIONS; ++j) center[j] = readInt(in);
      out.append(solve(speed, acceleration, centers)).append('\n');
    }
    System.out.print(out);
  }
}
