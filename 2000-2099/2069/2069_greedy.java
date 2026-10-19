import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    in.nextToken();
    int m = (int) in.nval;
    int[] v = new int[n];
    int[] h = new int[m];
    int maxV = 0;
    int maxH = 0;
    for (int i = 0; i < n; i++) {
      in.nextToken();
      v[i] = (int) in.nval;
      maxV = Math.max(maxV, v[i]);
    }
    for (int i = 0; i < m; i++) {
      in.nextToken();
      h[i] = (int) in.nval;
      maxH = Math.max(maxH, h[i]);
    }
    // one turn: down the left street and along the bottom, or along the top and down the right
    int best = Math.max(Math.min(v[0], h[m - 1]), Math.min(h[0], v[n - 1]));
    // two turns: the middle street is the best one of its kind
    best = Math.max(best, Math.min(h[0], Math.min(maxV, h[m - 1])));
    best = Math.max(best, Math.min(v[0], Math.min(maxH, v[n - 1])));
    System.out.println(best);
  }
}
