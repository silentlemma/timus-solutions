import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  static final int SPACE = 32;
  static final int RADIX = 10;

  static int readInt(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= SPACE && c >= 0);
    int value = 0;
    while (c > SPACE) {
      value = value * RADIX + c - '0';
      c = in.read();
    }
    return value;
  }

  static Integer[] order(int[] scores) {
    Integer[] ids = new Integer[scores.length];
    for (int i = 0; i < ids.length; i++) ids[i] = i;
    Arrays.sort(ids, (a, b) -> {
      int comparison = Integer.compare(scores[a], scores[b]);
      return comparison != 0 ? comparison : Integer.compare(a, b);
    });
    return ids;
  }

  static void reverse(Integer[] ids) {
    for (int i = 0, j = ids.length - 1; i < j; i++, j--) {
      int value = ids[i];
      ids[i] = ids[j];
      ids[j] = value;
    }
  }

  static int[][] solve(int[] first, int[] second) {
    Integer[] a = order(first), b = order(second);
    int totalA = 0, totalB = 0;
    for (int i = 0; i < first.length; i++) {
      totalA += first[i];
      totalB += second[i];
    }
    if (totalA > totalB)
      reverse(b);
    else if (totalA < totalB)
      reverse(a);
    int[][] answer = new int[first.length][2];
    for (int i = 0; i < answer.length; i++) {
      answer[i][0] = a[i];
      answer[i][1] = b[i];
    }
    return answer;
  }

  static void run(BufferedInputStream in, StringBuilder out) throws IOException {
    int n = readInt(in);
    int[] first = new int[n], second = new int[n];
    for (int i = 0; i < n; i++) first[i] = readInt(in);
    for (int i = 0; i < n; i++) second[i] = readInt(in);
    for (int[] row : solve(first, second))
      out.append(row[0] + 1).append(' ').append(row[1] + 1).append('\n');
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    StringBuilder out = new StringBuilder();
    run(in, out);
    System.out.print(out);
  }
}
