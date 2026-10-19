import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.function.Supplier;

public strictfp class Main {
  static final String STORM = "Storm";
  static final String BREATH = "Breath";
  static final String TAIL = "Tail";
  static final int INITIAL_ROOT_DIGITS = 16;
  static final int BOUND_ROOT_DIGITS = 32;
  static final int MASK_KEY_BITS = 16;
  static final int MISSING_PARENT = 255;
  static final int FRACTION_BITS = 52;
  static final int EXPONENT_BIAS = 1023;
  static final long FRACTION_MASK = (1L << FRACTION_BITS) - 1;
  static final long TEMPORARY_HEAP_LIMIT = 8L * 1024 * 1024;
  static final int COLLECTION_STRIDE = 32;

  static void compactTemporaryHeap() {
    Runtime runtime = Runtime.getRuntime();
    if (runtime.totalMemory() - runtime.freeMemory() >= TEMPORARY_HEAP_LIMIT) {
      System.gc();
    }
  }

  static final class Point {
    final long x, y;
    Point(long x, long y) {
      this.x = x;
      this.y = y;
    }
  }
  static final class Aura {
    final long cap, rise, fall;
    Aura(long cap, long rise, long fall) {
      this.cap = cap;
      this.rise = rise;
      this.fall = fall;
    }
  }
  static final class Spell {
    final String kind;
    final long power, duration;
    final Point[] places;
    Spell(String kind, long power, long duration, Point[] places) {
      this.kind = kind;
      this.power = power;
      this.duration = duration;
      this.places = places;
    }
  }
  static final class Interval {
    final double low, high;
    Interval(double low, double high) {
      this.low = low;
      this.high = high;
    }
  }
  static final Interval ZERO_INTERVAL = new Interval(0, 0);
  static double down(double x) {
    return Math.nextAfter(x, Double.NEGATIVE_INFINITY);
  }
  static double up(double x) {
    return Math.nextAfter(x, Double.POSITIVE_INFINITY);
  }
  static Interval interval(long x) {
    return new Interval(x, x);
  }
  static Interval add(Interval a, Interval b) {
    return new Interval(down(a.low + b.low), up(a.high + b.high));
  }
  static Interval subtract(Interval a, Interval b) {
    return new Interval(down(a.low - b.high), up(a.high - b.low));
  }
  static Interval multiply(Interval a, Interval b) {
    double x = a.low * b.low, y = a.low * b.high;
    double z = a.high * b.low, w = a.high * b.high;
    return new Interval(down(Math.min(Math.min(x, y), Math.min(z, w))),
        up(Math.max(Math.max(x, y), Math.max(z, w))));
  }
  static Interval divide(Interval a, long denominator) {
    return new Interval(down(a.low / denominator), up(a.high / denominator));
  }
  static Interval minimum(Interval a, Interval b) {
    return new Interval(Math.min(a.low, b.low), Math.min(a.high, b.high));
  }
  static Interval maximum(Interval a, Interval b) {
    return new Interval(Math.max(a.low, b.low), Math.max(a.high, b.high));
  }
  static Interval nonnegative(Interval a) {
    return maximum(ZERO_INTERVAL, a);
  }
  static long squaredDistance(Point a, Point b) {
    long x = a.x - b.x, y = a.y - b.y;
    return x * x + y * y;
  }
  static double travel(Point a, Point b, long speed) {
    return Math.sqrt(squaredDistance(a, b)) / speed;
  }

  static final class Rational implements Comparable<Rational> {
    static final Rational ZERO = new Rational(BigInteger.ZERO, BigInteger.ONE, true);
    static final Rational ONE = new Rational(BigInteger.ONE, BigInteger.ONE, true);
    final BigInteger numerator, denominator;
    Rational(BigInteger numerator, BigInteger denominator) {
      if (denominator.signum() == 0) {
        throw new ArithmeticException("zero divisor");
      }
      if (denominator.signum() < 0) {
        numerator = numerator.negate();
        denominator = denominator.negate();
      }
      BigInteger common = numerator.gcd(denominator);
      this.numerator = numerator.divide(common);
      this.denominator = denominator.divide(common);
    }
    Rational(BigInteger numerator, BigInteger denominator, boolean normalized) {
      this.numerator = numerator;
      this.denominator = denominator;
    }
    static Rational of(long value) {
      if (value == 0) {
        return ZERO;
      }
      if (value == 1) {
        return ONE;
      }
      return new Rational(BigInteger.valueOf(value), BigInteger.ONE, true);
    }
    static Rational fromDouble(double value) {
      if (value == 0) {
        return ZERO;
      }
      long raw = Double.doubleToLongBits(value);
      int exponent = (int) ((raw >>> FRACTION_BITS) & (2L * EXPONENT_BIAS + 1));
      long mantissa = raw & FRACTION_MASK;
      if (exponent == 0) {
        exponent = 1 - EXPONENT_BIAS - FRACTION_BITS;
      } else {
        mantissa |= 1L << FRACTION_BITS;
        exponent -= EXPONENT_BIAS + FRACTION_BITS;
      }
      BigInteger numerator = BigInteger.valueOf(mantissa);
      BigInteger denominator = BigInteger.ONE;
      if (exponent >= 0) {
        numerator = numerator.shiftLeft(exponent);
      } else {
        denominator = denominator.shiftLeft(-exponent);
      }
      if (raw < 0) {
        numerator = numerator.negate();
      }
      return new Rational(numerator, denominator);
    }
    Rational add(Rational other) {
      if (numerator.signum() == 0) {
        return other;
      }
      if (other.numerator.signum() == 0) {
        return this;
      }
      if (denominator.equals(other.denominator)) {
        return new Rational(numerator.add(other.numerator), denominator);
      }
      return new Rational(
          numerator.multiply(other.denominator).add(other.numerator.multiply(denominator)),
          denominator.multiply(other.denominator));
    }
    Rational negate() {
      if (numerator.signum() == 0) {
        return ZERO;
      }
      return new Rational(numerator.negate(), denominator, true);
    }
    Rational subtract(Rational other) {
      return this == other ? ZERO : add(other.negate());
    }
    Rational multiply(Rational other) {
      if (numerator.signum() == 0 || other.numerator.signum() == 0) {
        return ZERO;
      }
      return new Rational(
          numerator.multiply(other.numerator), denominator.multiply(other.denominator));
    }
    Rational divide(long other) {
      return new Rational(numerator, denominator.multiply(BigInteger.valueOf(other)));
    }
    int signum() {
      return numerator.signum();
    }
    public int compareTo(Rational other) {
      if (this == other) {
        return 0;
      }
      if (denominator.equals(other.denominator)) {
        return numerator.compareTo(other.numerator);
      }
      return numerator.multiply(other.denominator).compareTo(other.numerator.multiply(denominator));
    }
    double toDouble() {
      double result = numerator.doubleValue() / denominator.doubleValue();
      if (Double.isFinite(result)) {
        return result;
      }
      return new BigDecimal(numerator)
          .divide(new BigDecimal(denominator), MathContext.DECIMAL128)
          .doubleValue();
    }
  }
  static BigInteger integerSquareRoot(BigInteger value) {
    if (value.signum() == 0) {
      return BigInteger.ZERO;
    }
    BigInteger current = BigInteger.ONE.shiftLeft((value.bitLength() + 1) / 2);
    while (true) {
      BigInteger next = current.add(value.divide(current)).shiftRight(1);
      if (next.compareTo(current) >= 0) {
        return current;
      }
      current = next;
    }
  }
  static final Map<String, Rational[]> ROOT_BOUNDS = new HashMap<>();
  static Rational[] rootBounds(long radicand, int digits) {
    String key = radicand + ":" + digits;
    Rational[] known = ROOT_BOUNDS.get(key);
    if (known != null) {
      return known;
    }
    BigInteger denominator = BigInteger.TEN.pow(digits);
    BigInteger lower =
        integerSquareRoot(denominator.multiply(denominator).multiply(BigInteger.valueOf(radicand)));
    Rational[] result = {
        new Rational(lower, denominator), new Rational(lower.add(BigInteger.ONE), denominator)};
    ROOT_BOUNDS.put(key, result);
    return result;
  }

  // Sorted squarefree radicals make exact zero independent of numeric precision.
  static final class Surd implements Comparable<Surd> {
    static final Surd ZERO = new Surd(new long[0], new Rational[0]);
    final long[] radicands;
    final Rational[] coefficients;
    Surd(long[] radicands, Rational[] coefficients) {
      this.radicands = radicands;
      this.coefficients = coefficients;
    }
    static Surd of(long value) {
      return of(Rational.of(value));
    }
    static Surd of(Rational value) {
      return value.signum() == 0 ? ZERO : new Surd(new long[] {1}, new Rational[] {value});
    }
    Surd add(Surd other) {
      if (radicands.length == 0) {
        return other;
      }
      if (other.radicands.length == 0) {
        return this;
      }
      long[] keys = new long[radicands.length + other.radicands.length];
      Rational[] values = new Rational[keys.length];
      int first = 0, second = 0, count = 0;
      while (first < radicands.length || second < other.radicands.length) {
        long key;
        Rational value;
        if (second == other.radicands.length
            || (first < radicands.length && radicands[first] < other.radicands[second])) {
          key = radicands[first];
          value = coefficients[first++];
        } else if (first == radicands.length || other.radicands[second] < radicands[first]) {
          key = other.radicands[second];
          value = other.coefficients[second++];
        } else {
          key = radicands[first];
          value = coefficients[first++].add(other.coefficients[second++]);
        }
        if (value.signum() != 0) {
          keys[count] = key;
          values[count++] = value;
        }
      }
      return count == 0 ? ZERO : new Surd(Arrays.copyOf(keys, count), Arrays.copyOf(values, count));
    }
    Surd negate() {
      if (coefficients.length == 0) {
        return ZERO;
      }
      Rational[] values = new Rational[coefficients.length];
      for (int i = 0; i < values.length; i++) {
        values[i] = coefficients[i].negate();
      }
      return values.length == 0 ? ZERO : new Surd(radicands, values);
    }
    Surd subtract(Surd other) {
      return this == other ? ZERO : add(other.negate());
    }
    Surd multiply(Surd other) {
      TreeMap<Long, Rational> terms = new TreeMap<>();
      for (int i = 0; i < radicands.length; i++) {
        for (int j = 0; j < other.radicands.length; j++) {
          long common = gcd(radicands[i], other.radicands[j]);
          long key = (radicands[i] / common) * (other.radicands[j] / common);
          Rational value =
              coefficients[i].multiply(other.coefficients[j]).multiply(Rational.of(common));
          Rational previous = terms.get(key);
          if (previous != null) {
            value = value.add(previous);
          }
          if (value.signum() == 0) {
            terms.remove(key);
          } else {
            terms.put(key, value);
          }
        }
      }
      long[] keys = new long[terms.size()];
      Rational[] values = new Rational[keys.length];
      int index = 0;
      for (Map.Entry<Long, Rational> entry : terms.entrySet()) {
        keys[index] = entry.getKey();
        values[index++] = entry.getValue();
      }
      return keys.length == 0 ? ZERO : new Surd(keys, values);
    }
    Surd scale(long value) {
      if (value == 0) {
        return ZERO;
      }
      if (value == 1) {
        return this;
      }
      Rational[] result = new Rational[coefficients.length];
      for (int i = 0; i < result.length; i++) {
        result[i] = coefficients[i].multiply(Rational.of(value));
      }
      return result.length == 0 ? ZERO : new Surd(radicands, result);
    }
    Surd divide(long value) {
      if (value == 1) {
        return this;
      }
      Rational[] result = new Rational[coefficients.length];
      for (int i = 0; i < result.length; i++) {
        result[i] = coefficients[i].divide(value);
      }
      return result.length == 0 ? ZERO : new Surd(radicands, result);
    }
    Surd square() {
      return multiply(this);
    }
    Rational[] bounds(int digits) {
      Rational lower = Rational.ZERO, upper = Rational.ZERO;
      for (int i = 0; i < radicands.length; i++) {
        Rational value = coefficients[i];
        if (radicands[i] == 1) {
          lower = lower.add(value);
          upper = upper.add(value);
          continue;
        }
        Rational[] roots = rootBounds(radicands[i], digits);
        int left = value.signum() < 0 ? 1 : 0;
        lower = lower.add(value.multiply(roots[left]));
        upper = upper.add(value.multiply(roots[1 - left]));
      }
      return new Rational[] {lower, upper};
    }
    int signum() {
      if (coefficients.length == 0) {
        return 0;
      }
      if (coefficients.length == 1) {
        return coefficients[0].signum();
      }
      for (int digits = INITIAL_ROOT_DIGITS;; digits *= 2) {
        Rational[] enclosure = bounds(digits);
        if (enclosure[0].signum() > 0) {
          return 1;
        }
        if (enclosure[1].signum() < 0) {
          return -1;
        }
      }
    }
    public int compareTo(Surd other) {
      return this == other ? 0 : subtract(other).signum();
    }
    Interval floatBounds() {
      Rational[] exact = bounds(BOUND_ROOT_DIGITS);
      double lower = exact[0].toDouble(), upper = exact[1].toDouble();
      while (Rational.fromDouble(lower).compareTo(exact[0]) > 0) {
        lower = down(lower);
      }
      while (Rational.fromDouble(upper).compareTo(exact[1]) < 0) {
        upper = up(upper);
      }
      return new Interval(lower, upper);
    }
  }
  static long gcd(long a, long b) {
    while (b != 0) {
      long remainder = a % b;
      a = b;
      b = remainder;
    }
    return a;
  }
  static Surd min(Surd a, Surd b) {
    return a.compareTo(b) <= 0 ? a : b;
  }
  static Surd max(Surd a, Surd b) {
    return a.compareTo(b) >= 0 ? a : b;
  }
  static final Map<Long, Surd> ROOT_FACTORS = new HashMap<>();
  static Surd squareRoot(long value) {
    if (value == 0) {
      return Surd.ZERO;
    }
    Surd known = ROOT_FACTORS.get(value);
    if (known != null) {
      return known;
    }
    long remaining = value, outside = 1, inside = 1;
    for (long divisor = 2; divisor * divisor <= remaining; divisor++) {
      int count = 0;
      while (remaining % divisor == 0) {
        remaining /= divisor;
        count++;
      }
      for (int pair = 0; pair < count / 2; pair++) {
        outside *= divisor;
      }
      if ((count & 1) != 0) {
        inside *= divisor;
      }
    }
    Surd result = new Surd(new long[] {inside * remaining}, new Rational[] {Rational.of(outside)});
    ROOT_FACTORS.put(value, result);
    return result;
  }
  static Surd exactTravel(Point a, Point b, long speed) {
    return squareRoot(squaredDistance(a, b)).divide(speed);
  }
  static final int TRAVEL_KEY_BITS = 20;
  static final Map<Long, Interval> TRAVEL_BOUNDS = new HashMap<>();
  static Interval travelBounds(Point a, Point b, long speed) {
    long squared = squaredDistance(a, b);
    long key = (squared << TRAVEL_KEY_BITS) | speed;
    Interval known = TRAVEL_BOUNDS.get(key);
    if (known != null) {
      return known;
    }
    if (squared == 0) {
      return ZERO_INTERVAL;
    }
    double value = travel(a, b, speed), lower = down(value), upper = up(value);
    Rational target = Rational.of(squared), scale = Rational.of(speed * speed);
    while (Rational.fromDouble(lower)
               .multiply(Rational.fromDouble(lower))
               .multiply(scale)
               .compareTo(target)
        > 0) {
      lower = down(lower);
    }
    while (Rational.fromDouble(upper)
               .multiply(Rational.fromDouble(upper))
               .multiply(scale)
               .compareTo(target)
        < 0) {
      upper = up(upper);
    }
    Interval result = new Interval(lower, upper);
    TRAVEL_BOUNDS.put(key, result);
    return result;
  }

  static final class AuraValue {
    final double power, damage, deficit;
    AuraValue(double power, double damage, double deficit) {
      this.power = power;
      this.damage = damage;
      this.deficit = deficit;
    }
  }
  static AuraValue auraFloat(double start, Aura a, double running, double duration) {
    double falling = Math.min(running, start / a.fall);
    double after = Math.max(0, start - a.fall * running);
    double runArea = (start + after) * falling / 2;
    double runLoss =
        ((a.cap - start) + (a.cap - after)) * falling / 2 + a.cap * (running - falling);
    double casting = Math.max(0, duration - running);
    double rising = Math.min(casting, (a.cap - after) / a.rise);
    double finalPower = Math.min(a.cap, after + a.rise * casting);
    double castArea = (after + finalPower) * rising / 2 + a.cap * (casting - rising);
    double castLoss = ((a.cap - after) + (a.cap - finalPower)) * rising / 2;
    return new AuraValue(finalPower, runArea + castArea, runLoss + castLoss);
  }
  static Interval[] auraInterval(Interval start, Aura a, Interval running, Interval duration) {
    Interval cap = interval(a.cap);
    Interval falling = nonnegative(minimum(running, divide(start, a.fall)));
    Interval after = nonnegative(subtract(start, multiply(interval(a.fall), running)));
    Interval casting = nonnegative(subtract(duration, running));
    Interval rising =
        nonnegative(minimum(casting, divide(nonnegative(subtract(cap, after)), a.rise)));
    Interval finalPower = minimum(cap, add(after, multiply(interval(a.rise), casting)));
    Interval run =
        divide(multiply(add(nonnegative(subtract(cap, start)), nonnegative(subtract(cap, after))),
                   falling),
            2);
    run = add(run, multiply(cap, nonnegative(subtract(running, falling))));
    Interval cast = divide(
        multiply(
            add(nonnegative(subtract(cap, after)), nonnegative(subtract(cap, finalPower))), rising),
        2);
    return new Interval[] {finalPower, nonnegative(add(run, cast))};
  }
  static Surd[] exactAura(Surd start, Aura a, Surd running, Surd duration, boolean healing) {
    Surd cap = Surd.of(a.cap);
    if (start.subtract(cap).radicands.length == 0 && running.scale(a.fall).compareTo(cap) <= 0
        && running.scale(a.rise + a.fall).compareTo(duration.scale(a.rise)) <= 0) {
      Surd loss = running.square().scale(a.fall * (a.rise + a.fall)).divide(2 * a.rise);
      return new Surd[] {cap, healing ? loss : duration.scale(a.cap).subtract(loss)};
    }
    Surd after = max(Surd.ZERO, start.subtract(running.scale(a.fall)));
    Surd finalPower = min(cap, after.add(duration.subtract(running).scale(a.rise)));
    Surd run = start.square().subtract(after.square()).divide(2 * a.fall);
    Surd deficit =
        cap.subtract(after).square().subtract(cap.subtract(finalPower).square()).divide(2 * a.rise);
    Surd metric = healing ? running.scale(a.cap).subtract(run).add(deficit)
                          : run.add(duration.subtract(running).scale(a.cap)).subtract(deficit);
    return new Surd[] {finalPower, metric};
  }

  static final class Layout {
    final int[][] groups;
    final int[] ranks, offsets;
    Layout(int size) {
      int limit = 1 << size;
      int[] counts = new int[size + 1];
      for (int mask = 0; mask < limit; mask++) {
        counts[Integer.bitCount(mask)]++;
      }
      groups = new int[size + 1][];
      ranks = new int[limit];
      offsets = new int[size + 2];
      for (int count = 0; count <= size; count++) {
        groups[count] = new int[counts[count]];
        offsets[count + 1] = offsets[count] + counts[count] * counts[count];
      }
      Arrays.fill(counts, 0);
      for (int mask = 0; mask < limit; mask++) {
        int count = Integer.bitCount(mask), rank = counts[count]++;
        ranks[mask] = rank;
        groups[count][rank] = mask;
      }
    }
    int pairIndex(int first, int second) {
      int count = Integer.bitCount(first);
      return offsets[count] + ranks[first] * groups[count].length + ranks[second];
    }
  }
  static final Map<Integer, Layout> LAYOUTS = new HashMap<>();
  static Layout layoutFor(int size) {
    Layout result = LAYOUTS.get(size);
    if (result == null) {
      result = new Layout(size);
      LAYOUTS.put(size, result);
    }
    return result;
  }
  static final class CostTable {
    final double[] values;
    final Layout layout;
    final boolean pairs;
    CostTable(double[] values, Layout layout, boolean pairs) {
      this.values = values;
      this.layout = layout;
      this.pairs = pairs;
    }
    double get(int first, int second) {
      return values[pairs ? layout.pairIndex(first, second) : first];
    }
  }
  static CostTable assignment(
      double[][][] weights, int size, boolean pairs, boolean maximize, double cutoff) {
    int limit = 1 << size;
    Layout layout = layoutFor(size);
    int count = pairs ? layout.offsets[weights.length + 1] : limit;
    double[] result = new double[count];
    Arrays.fill(result, maximize ? -1 : cutoff);
    result[0] = 0;
    for (int actor = 0; actor < weights.length; actor++) {
      for (int left : layout.groups[actor]) {
        int[] seconds = pairs ? layout.groups[actor] : layout.groups[0];
        for (int right : seconds) {
          int index = pairs ? layout.pairIndex(left, right) : left;
          double current = result[index];
          if (maximize ? current < 0 : current >= cutoff) {
            continue;
          }
          for (int freeA = (limit - 1) ^ left; freeA != 0;) {
            int bitA = freeA & -freeA;
            freeA ^= bitA;
            int a = Integer.numberOfTrailingZeros(bitA);
            int freeB = pairs ? (limit - 1) ^ right : 1;
            for (; freeB != 0;) {
              int bitB = freeB & -freeB;
              freeB ^= bitB;
              int b = pairs ? Integer.numberOfTrailingZeros(bitB) : 0;
              int target = pairs ? layout.pairIndex(left | bitA, right | bitB) : left | bitA;
              double candidate = current + weights[actor][a][b];
              if (maximize ? candidate > result[target] : candidate < result[target]) {
                result[target] = candidate;
              }
            }
          }
        }
      }
    }
    return new CostTable(result, layout, pairs);
  }
  static int[] maskPlaces(int mask) {
    int[] result = new int[Integer.bitCount(mask)];
    int index = 0;
    for (; mask != 0;) {
      int bit = mask & -mask;
      mask ^= bit;
      result[index++] = Integer.numberOfTrailingZeros(bit);
    }
    return result;
  }
  static Surd[][][] restrictWeights(Surd[][][] weights, int first, int second, boolean pairs) {
    int[] left = maskPlaces(first), right = pairs ? maskPlaces(second) : new int[] {0};
    Surd[][][] result = new Surd[weights.length][left.length][right.length];
    for (int actor = 0; actor < weights.length; actor++) {
      for (int a = 0; a < left.length; a++) {
        for (int b = 0; b < right.length; b++) {
          result[actor][a][b] = weights[actor][left[a]][right[b]];
        }
      }
    }
    return result;
  }
  static boolean sameMatrix(Surd[][] a, Surd[][] b) {
    if (a == b) {
      return true;
    }
    for (int i = 0; i < a.length; i++) {
      for (int j = 0; j < a[i].length; j++) {
        if (a[i][j].subtract(b[i][j]).radicands.length != 0) {
          return false;
        }
      }
    }
    return true;
  }
  static int[] path(int index, int people, int size, boolean pairs, Layout layout, byte[] parent) {
    int[] result = new int[people];
    while (people > 0) {
      int code = parent[index] & MISSING_PARENT;
      result[--people] = code;
      int a = pairs ? code / size : code, b = pairs ? code % size : 0;
      if (pairs) {
        int rank = index - layout.offsets[people + 1];
        int width = layout.groups[people + 1].length;
        int first = layout.groups[people + 1][rank / width] ^ (1 << a);
        int second = layout.groups[people + 1][rank % width] ^ (1 << b);
        index = layout.pairIndex(first, second);
      } else {
        index ^= 1 << a;
      }
    }
    return result;
  }
  static Surd restrictedOptimum(Surd[][][] weights, boolean pairs) {
    int size = weights.length;
    boolean identical = true;
    for (int actor = 1; actor < size; actor++) {
      identical &= sameMatrix(weights[actor], weights[0]);
    }
    if (identical) {
      if (!pairs) {
        Surd sum = Surd.ZERO;
        for (Surd[] row : weights[0]) {
          sum = sum.add(row[0]);
        }
        return sum;
      }
      Surd[][] matrix = weights[0];
      weights = new Surd[size][size][1];
      for (int actor = 0; actor < size; actor++) {
        for (int place = 0; place < size; place++) {
          weights[actor][place][0] = matrix[actor][place];
        }
      }
      pairs = false;
    }
    Layout layout = layoutFor(size);
    int limit = 1 << size, count = pairs ? layout.offsets[size + 1] : limit;
    double[] lower = new double[count], upper = new double[count];
    Arrays.fill(lower, Double.POSITIVE_INFINITY);
    Arrays.fill(upper, Double.POSITIVE_INFINITY);
    byte[] parent = new byte[count];
    Arrays.fill(parent, (byte) MISSING_PARENT);
    lower[0] = 0;
    upper[0] = 0;
    Interval[][][] bounds = new Interval[size][size][pairs ? size : 1];
    int completed = 0;
    for (int actor = 0; actor < size; actor++) {
      for (int a = 0; a < size; a++) {
        for (int b = 0; b < bounds[actor][a].length; b++) {
          bounds[actor][a][b] = weights[actor][a][b].floatBounds();
          if (++completed % COLLECTION_STRIDE == 0) {
            compactTemporaryHeap();
          }
        }
      }
    }
    for (int actor = 0; actor < size; actor++) {
      Map<Integer, int[]> previousPaths = new HashMap<>();
      for (int left : layout.groups[actor]) {
        for (int right : pairs ? layout.groups[actor] : layout.groups[0]) {
          int index = pairs ? layout.pairIndex(left, right) : left;
          if (Double.isInfinite(lower[index])) {
            continue;
          }
          for (int freeA = (limit - 1) ^ left; freeA != 0;) {
            int bitA = freeA & -freeA;
            freeA ^= bitA;
            int a = Integer.numberOfTrailingZeros(bitA);
            for (int freeB = pairs ? (limit - 1) ^ right : 1; freeB != 0;) {
              int bitB = freeB & -freeB;
              freeB ^= bitB;
              int b = pairs ? Integer.numberOfTrailingZeros(bitB) : 0;
              int target = pairs ? layout.pairIndex(left | bitA, right | bitB) : left | bitA;
              Interval weight = bounds[actor][a][b];
              double low = down(lower[index] + weight.low), high = up(upper[index] + weight.high);
              boolean choose = Double.isInfinite(lower[target]) || high < lower[target];
              if (!choose && low < upper[target]) {
                int[] previous = previousPaths.get(index);
                if (previous == null) {
                  previous = path(index, actor, size, pairs, layout, parent);
                  previousPaths.put(index, previous);
                }
                int[] incumbent = path(target, actor + 1, size, pairs, layout, parent);
                Surd difference = Surd.ZERO;
                for (int person = 0; person <= actor; person++) {
                  int newCode = person == actor ? (pairs ? a * size + b : a) : previous[person];
                  int oldCode = incumbent[person];
                  if (newCode == oldCode) {
                    continue;
                  }
                  int na = pairs ? newCode / size : newCode, nb = pairs ? newCode % size : 0;
                  int oa = pairs ? oldCode / size : oldCode, ob = pairs ? oldCode % size : 0;
                  difference =
                      difference.add(weights[person][na][nb].subtract(weights[person][oa][ob]));
                }
                choose = difference.signum() < 0;
                if (++completed % COLLECTION_STRIDE == 0) {
                  compactTemporaryHeap();
                }
              }
              if (choose) {
                lower[target] = low;
                upper[target] = high;
                parent[target] = (byte) (pairs ? a * size + b : a);
              }
            }
          }
        }
      }
    }
    int finalIndex = pairs ? layout.pairIndex(limit - 1, limit - 1) : limit - 1;
    int[] chosen = path(finalIndex, size, size, pairs, layout, parent);
    Surd result = Surd.ZERO;
    for (int actor = 0; actor < size; actor++) {
      int code = chosen[actor];
      result = result.add(weights[actor][pairs ? code / size : code][pairs ? code % size : 0]);
    }
    return result;
  }

  static final class Group {
    final double[][][] weights;
    final double error;
    Group(double[][][] weights, double error) {
      this.weights = weights;
      this.error = error;
    }
  }
  static final class Candidates {
    int[] first = new int[1], second = new int[1];
    double[] values = new double[1];
    int count;
    void add(int a, int b, double value) {
      if (count == values.length) {
        int length = count * 2;
        first = Arrays.copyOf(first, length);
        second = Arrays.copyOf(second, length);
        values = Arrays.copyOf(values, length);
      }
      first[count] = a;
      second[count] = b;
      values[count++] = value;
    }
    Candidates retained(double threshold, double error) {
      Candidates kept = new Candidates();
      for (int i = 0; i < count; i++) {
        if (up(values[i] + error) >= threshold) {
          kept.add(first[i], second[i], values[i]);
        }
      }
      return kept;
    }
    Integer[] order() {
      Integer[] order = new Integer[count];
      for (int i = 0; i < count; i++) {
        order[i] = i;
      }
      Arrays.sort(order, (a, b) -> Double.compare(values[b], values[a]));
      return order;
    }
  }
  static final class Damage {
    final Interval bounds;
    Supplier<Surd> refine;
    Surd exact;
    Damage(double value, double error, Supplier<Surd> refine) {
      bounds = new Interval(down(value - error), up(value + error));
      this.refine = refine;
    }
    Surd exactValue() {
      if (refine != null) {
        exact = refine.get();
        refine = null;
      }
      return exact;
    }
  }
  static final class Block {
    final Aura[] attackers, healers;
    final long health, speed;
    final Point start;
    final Spell[] breaths;
    final Spell storm;
    final boolean initial;
    final double latest;
    final Interval latestBounds;
    Block(Aura[] attackers, Aura[] healers, long health, long speed, Point start, Spell[] breaths,
        Spell storm, boolean initial) {
      this.attackers = attackers;
      this.healers = healers;
      this.health = health;
      this.speed = speed;
      this.start = start;
      this.breaths = breaths;
      this.storm = storm;
      this.initial = initial;
      double longest = travel(start, storm.places[0], speed);
      Interval enclosure = travelBounds(start, storm.places[0], speed);
      if (breaths.length != 0) {
        longest = 0;
        enclosure = ZERO_INTERVAL;
        for (Point place : breaths[breaths.length - 1].places) {
          longest = Math.max(longest, travel(place, storm.places[0], speed));
          enclosure = maximum(enclosure, travelBounds(place, storm.places[0], speed));
        }
      }
      latest = longest;
      latestBounds = enclosure;
    }
    Surd exactLatest() {
      if (breaths.length == 0) {
        return exactTravel(start, storm.places[0], speed);
      }
      Surd longest = Surd.ZERO;
      for (Point place : breaths[breaths.length - 1].places) {
        longest = max(longest, exactTravel(place, storm.places[0], speed));
      }
      return longest;
    }
    long healerCaps() {
      long sum = 0;
      for (Aura a : healers) {
        sum += a.cap;
      }
      return sum;
    }
    long fixedLoss() {
      long sum = 0, caps = healerCaps();
      for (Spell s : breaths) {
        sum += (s.power - caps) * s.duration;
      }
      return sum;
    }
    Surd exactBudget() {
      return Surd.of(health - fixedLoss())
          .subtract(exactLatest().scale(storm.power - healerCaps()));
    }
    Surd[][][] exactGroup(Aura[] auras, boolean healing) {
      Spell first = breaths.length == 0 ? storm : breaths[0];
      int size = first.places.length;
      Surd[] outgoing = new Surd[size];
      for (int a = 0; a < size; a++) {
        outgoing[a] = exactTravel(start, first.places[a], speed);
      }
      Surd[] returning = breaths.length == 0 ? new Surd[0] : new Surd[size];
      Surd longest = exactLatest();
      for (int a = 0; a < returning.length; a++) {
        returning[a] = exactTravel(breaths[breaths.length - 1].places[a], storm.places[0], speed);
      }
      boolean pairs = breaths.length == 2;
      Surd[][] between = new Surd[size][pairs ? size : 0];
      if (pairs) {
        for (int a = 0; a < size; a++) {
          for (int b = 0; b < size; b++) {
            between[a][b] = exactTravel(first.places[a], breaths[1].places[b], speed);
          }
        }
      }
      Surd[][][] result = new Surd[auras.length][size][pairs ? size : 1];
      int completed = 0;
      for (int actor = 0; actor < auras.length; actor++) {
        Aura aura = auras[actor];
        int identical = -1;
        for (int previous = 0; previous < actor; previous++) {
          Aura other = auras[previous];
          if (aura.cap == other.cap && aura.rise == other.rise && aura.fall == other.fall) {
            identical = previous;
            break;
          }
        }
        if (identical >= 0) {
          result[actor] = result[identical];
          continue;
        }
        Surd power = Surd.of(initial && !healing ? 0 : aura.cap);
        for (int a = 0; a < size; a++) {
          Surd duration = healing && breaths.length == 0 ? longest : Surd.of(first.duration);
          Surd[] state = exactAura(power, aura, outgoing[a], duration, healing);
          for (int b = 0; b < result[actor][a].length; b++) {
            Surd value = state[1];
            if (breaths.length != 0) {
              Surd at = state[0];
              int slot = a;
              if (pairs) {
                Surd[] middle =
                    exactAura(at, aura, between[a][b], Surd.of(breaths[1].duration), healing);
                at = middle[0];
                value = value.add(middle[1]);
                slot = b;
              }
              Surd end = healing ? longest : Surd.of(storm.duration);
              value = value.add(exactAura(at, aura, returning[slot], end, healing)[1]);
            }
            result[actor][a][b] = value;
            if (++completed % COLLECTION_STRIDE == 0) {
              compactTemporaryHeap();
            }
          }
        }
      }
      return result;
    }
    Group group(Aura[] auras, boolean healing) {
      Spell first = breaths.length == 0 ? storm : breaths[0];
      int size = first.places.length;
      boolean pairs = breaths.length == 2;
      double[] outgoing = new double[size], returning = new double[size];
      Interval[] outBounds = new Interval[size], retBounds = new Interval[size];
      double[][] between = new double[size][pairs ? size : 0];
      Interval[][] betweenBounds = new Interval[size][pairs ? size : 0];
      for (int a = 0; a < size; a++) {
        outgoing[a] = travel(start, first.places[a], speed);
        outBounds[a] = travelBounds(start, first.places[a], speed);
        if (breaths.length != 0) {
          Point place = breaths[breaths.length - 1].places[a];
          returning[a] = travel(place, storm.places[0], speed);
          retBounds[a] = travelBounds(place, storm.places[0], speed);
        }
        if (pairs) {
          for (int b = 0; b < size; b++) {
            between[a][b] = travel(first.places[a], breaths[1].places[b], speed);
            betweenBounds[a][b] = travelBounds(first.places[a], breaths[1].places[b], speed);
          }
        }
      }
      double[][][] result = new double[auras.length][][];
      double error = 0, largestSum = 0;
      double[] individualErrors = new double[auras.length];
      double[] individualWeights = new double[auras.length];
      int completed = 0;
      for (int actor = 0; actor < auras.length; actor++) {
        Aura aura = auras[actor];
        int identical = -1;
        for (int previous = 0; previous < actor; previous++) {
          Aura other = auras[previous];
          if (aura.cap == other.cap && aura.rise == other.rise && aura.fall == other.fall) {
            identical = previous;
            break;
          }
        }
        if (identical >= 0) {
          result[actor] = result[identical];
          individualErrors[actor] = individualErrors[identical];
          individualWeights[actor] = individualWeights[identical];
          error = up(error + individualErrors[actor]);
          largestSum = up(largestSum + individualWeights[actor]);
          continue;
        }
        result[actor] = new double[size][pairs ? size : 1];
        long initialPower = initial && !healing ? 0 : aura.cap;
        double largestError = 0, largestWeight = 0;
        for (int a = 0; a < size; a++) {
          double duration = healing && breaths.length == 0 ? latest : first.duration;
          Interval durationBounds =
              healing && breaths.length == 0 ? latestBounds : interval(first.duration);
          AuraValue state = auraFloat(initialPower, aura, outgoing[a], duration);
          Interval[] stateBounds =
              auraInterval(interval(initialPower), aura, outBounds[a], durationBounds);
          for (int b = 0; b < result[actor][a].length; b++) {
            double value = healing ? state.deficit : state.damage;
            Interval loss = stateBounds[1], area = multiply(interval(aura.cap), durationBounds);
            if (breaths.length != 0) {
              AuraValue middle = state;
              Interval powerBound = stateBounds[0];
              int slot = a;
              if (pairs) {
                middle = auraFloat(state.power, aura, between[a][b], breaths[1].duration);
                Interval[] middleBounds = auraInterval(
                    powerBound, aura, betweenBounds[a][b], interval(breaths[1].duration));
                powerBound = middleBounds[0];
                loss = add(loss, middleBounds[1]);
                area = add(area, interval(aura.cap * breaths[1].duration));
                value += healing ? middle.deficit : middle.damage;
                slot = b;
              }
              double end = healing ? latest : storm.duration;
              Interval endBounds = healing ? latestBounds : interval(storm.duration);
              AuraValue finalState = auraFloat(middle.power, aura, returning[slot], end);
              Interval[] finalBounds = auraInterval(powerBound, aura, retBounds[slot], endBounds);
              loss = add(loss, finalBounds[1]);
              area = add(area, multiply(interval(aura.cap), endBounds));
              value += healing ? finalState.deficit : finalState.damage;
            }
            Interval enclosure = healing ? loss : subtract(area, loss);
            largestError = up(Math.max(largestError,
                Math.max(Math.abs(value - enclosure.low), Math.abs(enclosure.high - value))));
            largestWeight = Math.max(largestWeight,
                Math.max(
                    Math.abs(value), Math.max(Math.abs(enclosure.low), Math.abs(enclosure.high))));
            result[actor][a][b] = value;
            if (++completed % COLLECTION_STRIDE == 0) {
              compactTemporaryHeap();
            }
          }
        }
        individualErrors[actor] = largestError;
        individualWeights[actor] = largestWeight;
        error = up(error + largestError);
        largestSum = up(largestSum + largestWeight);
      }
      return new Group(result, up(error + 2 * auras.length * Math.ulp(largestSum)));
    }
    Surd exactDamage(Candidates candidates, double error) {
      Surd[][][] weights = exactGroup(attackers, false);
      if (breaths.length == 0) {
        Surd total = Surd.ZERO;
        for (Surd[][] person : weights) {
          total = total.add(person[0][0]);
        }
        return total;
      }
      boolean pairs = breaths.length == 2;
      Surd globalUpper = Surd.ZERO;
      for (Surd[][] person : weights) {
        Surd largest = person[0][0];
        for (Surd[] row : person) {
          for (Surd value : row) {
            largest = max(largest, value);
          }
        }
        globalUpper = globalUpper.add(largest);
      }
      for (int index = 0; index < candidates.count; index++) {
        if (pairs && candidates.first[index] != candidates.second[index]) {
          continue;
        }
        int[] places = maskPlaces(candidates.first[index]);
        Surd diagonal = Surd.ZERO;
        for (int actor = 0; actor < places.length; actor++) {
          int place = places[actor];
          diagonal = diagonal.add(weights[actor][place][pairs ? place : 0]);
        }
        if (diagonal.subtract(globalUpper).radicands.length == 0) {
          return globalUpper;
        }
        break;
      }
      Surd best = null;
      double bestLower = Double.NEGATIVE_INFINITY;
      for (int index : candidates.order()) {
        if (up(candidates.values[index] + error) < bestLower) {
          break;
        }
        Surd[][][] part =
            restrictWeights(weights, candidates.first[index], candidates.second[index], pairs);
        Surd upper = Surd.ZERO, diagonal = Surd.ZERO;
        for (int actor = 0; actor < part.length; actor++) {
          Surd largest = part[actor][0][0];
          for (Surd[] row : part[actor]) {
            for (Surd value : row) {
              largest = max(largest, value);
            }
          }
          upper = upper.add(largest);
          diagonal = diagonal.add(part[actor][actor][pairs ? actor : 0]);
        }
        if (best != null && upper.compareTo(best) <= 0) {
          continue;
        }
        Surd value = upper;
        if (diagonal.subtract(upper).radicands.length != 0) {
          Surd[][][] negative = new Surd[part.length][][];
          for (int actor = 0; actor < part.length; actor++) {
            negative[actor] = new Surd[part[actor].length][];
            for (int a = 0; a < part[actor].length; a++) {
              negative[actor][a] = new Surd[part[actor][a].length];
              for (int b = 0; b < part[actor][a].length; b++) {
                negative[actor][a][b] = part[actor][a][b].negate();
              }
            }
          }
          value = restrictedOptimum(negative, pairs).negate();
        }
        if (best == null || value.compareTo(best) > 0) {
          best = value;
          if (best.subtract(globalUpper).radicands.length == 0) {
            return best;
          }
          bestLower = best.floatBounds().low;
        }
      }
      return best;
    }
    Damage damage() {
      double budget = health - fixedLoss() - (storm.power - healerCaps()) * latest;
      Interval budgetBounds = subtract(interval(health - fixedLoss()),
          multiply(interval(storm.power - healerCaps()), latestBounds));
      if (budgetBounds.high <= 0) {
        return null;
      }
      Group healerGroup = group(healers, true);
      double error = up(healerGroup.error
          + up(
              Math.max(Math.abs(budget - budgetBounds.low), Math.abs(budgetBounds.high - budget))));
      SurvivalCheck survivalCheck = new SurvivalCheck(this, budget, error);
      if (breaths.length == 0) {
        double loss = 0;
        for (double[][] person : healerGroup.weights) {
          loss += person[0][0];
        }
        if (!survivalCheck.survives(loss, 0, 0)) {
          return null;
        }
        Group attackersGroup = group(attackers, false);
        double value = 0;
        for (double[][] person : attackersGroup.weights) {
          value += person[0][0];
        }
        return new Damage(
            value, attackersGroup.error, () -> exactDamage(null, attackersGroup.error));
      }
      int size = attackers.length + healers.length, full = (1 << size) - 1;
      boolean pairs = breaths.length == 2;
      int[] masks = layoutFor(size).groups[healers.length];
      double upperLoss = 0;
      for (double[][] person : healerGroup.weights) {
        double largest = 0;
        for (double[] row : person) {
          for (double value : row) {
            largest = Math.max(largest, value);
          }
        }
        upperLoss = up(upperLoss + largest);
      }
      boolean allSurvive = up(upperLoss + error) < budget;
      CostTable survival = allSurvive
          ? null
          : assignment(healerGroup.weights, size, pairs, false, up(budget + error));
      boolean any = allSurvive;
    search:
      for (int first : masks) {
        if (any) {
          break;
        }
        for (int second : pairs ? masks : layoutFor(size).groups[0]) {
          if (survivalCheck.survives(survival.get(first, second), first, second)) {
            any = true;
            break search;
          }
        }
      }
      if (!any) {
        return null;
      }
      Group attackersGroup = group(attackers, false);
      CostTable damage =
          assignment(attackersGroup.weights, size, pairs, true, Double.POSITIVE_INFINITY);
      Candidates candidates = new Candidates();
      double best = Double.NEGATIVE_INFINITY;
      for (int first : masks) {
        for (int second : pairs ? masks : layoutFor(size).groups[0]) {
          if (!allSurvive && !survivalCheck.survives(survival.get(first, second), first, second)) {
            continue;
          }
          int left = full ^ first, right = pairs ? full ^ second : 0;
          double value = damage.get(left, right);
          best = Math.max(best, value);
          candidates.add(left, right, value);
        }
      }
      Candidates retained =
          candidates.retained(down(best - attackersGroup.error), attackersGroup.error);
      return new Damage(
          best, attackersGroup.error, () -> exactDamage(retained, attackersGroup.error));
    }
  }
  static final class SurvivalCheck {
    final Block block;
    final double budget, error;
    SurvivalRefiner refiner;
    SurvivalCheck(Block block, double budget, double error) {
      this.block = block;
      this.budget = budget;
      this.error = error;
    }
    boolean survives(double value, int first, int second) {
      if (Double.isInfinite(value)) {
        return false;
      }
      if (up(value + error) < budget) {
        return true;
      }
      if (down(value - error) >= budget) {
        return false;
      }
      if (block.breaths.length == 0) {
        Surd loss = Surd.ZERO;
        for (Surd[][] person : block.exactGroup(block.healers, true)) {
          loss = loss.add(person[0][0]);
        }
        return loss.compareTo(block.exactBudget()) < 0;
      }
      if (refiner == null) {
        refiner = new SurvivalRefiner(block);
      }
      return refiner.feasible(first, second);
    }
  }
  static final class SurvivalRefiner {
    final Surd[][][] weights;
    final Surd budget;
    final boolean pairs;
    final Map<Integer, Boolean> cache = new HashMap<>();
    SurvivalRefiner(Block block) {
      weights = block.exactGroup(block.healers, true);
      budget = block.exactBudget();
      pairs = block.breaths.length == 2;
    }
    boolean feasible(int first, int second) {
      int key = (first << MASK_KEY_BITS) | second;
      Boolean known = cache.get(key);
      if (known != null) {
        return known;
      }
      Surd[][][] part = restrictWeights(weights, first, second, pairs);
      Surd lower = Surd.ZERO, diagonal = Surd.ZERO;
      for (int actor = 0; actor < part.length; actor++) {
        Surd smallest = part[actor][0][0];
        for (Surd[] row : part[actor]) {
          for (Surd value : row) {
            smallest = min(smallest, value);
          }
        }
        lower = lower.add(smallest);
        diagonal = diagonal.add(part[actor][actor][pairs ? actor : 0]);
      }
      boolean result = false;
      if (lower.compareTo(budget) < 0) {
        result =
            diagonal.compareTo(budget) < 0 || restrictedOptimum(part, pairs).compareTo(budget) < 0;
      }
      cache.put(key, result);
      if (cache.size() % COLLECTION_STRIDE == 0) {
        compactTemporaryHeap();
      }
      return result;
    }
  }
  static boolean killed(List<Damage> amounts, long health) {
    Interval total = ZERO_INTERVAL;
    for (Damage amount : amounts) {
      total = add(total, amount.bounds);
    }
    if (total.low >= health) {
      return true;
    }
    if (total.high < health) {
      return false;
    }
    Surd exact = Surd.ZERO;
    for (Damage amount : amounts) {
      exact = exact.add(amount.exactValue());
    }
    return exact.compareTo(Surd.of(health)) >= 0;
  }
  static int solve(
      Aura[] attackers, Aura[] healers, long health, long speed, long dragon, Spell[] spells) {
    Point start = new Point(0, 0);
    boolean initial = true;
    List<Spell> breaths = new ArrayList<>();
    List<Damage> amounts = new ArrayList<>();
    for (int index = 0; index < spells.length; index++) {
      Spell spell = spells[index];
      if (spell.kind.equals(TAIL)) {
        break;
      }
      if (spell.kind.equals(BREATH)) {
        breaths.add(spell);
        continue;
      }
      Block block = new Block(
          attackers, healers, health, speed, start, breaths.toArray(new Spell[0]), spell, initial);
      Damage amount = block.damage();
      if (amount == null) {
        return 0;
      }
      amounts.add(amount);
      compactTemporaryHeap();
      if (killed(amounts, dragon)) {
        return index + 1;
      }
      start = spell.places[0];
      initial = false;
      breaths.clear();
    }
    return 0;
  }
  static final class FastInput {
    final InputStream stream;
    FastInput(InputStream stream) {
      this.stream = new BufferedInputStream(stream);
    }
    String next() throws IOException {
      StringBuilder result = new StringBuilder();
      int symbol;
      do {
        symbol = stream.read();
      } while (symbol >= 0 && symbol <= ' ');
      while (symbol > ' ') {
        result.append((char) symbol);
        symbol = stream.read();
      }
      return result.toString();
    }
    long nextLong() throws IOException {
      return Long.parseLong(next());
    }
    int nextInt() throws IOException {
      return Integer.parseInt(next());
    }
  }
  static int readAndSolve(FastInput input) throws IOException {
    int n = input.nextInt(), m = input.nextInt(), k = input.nextInt();
    long health = input.nextLong(), speed = input.nextLong(), dragon = input.nextLong();
    Aura[] attackers = new Aura[n], healers = new Aura[m];
    for (int i = 0; i < n; i++) {
      attackers[i] = new Aura(input.nextLong(), input.nextLong(), input.nextLong());
    }
    for (int i = 0; i < m; i++) {
      healers[i] = new Aura(input.nextLong(), input.nextLong(), input.nextLong());
    }
    Spell[] spells = new Spell[k];
    for (int i = 0; i < k; i++) {
      String kind = input.next();
      long power = 0, duration = 0;
      Point[] places = new Point[0];
      if (!kind.equals(TAIL)) {
        power = input.nextLong();
        duration = input.nextLong();
        places = new Point[kind.equals(BREATH) ? n + m : 1];
        for (int j = 0; j < places.length; j++) {
          places[j] = new Point(input.nextLong(), input.nextLong());
        }
      }
      spells[i] = new Spell(kind, power, duration, places);
    }
    return solve(attackers, healers, health, speed, dragon, spells);
  }
  public static void main(String[] args) throws IOException {
    int answer = readAndSolve(new FastInput(System.in));
    if (answer == 0) {
      System.out.println("You are not prepared");
    } else {
      System.out.println("No useful loot again\n" + answer);
    }
  }
}
