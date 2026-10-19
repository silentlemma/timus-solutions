import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
  private static final BigInteger TWO = BigInteger.valueOf(2);
  // N is the distance of Q from the vertex times SCALE |A|^3
  private static final BigInteger SCALE = BigInteger.valueOf(4);

  private static BigInteger cross(BigInteger ux, BigInteger uy, BigInteger vx, BigInteger vy) {
    return ux.multiply(vy).subtract(uy.multiply(vx));
  }

  private static String[] words;
  private static int pos;

  private static BigInteger read() {
    return new BigInteger(words[pos++]);
  }

  private static String answer() {
    // the curve is C + B t + A t^2 with A = (a, d), B = (b, e), C = (c, f)
    BigInteger a = read(), b = read(), c = read(), d = read(), e = read(), f = read();
    BigInteger wx = read().subtract(c); // P relative to C
    BigInteger wy = read().subtract(f);
    BigInteger r = read();
    BigInteger r2 = r.multiply(r);
    if (a.signum() == 0 && d.signum() == 0) {
      if (b.signum() == 0 && e.signum() == 0) {
        // a single point: every line through it is an axis, and Q runs over the
        // circle with diameter CP, from C itself to P
        return wx.multiply(wx).add(wy.multiply(wy)).compareTo(r2) <= 0 ? "YES" : "MAYBE";
      }
      // a line: the line itself is an axis (Q lies on it), and so is every
      // perpendicular, with Q at the distance of P from the line
      BigInteger dist = cross(wx, wy, b, e);
      BigInteger limit = r2.multiply(b.multiply(b).add(e.multiply(e)));
      return dist.multiply(dist).compareTo(limit) <= 0 ? "YES" : "MAYBE";
    }
    // one axis along A; along it, P lies at N / (4 |A|^3) from the vertex
    BigInteger a2 = a.multiply(a).add(d.multiply(d));
    BigInteger ab = a.multiply(b).add(d.multiply(e));
    BigInteger along = wx.multiply(a).add(wy.multiply(d));
    BigInteger n = SCALE.multiply(a2).multiply(along).add(ab.multiply(ab));
    BigInteger k2 = cross(a, d, b, e).pow(2); // zero for a ray, otherwise the parabola width
    BigInteger a6 = a2.multiply(a2).multiply(a2);
    boolean inside;
    if (n.compareTo(TWO.multiply(k2)) <= 0) {
      // the nearest point of the curve is its vertex (the end of a ray)
      inside = n.multiply(n).compareTo(SCALE.pow(2).multiply(r2).multiply(a6)) <= 0;
    } else {
      // Q far enough inside: squared distance k2 (N - k2) / (4 |A|^6), zero on a ray
      inside = k2.multiply(n.subtract(k2)).compareTo(SCALE.multiply(r2).multiply(a6)) <= 0;
    }
    return inside ? "YES" : "NO";
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder all = new StringBuilder();
    for (String line = in.readLine(); line != null; line = in.readLine()) {
      all.append(line).append(' ');
    }
    words = all.toString().trim().split("\\s+");
    int t = read().intValue();
    StringBuilder out = new StringBuilder();
    for (int i = 0; i < t; i++) out.append(answer()).append('\n');
    System.out.print(out);
  }
}
