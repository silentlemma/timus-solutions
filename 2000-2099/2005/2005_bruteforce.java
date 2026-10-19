import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  private static final int POINTS = 5;
  private static final int END = POINTS - 1;
  private static final int FORBIDDEN_LAST = 2;
  private static final int MIDDLE_SUM = END * (END - 1) / 2;
  private static final int BASE = 10;

  private static final class Result {
    int cost = -1;
    int[] route;
  }

  private static Result solve(int[][] distance) {
    Result best = new Result();
    for (int first = 1; first < END; first++) {
      for (int last = 1; last < END; last++) {
        if (first == last || last == FORBIDDEN_LAST)
          continue;
        int middle = MIDDLE_SUM - first - last;
        int[] route = {0, first, middle, last, END};
        int cost = 0;
        for (int i = 0; i < END; i++) cost += distance[route[i]][route[i + 1]];
        if (best.cost < 0 || cost < best.cost) {
          best.cost = cost;
          best.route = route;
        }
      }
    }
    return best;
  }

  private static int readInt(BufferedInputStream input) throws IOException {
    int ch;
    do {
      ch = input.read();
    } while (ch <= ' ' && ch != -1);
    int value = 0;
    while (ch > ' ') {
      value = value * BASE + ch - '0';
      ch = input.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream input = new BufferedInputStream(System.in);
    int[][] distance = new int[POINTS][POINTS];
    for (int i = 0; i < POINTS; i++)
      for (int j = 0; j < POINTS; j++) distance[i][j] = readInt(input);
    Result answer = solve(distance);
    StringBuilder output = new StringBuilder().append(answer.cost).append('\n');
    for (int i = 0; i < POINTS; i++) {
      if (i > 0)
        output.append(' ');
      output.append(answer.route[i] + 1);
    }
    System.out.println(output);
  }
}
