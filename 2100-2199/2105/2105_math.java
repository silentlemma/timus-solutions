import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
  private static final int ALICE = 1;
  private static StreamTokenizer in;

  private static long next() throws IOException {
    in.nextToken();
    return (long) in.nval;
  }

  public static void main(String[] args) throws IOException {
    in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    long length = next();
    long total = next();
    long va = next();
    long vb = next();
    int n = (int) next();
    // riding in opposite directions, they meet whenever the distance ridden by
    // both together reaches a new multiple of the length; the intervals of one
    // kid do not overlap, so their durations add up
    long[] resting = new long[2];
    for (int i = 0; i < n; i++) {
      long kid = next();
      next(); // the start does not matter
      resting[kid == ALICE ? 0 : 1] += next();
    }
    long ridden = va * (total - resting[0]) + vb * (total - resting[1]);
    System.out.println(ridden / length);
  }
}
