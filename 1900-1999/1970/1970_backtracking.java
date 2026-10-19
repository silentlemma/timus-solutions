import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static final int PIECE_SIDE = 4;
  static final int GRID_SIDE = 3;
  static final int PIECE_COUNT = GRID_SIDE * GRID_SIDE;
  static final int TURN_COUNT = 4;
  static final int STATE_COUNT = PIECE_COUNT * TURN_COUNT;
  static final int PIXELS = PIECE_SIDE * PIECE_SIDE;
  static final int STRIDE = PIECE_SIDE - 1;
  static final int BOARD_SIDE = GRID_SIDE * STRIDE + 1;

  static class Solver {
    final int[][] states = new int[STATE_COUNT][PIXELS];
    final long[] masks = new long[PIECE_COUNT];
    final long[][] compatible = new long[TURN_COUNT][STATE_COUNT];
    final int[][] neighbors = new int[PIECE_COUNT][TURN_COUNT];
    final int[] degree = new int[PIECE_COUNT];
    final int[] placement = new int[PIECE_COUNT];

    boolean search(long[] domains, int remaining) {
      if (remaining == 0)
        return true;
      int slot = -1, best = STATE_COUNT + 1;
      for (int i = 0; i < PIECE_COUNT; i++) {
        if (placement[i] >= 0)
          continue;
        int count = Long.bitCount(domains[i]);
        if (count < best || (count == best && degree[i] > degree[slot])) {
          slot = i;
          best = count;
        }
      }
      for (long choices = domains[slot]; choices != 0; choices &= choices - 1) {
        int state = Long.numberOfTrailingZeros(choices);
        placement[slot] = state;
        long unused = ~masks[state / TURN_COUNT];
        long[] following = domains.clone();
        for (int i = 0; i < PIECE_COUNT; i++) following[i] &= unused;
        for (int direction = 0; direction < TURN_COUNT; direction++) {
          int adjacent = neighbors[slot][direction];
          if (adjacent >= 0 && placement[adjacent] < 0) {
            following[adjacent] &= compatible[direction][state];
          }
        }
        boolean possible = true;
        for (int i = 0; i < PIECE_COUNT; i++) {
          if (placement[i] < 0 && following[i] == 0)
            possible = false;
        }
        if (possible && search(following, remaining - 1))
          return true;
        placement[slot] = -1;
      }
      return false;
    }

    int[][] assemble(int[][] pieces) {
      long initial = 0;
      for (int index = 0; index < PIECE_COUNT; index++) {
        int[] current = pieces[index].clone();
        for (int turn = 0; turn < TURN_COUNT; turn++) {
          int state = index * TURN_COUNT + turn;
          states[state] = current;
          masks[index] |= 1L << state;
          boolean duplicate = false;
          for (int previous = index * TURN_COUNT; previous < state; previous++) {
            duplicate |= Arrays.equals(states[previous], current);
          }
          if (!duplicate && (index != 0 || turn == 0))
            initial |= 1L << state;
          int[] rotated = new int[PIXELS];
          for (int r = 0; r < PIECE_SIDE; r++) {
            for (int c = 0; c < PIECE_SIDE; c++) {
              rotated[r * PIECE_SIDE + c] = current[(PIECE_SIDE - 1 - c) * PIECE_SIDE + r];
            }
          }
          current = rotated;
        }
      }
      int[][][] edges = new int[STATE_COUNT][TURN_COUNT][PIECE_SIDE];
      for (int state = 0; state < STATE_COUNT; state++) {
        for (int i = 0; i < PIECE_SIDE; i++) {
          edges[state][0][i] = states[state][i];
          edges[state][1][i] = states[state][i * PIECE_SIDE + PIECE_SIDE - 1];
          edges[state][2][i] = states[state][(PIECE_SIDE - 1) * PIECE_SIDE + i];
          edges[state][TURN_COUNT - 1][i] = states[state][i * PIECE_SIDE];
        }
      }
      for (int direction = 0; direction < TURN_COUNT; direction++) {
        for (int first = 0; first < STATE_COUNT; first++) {
          for (int second = 0; second < STATE_COUNT; second++) {
            int opposite = (direction + 2) % TURN_COUNT;
            if (first / TURN_COUNT != second / TURN_COUNT
                && Arrays.equals(edges[first][direction], edges[second][opposite])) {
              compatible[direction][first] |= 1L << second;
            }
          }
        }
      }
      int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1};
      for (int slot = 0; slot < PIECE_COUNT; slot++) {
        Arrays.fill(neighbors[slot], -1);
        for (int direction = 0; direction < TURN_COUNT; direction++) {
          int r = slot / GRID_SIDE + dr[direction];
          int c = slot % GRID_SIDE + dc[direction];
          if (0 <= r && r < GRID_SIDE && 0 <= c && c < GRID_SIDE) {
            neighbors[slot][direction] = r * GRID_SIDE + c;
            degree[slot]++;
          }
        }
      }
      Arrays.fill(placement, -1);
      long[] domains = new long[PIECE_COUNT];
      Arrays.fill(domains, initial);
      if (!search(domains, PIECE_COUNT)) {
        throw new IllegalStateException("The guaranteed arrangement was not found");
      }
      int[][] board = new int[BOARD_SIDE][BOARD_SIDE];
      for (int slot = 0; slot < PIECE_COUNT; slot++) {
        for (int r = 0; r < PIECE_SIDE; r++) {
          for (int c = 0; c < PIECE_SIDE; c++) {
            board[slot / GRID_SIDE * STRIDE + r][slot % GRID_SIDE * STRIDE + c] =
                states[placement[slot]][r * PIECE_SIDE + c];
          }
        }
      }
      return board;
    }
  }

  static int[][] assemble(int[][] pieces) {
    return new Solver().assemble(pieces);
  }

  public static void main(String[] args) {
    try (Scanner in = new Scanner(System.in)) {
      int[][] pieces = new int[PIECE_COUNT][PIXELS];
      for (int[] piece : pieces) {
        for (int i = 0; i < PIXELS; i++) piece[i] = in.nextInt();
      }
      StringBuilder out = new StringBuilder();
      for (int[] row : assemble(pieces)) {
        for (int c = 0; c < BOARD_SIDE; c++) {
          if (c != 0)
            out.append(' ');
          out.append(row[c]);
        }
        out.append('\n');
      }
      System.out.print(out);
    }
  }
}
