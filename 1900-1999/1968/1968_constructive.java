import java.util.Scanner;

public class Main {
  static final int BLOCK_SIDE = 2;

  static String[][] reconstruct(int[][] photo) {
    int rows = photo.length, columns = photo[0].length;
    int[][] counts = new int[rows][columns];
    for (int row = 0; row < rows; row++) {
      for (int column = 0; column < columns; column++) {
        int value = photo[row][column];
        if (row > 0)
          value -= counts[row - 1][column];
        if (column > 0)
          value -= counts[row][column - 1];
        if (row > 0 && column > 0)
          value -= counts[row - 1][column - 1];
        counts[row][column] = value;
      }
    }
    int height = Math.min(rows, columns) / BLOCK_SIDE;
    String[][] layers = new String[height][];
    for (int level = 0; level < height; level++) {
      layers[level] = new String[rows / BLOCK_SIDE - level];
      for (int row = 0; row < layers[level].length; row++) {
        StringBuilder line = new StringBuilder();
        for (int column = 0; column < columns / BLOCK_SIDE - level; column++) {
          int x = level + BLOCK_SIDE * row, y = level + BLOCK_SIDE * column;
          line.append(counts[x][y] > level / BLOCK_SIDE ? 'R' : 'W');
        }
        layers[level][row] = line.toString();
      }
    }
    return layers;
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      int rows = input.nextInt(), columns = input.nextInt();
      int[][] photo = new int[rows][columns];
      for (int[] line : photo) {
        for (int column = 0; column < columns; column++) line[column] = input.nextInt();
      }
      String[][] layers = reconstruct(photo);
      StringBuilder output = new StringBuilder();
      for (int level = 0; level < layers.length; level++) {
        if (level > 0)
          output.append('\n');
        for (String line : layers[level]) output.append(line).append('\n');
      }
      System.out.print(output);
    }
  }
}
