import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int ALPHABET = 26;
  static final int VALUE_LIMIT = 100000;
  static final int TICKS = 1000000;
  static final int DIRECTIONS = 4;
  static final int UP = 3;

  static String solve(String[] grid, int[] inputs) {
    int[] dr = {0, 1, 0, -1};
    int[] dc = {1, 0, -1, 0};
    int[] memory = new int[ALPHABET];
    int row = 0, column = 0, direction = 0, current = 0, cursor = 0;
    StringBuilder output = new StringBuilder();
    for (int tick = 0; tick < TICKS; tick++) {
      char op = grid[row].charAt(column);
      switch (op) {
        case '#':
          return output.toString();
        case '>':
          direction = 0;
          break;
        case 'v':
          direction = 1;
          break;
        case '<':
          direction = 2;
          break;
        case '^':
          direction = UP;
          break;
        case '?':
          current = inputs[cursor];
          if (cursor + 1 < inputs.length)
            cursor++;
          break;
        case '!':
          output.append(current).append('\n');
          current = 0;
          break;
        case '+':
          current++;
          break;
        case '-':
          current--;
          break;
        case '@':
          direction = (direction + (current == 0 ? DIRECTIONS - 1 : 1)) % DIRECTIONS;
          break;
        default:
          if (op >= 'A' && op <= 'Z') {
            int index = op - 'A';
            int previous = current;
            current = memory[index];
            memory[index] = previous;
          }
      }
      if (current < -VALUE_LIMIT || current > VALUE_LIMIT) {
        output.append("OVERFLOW ERROR\n");
        return output.toString();
      }
      row += dr[direction];
      column += dc[direction];
      if (row < 0 || row >= grid.length || column < 0 || column >= grid[0].length()) {
        output.append("RUNTIME ERROR\n");
        return output.toString();
      }
    }
    output.append("TIME LIMIT EXCEEDED\n");
    return output.toString();
  }

  static String readToken(BufferedInputStream in) throws IOException {
    StringBuilder token = new StringBuilder();
    int character;
    do {
      character = in.read();
    } while (character >= 0 && character <= ' ');
    while (character > ' ') {
      token.append((char) character);
      character = in.read();
    }
    return token.toString();
  }

  static int readNumber(BufferedInputStream in) throws IOException {
    int character;
    do {
      character = in.read();
    } while (character >= 0 && character <= ' ');
    int sign = 1;
    if (character == '-' || character == '+') {
      sign = character == '-' ? -1 : 1;
      character = in.read();
    }
    int value = 0;
    while (character > ' ') {
      value = value * 10 + character - '0';
      character = in.read();
    }
    return sign * value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int height = readNumber(in);
    readNumber(in);
    String[] grid = new String[height];
    for (int index = 0; index < height; index++) grid[index] = readToken(in);
    int count = readNumber(in);
    int[] inputs = new int[count];
    for (int index = 0; index < count; index++) inputs[index] = readNumber(in);
    System.out.print(solve(grid, inputs));
  }
}
