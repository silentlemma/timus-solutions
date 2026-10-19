import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
  static final int TEAM_COUNT = 4;
  static final int WIN_POINTS = 3;
  static final int OUTCOME_COUNT = 3;
  static final int ORDER_COUNT = 24;

  static class Game {
    final int a, b, c, d;
    Game(int a, int b, int c, int d) {
      this.a = a;
      this.b = b;
      this.c = c;
      this.d = d;
    }
  }
  static class Row {
    final long[] coefficients;
    long bound;
    Row(long[] coefficients, long bound) {
      this.coefficients = coefficients;
      this.bound = bound;
    }
  }

  static long gcd(long a, long b) {
    a = Math.abs(a);
    b = Math.abs(b);
    while (b != 0) {
      long next = a % b;
      a = b;
      b = next;
    }
    return a;
  }

  static List<Row> simplify(List<Row> rows) {
    List<Row> unique = new ArrayList<>();
    for (Row row : rows) {
      long divisor = 0;
      for (long value : row.coefficients) divisor = gcd(divisor, value);
      if (divisor == 0) {
        if (row.bound < 0)
          return null;
        continue;
      }
      long[] coefficients = row.coefficients.clone();
      for (int i = 0; i < coefficients.length; i++) coefficients[i] /= divisor;
      long bound = Math.floorDiv(row.bound, divisor);
      Row found = null;
      for (Row current : unique) {
        if (Arrays.equals(current.coefficients, coefficients)) {
          found = current;
          break;
        }
      }
      if (found == null)
        unique.add(new Row(coefficients, bound));
      else
        found.bound = Math.min(found.bound, bound);
    }
    return unique;
  }

  static boolean integerFeasible(List<Row> input) {
    List<Row> rows = simplify(input);
    if (rows == null)
      return false;
    while (!rows.isEmpty()) {
      int dimension = rows.get(0).coefficients.length;
      int column = -1, bestCost = Integer.MAX_VALUE;
      for (int i = 0; i < dimension; i++) {
        int positive = 0, negative = 0;
        boolean unitUpper = true, unitLower = true;
        for (Row row : rows) {
          long value = row.coefficients[i];
          if (value > 0) {
            positive++;
            unitUpper = unitUpper && value == 1;
          }
          if (value < 0) {
            negative++;
            unitLower = unitLower && value == -1;
          }
        }
        if ((unitUpper || unitLower) && positive * negative < bestCost) {
          column = i;
          bestCost = positive * negative;
        }
      }
      List<Row> projected = new ArrayList<>();
      for (Row row : rows) {
        if (row.coefficients[column] == 0) {
          long[] coefficients = new long[dimension - 1];
          int at = 0;
          for (int i = 0; i < dimension; i++)
            if (i != column)
              coefficients[at++] = row.coefficients[i];
          projected.add(new Row(coefficients, row.bound));
        }
      }
      for (Row lower : rows)
        if (lower.coefficients[column] < 0) {
          for (Row upper : rows)
            if (upper.coefficients[column] > 0) {
              long[] coefficients = new long[dimension - 1];
              int at = 0;
              for (int i = 0; i < dimension; i++)
                if (i != column) {
                  coefficients[at++] = upper.coefficients[column] * lower.coefficients[i]
                      - lower.coefficients[column] * upper.coefficients[i];
                }
              long bound = upper.coefficients[column] * lower.bound
                  - lower.coefficients[column] * upper.bound;
              projected.add(new Row(coefficients, bound));
            }
        }
      rows = simplify(projected);
      if (rows == null)
        return false;
    }
    return true;
  }

  static boolean nextOrder(int[] order) {
    int i = TEAM_COUNT - 2;
    while (i >= 0 && order[i] >= order[i + 1]) i--;
    if (i < 0)
      return false;
    int j = TEAM_COUNT - 1;
    while (order[j] <= order[i]) j--;
    int saved = order[i];
    order[i] = order[j];
    order[j] = saved;
    for (int a = i + 1, b = TEAM_COUNT - 1; a < b; a++, b--) {
      saved = order[a];
      order[a] = order[b];
      order[b] = saved;
    }
    return true;
  }

  static List<int[]> possibleOrders(Game[] matches) {
    int[] initialPoints = new int[TEAM_COUNT];
    long[] initialDifference = new long[TEAM_COUNT];
    boolean[][] played = new boolean[TEAM_COUNT][TEAM_COUNT];
    for (Game game : matches) {
      played[game.a][game.b] = true;
      initialDifference[game.a] += game.c - game.d;
      initialDifference[game.b] += game.d - game.c;
      if (game.c == game.d) {
        initialPoints[game.a]++;
        initialPoints[game.b]++;
      } else
        initialPoints[game.c > game.d ? game.a : game.b] += WIN_POINTS;
    }
    List<int[]> remaining = new ArrayList<>();
    for (int a = 0; a < TEAM_COUNT; a++)
      for (int b = a + 1; b < TEAM_COUNT; b++) {
        if (!played[a][b])
          remaining.add(new int[] {a, b});
      }
    List<int[]> orders = new ArrayList<>();
    int[] permutation = new int[TEAM_COUNT];
    for (int i = 0; i < TEAM_COUNT; i++) permutation[i] = i;
    do {
      orders.add(permutation.clone());
    } while (nextOrder(permutation));
    boolean[] found = new boolean[ORDER_COUNT];
    int foundCount = 0, patternCount = 1;
    for (int i = 0; i < remaining.size(); i++) patternCount *= OUTCOME_COUNT;
    for (int pattern = 0; pattern < patternCount && foundCount < ORDER_COUNT; pattern++) {
      int code = pattern;
      int[] points = initialPoints.clone();
      long[] difference = initialDifference.clone();
      List<int[]> edges = new ArrayList<>();
      for (int[] pair : remaining) {
        int outcome = code % OUTCOME_COUNT;
        code /= OUTCOME_COUNT;
        if (outcome == 0) {
          points[pair[0]]++;
          points[pair[1]]++;
        } else {
          int winner = outcome == 1 ? pair[0] : pair[1], loser = outcome == 1 ? pair[1] : pair[0];
          points[winner] += WIN_POINTS;
          difference[winner]++;
          difference[loser]--;
          edges.add(new int[] {winner, loser});
        }
      }
      for (int index = 0; index < ORDER_COUNT; index++) {
        if (found[index])
          continue;
        int[] order = orders.get(index);
        boolean compatible = true;
        for (int i = 0; i + 1 < TEAM_COUNT; i++)
          if (points[order[i]] < points[order[i + 1]])
            compatible = false;
        if (!compatible)
          continue;
        List<Row> rows = new ArrayList<>();
        for (int column = 0; column < edges.size(); column++) {
          long[] coefficients = new long[edges.size()];
          coefficients[column] = -1;
          rows.add(new Row(coefficients, 0));
        }
        for (int i = 0; i + 1 < TEAM_COUNT; i++) {
          int a = order[i], b = order[i + 1];
          if (points[a] != points[b])
            continue;
          long[] coefficients = new long[edges.size()];
          for (int j = 0; j < edges.size(); j++) {
            int[] edge = edges.get(j);
            coefficients[j] = (edge[0] == b ? 1 : 0) - (edge[1] == b ? 1 : 0)
                - (edge[0] == a ? 1 : 0) + (edge[1] == a ? 1 : 0);
          }
          rows.add(new Row(coefficients, difference[a] - difference[b]));
        }
        if (integerFeasible(rows)) {
          found[index] = true;
          foundCount++;
        }
      }
    }
    List<int[]> result = new ArrayList<>();
    for (int i = 0; i < ORDER_COUNT; i++)
      if (found[i])
        result.add(orders.get(i));
    return result;
  }

  static class FastInput {
    final BufferedInputStream input = new BufferedInputStream(System.in);
    int nextInt() throws IOException {
      int c;
      do {
        c = input.read();
      } while (c <= ' ' && c != -1);
      int value = 0;
      while (c > ' ') {
        value = value * 10 + c - '0';
        c = input.read();
      }
      return value;
    }
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    Game[] matches = new Game[n];
    for (int i = 0; i < n; i++)
      matches[i] = new Game(in.nextInt() - 1, in.nextInt() - 1, in.nextInt(), in.nextInt());
    List<int[]> orders = possibleOrders(matches);
    StringBuilder out = new StringBuilder();
    out.append(orders.size()).append('\n');
    for (int[] order : orders) {
      for (int i = 0; i < TEAM_COUNT; i++) {
        if (i > 0)
          out.append(' ');
        out.append(order[i] + 1);
      }
      out.append('\n');
    }
    System.out.print(out);
  }
}
