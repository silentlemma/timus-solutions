import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int k = in.nextInt();
    int[] s = new int[n];
    int total = 0;
    int largest = 0;
    for (int i = 0; i < n; i++) {
      s[i] = in.nextInt();
      total += s[i];
      largest = Math.max(largest, s[i]);
    }
    // Every sponsor needs its own problems, and no problem holds more than k.
    int m = Math.max(largest, (total + k - 1) / k);
    // Write the sponsors one after another and deal the copies round robin:
    // a sponsor's copies are consecutive and at most m, so they land in
    // different problems, and every problem gets at most ceil(total / m) <= k.
    List<List<Integer>> problems = new ArrayList<>();
    for (int i = 0; i < m; i++) problems.add(new ArrayList<>());
    int position = 0;
    for (int i = 0; i < n; i++) {
      for (int c = 0; c < s[i]; c++) problems.get(position++ % m).add(i + 1);
    }
    StringBuilder out = new StringBuilder();
    out.append(m).append('\n');
    for (List<Integer> p : problems) {
      out.append(p.size());
      for (int x : p) out.append(' ').append(x);
      out.append('\n');
    }
    System.out.print(out);
  }
}
