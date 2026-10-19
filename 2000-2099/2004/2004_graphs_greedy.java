import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  private static String solve(int order) {
    int size = 1 << order;
    int mask = size - 1;
    boolean[] seen = new boolean[size];
    seen[0] = true;
    char[] result = new char[size + order - 1];
    Arrays.fill(result, 0, order, '0');
    int window = 0;
    int at = order;
    for (int step = 0; step < size - 1; step++) {
      window = (window << 1) & mask;
      if (!seen[window | 1]) {
        window |= 1;
        result[at++] = '1';
      } else {
        result[at++] = '0';
      }
      seen[window] = true;
    }
    return new String(result);
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    int order = Integer.parseInt(input.readLine().trim());
    System.out.println(solve(order));
  }
}
