import java.util.Locale;
import java.util.Scanner;

public class Main {
  static final int DIMENSIONS = 3;
  static final int ITERATIONS = 80;

  static long dot(long[] a, long[] b) {
    long total = 0;
    for (int i = 0; i < DIMENSIONS; i++) total += a[i] * b[i];
    return total;
  }

  static double meetingTime(long[] carrier, long[] ship, double speed) {
    long radiusSquared = dot(carrier, carrier), distanceSquared = dot(ship, ship);
    double radius = Math.sqrt(radiusSquared), distance = Math.sqrt(distanceSquared);
    long delta = distanceSquared - radiusSquared;
    double tangent = Math.sqrt(delta), radialGap = delta / (distance + radius);
    long[] cross = {carrier[1] * ship[2] - carrier[2] * ship[1],
        carrier[2] * ship[0] - carrier[0] * ship[2], carrier[0] * ship[1] - carrier[1] * ship[0]};
    double angle = Math.atan2(Math.sqrt(dot(cross, cross)), dot(carrier, ship));
    double visibleAngle = Math.atan2(tangent, radius), radialTime = radialGap / speed;
    if (radius * angle <= radialTime)
      return radialTime;
    double low = 0, high = angle;
    for (int step = 0; step < ITERATIONS; step++) {
      double beta = (low + high) / 2;
      if (radius * (angle - beta)
          > shipLength(beta, visibleAngle, tangent, radius, distance, radialGap) / speed)
        low = beta;
      else
        high = beta;
    }
    double beta = (low + high) / 2;
    return Math.max(radius * (angle - beta),
        shipLength(beta, visibleAngle, tangent, radius, distance, radialGap) / speed);
  }

  static double shipLength(double beta, double visibleAngle, double tangent, double radius,
      double distance, double radialGap) {
    if (beta <= visibleAngle) {
      double sideways = 2 * Math.sqrt(distance * radius) * Math.sin(beta / 2);
      return Math.hypot(radialGap, sideways);
    }
    return tangent + radius * (beta - visibleAngle);
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long[] carrier = new long[DIMENSIONS], ship = new long[DIMENSIONS];
    for (int i = 0; i < DIMENSIONS; i++) carrier[i] = in.nextLong();
    for (int i = 0; i < DIMENSIONS; i++) ship[i] = in.nextLong();
    System.out.printf(Locale.US, "%.10f%n", meetingTime(carrier, ship, in.nextInt()));
  }
}
