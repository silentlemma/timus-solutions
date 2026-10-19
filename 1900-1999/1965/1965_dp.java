import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int DECIMAL_BASE = 10;
  static int[][] fixedDirections(int[] values, int firstDirection, int secondDirection) {
    int size = values.length;
    int[] direction = {firstDirection, secondDirection};
    int[] other = {secondDirection == 1 ? 0 : size + 1, firstDirection == 1 ? 0 : size + 1};
    byte[][] parent = new byte[2][size];
    int previous = values[0];
    for (int index = 1; index < size; index++) {
      int value = values[index];
      int[] next = {-1, -1};
      for (int owner = 0; owner < 2; owner++) {
        if (other[owner] >= 0 && direction[owner] * (value - previous) > 0) {
          next[owner] = other[owner];
          parent[owner][index] = (byte) owner;
        }
        if (other[1 - owner] >= 0 && direction[owner] * (value - other[1 - owner]) > 0) {
          if (next[owner] < 0 || direction[1 - owner] * (previous - next[owner]) < 0) {
            next[owner] = previous;
            parent[owner][index] = (byte) (1 - owner);
          }
        }
      }
      if (next[0] < 0 && next[1] < 0)
        return null;
      other = next;
      previous = value;
    }
    int owner = other[0] >= 0 ? 0 : 1;
    int[] assignment = new int[size];
    int[] counts = new int[2];
    for (int index = size - 1; index >= 0; index--) {
      assignment[index] = owner;
      counts[owner]++;
      owner = parent[owner][index];
    }
    if (counts[0] == 0) {
      assignment[size - 1] = 0;
      counts[0]++;
      counts[1]--;
    } else if (counts[1] == 0) {
      assignment[size - 1] = 1;
      counts[1]++;
      counts[0]--;
    }
    int[][] groups = {new int[counts[0]], new int[counts[1]]};
    int[] at = new int[2];
    for (int index = 0; index < size; index++) {
      owner = assignment[index];
      groups[owner][at[owner]++] = values[index];
    }
    return groups;
  }

  static int[][] partition(int[] values) {
    int[][] directions = {{1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
    for (int[] direction : directions) {
      int[][] groups = fixedDirections(values, direction[0], direction[1]);
      if (groups != null)
        return groups;
    }
    return null;
  }

  static int nextInt(BufferedInputStream input) throws IOException {
    int symbol;
    do {
      symbol = input.read();
    } while (symbol <= ' ' && symbol >= 0);
    int value = 0;
    while (symbol > ' ') {
      value = value * DECIMAL_BASE + symbol - '0';
      symbol = input.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream input = new BufferedInputStream(System.in);
    int size = nextInt(input);
    int[] values = new int[size];
    for (int i = 0; i < size; i++) values[i] = nextInt(input);
    int[][] groups = partition(values);
    if (groups == null) {
      System.out.println("Fail");
      return;
    }
    StringBuilder output = new StringBuilder();
    output.append(groups[0].length).append(' ').append(groups[1].length).append('\n');
    for (int[] group : groups) {
      for (int value : group) output.append(value).append(' ');
      output.append('\n');
    }
    System.out.print(output);
  }
}
