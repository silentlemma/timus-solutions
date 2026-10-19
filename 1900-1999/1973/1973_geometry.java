import java.math.BigInteger;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  static final BigInteger DIAGONAL_WEIGHT = BigInteger.valueOf(2);
  static final BigInteger PAIR_WEIGHT = BigInteger.valueOf(3);
  static final BigInteger NORMALIZER = BigInteger.valueOf(27);

  static double expectation(long[][] vertices) {
    long originX = vertices[0][0], originY = vertices[0][1];
    long previousX = vertices[1][0] - originX, previousY = vertices[1][1] - originY;
    long total = 0;
    BigInteger weightedX = BigInteger.ZERO, weightedY = BigInteger.ZERO;
    BigInteger numerator = BigInteger.ZERO;
    for (int i = 2; i < vertices.length; i++) {
      long x = vertices[i][0] - originX, y = vertices[i][1] - originY;
      long area = previousX * y - previousY * x;
      long sumX = previousX + x, sumY = previousY + y;
      BigInteger between = weightedX.multiply(BigInteger.valueOf(sumY))
                               .subtract(weightedY.multiply(BigInteger.valueOf(sumX)));
      BigInteger d = BigInteger.valueOf(area);
      BigInteger cube = d.multiply(d).multiply(d).multiply(DIAGONAL_WEIGHT);
      BigInteger paired = d.multiply(between).multiply(PAIR_WEIGHT);
      numerator = numerator.add(cube).add(paired);
      weightedX = weightedX.add(d.multiply(BigInteger.valueOf(sumX)));
      weightedY = weightedY.add(d.multiply(BigInteger.valueOf(sumY)));
      total += area;
      previousX = x;
      previousY = y;
    }
    BigInteger denominator =
        BigInteger.valueOf(total).multiply(BigInteger.valueOf(total)).multiply(NORMALIZER);
    return numerator.doubleValue() / denominator.doubleValue();
  }

  public static void main(String[] args) {
    try (Scanner in = new Scanner(System.in)) {
      int count = in.nextInt();
      long[][] vertices = new long[count][2];
      for (long[] vertex : vertices) {
        vertex[0] = in.nextLong();
        vertex[1] = in.nextLong();
      }
      System.out.printf(Locale.US, "%.12f%n", expectation(vertices));
    }
  }
}
