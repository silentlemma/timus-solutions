import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
  private static final int LIMIT = 2000000; // the largest possible sum of two notes

  private static int[][] near; // the even notes each odd note can pair with
  private static int[] partner; // the odd note matched to each even note, -1 if none
  private static boolean[] visited;

  private static boolean augment(int u) {
    for (int v : near[u]) {
      if (visited[v]) continue;
      visited[v] = true;
      if (partner[v] < 0 || augment(partner[v])) {
        partner[v] = u;
        return true;
      }
    }
    return false;
  }

  public static void main(String[] args) throws IOException {
    boolean[] composite = new boolean[LIMIT + 1];
    composite[0] = true;
    composite[1] = true;
    for (int i = 2; (long) i * i <= LIMIT; i++) {
      if (!composite[i]) {
        for (int j = i * i; j <= LIMIT; j += i) composite[j] = true;
      }
    }
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    int[] odd = new int[n];
    int[] even = new int[n];
    int odds = 0;
    int evens = 0;
    int ones = 0;
    for (int i = 0; i < n; i++) {
      in.nextToken();
      int c = (int) in.nval;
      if (c == 1) {
        ones++;
      } else if (c % 2 == 1) {
        odd[odds++] = c;
      } else {
        even[evens++] = c;
      }
    }
    // A prime sum is 2 = 1 + 1 or an odd prime, the sum of an odd and an even
    // note. So the surplus of odd notes must be paired as ones among themselves.
    int surplus = ones + odds - evens;
    if (surplus < 0 || surplus > ones) {
      System.out.println("NO");
      return;
    }
    int onePairs = surplus / 2;
    for (int i = 0; i < ones - 2 * onePairs; i++) odd[odds++] = 1;
    near = new int[odds][];
    for (int u = 0; u < odds; u++) {
      int[] list = new int[evens];
      int size = 0;
      for (int v = 0; v < evens; v++) {
        if (!composite[odd[u] + even[v]]) list[size++] = v;
      }
      near[u] = Arrays.copyOf(list, size);
    }
    partner = new int[evens];
    Arrays.fill(partner, -1);
    for (int u = 0; u < odds; u++) {
      visited = new boolean[evens];
      if (!augment(u)) {
        System.out.println("NO");
        return;
      }
    }
    StringBuilder out = new StringBuilder("YES\n");
    for (int i = 0; i < onePairs; i++) out.append("1 1\n");
    for (int v = 0; v < evens; v++) {
      out.append(odd[partner[v]]).append(' ').append(even[v]).append('\n');
    }
    System.out.print(out);
  }
}
