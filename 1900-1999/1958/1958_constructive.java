import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static class Operations {
    final int[] values;
    int size;
    Operations(int capacity) {
      values = new int[capacity];
    }
    void add(int value) {
      values[size++] = value;
    }
  }

  static void flush(int[] values, Operations operations) {
    int n = values.length;
    while (values[n - 1] != n) {
      int value = values[n - 1];
      values[n - 1] = values[value - 1];
      values[value - 1] = value;
      operations.add(value);
    }
  }

  static Operations sortOperations(int[] permutation) {
    int[] values = permutation.clone();
    int n = values.length;
    Operations operations = new Operations((n - 1) * (2 * n - 1));
    flush(values, operations);
    int unfixed = n - 1;
    while (unfixed > 0) {
      while (unfixed > 0 && values[unfixed - 1] == unfixed) unfixed--;
      if (unfixed == 0)
        break;
      int start = 0;
      while (values[start] != 1) start++;
      for (int position = start; position + 1 < n; position++) {
        values[position] = values[position + 1];
        values[position + 1] = 1;
        operations.add(1);
      }
      flush(values, operations);
    }
    return operations;
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
    int[] values = new int[n];
    for (int i = 0; i < n; i++) values[i] = in.nextInt();
    Operations operations = sortOperations(values);
    StringBuilder out = new StringBuilder();
    out.append(operations.size).append('\n');
    for (int i = 0; i < operations.size; i++) out.append(operations.values[i]).append('\n');
    System.out.print(out);
  }
}
