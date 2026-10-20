import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
  private static final int FACES = 6; // a six lets the player roll again in the same turn

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    int[] jump = new int[n + 1];
    for (int i = 2; i < n; i++) {
      in.nextToken();
      jump[i] = (int) in.nval;
    }
    // land[i]: where the token rests after arriving at i and following snakes
    int[] land = new int[n + 1];
    for (int i = 1; i <= n; i++) land[i] = jump[i] > 0 ? land[i - jump[i]] : i;

    // turns holds the fewest turns begun when the token is about to roll at a
    // cell, and a six keeps the turn going at weight 0 while other rolls cost 1
    int infinity = n + 1;
    int[] turns = new int[n + 1];
    Arrays.fill(turns, infinity);
    turns[1] = 1;
    ArrayDeque<Integer> queue = new ArrayDeque<>();
    queue.add(1);
    int best = infinity;
    while (!queue.isEmpty()) {
      int cell = queue.pollFirst();
      int current = turns[cell];
      if (current >= best) continue;
      for (int face = 1; face <= FACES; face++) {
        int target = land[Math.min(cell + face, n)];
        if (target == n) {
          best = Math.min(best, current);
          continue;
        }
        int cost = face == FACES ? current : current + 1;
        if (cost < turns[target]) {
          turns[target] = cost;
          if (face == FACES) {
            queue.addFirst(target);
          } else {
            queue.addLast(target);
          }
        }
      }
    }
    System.out.println(best < infinity ? best : -1);
  }
}
