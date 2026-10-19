import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    // every move adds two heaps, and the game ends when all heaps are ones
    long moves = 0;
    for (int i = 0; i < n; i++) {
      in.nextToken();
      moves += ((int) in.nval - 1) / 2;
    }
    System.out.println(moves % 2 == 1 ? "Daenerys" : "Stannis");
  }
}
