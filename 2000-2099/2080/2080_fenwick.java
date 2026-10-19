import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
  private static int k;
  private static int[] tree;

  private static void add(int j) {
    for (; j <= k; j += j & -j) tree[j]++;
  }

  private static int prefix(int j) {
    int s = 0;
    for (; j > 0; j -= j & -j) s += tree[j];
    return s;
  }

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    in.nextToken();
    k = (int) in.nval;
    int[] uses = new int[k + 1];
    for (int i = 1; i <= k; i++) {
      in.nextToken();
      uses[i] = (int) in.nval;
    }
    // the stack is kept in order of next use: after a card is used, the cards above
    // it are those used before its next use, the distinct cards in between
    int[] nxt = new int[k + 1];
    int[] seen = new int[n + 1];
    Arrays.fill(seen, k + 1);
    for (int i = k; i >= 1; i--) {
      nxt[i] = seen[uses[i]];
      seen[uses[i]] = i;
    }
    // Fenwick tree over moments: a moment j counts once the query time i reaches
    // the previous use of its card, so the counted moments are first uses after i
    tree = new int[k + 1];
    for (int card = 1; card <= n; card++) if (seen[card] <= k) add(seen[card]);
    StringBuilder out = new StringBuilder();
    // first the cards in order of first use, then the unused ones
    for (int i = 1; i <= k; i++) if (seen[uses[i]] == i) out.append(uses[i]).append(' ');
    for (int card = 1; card <= n; card++) if (seen[card] > k) out.append(card).append(' ');
    out.setLength(out.length() - 1);
    out.append('\n');
    for (int i = 1; i <= k; i++) {
      if (nxt[i] <= k) add(nxt[i]);
      out.append(prefix(nxt[i] - 1) - prefix(i)).append('\n');
    }
    System.out.print(out);
  }
}
