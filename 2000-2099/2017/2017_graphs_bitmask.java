import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.List;

public class Main {
  static final int SPACE = 32;

  static String readToken(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= SPACE && c >= 0);
    StringBuilder token = new StringBuilder();
    while (c > SPACE) {
      token.append((char) c);
      c = in.read();
    }
    return token.toString();
  }

  static int[] solve(String[] locations, BitSet[] claims) {
    int n = locations.length;
    List<List<Integer>> graph = new ArrayList<>();
    for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (!locations[i].equals(locations[j]) && claims[i].intersects(claims[j])) {
          graph.get(i).add(j);
          graph.get(j).add(i);
        }
      }
    }
    int[] color = new int[n];
    Arrays.fill(color, -1);
    List<Integer> answer = new ArrayList<>();
    int[] pending = new int[n];
    for (int start = 0; start < n; start++) {
      if (color[start] != -1)
        continue;
      color[start] = 0;
      List<List<Integer>> sides = new ArrayList<>();
      sides.add(new ArrayList<>());
      sides.add(new ArrayList<>());
      pending[0] = start;
      int end = 1;
      for (int at = 0; at < end; at++) {
        int vertex = pending[at];
        sides.get(color[vertex]).add(vertex);
        for (int target : graph.get(vertex)) {
          if (color[target] == -1) {
            color[target] = color[vertex] ^ 1;
            pending[end++] = target;
          }
        }
      }
      int side = sides.get(0).size() <= sides.get(1).size() ? 0 : 1;
      answer.addAll(sides.get(side));
    }
    if (answer.isEmpty())
      answer.add(0);
    int[] result = new int[answer.size()];
    for (int i = 0; i < result.length; i++) result[i] = answer.get(i);
    return result;
  }

  static void run(BufferedInputStream in, StringBuilder out) throws IOException {
    int n = Integer.parseInt(readToken(in));
    String[] locations = new String[n];
    BitSet[] claims = new BitSet[n];
    for (int i = 0; i < n; i++) {
      locations[i] = readToken(in);
      int count = Integer.parseInt(readToken(in));
      claims[i] = new BitSet(n);
      claims[i].set(i);
      while (count-- > 0) claims[i].set(Integer.parseInt(readToken(in)) - 1);
    }
    int[] answer = solve(locations, claims);
    out.append(answer.length).append('\n');
    for (int i = 0; i < answer.length; i++) {
      if (i > 0)
        out.append(' ');
      out.append(answer[i] + 1);
    }
    out.append('\n');
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    StringBuilder out = new StringBuilder();
    run(in, out);
    System.out.print(out);
  }
}
