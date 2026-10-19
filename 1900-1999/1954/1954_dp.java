import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
  static final int ALPHABET = 26;
  static final int TARGET = 5;
  static final int INF = TARGET + 1;
  static final int OUTER_SPLIT = 3;
  public static void main(String[] args) throws IOException {
    String text = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
    int n = text.length(), capacity = n + 2;
    char[] data = (" " + text).toCharArray();
    int[] edges = new int[capacity * ALPHABET], lengths = new int[capacity];
    int[] links = new int[capacity], diff = new int[capacity], series = new int[capacity];
    lengths[0] = -1;
    byte[] best = new byte[2 * (n + 1)], group = new byte[2 * capacity];
    Arrays.fill(best, (byte) INF);
    Arrays.fill(group, (byte) INF);
    best[0] = 0;
    int[] parent = new int[2 * (n + 1)], start = new int[2 * capacity];
    int count = 2, last = 1;
    for (int i = 1; i <= n; i++) {
      int code = data[i] - 'a', current = last;
      while (data[i - lengths[current] - 1] != data[i]) current = links[current];
      int slot = current * ALPHABET + code, following = edges[slot];
      if (following == 0) {
        following = count++;
        edges[slot] = following;
        lengths[following] = lengths[current] + 2;
        if (lengths[following] == 1)
          links[following] = 1;
        else {
          int suffix = links[current];
          while (data[i - lengths[suffix] - 1] != data[i]) suffix = links[suffix];
          links[following] = edges[suffix * ALPHABET + code];
        }
        int suffix = links[following];
        diff[following] = lengths[following] - lengths[suffix];
        series[following] = diff[following] == diff[suffix] ? series[suffix] : suffix;
      }
      last = following;
      for (int v = last; lengths[v] > 0; v = series[v]) {
        int base = i - lengths[series[v]] - diff[v], suffix = links[v];
        for (int p = 0; p < 2; p++) {
          int index = 2 * v + p;
          group[index] = best[2 * base + p];
          start[index] = base;
          if (diff[v] == diff[suffix] && group[2 * suffix + p] < group[index]) {
            group[index] = group[2 * suffix + p];
            start[index] = start[2 * suffix + p];
          }
          int target = 2 * i + (p ^ 1);
          if (group[index] + 1 < best[target]) {
            best[target] = (byte) (group[index] + 1);
            parent[target] = start[index];
          }
        }
      }
    }
    if (best[2 * n + 1] > TARGET) {
      System.out.println("NO");
      return;
    }
    List<String> result = new ArrayList<>();
    for (int i = n, parity = 1; i > 0; parity ^= 1) {
      int before = parent[2 * i + parity];
      result.add(text.substring(before, i));
      i = before;
    }
    Collections.reverse(result);
    while (result.size() < TARGET) {
      int longest = -1;
      for (int i = 0; i < result.size(); i++)
        if (result.get(i).length() >= OUTER_SPLIT) {
          longest = i;
          break;
        }
      if (longest >= 0) {
        String part = result.remove(longest);
        result.addAll(longest,
            Arrays.asList(part.substring(0, 1), part.substring(1, part.length() - 1),
                part.substring(part.length() - 1)));
      } else {
        int remaining = 2;
        List<String> next = new ArrayList<>();
        for (String part : result) {
          if (part.length() == 2 && remaining > 0) {
            next.add(part.substring(0, 1));
            next.add(part.substring(1));
            remaining--;
          } else
            next.add(part);
        }
        result = next;
      }
    }
    StringBuilder output = new StringBuilder("YES\n");
    for (String part : result) output.append(part).append('\n');
    System.out.print(output);
  }
}
