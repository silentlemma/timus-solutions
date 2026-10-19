import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  private static final long QUAD = 4; // the discriminant of a t^2 + b t + c is b^2 - 4 a c

  // compares sign * sqrt(disc) with the integer k exactly: -1, 0 or 1
  private static int signSqrtVs(int sign, long disc, long k) {
    if (sign > 0) return k < 0 ? 1 : Long.compare(disc, k * k);
    return k > 0 ? -1 : Long.compare(k * k, disc);
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long x = in.nextLong();
    long y = in.nextLong();
    long z = in.nextLong();
    long vx = in.nextLong();
    long vy = in.nextLong();
    long ex = in.nextLong();
    long ey = in.nextLong();
    // Stewart: the point at fraction t of the way from Denis to the hall is at
    // squared distance (1 - t) X^2 + t Y^2 - t (1 - t) Z^2 from Vanya; Eugene is
    // at d^2, so t solves z2 t^2 + b t + c = 0 with integer coefficients
    long d2 = (ex - vx) * (ex - vx) + (ey - vy) * (ey - vy);
    long z2 = z * z;
    long b = y * y - x * x - z2;
    long c = x * x - d2;
    long disc = b * b - QUAD * z2 * c;
    List<double[]> found = new ArrayList<>(); // t, and 1 when Eugene is at Denis's place
    if (disc >= 0) {
      for (int s = 1; s >= -1; s -= 2) {
        if (s < 0 && disc == 0) break;
        // t = (-b + s sqrt(disc)) / (2 z2) must lie in [0, 1]
        if (signSqrtVs(s, disc, b) < 0 || signSqrtVs(s, disc, 2 * z2 + b) > 0) continue;
        double t = (-b + s * Math.sqrt((double) disc)) / (2.0 * z2);
        found.add(new double[] {t, c == 0 && signSqrtVs(s, disc, b) == 0 ? 1 : 0});
      }
    }
    // a model triangle: Vanya at 0, Denis on the x axis, the hall above it
    double cosV = (double) (x * x + y * y - z2) / (2.0 * x * y);
    double hx = y * cosV;
    double hy = y * Math.sqrt(Math.max(0, 1 - cosV * cosV));
    double ux = ex - vx;
    double uy = ey - vy;
    StringBuilder out = new StringBuilder();
    int count = 0;
    for (double[] r : found) {
      double px = x + r[0] * (hx - x);
      double py = r[0] * hy;
      for (int mirror = 1; mirror >= -1; mirror -= 2) {
        if (mirror < 0 && r[1] > 0) break;
        // rotate (and maybe reflect) the model so that its point lands on Eugene
        double qx = px;
        double qy = mirror * py;
        double norm = qx * qx + qy * qy;
        double cosR = (qx * ux + qy * uy) / norm;
        double sinR = (qx * uy - qy * ux) / norm;
        out.append(String.format(Locale.US, "%.12f %.12f", vx + cosR * x, vy + sinR * x));
        out.append('\n');
        count++;
      }
    }
    System.out.print(count + "\n" + out);
  }
}
