import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static final int SMALL_ODD_LIMIT = 5;
  static final int FIRST_ODD_PRIME = 3;
  static final int COLUMN = 2;

  static class Builder {
    int[][] grid;
    int value;
    Builder(int n) {
      grid = new int[n][n];
    }
    void visit(int row, int col) {
      grid[row][col] = ++value;
    }
  }

  static int[][] construct(int n) {
    Builder b = new Builder(n);
    if (n % 2 == 1 && n < SMALL_ODD_LIMIT) {
      for (int row = 0; row < n; row++) {
        for (int step = 0; step < n; step++) b.visit(row, row % 2 == 0 ? step : n - 1 - step);
      }
      return b.grid;
    }
    int limit = n * n;
    boolean[] prime = new boolean[limit + 1];
    Arrays.fill(prime, 2, limit + 1, true);
    for (int p = 2; p * p <= limit; p++) {
      if (prime[p]) {
        for (int multiple = p * p; multiple <= limit; multiple += p) prime[multiple] = false;
      }
    }
    int[] following = new int[limit + 1], widths = new int[n];
    int largest = 0;
    for (int p = limit; p >= 0; p--) {
      following[p] = largest;
      if (prime[p])
        largest = p;
    }
    if (n % 2 == 0) {
      b.visit(0, 1);
      b.visit(0, 0);
      b.visit(1, 0);
      for (int row = 1; row < n - 2; row += 2) {
        int width = (following[b.value] - b.value - 2) / 2;
        widths[row] = width;
        for (int col = 1; col <= width; col++) b.visit(row, col);
        b.visit(row + 1, width);
        for (int col = width - 1; col >= 0; col--) b.visit(row + 1, col);
        b.visit(row + 2, 0);
      }
      for (int col = 1; col < n; col++) b.visit(n - 1, col);
      for (int row = n - 2; row > 1; row -= 2) {
        int width = widths[row - 1];
        for (int col = n - 1; col > width; col--) b.visit(row, col);
        for (int col = width + 1; col < n; col++) b.visit(row - 1, col);
      }
      for (int col = n - 1; col > 1; col--) b.visit(0, col);
      return b.grid;
    }
    int rightWidth = n - COLUMN - 1, initial = -1;
    for (int candidate = 0; candidate <= rightWidth; candidate++) {
      if (candidate == rightWidth - 1)
        continue;
      int first = FIRST_ODD_PRIME + 2 * candidate, current = first + 2 * n;
      if (!prime[first] || !prime[current])
        continue;
      boolean valid = true;
      for (int row = n - 1; row > COLUMN + 1; row -= 2) {
        int nextPrime = following[current], width = (nextPrime - current - 2) / 2;
        if (width < 0 || width >= rightWidth) {
          valid = false;
          break;
        }
        widths[row] = width;
        current = nextPrime;
      }
      if (valid) {
        initial = candidate;
        break;
      }
    }
    if (initial < 0)
      throw new IllegalStateException("No admissible prime prefix");
    b.visit(1, 1);
    b.visit(1, COLUMN);
    for (int col = COLUMN + 1; col <= COLUMN + initial; col++) b.visit(1, col);
    for (int col = COLUMN + initial; col >= COLUMN; col--) b.visit(0, col);
    b.visit(0, 1);
    b.visit(0, 0);
    b.visit(1, 0);
    b.visit(2, 0);
    b.visit(2, 1);
    for (int row = COLUMN + 1; row < n; row += 2) {
      b.visit(row, 1);
      b.visit(row, 0);
      b.visit(row + 1, 0);
      b.visit(row + 1, 1);
    }
    b.visit(n - 1, COLUMN);
    for (int row = n - 1; row > COLUMN + 1; row -= 2) {
      int width = widths[row];
      for (int col = COLUMN + 1; col <= COLUMN + width; col++) b.visit(row, col);
      b.visit(row - 1, COLUMN + width);
      for (int col = COLUMN + width - 1; col >= COLUMN; col--) b.visit(row - 1, col);
      b.visit(row - 2, COLUMN);
    }
    int left = COLUMN + initial + 1;
    if (left == n) {
      for (int col = COLUMN + 1; col < n; col++) b.visit(2, col);
    } else {
      for (int col = COLUMN + 1; col <= left; col++) b.visit(2, col);
      b.visit(1, left);
      for (int col = left; col < n; col++) b.visit(0, col);
      for (int col = n - 1; col > left; col--) b.visit(1, col);
      for (int col = left + 1; col < n; col++) b.visit(2, col);
    }
    for (int row = COLUMN + 1; row < n; row += 2) {
      int width = widths[row + 1];
      for (int col = n - 1; col > COLUMN + width; col--) b.visit(row, col);
      for (int col = COLUMN + width + 1; col < n; col++) b.visit(row + 1, col);
    }
    return b.grid;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    StringBuilder output = new StringBuilder();
    for (int[] row : construct(n)) {
      for (int col = 0; col < n; col++) {
        if (col > 0)
          output.append(' ');
        output.append(row[col]);
      }
      output.append('\n');
    }
    System.out.print(output);
  }
}
