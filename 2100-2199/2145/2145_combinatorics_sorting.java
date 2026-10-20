import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    long[] a = new long[n];
    long[] b = new long[n];
    for (int i = 0; i < n; i++) {
      in.nextToken();
      a[i] = (long) in.nval;
    }
    for (int i = 0; i < n; i++) {
      in.nextToken();
      b[i] = (long) in.nval;
    }
    in.nextToken();
    long p = (long) in.nval;
    Arrays.sort(a);
    Arrays.sort(b);
    // The i-th weakest student can take any of the problems they can solve,
    // except the i problems already taken by weaker students.
    long ways = 1 % p;
    int solvable = 0;
    for (int i = 0; i < n; i++) {
      while (solvable < n && b[solvable] <= a[i]) solvable++;
      ways = ways * ((solvable - i) % p) % p;
    }
    System.out.println(ways);
  }
}
