import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  private static final int DIM = 3;

  private static long[] sub(long[] u, long[] v) {
    long[] r = new long[DIM];
    for (int i = 0; i < DIM; i++) r[i] = u[i] - v[i];
    return r;
  }

  private static long dot(long[] u, long[] v) {
    long s = 0;
    for (int i = 0; i < DIM; i++) s += u[i] * v[i];
    return s;
  }

  private static long[] cross(long[] u, long[] v) {
    return new long[] {
      u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]
    };
  }

  // the dot product in big integers: the mixed product reaches 5 * 10^19
  private static BigInteger bigDot(long[] u, long[] v) {
    BigInteger s = BigInteger.ZERO;
    for (int i = 0; i < DIM; i++) {
      s = s.add(BigInteger.valueOf(u[i]).multiply(BigInteger.valueOf(v[i])));
    }
    return s;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long[][] p = new long[DIM + 1][DIM];
    for (long[] q : p) for (int i = 0; i < DIM; i++) q[i] = in.nextLong();
    long[] ab = sub(p[1], p[0]);
    long[] cd = sub(p[DIM], p[2]);
    long[] ac = sub(p[2], p[0]);
    // the turn is a right angle, the two lines meet, the turning point
    // P = A + t AB with t = (AC . AB) / |AB|^2 is not before B, and C is not
    // before P on the second line, (C - P) . CD = AC . CD >= 0
    boolean ok = dot(ab, cd) == 0 && bigDot(ac, cross(ab, cd)).signum() == 0
        && dot(ac, ab) >= dot(ab, ab) && dot(ac, cd) >= 0;
    System.out.println(ok ? "Valid" : "Invalid");
  }
}
