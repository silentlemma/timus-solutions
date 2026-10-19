import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
  private static final long FIRST_ODD = 3;
  private static final long MIN_HYPOTENUSE = 5;
  private static final int SIDE_COUNT = 3;

  static BigInteger integerRoot(BigInteger value) {
    if (value.signum() == 0)
      return BigInteger.ZERO;
    BigInteger current = BigInteger.ONE.shiftLeft((value.bitLength() + 1) / 2);
    while (true) {
      BigInteger next = current.add(value.divide(current)).shiftRight(1);
      if (next.compareTo(current) >= 0)
        return current;
      current = next;
    }
  }

  static long smallRoot(long value) {
    long low = 0, high = value + 1;
    while (high - low > 1) {
      long middle = (high + low) / 2;
      if (middle * middle <= value)
        low = middle;
      else
        high = middle;
    }
    return low;
  }

  static long gcd(long a, long b) {
    while (b != 0) {
      long next = a % b;
      a = b;
      b = next;
    }
    return a;
  }

  static List<Long> divisors(long number) {
    List<Long> values = new ArrayList<>();
    values.add(1L);
    for (long prime = 2; prime * prime <= number; prime = prime == 2 ? FIRST_ODD : prime + 2) {
      int previous = values.size();
      long power = 1;
      while (number % prime == 0) {
        number /= prime;
        power *= prime;
        for (int i = 0; i < previous; i++) values.add(values.get(i) * power);
      }
    }
    if (number > 1) {
      int previous = values.size();
      for (int i = 0; i < previous; i++) values.add(values.get(i) * number);
    }
    return values;
  }

  static class Geometry {
    final BigInteger dot, cross, denominator;
    Geometry(BigInteger dotValue, BigInteger crossValue, long radius) {
      dot = dotValue;
      cross = crossValue;
      denominator = BigInteger.valueOf(radius * radius);
    }
    long[] point(long x, long y) {
      BigInteger bx = BigInteger.valueOf(x), by = BigInteger.valueOf(y);
      BigInteger u = dot.multiply(bx).subtract(cross.multiply(by));
      BigInteger v = dot.multiply(by).add(cross.multiply(bx));
      BigInteger[] first = u.divideAndRemainder(denominator);
      BigInteger[] second = v.divideAndRemainder(denominator);
      if (first[1].signum() != 0 || second[1].signum() != 0)
        return null;
      return new long[] {0, 0, x, y, first[0].longValueExact(), second[0].longValueExact()};
    }
  }

  static long[] solve(long[] input) {
    long[] sides = input.clone();
    Arrays.sort(sides);
    long radius = sides[0], length = sides[1], opposite = sides[2];
    long twiceDot = radius * radius + length * length - opposite * opposite;
    if (twiceDot % 2 != 0)
      return null;
    BigInteger dot = BigInteger.valueOf(twiceDot / 2);
    BigInteger square = BigInteger.valueOf(radius * radius)
                            .multiply(BigInteger.valueOf(length * length))
                            .subtract(dot.multiply(dot));
    if (square.signum() < 0)
      return null;
    BigInteger cross = integerRoot(square);
    if (!cross.multiply(cross).equals(square))
      return null;
    Geometry geometry = new Geometry(dot, cross, radius);
    long[] answer = geometry.point(radius, 0);
    if (answer != null)
      return answer;
    answer = geometry.point(0, radius);
    if (answer != null)
      return answer;
    for (long hypotenuse : divisors(radius)) {
      if (hypotenuse < MIN_HYPOTENUSE || hypotenuse % 2 == 0)
        continue;
      long end = smallRoot(hypotenuse - 1);
      for (long m = smallRoot(hypotenuse / 2) + 1; m <= end; m++) {
        long rest = hypotenuse - m * m, k = smallRoot(rest);
        if (k * k != rest || gcd(m, k) != 1 || (m - k) % 2 == 0)
          continue;
        long scale = radius / hypotenuse;
        long x = scale * (m * m - k * k), y = scale * 2 * m * k;
        answer = geometry.point(x, y);
        if (answer != null)
          return answer;
        answer = geometry.point(y, x);
        if (answer != null)
          return answer;
      }
    }
    return null;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    String line = input.readLine();
    if (line == null)
      return;
    StringTokenizer tokens = new StringTokenizer(line);
    long[] sides = new long[SIDE_COUNT];
    for (int i = 0; i < SIDE_COUNT; i++) sides[i] = Long.parseLong(tokens.nextToken());
    long[] answer = solve(sides);
    if (answer == null)
      System.out.println(-1);
    else {
      StringBuilder output = new StringBuilder();
      for (int i = 0; i < answer.length; i += 2)
        output.append(answer[i]).append(' ').append(answer[i + 1]).append('\n');
      System.out.print(output);
    }
  }
}
