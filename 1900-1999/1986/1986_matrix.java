import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
  static final int PERCENT = 100;
  static final long SCALE = 1000000;
  static final int DIGITS = 6;

  static BigInteger determinant(BigInteger[][] matrix) {
    int n = matrix.length;
    if (n == 0)
      return BigInteger.ONE;
    BigInteger[][] a = new BigInteger[n][];
    for (int i = 0; i < n; i++) a[i] = Arrays.copyOf(matrix[i], n);
    BigInteger previous = BigInteger.ONE;
    int sign = 1;
    for (int k = 0; k < n - 1; k++) {
      int pivotRow = k;
      while (pivotRow < n && a[pivotRow][k].signum() == 0) pivotRow++;
      if (pivotRow == n)
        return BigInteger.ZERO;
      if (pivotRow != k) {
        BigInteger[] temp = a[k];
        a[k] = a[pivotRow];
        a[pivotRow] = temp;
        sign = -sign;
      }
      BigInteger pivot = a[k][k];
      for (int row = k + 1; row < n; row++) {
        for (int col = k + 1; col < n; col++)
          a[row][col] =
              a[row][col].multiply(pivot).subtract(a[row][k].multiply(a[k][col])).divide(previous);
        a[row][k] = BigInteger.ZERO;
      }
      previous = pivot;
    }
    return a[n - 1][n - 1].multiply(BigInteger.valueOf(sign));
  }

  static String solve(String input) {
    Map<String, Map<String, Integer>> recipes = new TreeMap<>();
    TreeSet<String> parts = new TreeSet<>();
    for (String line : input.split("\n")) {
      if (line.trim().isEmpty())
        continue;
      String[] sides = line.split(":", 2), tokens = sides[1].trim().split("\\s+");
      Map<String, Integer> row = new TreeMap<>();
      for (int i = 0; i < tokens.length; i += 2) {
        row.put(tokens[i], Integer.parseInt(tokens[i + 1]));
        parts.add(tokens[i]);
      }
      recipes.put(sides[0].trim(), row);
    }
    List<String> names = new ArrayList<>(recipes.keySet());
    parts.removeAll(names);
    List<String> bases = new ArrayList<>(parts);
    int n = names.size(), m = bases.size();
    BigInteger[][] a = new BigInteger[n][n], numerators = new BigInteger[n][m];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        a[i][j] = BigInteger.valueOf(
            (i == j ? PERCENT : 0) - recipes.get(names.get(i)).getOrDefault(names.get(j), 0));
    BigInteger denominator = determinant(a);
    for (int col = 0; col < n; col++)
      for (int base = 0; base < m; base++) {
        BigInteger[][] replaced = new BigInteger[n][];
        for (int row = 0; row < n; row++) {
          replaced[row] = Arrays.copyOf(a[row], n);
          replaced[row][col] =
              BigInteger.valueOf(recipes.get(names.get(row)).getOrDefault(bases.get(base), 0));
        }
        numerators[col][base] = determinant(replaced);
      }
    StringBuilder output = new StringBuilder();
    BigInteger multiplier = BigInteger.valueOf(PERCENT * SCALE);
    for (int row = 0; row < n; row++) {
      long[] units = new long[m];
      long total = 0;
      int largest = 0;
      for (int base = 0; base < m; base++) {
        units[base] =
            numerators[row][base].multiply(multiplier).divide(denominator).longValueExact();
        total += units[base];
        if (numerators[row][base].compareTo(numerators[row][largest]) > 0)
          largest = base;
      }
      units[largest] += PERCENT * SCALE - total;
      output.append(names.get(row)).append(" :");
      for (int base = 0; base < m; base++) {
        output.append(' ')
            .append(bases.get(base))
            .append(' ')
            .append(units[base] / SCALE)
            .append('.');
        String fraction = Long.toString(units[base] % SCALE);
        for (int d = fraction.length(); d < DIGITS; d++) output.append('0');
        output.append(fraction);
      }
      output.append('\n');
    }
    return output.toString();
  }

  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder input = new StringBuilder();
    String line;
    while ((line = reader.readLine()) != null) input.append(line).append('\n');
    System.out.print(solve(input.toString()));
  }
}
